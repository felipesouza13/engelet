"""
Motor de busca em massa AUTÔNOMO (standalone) — OpenAlex + arXiv.

Roda sem chave e sem o front: varre uma lista de consultas (foco em
subestações, solar e EE ampla), coleta PDFs open-access e baixa para
livros_normas/artigos-cientificos/<tema>/, deduplicando contra o que já existe.

Uso: ./.venv/Scripts/python.exe buscas_auto.py
É a base do futuro módulo buscas.py (endpoint /api/buscar).
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LIVROS = RAIZ / "livros_normas"
ART = LIVROS / "artigos-cientificos"
EMAIL = "felipesouza13@gmail.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

POR_CONSULTA = 12      # downloads bem-sucedidos por consulta
TETO_GLOBAL = 450      # teto de segurança por execução
MIN_BYTES = 20000      # ignora PDFs minúsculos/quebrados

# ---------------------------------------------------------------------------
# Consultas (tema-slug, query EN). Foco: subestações + solar + EE ampla.
# ---------------------------------------------------------------------------
CONSULTAS: list[tuple[str, str]] = [
    # ---- SUBESTAÇÕES (prioridade) ----
    ("subestacoes-protecao", "power system protection relay coordination substation"),
    ("subestacoes-protecao", "differential protection power transformer relay"),
    ("subestacoes-protecao", "distance protection transmission line fault"),
    ("subestacoes-protecao", "busbar protection substation"),
    ("subestacoes-transformadores", "power transformer condition monitoring diagnosis"),
    ("subestacoes-transformadores", "transformer dissolved gas analysis fault diagnosis"),
    ("subestacoes-transformadores", "power transformer insulation aging degradation"),
    ("subestacoes-aterramento", "substation grounding grid design safety"),
    ("subestacoes-aterramento", "ground potential rise step touch voltage substation"),
    ("subestacoes-gis-sf6", "gas insulated switchgear partial discharge diagnosis"),
    ("subestacoes-gis-sf6", "SF6 alternative gas insulated switchgear eco-friendly"),
    ("subestacoes-disjuntores", "high voltage circuit breaker switching transient"),
    ("subestacoes-disjuntores", "circuit breaker condition monitoring diagnostics"),
    ("subestacoes-iec61850", "IEC 61850 substation automation system"),
    ("subestacoes-iec61850", "digital substation process bus sampled values"),
    ("subestacoes-isolamento-surtos", "insulation coordination surge arrester substation"),
    ("subestacoes-isolamento-surtos", "lightning overvoltage protection substation"),
    ("subestacoes-confiabilidade", "substation reliability assessment maintenance"),
    ("subestacoes-medicao", "instrument transformer current voltage measurement accuracy"),
    # ---- SOLAR (preenchendo lacunas) ----
    ("solar-celulas", "TOPCon solar cell efficiency passivation"),
    ("solar-celulas", "heterojunction HJT silicon solar cell"),
    ("solar-inversores", "grid-forming inverter photovoltaic control"),
    ("solar-inversores", "photovoltaic inverter reliability lifetime"),
    ("solar-previsao", "solar irradiance forecasting deep learning"),
    ("solar-faults", "photovoltaic array fault detection machine learning"),
    ("solar-armazenamento", "battery energy storage photovoltaic sizing optimization"),
    ("solar-mppt", "maximum power point tracking partial shading photovoltaic"),
    # ---- ENGENHARIA ELÉTRICA AMPLA ----
    ("ee-qualidade-energia", "power quality harmonics distribution network mitigation"),
    ("ee-sep", "optimal power flow distribution system"),
    ("ee-sep", "power system state estimation distribution"),
    ("ee-maquinas", "induction motor fault diagnosis condition monitoring"),
    ("ee-eletronica-potencia", "multilevel inverter topology renewable"),
    ("ee-microrredes", "microgrid energy management control review"),
    ("ee-protecao-gd", "protection distributed generation distribution network"),
]


def slug(texto: str, n: int = 64) -> str:
    t = re.sub(r"[^a-zA-Z0-9]+", "-", (texto or "").lower()).strip("-")
    return t[:n].strip("-")


def http_get(url: str, timeout: int = 40) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def existentes() -> set[str]:
    """Slugs dos arquivos já presentes (dedupe contra a base inteira)."""
    s = set()
    if LIVROS.exists():
        for p in LIVROS.rglob("*.pdf"):
            s.add(slug(p.stem))
    return s


def buscar_openalex(query: str, per_page: int = 25) -> list[dict]:
    base = "https://api.openalex.org/works"
    qs = urllib.parse.urlencode({
        "search": query,
        "filter": "open_access.is_oa:true",
        "per-page": per_page,
        "mailto": EMAIL,
    })
    try:
        data = json.loads(http_get(f"{base}?{qs}"))
    except Exception as e:  # noqa: BLE001
        print(f"   [openalex erro] {e}", flush=True)
        return []
    out = []
    for w in data.get("results", []):
        loc = w.get("best_oa_location") or {}
        pdf = loc.get("pdf_url") or (w.get("open_access") or {}).get("oa_url")
        if not pdf:
            continue
        out.append({
            "titulo": w.get("title") or "sem-titulo",
            "ano": w.get("publication_year") or "",
            "pdf": pdf,
            "fonte": "OpenAlex",
        })
    return out


def buscar_arxiv(query: str, max_results: int = 15) -> list[dict]:
    base = "http://export.arxiv.org/api/query"
    qs = urllib.parse.urlencode({
        "search_query": f"all:{query}",
        "start": 0,
        "max_results": max_results,
        "sortBy": "relevance",
    })
    try:
        xml = http_get(f"{base}?{qs}")
    except Exception as e:  # noqa: BLE001
        print(f"   [arxiv erro] {e}", flush=True)
        return []
    ns = {"a": "http://www.w3.org/2005/Atom"}
    out = []
    try:
        root = ET.fromstring(xml)
    except Exception:  # noqa: BLE001
        return []
    for e in root.findall("a:entry", ns):
        idu = (e.findtext("a:id", default="", namespaces=ns) or "")
        titulo = (e.findtext("a:title", default="", namespaces=ns) or "").strip()
        ano = (e.findtext("a:published", default="", namespaces=ns) or "")[:4]
        pdf = ""
        for ln in e.findall("a:link", ns):
            if ln.get("title") == "pdf" or ln.get("type") == "application/pdf":
                pdf = ln.get("href", "")
        if not pdf and "/abs/" in idu:
            pdf = idu.replace("/abs/", "/pdf/")
        if pdf:
            out.append({"titulo": titulo, "ano": ano, "pdf": pdf, "fonte": "arXiv"})
    return out


def baixar(url: str, destino: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                   "Accept": "application/pdf,*/*"})
        with urllib.request.urlopen(req, timeout=90) as r:
            dados = r.read()
    except Exception:  # noqa: BLE001
        return False
    if len(dados) < MIN_BYTES or dados[:5] != b"%PDF-":
        return False
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_bytes(dados)
    return True


def main() -> None:
    vistos = existentes()
    print(f"Base já tem {len(vistos)} PDFs (dedupe ativo).", flush=True)
    total = 0
    for i, (tema, query) in enumerate(CONSULTAS, 1):
        if total >= TETO_GLOBAL:
            print("Teto global atingido.", flush=True)
            break
        print(f"\n[{i}/{len(CONSULTAS)}] {tema} :: {query}", flush=True)
        candidatos = buscar_openalex(query, 50)
        time.sleep(2)                      # respeita rate-limit do arXiv
        candidatos += buscar_arxiv(query)
        print(f"   {len(candidatos)} candidatos", flush=True)
        baixados = 0
        for c in candidatos:
            if baixados >= POR_CONSULTA or total >= TETO_GLOBAL:
                break
            sl = slug(c["titulo"])
            if not sl or sl in vistos:
                continue
            nome = f"EN-{c['fonte']}-{c['ano']}-{sl}.pdf"
            destino = ART / tema / nome
            if baixar(c["pdf"], destino):
                vistos.add(sl)
                baixados += 1
                total += 1
                print(f"   OK  {tema}/{nome[:70]}", flush=True)
            time.sleep(0.4)
        print(f"   => {baixados} baixados (total {total})", flush=True)
        time.sleep(1.0)
    print(f"\n=== FIM: {total} PDFs novos baixados ===", flush=True)


if __name__ == "__main__":
    main()
