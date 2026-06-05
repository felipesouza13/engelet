"""2ª onda de busca em massa — OpenAlex só (multilíngue, PT+EN), subtemas profundos.
Reusa as funções de buscas_auto.py."""
from __future__ import annotations
import time
from buscas_auto import (buscar_openalex, baixar, existentes, slug, ART,
                         POR_CONSULTA, TETO_GLOBAL)

CONSULTAS: list[tuple[str, str]] = [
    # Subestações — subtemas profundos
    ("subestacoes-protecao", "numerical relay testing commissioning protection"),
    ("subestacoes-protecao", "recloser sectionalizer distribution protection coordination"),
    ("subestacoes-protecao", "adaptive protection smart grid microgrid"),
    ("subestacoes-transformadores", "transformer protection differential inrush restraint"),
    ("subestacoes-transformadores", "on-load tap changer monitoring diagnostics"),
    ("subestacoes-transformadores", "distribution transformer loss efficiency design"),
    ("subestacoes-aterramento", "soil resistivity measurement grounding system"),
    ("subestacoes-spda", "lightning protection system structures risk"),
    ("subestacoes-arco-eletrico", "arc flash hazard analysis electrical safety"),
    ("subestacoes-comissionamento", "substation commissioning testing acceptance"),
    ("subestacoes-manobra", "switching overvoltage transient power system"),
    # Português (OpenAlex multilíngue → literatura BR)
    ("br-subestacoes", "subestação proteção sistema elétrico potência"),
    ("br-aterramento", "aterramento malha de terra segurança subestação"),
    ("br-solar", "energia solar fotovoltaica geração distribuída Brasil"),
    ("br-solar", "sistema fotovoltaico desempenho perdas eficiência"),
    ("br-qualidade", "qualidade de energia elétrica harmônicos distribuição"),
    ("br-protecao", "proteção sistemas elétricos relés coordenação"),
    # Solar — subtemas profundos
    ("solar-degradacao", "photovoltaic module degradation field reliability outdoor"),
    ("solar-reciclagem", "photovoltaic module recycling end of life circular"),
    ("solar-flutuante", "floating photovoltaic system performance water"),
    ("solar-perovskita", "perovskite solar cell stability encapsulation"),
    ("solar-om", "photovoltaic operation maintenance performance ratio"),
    # EE ampla — subtemas
    ("ee-estabilidade", "power system transient stability assessment"),
    ("ee-hvdc", "HVDC transmission control converter station"),
    ("ee-facts", "FACTS reactive power compensation voltage"),
    ("ee-smartgrid", "smart grid distribution automation self-healing"),
    ("ee-eletronica-potencia", "DC-DC converter renewable energy control"),
    ("ee-maquinas", "permanent magnet synchronous machine drive control"),
    ("ee-armazenamento", "grid scale energy storage technologies review"),
]


def main() -> None:
    vistos = existentes()
    print(f"Base já tem {len(vistos)} PDFs (dedupe ativo).", flush=True)
    total = 0
    for i, (tema, query) in enumerate(CONSULTAS, 1):
        if total >= TETO_GLOBAL:
            print("Teto global atingido."); break
        print(f"\n[{i}/{len(CONSULTAS)}] {tema} :: {query}", flush=True)
        candidatos = buscar_openalex(query, 60)
        print(f"   {len(candidatos)} candidatos", flush=True)
        baixados = 0
        for c in candidatos:
            if baixados >= POR_CONSULTA or total >= TETO_GLOBAL:
                break
            sl = slug(c["titulo"])
            if not sl or sl in vistos:
                continue
            nome = f"{c['fonte']}-{c['ano']}-{sl}.pdf"
            if baixar(c["pdf"], ART / tema / nome):
                vistos.add(sl); baixados += 1; total += 1
                print(f"   OK  {tema}/{nome[:70]}", flush=True)
            time.sleep(0.4)
        print(f"   => {baixados} baixados (total {total})", flush=True)
        time.sleep(0.8)
    print(f"\n=== FIM 2a onda: {total} PDFs novos ===", flush=True)


if __name__ == "__main__":
    main()
