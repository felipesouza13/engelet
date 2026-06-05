"""
Motor de busca em massa — OpenAlex + arXiv (acadêmico, sem chave) + Tavily (web).

Usado pelos endpoints /api/buscar/* de main.py. Roda em worker thread,
emite eventos de progresso (para polling) e respeita uma flag de cancelamento.

Saídas:
  - acadêmico → livros_normas/artigos-cientificos/<tema>/
  - web (Tavily) → livros_normas/buscas-web/<tema>/
Tudo entra como "pendente" (a listagem do rag.py detecta automaticamente).
"""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Callable

RAIZ = Path(__file__).resolve().parents[2]
LIVROS = RAIZ / "livros_normas"
ART = LIVROS / "artigos-cientificos"
WEB = LIVROS / "buscas-web"
BACKEND = Path(__file__).resolve().parent
CONFIG_PATH = BACKEND / "busca_config.json"

EMAIL = "felipesouza13@gmail.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")
MIN_BYTES = 20000

# Domínios usados quando "Brasil" é marcado como filtro de fonte
DOMINIOS_BR = ["canalsolar.com.br", "scielo.br", "portalsolar.com.br",
               "gov.br", "osetoreletrico.com.br", "abntonline.com.br"]

# ---------------------------------------------------------------------------
# Presets de consultas por eixo
# ---------------------------------------------------------------------------
PRESETS_ACAD: dict[str, list[tuple[str, str]]] = {
    "solar": [
        ("solar-celulas", "TOPCon heterojunction silicon solar cell efficiency"),
        ("solar-inversores", "photovoltaic inverter grid-forming reliability"),
        ("solar-mppt", "maximum power point tracking partial shading photovoltaic"),
        ("solar-faults", "photovoltaic fault detection machine learning thermography"),
        ("solar-previsao", "solar power irradiance forecasting deep learning"),
        ("solar-armazenamento", "battery storage photovoltaic sizing optimization"),
        ("solar-degradacao", "photovoltaic module degradation field reliability"),
        ("solar-gd", "distributed generation photovoltaic grid connection"),
    ],
    "subestacoes": [
        ("subestacoes-protecao", "power system protection relay coordination substation"),
        ("subestacoes-transformadores", "power transformer condition monitoring diagnosis"),
        ("subestacoes-aterramento", "substation grounding grid design step touch voltage"),
        ("subestacoes-gis-sf6", "gas insulated switchgear partial discharge"),
        ("subestacoes-disjuntores", "high voltage circuit breaker switching transient"),
        ("subestacoes-iec61850", "IEC 61850 digital substation automation"),
        ("subestacoes-isolamento-surtos", "insulation coordination surge arrester substation"),
        ("subestacoes-confiabilidade", "substation reliability maintenance assessment"),
    ],
    "ee_ampla": [
        ("ee-qualidade-energia", "power quality harmonics distribution network"),
        ("ee-sep", "optimal power flow state estimation distribution"),
        ("ee-maquinas", "induction motor fault diagnosis condition monitoring"),
        ("ee-eletronica-potencia", "multilevel inverter DC-DC converter renewable"),
        ("ee-microrredes", "microgrid energy management control"),
        ("ee-estabilidade", "power system transient stability assessment"),
    ],
    # Conteúdo brasileiro (OpenAlex é multilíngue → indexa SciELO/periódicos BR)
    "brasil": [
        ("br-solar", "energia solar fotovoltaica desempenho geração distribuída"),
        ("br-solar", "sistema fotovoltaico eficiência perdas sombreamento"),
        ("br-subestacoes", "subestação proteção sistema elétrico de potência"),
        ("br-aterramento", "aterramento malha de terra subestação segurança"),
        ("br-qualidade", "qualidade de energia elétrica harmônicos distribuição"),
        ("br-sep", "sistema elétrico de potência fluxo de carga distribuição"),
    ],
    # Aterramento / SPDA / resistividade do solo
    "aterramento": [
        ("aterramento-malha", "substation grounding grid design optimization safety"),
        ("aterramento-resistividade", "soil resistivity measurement Wenner stratification"),
        ("aterramento-transitorio", "grounding electrode impedance high frequency lightning"),
        ("spda-descargas", "lightning protection system design risk assessment"),
        ("spda-descargas", "lightning electromagnetic transient grounding simulation"),
        ("br-aterramento", "aterramento malha de terra subestação dimensionamento"),
        ("br-spda", "SPDA proteção contra descargas atmosféricas edificações"),
    ],
}

# Consultas web (Tavily) — NORMAS / DATASHEETS / ARTIGOS.
# Cada item: {"tema", "query", "domains": [...] | None}
PRESETS_WEB: dict[str, list[dict]] = {
    "solar": [
        {"tema": "solar", "query": "datasheet inversor solar fotovoltaico filetype:pdf", "domains": None},
        {"tema": "solar", "query": "datasheet módulo painel solar fotovoltaico filetype:pdf", "domains": None},
        {"tema": "solar", "query": "norma técnica conexão microgeração distribuída distribuidora pdf", "domains": None},
    ],
    "subestacoes": [
        {"tema": "subestacoes", "query": "norma técnica subestação NBR média tensão filetype:pdf", "domains": None},
        {"tema": "subestacoes", "query": "manual relé de proteção SEL ABB Schweitzer filetype:pdf", "domains": None},
        {"tema": "subestacoes", "query": "datasheet disjuntor transformador subestação filetype:pdf", "domains": None},
    ],
    "ee_ampla": [
        {"tema": "ee_ampla", "query": "NR-10 NR-35 segurança instalações elétricas filetype:pdf", "domains": None},
        {"tema": "ee_ampla", "query": "norma ABNT NBR instalações elétricas filetype:pdf", "domains": None},
    ],
    "brasil": [
        {"tema": "canalsolar", "query": "energia solar fotovoltaica artigo técnico inversor módulo", "domains": ["canalsolar.com.br"]},
        {"tema": "canalsolar", "query": "subestação proteção sistema elétrico geração distribuída", "domains": ["canalsolar.com.br"]},
        {"tema": "portalsolar", "query": "energia solar fotovoltaica guia técnico dimensionamento", "domains": ["portalsolar.com.br"]},
        {"tema": "scielo-br", "query": "energia solar fotovoltaica sistema elétrico potência", "domains": ["scielo.br"]},
        {"tema": "br-teses", "query": "termografia fotovoltaica subestação dissertação tese filetype:pdf", "domains": None},
        {"tema": "br-normas", "query": "norma técnica instalações elétricas NBR distribuidora ANEEL filetype:pdf", "domains": None},
    ],
    "aterramento": [
        {"tema": "aterramento", "query": "aterramento SPDA resistividade do solo guia técnico filetype:pdf", "domains": None},
        {"tema": "aterramento", "query": "tensão de passo e toque malha de terra subestação filetype:pdf", "domains": None},
        {"tema": "canalsolar", "query": "aterramento SPDA sistema fotovoltaico proteção", "domains": ["canalsolar.com.br"]},
    ],
}


# ---------------------------------------------------------------------------
# Config (chave Tavily) — nunca commitada (ver .gitignore)
# ---------------------------------------------------------------------------
def carregar_config() -> dict:
    if CONFIG_PATH.exists():
        try:
            return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def salvar_config(provider: str, api_key: str) -> None:
    CONFIG_PATH.write_text(
        json.dumps({"provider": provider, "api_key": api_key},
                   ensure_ascii=False, indent=2), encoding="utf-8")


def tem_chave() -> bool:
    return bool(carregar_config().get("api_key"))


# ---------------------------------------------------------------------------
# Helpers de busca / download
# ---------------------------------------------------------------------------
def slug(texto: str, n: int = 64) -> str:
    t = re.sub(r"[^a-zA-Z0-9]+", "-", (texto or "").lower()).strip("-")
    return t[:n].strip("-")


def _http_get(url: str, timeout: int = 40) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def buscar_openalex(query: str, per_page: int = 50, pais: str | None = None) -> list[dict]:
    filtros = "open_access.is_oa:true"
    if pais:  # restringe a trabalhos de autores afiliados ao país (ex.: BR)
        filtros += f",authorships.institutions.country_code:{pais.lower()}"
    qs = urllib.parse.urlencode({
        "search": query, "filter": filtros,
        "per-page": per_page, "mailto": EMAIL,
    })
    try:
        data = json.loads(_http_get(f"https://api.openalex.org/works?{qs}"))
    except Exception:  # noqa: BLE001
        return []
    out = []
    for w in data.get("results", []):
        loc = w.get("best_oa_location") or {}
        pdf = loc.get("pdf_url") or (w.get("open_access") or {}).get("oa_url")
        if pdf:
            out.append({"titulo": w.get("title") or "sem-titulo",
                        "ano": w.get("publication_year") or "",
                        "url": pdf, "fonte": "OpenAlex"})
    return out


def buscar_arxiv(query: str, max_results: int = 12) -> list[dict]:
    qs = urllib.parse.urlencode({
        "search_query": f"all:{query}", "start": 0,
        "max_results": max_results, "sortBy": "relevance",
    })
    try:
        xml = _http_get(f"http://export.arxiv.org/api/query?{qs}")
        root = ET.fromstring(xml)
    except Exception:  # noqa: BLE001
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    for e in root.findall("a:entry", ns):
        idu = e.findtext("a:id", default="", namespaces=ns) or ""
        titulo = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
        ano = (e.findtext("a:published", default="", namespaces=ns) or "")[:4]
        pdf = ""
        for ln in e.findall("a:link", ns):
            if ln.get("title") == "pdf" or ln.get("type") == "application/pdf":
                pdf = ln.get("href", "")
        if not pdf and "/abs/" in idu:
            pdf = idu.replace("/abs/", "/pdf/")
        if pdf:
            out.append({"titulo": titulo, "ano": ano, "url": pdf, "fonte": "arXiv"})
    return out


def buscar_tavily(query: str, max_results: int, api_key: str,
                  include_domains: list[str] | None = None,
                  raw: bool = False) -> list[dict]:
    payload = {"api_key": api_key, "query": query,
               "max_results": max_results, "include_raw_content": raw}
    if include_domains:
        payload["include_domains"] = include_domains
    body = json.dumps(payload).encode()
    req = urllib.request.Request("https://api.tavily.com/search", data=body,
                                 headers={"Content-Type": "application/json",
                                          "User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
    except Exception:  # noqa: BLE001
        return []
    out = []
    for res in data.get("results", []):
        url = res.get("url", "")
        out.append({"titulo": res.get("title") or url, "ano": "",
                    "url": url, "fonte": "Tavily",
                    "conteudo": res.get("raw_content") or res.get("content") or ""})
    # prioriza PDFs diretos
    out.sort(key=lambda c: 0 if c["url"].lower().endswith(".pdf") else 1)
    return out


def salvar_md(titulo: str, url: str, conteudo: str, destino: Path) -> bool:
    texto = f"# {titulo}\n\n**Fonte:** {url}\n\n{conteudo.strip()}\n"
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")
    return True


def baixar(url: str, destino: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={
            "User-Agent": UA, "Accept": "application/pdf,*/*"})
        with urllib.request.urlopen(req, timeout=90) as r:
            dados = r.read()
    except Exception:  # noqa: BLE001
        return False
    if len(dados) < MIN_BYTES or dados[:5] != b"%PDF-":
        return False
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(dados)
    return True


def _existentes() -> set[str]:
    s = set()
    if LIVROS.exists():
        for ext in ("*.pdf", "*.md"):
            for p in LIVROS.rglob(ext):
                s.add(slug(p.stem))
    return s


# ---------------------------------------------------------------------------
# Orquestrador
# ---------------------------------------------------------------------------
def buscar_em_massa(
    config: dict,
    progresso: Callable[[dict], None] | None = None,
    cancelado: Callable[[], bool] | None = None,
) -> dict:
    """
    config = {eixos:[...], usar_web:bool, max_por_consulta:int}
    Eventos: inicio / consulta / encontrados / download / consulta_fim / fim / erro
    """
    def emit(e):
        if progresso:
            progresso(e)

    def cancel():
        return bool(cancelado and cancelado())

    eixos = config.get("eixos", [])
    usar_web = bool(config.get("usar_web", False))
    cap = int(config.get("max_por_consulta", 30))

    # "Brasil" funciona como FILTRO de fonte: se marcado junto de outros eixos,
    # restringe a busca daqueles eixos a fontes BR (OpenAlex país=BR + domínios BR).
    # Marcado sozinho, usa os presets gerais "brasil".
    foco_br = "brasil" in eixos
    conteudo = [e for e in eixos if e != "brasil"]
    api_key = carregar_config().get("api_key", "")

    # tarefa: (tema, query, modo, domains, pais)
    tarefas: list[tuple] = []

    def add_acad(eixo, pais=None, prefixo=""):
        for tema, q in PRESETS_ACAD.get(eixo, []):
            tarefas.append((prefixo + tema, q, "acad", None, pais))

    def add_web(eixo, dom_override=False, sufixo="", prefixo=""):
        if not (usar_web and api_key):
            return
        for p in PRESETS_WEB.get(eixo, []):
            dom = dom_override if dom_override is not False else p.get("domains")
            tarefas.append((prefixo + p["tema"], (p["query"] + sufixo).strip(),
                            "web", dom, None))

    if foco_br and conteudo:
        for eixo in conteudo:               # restringe cada eixo a fontes BR
            add_acad(eixo, pais="BR", prefixo="br-")
            add_web(eixo, dom_override=DOMINIOS_BR, sufixo=" Brasil", prefixo="br-")
    else:
        for eixo in eixos:                  # comportamento normal (inclui 'brasil' só)
            add_acad(eixo)
            add_web(eixo)

    emit({"tipo": "inicio", "total_consultas": len(tarefas)})
    if not tarefas:
        emit({"tipo": "fim", "total_baixados": 0, "consultas_feitas": 0})
        return {"baixados": 0, "consultas": 0}

    vistos = _existentes()
    total = 0
    feitas = 0
    for i, (tema, query, modo, domains, pais) in enumerate(tarefas, 1):
        if cancel():
            emit({"tipo": "erro", "query": query, "msg": "Cancelado pelo usuário."})
            break
        emit({"tipo": "consulta", "query": query, "tema": tema, "modo": modo,
              "indice": i, "total_consultas": len(tarefas)})
        try:
            if modo == "acad":
                cand = buscar_openalex(query, 60, pais=pais)
                if not pais:        # arXiv é global (EN); só entra fora do foco BR
                    time.sleep(1.5)
                    cand += buscar_arxiv(query)
                base = ART
            else:
                cand = buscar_tavily(query, 20, api_key,
                                     include_domains=domains, raw=True)
                base = WEB
        except Exception as e:  # noqa: BLE001
            emit({"tipo": "erro", "query": query, "msg": str(e)})
            feitas += 1
            continue
        emit({"tipo": "encontrados", "query": query, "n": len(cand)})

        baixados = 0
        for c in cand:
            if cancel() or baixados >= cap:
                break
            sl = slug(c["titulo"] or c["url"])
            if not sl or sl in vistos:
                continue
            vistos.add(sl)
            nome = f"{c['fonte']}-{c.get('ano', '')}-{sl}.pdf"
            destino = base / tema / nome
            destino_md = base / tema / f"Tavily-{sl}.md"
            if destino.exists() or destino_md.exists():  # já capturado — pula
                continue
            ok = baixar(c["url"], destino)
            # fallback: artigo HTML (Canal Solar/blogs) → salva texto como .md
            if not ok and modo == "web" and len(c.get("conteudo", "")) > 600:
                salvar_md(c["titulo"], c["url"], c["conteudo"], destino_md)
                ok = True
                nome = destino_md.name
            emit({"tipo": "download", "arquivo": f"{tema}/{nome}",
                  "fonte": c["url"], "ok": ok})
            if ok:
                baixados += 1
                total += 1
            time.sleep(0.3)

        feitas += 1
        emit({"tipo": "consulta_fim", "query": query, "tema": tema,
              "baixados": baixados, "consultas_feitas": feitas,
              "total_baixados": total})
        time.sleep(0.6)

    emit({"tipo": "fim", "total_baixados": total, "consultas_feitas": feitas})
    return {"baixados": total, "consultas": feitas}
