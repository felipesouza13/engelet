"""
API FastAPI da ferramenta de RAG.

Endpoints:
  GET  /api/arquivos              -> lista arquivos de livros_normas + status
  POST /api/arquivos/status       -> {path, status} aprova/reprova/reseta
  POST /api/arquivos/status_lote  -> {paths, status} em lote
  POST /api/indexar/iniciar       -> dispara indexação dos APROVADOS (background)
  GET  /api/indexar/status        -> progresso atual (polling)
  POST /api/consultar             -> {pergunta, k} busca semântica (teste)
"""
from __future__ import annotations

import threading

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import rag
import buscas
import ocr_service

app = FastAPI(title="RAG livros_normas")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/arquivos")
def get_arquivos():
    return rag.listar_arquivos()


class StatusBody(BaseModel):
    path: str
    status: str  # "pendente" | "aprovado" | "indexado"


@app.post("/api/arquivos/status")
def post_status(body: StatusBody):
    if body.status not in {"pendente", "aprovado", "reprovado", "indexado"}:
        return {"ok": False, "erro": "status inválido"}
    rag.definir_status(body.path, body.status)
    return {"ok": True}


class StatusLoteBody(BaseModel):
    paths: list[str]
    status: str


@app.post("/api/arquivos/status_lote")
def post_status_lote(body: StatusLoteBody):
    if body.status not in {"pendente", "aprovado", "reprovado", "indexado"}:
        return {"ok": False, "erro": "status inválido"}
    for p in body.paths:
        rag.definir_status(p, body.status)
    return {"ok": True, "total": len(body.paths)}


# ---------------------------------------------------------------------------
# Indexação em background + progresso consultável por polling.
# Robusto contra quedas de conexão / fechar a aba: o worker roda no servidor
# e o front apenas consulta /api/indexar/status periodicamente.
# ---------------------------------------------------------------------------
_prog_lock = threading.Lock()
_progresso: dict = {
    "rodando": False,
    "terminado": False,
    "total_arquivos": 0,
    "arquivos_feitos": 0,
    "chunks_acum": 0,
    "atual": None,
    "log": [],
}


def _on_evt(e: dict) -> None:
    with _prog_lock:
        t = e["tipo"]
        if t == "inicio":
            _progresso["total_arquivos"] = e["total_arquivos"]
            _progresso["log"].append(f"Iniciando: {e['total_arquivos']} arquivo(s).")
        elif t == "extraindo":
            _progresso["atual"] = {
                "path": e["path"], "fase": "extraindo",
                "pagina": e.get("pagina", 0), "paginas": e.get("paginas", 0),
                "chunkNo": 0, "chunksArq": 0,
            }
        elif t == "arquivo":
            _progresso["atual"] = {
                "path": e["path"], "fase": "embeddings",
                "chunkNo": 0, "chunksArq": e["chunks"],
            }
            _progresso["log"].append(f"📄 {e['path']} — {e['chunks']} chunk(s).")
        elif t == "chunk":
            _progresso["arquivos_feitos"] = e["arquivos_feitos"]
            _progresso["chunks_acum"] = e["chunks_acumulados"]
            _progresso["atual"] = {
                "path": e["path"], "fase": "embeddings",
                "chunkNo": e["chunk_no_arquivo"], "chunksArq": e["chunks_no_arquivo"],
            }
        elif t == "arquivo_fim":
            _progresso["arquivos_feitos"] = e["arquivos_feitos"]
            _progresso["chunks_acum"] = e["chunks_acumulados"]
            _progresso["atual"] = None
        elif t == "erro":
            _progresso["log"].append(f"⚠️ Erro em {e.get('path', '?')}: {e.get('msg', '')}")
        if len(_progresso["log"]) > 300:
            _progresso["log"] = _progresso["log"][-300:]


@app.post("/api/indexar/iniciar")
def iniciar_indexacao():
    with _prog_lock:
        if _progresso["rodando"]:
            return {"ok": False, "erro": "Indexação já está em execução."}
        _progresso.update(
            rodando=True, terminado=False, total_arquivos=0,
            arquivos_feitos=0, chunks_acum=0, atual=None, log=[],
        )
    aprovados = rag.arquivos_aprovados()
    if not aprovados:
        with _prog_lock:
            _progresso.update(rodando=False, terminado=True)
            _progresso["log"].append("Nenhum arquivo aprovado.")
        return {"ok": True, "total": 0}

    def worker():
        try:
            rag.indexar(aprovados, progresso=_on_evt)
        except Exception as e:  # noqa: BLE001
            with _prog_lock:
                _progresso["log"].append(f"⚠️ Falha geral: {e}")
        finally:
            with _prog_lock:
                _progresso["rodando"] = False
                _progresso["terminado"] = True
                _progresso["atual"] = None
                _progresso["log"].append("✅ Concluído.")

    threading.Thread(target=worker, daemon=True).start()
    return {"ok": True, "total": len(aprovados)}


@app.get("/api/indexar/status")
def status_indexacao():
    with _prog_lock:
        return {
            "rodando": _progresso["rodando"],
            "terminado": _progresso["terminado"],
            "total_arquivos": _progresso["total_arquivos"],
            "arquivos_feitos": _progresso["arquivos_feitos"],
            "chunks_acum": _progresso["chunks_acum"],
            "atual": _progresso["atual"],
            "log": list(_progresso["log"]),
        }


# ---------------------------------------------------------------------------
# Busca em massa na web (OpenAlex + arXiv + Tavily) — mesmo padrão de job/polling.
# ---------------------------------------------------------------------------
_busca_lock = threading.Lock()
_busca_cancelar = {"flag": False}
_busca_prog: dict = {
    "rodando": False,
    "terminado": False,
    "total_consultas": 0,
    "consultas_feitas": 0,
    "baixados": 0,
    "atual": None,
    "log": [],
}


def _on_evt_busca(e: dict) -> None:
    with _busca_lock:
        t = e["tipo"]
        if t == "inicio":
            _busca_prog["total_consultas"] = e["total_consultas"]
            _busca_prog["log"].append(f"Iniciando: {e['total_consultas']} consulta(s).")
        elif t == "consulta":
            _busca_prog["atual"] = {
                "query": e["query"], "tema": e["tema"], "modo": e["modo"],
                "indice": e["indice"], "total": e["total_consultas"],
            }
        elif t == "encontrados":
            _busca_prog["log"].append(f"🔎 {e['query'][:60]} — {e['n']} candidato(s).")
        elif t == "download":
            if e["ok"]:
                _busca_prog["log"].append(f"   ✅ {e['arquivo'][:70]}")
        elif t == "consulta_fim":
            _busca_prog["consultas_feitas"] = e["consultas_feitas"]
            _busca_prog["baixados"] = e["total_baixados"]
            _busca_prog["log"].append(
                f"→ {e['tema']}: {e['baixados']} baixado(s) (total {e['total_baixados']}).")
        elif t == "erro":
            _busca_prog["log"].append(f"⚠️ {e.get('query', '')}: {e.get('msg', '')}")
        if len(_busca_prog["log"]) > 400:
            _busca_prog["log"] = _busca_prog["log"][-400:]


class BuscaConfigBody(BaseModel):
    provider: str = "tavily"
    api_key: str


@app.post("/api/busca/config")
def post_busca_config(body: BuscaConfigBody):
    buscas.salvar_config(body.provider, body.api_key.strip())
    return {"ok": True}


@app.get("/api/busca/config")
def get_busca_config():
    cfg = buscas.carregar_config()
    return {"provider": cfg.get("provider", "tavily"), "tem_chave": bool(cfg.get("api_key"))}


class BuscaBody(BaseModel):
    eixos: list[str]
    usar_web: bool = False
    max_por_consulta: int = 30


@app.post("/api/buscar/iniciar")
def iniciar_busca(body: BuscaBody):
    with _busca_lock:
        if _busca_prog["rodando"]:
            return {"ok": False, "erro": "Busca já está em execução."}
        _busca_cancelar["flag"] = False
        _busca_prog.update(rodando=True, terminado=False, total_consultas=0,
                           consultas_feitas=0, baixados=0, atual=None, log=[])
    if body.usar_web and not buscas.tem_chave():
        with _busca_lock:
            _busca_prog.update(rodando=False, terminado=True)
            _busca_prog["log"].append("Sem chave Tavily — busca web desativada.")
        return {"ok": False, "erro": "Sem chave Tavily configurada."}

    cfg = {"eixos": body.eixos, "usar_web": body.usar_web,
           "max_por_consulta": body.max_por_consulta}

    def worker():
        try:
            buscas.buscar_em_massa(cfg, progresso=_on_evt_busca,
                                   cancelado=lambda: _busca_cancelar["flag"])
        except Exception as e:  # noqa: BLE001
            with _busca_lock:
                _busca_prog["log"].append(f"⚠️ Falha geral: {e}")
        finally:
            with _busca_lock:
                _busca_prog["rodando"] = False
                _busca_prog["terminado"] = True
                _busca_prog["atual"] = None
                _busca_prog["log"].append("✅ Busca concluída.")

    threading.Thread(target=worker, daemon=True).start()
    return {"ok": True}


@app.get("/api/buscar/status")
def status_busca():
    with _busca_lock:
        return {
            "rodando": _busca_prog["rodando"],
            "terminado": _busca_prog["terminado"],
            "total_consultas": _busca_prog["total_consultas"],
            "consultas_feitas": _busca_prog["consultas_feitas"],
            "baixados": _busca_prog["baixados"],
            "atual": _busca_prog["atual"],
            "log": list(_busca_prog["log"]),
        }


@app.post("/api/buscar/parar")
def parar_busca():
    _busca_cancelar["flag"] = True
    return {"ok": True}


# ---------------------------------------------------------------------------
# OCR em background (ocrmypdf) — mesmo padrão de job/polling.
# ---------------------------------------------------------------------------
_ocr_lock = threading.Lock()
_ocr_cancelar = {"flag": False}
_ocr_prog: dict = {
    "rodando": False,
    "terminado": False,
    "total": 0,
    "feitos": 0,
    "sucesso": 0,
    "atual": None,
    "log": [],
}


class OcrBody(BaseModel):
    paths: list[str]


@app.post("/api/ocr/iniciar")
def iniciar_ocr(body: OcrBody):
    paths = [p for p in body.paths if p.lower().endswith(".pdf")]
    if not paths:
        return {"ok": False, "erro": "Nenhum PDF informado."}
    with _ocr_lock:
        if _ocr_prog["rodando"]:
            return {"ok": False, "erro": "OCR já está em execução."}
        _ocr_cancelar["flag"] = False
        _ocr_prog.update(rodando=True, terminado=False, total=len(paths),
                         feitos=0, sucesso=0, atual=None, log=[])
        _ocr_prog["log"].append(f"Iniciando OCR de {len(paths)} arquivo(s).")

    def worker():
        try:
            for rel in paths:
                if _ocr_cancelar["flag"]:
                    with _ocr_lock:
                        _ocr_prog["log"].append("⛔ Cancelado pelo usuário.")
                    break
                with _ocr_lock:
                    _ocr_prog["atual"] = rel
                r = ocr_service.ocr_arquivo(rel)
                with _ocr_lock:
                    _ocr_prog["feitos"] += 1
                    if r["ok"]:
                        _ocr_prog["sucesso"] += 1
                        _ocr_prog["log"].append(f"✅ {rel}")
                    else:
                        _ocr_prog["log"].append(f"⚠️ {rel}: {r['msg']}")
        except Exception as e:  # noqa: BLE001
            with _ocr_lock:
                _ocr_prog["log"].append(f"⚠️ Falha geral: {e}")
        finally:
            with _ocr_lock:
                _ocr_prog["rodando"] = False
                _ocr_prog["terminado"] = True
                _ocr_prog["atual"] = None
                _ocr_prog["log"].append(
                    f"Concluído: {_ocr_prog['sucesso']}/{_ocr_prog['feitos']} com sucesso.")

    threading.Thread(target=worker, daemon=True).start()
    return {"ok": True, "total": len(paths)}


@app.get("/api/ocr/status")
def status_ocr():
    with _ocr_lock:
        return {
            "rodando": _ocr_prog["rodando"],
            "terminado": _ocr_prog["terminado"],
            "total": _ocr_prog["total"],
            "feitos": _ocr_prog["feitos"],
            "sucesso": _ocr_prog["sucesso"],
            "atual": _ocr_prog["atual"],
            "log": list(_ocr_prog["log"]),
        }


@app.post("/api/ocr/parar")
def parar_ocr():
    _ocr_cancelar["flag"] = True
    return {"ok": True}


class ConsultaBody(BaseModel):
    pergunta: str
    k: int = 5


@app.post("/api/consultar")
def post_consultar(body: ConsultaBody):
    return rag.consultar(body.pergunta, body.k)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8077)
