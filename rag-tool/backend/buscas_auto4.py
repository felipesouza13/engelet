"""4ª onda — tema ATERRAMENTO / SPDA / RESISTIVIDADE DO SOLO (acadêmica, PT+EN).
Reusa helpers de buscas.py (dedupe por destino.exists). Sem Tavily."""
from __future__ import annotations
import time
from buscas import buscar_openalex, buscar_arxiv, baixar, slug, ART, _existentes

POR_CONSULTA = 14
TETO_GLOBAL = 280

CONSULTAS: list[tuple[str, str]] = [
    # Malha de terra / subestação
    ("aterramento-malha", "substation grounding grid design optimization safety"),
    ("aterramento-malha", "ground grid step touch voltage IEEE 80 analysis"),
    ("aterramento-malha", "grounding system finite element method soil"),
    ("aterramento-malha", "ground grid corrosion mitigation copper"),
    # Resistividade / estratificação do solo
    ("aterramento-resistividade", "soil resistivity measurement Wenner method"),
    ("aterramento-resistividade", "soil stratification two layer model grounding"),
    ("aterramento-resistividade", "soil resistivity seasonal variation moisture"),
    # Impedância / transitórios / alta frequência
    ("aterramento-transitorio", "grounding electrode impedance high frequency lightning"),
    ("aterramento-transitorio", "soil ionization grounding transient impulse"),
    ("aterramento-transitorio", "tower footing resistance transmission line lightning"),
    # SPDA / descargas atmosféricas
    ("spda-descargas", "lightning protection system design risk assessment"),
    ("spda-descargas", "lightning electromagnetic transient grounding simulation"),
    ("spda-descargas", "down conductor earth termination lightning protection"),
    ("spda-descargas", "surge protective device coordination grounding"),
    # Brasil (PT)
    ("br-aterramento", "aterramento malha de terra subestação dimensionamento"),
    ("br-aterramento", "resistividade do solo estratificação método de Wenner"),
    ("br-aterramento", "tensão de passo e de toque segurança aterramento"),
    ("br-spda", "SPDA proteção contra descargas atmosféricas edificações"),
    ("br-aterramento", "aterramento de torres linha de transmissão impulso atmosférico"),
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
    print(f"\n=== FIM 4a onda (aterramento/SPDA): {total} novos ===", flush=True)


if __name__ == "__main__":
    main()
