# OCR de normas escaneadas — gera PDF pesquisável no lugar do original.
# Originais ficam em livros_normas/originais-escaneados/.
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

os.environ["PATH"] = (
    r"C:\Program Files\Tesseract-OCR;C:\Program Files\gs\gs10.07.1\bin;"
    + os.environ["PATH"]
)
os.environ["TESSDATA_PREFIX"] = r"D:\Coding\engelet\rag-tool\ocr\tessdata"

DIR = Path(r"D:\Coding\engelet\livros_normas\normas-web-oficiais")
BACKUP = Path(r"D:\Coding\engelet\livros_normas\originais-escaneados")
BACKUP.mkdir(exist_ok=True)

ARQUIVOS = [
    "844982701-NBR-17193-SEGURANCA-CONTRA-INCENDIOS-EM-INSTALACOES-FOTOVOLTAICAS.pdf",
    "pdfcoffee.com_nbr-iec-62116-2012-8-pdf-free.pdf",
    "pdfcoffee.com_nbr-15749-malha-de-aterramentopdf-pdf-free.pdf",
    "pdfcoffee.com_nbr-6855-2018-transformador-de-potencial-indutivo-pdf-free.pdf",
    "pdfcoffee.com_nbr-14039-pdf-free.pdf",
    "pdfcoffee.com_nbr-5356-completa-1a5-pdf-free.pdf",
]


def log(msg: str) -> None:
    print(f"[{time.strftime('%H:%M:%S')}] {msg}", flush=True)


falhas = []
for nome in ARQUIVOS:
    entrada = DIR / nome
    saida = entrada.with_suffix(".ocr-tmp.pdf")
    log(f"=== OCR: {nome}")
    proc = subprocess.run(
        [sys.executable, "-m", "ocrmypdf",
         "--force-ocr", "-l", "por", "--output-type", "pdf",
         "--optimize", "1", str(entrada), str(saida)],
    )
    if proc.returncode == 0 and saida.exists():
        shutil.move(str(entrada), str(BACKUP / nome))
        shutil.move(str(saida), str(entrada))
        log(f"=== OK: {nome}")
    else:
        falhas.append(nome)
        log(f"=== FALHOU (exit {proc.returncode}): {nome}")
        saida.unlink(missing_ok=True)

log(f"Concluído. Falhas: {falhas or 'nenhuma'}")
