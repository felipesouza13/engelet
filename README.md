# RAG · livros_normas — Base de conhecimento de normas de engenharia elétrica

RAG (Retrieval-Augmented Generation) local com normas técnicas de engenharia elétrica
brasileiras: NBR, ABNT NBR IEC, PRODIST/ANEEL, normas da Equatorial Goiás (NTs),
NRs do MTE, INMETRO e material correlato (datasheets, artigos, livros).

**Para quem está integrando:** a forma recomendada de consumir esta base é a
**API HTTP de consulta semântica** (seção [Integração em outro projeto](#integração-em-outro-projeto)).
Você manda uma pergunta em PT-BR, recebe os trechos mais relevantes do corpus com a
fonte de cada um.

---

## Visão geral

```
engelet/
├── livros_normas/            # corpus: PDFs, DOCX, MD, TXT (subpastas varridas)
│   ├── normas-web-oficiais/  #   normas baixadas da web
│   ├── buscas-web/           #   resultados de busca em massa (Tavily/OpenAlex/arXiv)
│   └── originais-escaneados/ #   backups pré-OCR (IGNORADA pela varredura)
└── rag-tool/
    ├── backend/              # FastAPI · porta 8077
    │   ├── main.py           #   API (arquivos, indexação, OCR, busca web, consulta)
    │   ├── rag.py            #   extração → chunking → embeddings → ChromaDB
    │   ├── ocr_service.py    #   OCR de PDFs escaneados (ocrmypdf + Tesseract)
    │   ├── buscas.py         #   busca em massa na web
    │   ├── chroma_db/        #   índice vetorial (gerado, fora do git)
    │   └── estado.json       #   status por arquivo (gerado, fora do git)
    ├── frontend/             # React + Vite · porta 5174 (curadoria, opcional)
    └── ocr/                  # toolchain de OCR (tessdata local + script standalone)
```

**Stack:** FastAPI + ChromaDB (persistente, cosine) + `sentence-transformers`
com `intfloat/multilingual-e5-small` (multilíngue, bom em PT-BR). Tudo local,
sem chamadas a APIs pagas para indexar/consultar.

**Pipeline:** arquivos entram em `livros_normas/` → curadoria (aprovar/rejeitar
na interface ou via API) → indexação (extração de texto, chunks de 1000 chars com
overlap de 200, embeddings, ChromaDB) → consulta semântica.

> ⚠️ O índice (`chroma_db/`) e o estado (`estado.json`) **não são versionados**.
> Quem clona o repositório precisa rodar a indexação uma vez (ou apontar para um
> backend já em execução que tenha o índice).

---

## Como rodar

### Backend (obrigatório)

```powershell
cd rag-tool/backend
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py            # http://127.0.0.1:8077
```

Na primeira indexação/consulta o modelo de embeddings (~470 MB) é baixado do
Hugging Face automaticamente.

### Frontend (opcional — só para curadoria visual)

```powershell
cd rag-tool/frontend
npm install
npm run dev               # http://localhost:5174 (proxy de /api para :8077)
```

---

## Integração em outro projeto

### Endpoint principal: `POST /api/consultar`

```http
POST http://127.0.0.1:8077/api/consultar
Content-Type: application/json

{ "pergunta": "seção mínima do condutor de proteção em baixa tensão", "k": 5 }
```

Resposta — lista dos `k` chunks mais próximos, ordenados por relevância:

```json
[
  {
    "texto": "…trecho do documento (até ~1000 caracteres)…",
    "path": "normas-web-oficiais/694576894-NBR5410-Proposta-2023.pdf",
    "distancia": 0.1834
  }
]
```

- `texto` — conteúdo do chunk (use como contexto no prompt do seu LLM).
- `path` — arquivo de origem, relativo a `livros_normas/` (use como citação).
- `distancia` — distância cosseno (menor = mais relevante; < 0,25 costuma ser bom).

### Exemplo em Python

```python
import requests

def consultar_rag(pergunta: str, k: int = 5) -> list[dict]:
    r = requests.post(
        "http://127.0.0.1:8077/api/consultar",
        json={"pergunta": pergunta, "k": k},
        timeout=60,
    )
    r.raise_for_status()
    return r.json()

contexto = consultar_rag("requisitos de aterramento de subestação de média tensão")
for c in contexto:
    print(f"[{c['distancia']:.3f}] {c['path']}\n{c['texto'][:200]}\n")
```

### Exemplo em JavaScript/TypeScript

```js
async function consultarRag(pergunta, k = 5) {
  const res = await fetch("http://127.0.0.1:8077/api/consultar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ pergunta, k }),
  });
  if (!res.ok) throw new Error(`RAG: HTTP ${res.status}`);
  return res.json();
}
```

### Padrão de uso com LLM (RAG clássico)

1. Recebe a pergunta do usuário.
2. `POST /api/consultar` com a pergunta (k entre 5 e 10).
3. Monta o prompt: pergunta + chunks como contexto, citando `path` de cada um.
4. Instrui o LLM a responder **somente com base no contexto** e citar as fontes.

### Acesso direto ao ChromaDB (alternativa sem HTTP)

Se o seu projeto roda na mesma máquina e prefere ler o índice diretamente:

- Caminho: `rag-tool/backend/chroma_db/` · coleção: `livros_normas` · espaço: cosine.
- **Atenção:** o modelo e5 exige prefixos — os documentos foram indexados como
  `"passage: <texto>"`; toda query precisa ser embedada como `"query: <pergunta>"`
  com `intfloat/multilingual-e5-small` e `normalize_embeddings=True`.
  Sem os prefixos a relevância degrada bastante.
- Não escreva na coleção por fora — a indexação é responsabilidade deste projeto.

```python
import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("intfloat/multilingual-e5-small")
col = chromadb.PersistentClient(path="rag-tool/backend/chroma_db").get_collection("livros_normas")
vetor = model.encode(["query: limites de tensão em regime permanente PRODIST"],
                     normalize_embeddings=True).tolist()
res = col.query(query_embeddings=vetor, n_results=5)
```

---

## Referência da API

| Método | Rota | Corpo | Descrição |
|---|---|---|---|
| GET | `/api/arquivos` | — | Lista arquivos do corpus com `status` (`pendente`/`aprovado`/`reprovado`/`indexado`), `extraivel`, `chunks` |
| POST | `/api/arquivos/status` | `{path, status}` | Define status de um arquivo |
| POST | `/api/arquivos/status_lote` | `{paths, status}` | Idem, em lote |
| POST | `/api/indexar/iniciar` | — | Indexa todos os **aprovados** (job em background) |
| GET | `/api/indexar/status` | — | Progresso da indexação (polling) |
| POST | `/api/consultar` | `{pergunta, k}` | **Busca semântica** (integração) |
| POST | `/api/ocr/iniciar` | `{paths}` | OCR de PDFs escaneados (job em background) |
| GET | `/api/ocr/status` | — | Progresso do OCR |
| POST | `/api/ocr/parar` | — | Cancela o OCR |
| POST | `/api/buscar/iniciar` | `{eixos, usar_web, max_por_consulta}` | Busca em massa na web (OpenAlex/arXiv/Tavily) |
| GET | `/api/buscar/status` | — | Progresso da busca |
| POST | `/api/buscar/parar` | — | Cancela a busca |
| POST | `/api/busca/config` | `{provider, api_key}` | Configura chave Tavily |

Jobs em background (indexação, OCR, busca) seguem o mesmo padrão: `POST .../iniciar`
retorna na hora e o progresso é consultado por `GET .../status` (campos `rodando`,
`terminado`, contadores e `log`).

---

## Fluxo de curadoria (alimentar a base)

1. Coloque arquivos em `livros_normas/` (qualquer subpasta; PDF, DOCX, MD, TXT).
2. Na interface (ou via API), aba **Pendentes**: aprove os desejados.
   Arquivos marcados "Sem texto" são PDFs escaneados → use o botão **OCR**
   (requer o toolchain abaixo) e aprove depois.
3. Aba **Aprovados**: **🚀 Disparar RAG** para indexar.
4. Indexados ficam disponíveis imediatamente em `/api/consultar`.

Reindexação é idempotente por arquivo (os chunks antigos do mesmo `path` são
substituídos).

## OCR de PDFs escaneados (opcional)

O endpoint `/api/ocr/iniciar` depende de ferramentas externas na máquina:

- **Tesseract 5.x** em `C:\Program Files\Tesseract-OCR` (winget: `UB-Mannheim.TesseractOCR`)
- **Ghostscript 10.x** em `C:\Program Files\gs\<versão>\bin` ([releases Artifex](https://github.com/ArtifexSoftware/ghostpdl-downloads/releases))
- **ocrmypdf** no Python global: `pip install ocrmypdf`
  (caminho configurável via env `RAG_OCR_PYTHON`)
- Tessdata PT-BR já incluso no repo em `rag-tool/ocr/tessdata`

O OCR substitui o PDF in-place por uma versão pesquisável e move o escaneado
original para `livros_normas/originais-escaneados/` (pasta ignorada pela varredura).

## Configuração (variáveis de ambiente do backend)

| Variável | Padrão | Descrição |
|---|---|---|
| `RAG_EMB_MODEL` | `intfloat/multilingual-e5-small` | Modelo de embeddings |
| `RAG_CHUNK_SIZE` | `1000` | Tamanho do chunk (caracteres) |
| `RAG_CHUNK_OVERLAP` | `200` | Sobreposição entre chunks |
| `RAG_OCR_PYTHON` | `C:\Python314\python.exe` | Python com ocrmypdf instalado |

> Se mudar `RAG_EMB_MODEL`, reindexe tudo — embeddings de modelos diferentes
> não são comparáveis. Modelos da família e5 mantêm a convenção de prefixos
> `passage:`/`query:`.

## Escopo do corpus

Normas **nacionais** e do estado de **Goiás** (Equatorial Goiás, CBMGO),
PRODIST/ANEEL, NRs e material técnico de apoio. NBRs são obras pagas da ABNT —
o corpus local é de uso privado/estudo; **não redistribuir os PDFs**
(por isso `livros_normas/` pode ficar fora de repositórios públicos).
