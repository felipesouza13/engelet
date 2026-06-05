"""
OCR de PDFs escaneados via ocrmypdf (instalado no Python global, fora do venv).

Gera um PDF pesquisável no lugar do original; o original vai para
livros_normas/originais-escaneados/ (preservando subpastas).
"""
from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import rag

# Python global com ocrmypdf instalado (o venv do backend não tem).
PYTHON_OCR = os.environ.get("RAG_OCR_PYTHON", r"C:\Python314\python.exe")
TESSDATA = Path(__file__).resolve().parents[1] / "ocr" / "tessdata"
BACKUP_DIR = "originais-escaneados"  # subpasta de livros_normas (excluída da listagem)


def _env_ocr() -> dict:
    env = os.environ.copy()
    env["PATH"] = (
        r"C:\Program Files\Tesseract-OCR;C:\Program Files\gs\gs10.07.1\bin;"
        + env["PATH"]
    )
    env["TESSDATA_PREFIX"] = str(TESSDATA)
    return env


def ocr_arquivo(rel: str) -> dict:
    """
    Roda OCR em livros_normas/<rel>. Em caso de sucesso, substitui o arquivo
    pelo PDF pesquisável e guarda o original em originais-escaneados/<rel>.

    Retorna {"ok": bool, "msg": str}.
    """
    entrada = rag.LIVROS / rel
    if not entrada.exists():
        return {"ok": False, "msg": "Arquivo não encontrado."}
    if entrada.suffix.lower() != ".pdf":
        return {"ok": False, "msg": "OCR só se aplica a PDF."}

    saida = entrada.with_suffix(".ocr-tmp.pdf")
    try:
        proc = subprocess.run(
            [PYTHON_OCR, "-m", "ocrmypdf",
             "--force-ocr", "-l", "por", "--output-type", "pdf",
             "--optimize", "1", str(entrada), str(saida)],
            env=_env_ocr(), capture_output=True, text=True, errors="ignore",
        )
    except OSError as e:
        return {"ok": False, "msg": f"Falha ao executar ocrmypdf: {e}"}

    if proc.returncode != 0 or not saida.exists():
        saida.unlink(missing_ok=True)
        detalhe = (proc.stderr or proc.stdout or "").strip().splitlines()
        detalhe = detalhe[-1] if detalhe else ""
        return {"ok": False, "msg": f"ocrmypdf exit {proc.returncode}. {detalhe}"}

    backup = rag.LIVROS / BACKUP_DIR / rel
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(entrada), str(backup))
    shutil.move(str(saida), str(entrada))
    return {"ok": True, "msg": "OCR concluído."}
