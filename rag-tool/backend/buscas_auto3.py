"""3ª onda autônoma (back) — acadêmica (OpenAlex+arXiv), consultas novas/profundas.
Roda em paralelo à busca web do front; reusa helpers de buscas.py (dedupe por
destino.exists). SEM Tavily (não consome créditos do usuário)."""
from __future__ import annotations
import time
from buscas import buscar_openalex, buscar_arxiv, baixar, slug, ART, _existentes

POR_CONSULTA = 12
TETO_GLOBAL = 500

CONSULTAS: list[tuple[str, str]] = [
    # Subestações — ângulos novos
    ("subestacoes-transformadores", "power transformer bushing failure diagnosis"),
    ("subestacoes-transformadores", "power transformer thermal model hot spot"),
    ("subestacoes-protecao", "current transformer saturation protection relay"),
    ("subestacoes-protecao", "synchrophasor PMU wide area protection"),
    ("subestacoes-protecao", "fault location distribution network method"),
    ("subestacoes-gis-sf6", "GIS very fast transient overvoltage"),
    ("subestacoes-gis-sf6", "SF6 decomposition circuit breaker arcing"),
    ("subestacoes-ciberseguranca", "IEC 62351 substation cyber security"),
    ("subestacoes-aterramento", "substation grounding transient lightning impulse"),
    ("subestacoes-confiabilidade", "power transformer asset management life cycle"),
    # Solar — ângulos novos
    ("solar-bifacial", "bifacial photovoltaic energy yield modeling"),
    ("solar-pid", "potential induced degradation photovoltaic mechanism"),
    ("solar-tracker", "solar tracker control algorithm backtracking"),
    ("solar-antiilhamento", "photovoltaic inverter anti-islanding detection"),
    ("solar-flutuante", "floating photovoltaic thermal performance review"),
    ("solar-soiling", "photovoltaic soiling cleaning robot loss"),
    ("solar-eletroluminescencia", "electroluminescence imaging photovoltaic crack defect"),
    ("solar-curva-iv", "photovoltaic IV curve characterization outdoor"),
    # EE ampla — ângulos novos
    ("ee-qualidade-energia", "voltage sag mitigation dynamic voltage restorer"),
    ("ee-qualidade-energia", "harmonic resonance distribution capacitor"),
    ("ee-facts", "STATCOM SVC reactive power voltage control"),
    ("ee-sep", "distribution network reconfiguration optimization loss"),
    ("ee-eletronica-potencia", "grid-connected inverter LCL filter control"),
    ("ee-protecao-gd", "fault current distributed generation protection coordination"),
    # Brasil (PT) — ângulos novos
    ("br-solar", "sistema fotovoltaico flutuante reservatório Brasil"),
    ("br-solar", "proteção sistema fotovoltaico cabine primária média tensão"),
    ("br-subestacoes", "religador rede de distribuição proteção"),
    ("br-armazenamento", "armazenamento de energia baterias rede elétrica"),
    ("br-microrredes", "microrredes ilhadas controle gerenciamento"),
    ("br-maquinas", "máquina de indução diagnóstico de falhas"),
]


def main() -> None:
    vistos = _existentes()
    print(f"Base já tem {len(vistos)} arquivos (dedupe ativo).", flush=True)
    total = 0
    for i, (tema, q) in enumerate(CONSULTAS, 1):
        if total >= TETO_GLOBAL:
            break
        print(f"\n[{i}/{len(CONSULTAS)}] {tema} :: {q}", flush=True)
        cand = buscar_openalex(q, 60)
        time.sleep(1.5)
        cand += buscar_arxiv(q)
        baixados = 0
        for c in cand:
            if baixados >= POR_CONSULTA or total >= TETO_GLOBAL:
                break
            sl = slug(c["titulo"] or c["url"])
            if not sl or sl in vistos:
                continue
            vistos.add(sl)
            destino = ART / tema / f"{c['fonte']}-{c.get('ano','')}-{sl}.pdf"
            if destino.exists():
                continue
            if baixar(c["url"], destino):
                baixados += 1; total += 1
                print(f"   OK  {tema}/{destino.name[:64]}", flush=True)
            time.sleep(0.3)
        print(f"   => {baixados} (total {total})", flush=True)
        time.sleep(0.6)
    print(f"\n=== FIM 3a onda: {total} novos ===", flush=True)


if __name__ == "__main__":
    main()
