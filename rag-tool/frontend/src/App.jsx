import React, { useEffect, useMemo, useRef, useState } from "react";

const ABAS = [
  { id: "pendente", rotulo: "Pendentes" },
  { id: "aprovado", rotulo: "Aprovados" },
  { id: "reprovado", rotulo: "Reprovados" },
  { id: "indexado", rotulo: "Indexados" },
  { id: "buscar", rotulo: "🔎 Buscar" },
];

const EIXOS = [
  ["solar", "Solar"],
  ["subestacoes", "Subestações"],
  ["ee_ampla", "EE ampla"],
  ["aterramento", "Aterramento/SPDA"],
  ["brasil", "🇧🇷 Brasil (só fontes BR)"],
];

const ICONE_EXT = { pdf: "📕", docx: "📘", md: "📝", txt: "📄" };

// Categorias derivadas do caminho do arquivo (sem precisar do backend).
const CATEGORIAS = [
  { id: "todas", rotulo: "Todas" },
  { id: "norma", rotulo: "Normas" },
  { id: "datasheet", rotulo: "Datasheets" },
  { id: "artigo", rotulo: "Artigos Científicos" },
  { id: "web", rotulo: "Web (normas/datasheets)" },
  { id: "livro", rotulo: "Livros/Material" },
];

const RE_NORMA =
  /(nbr|nr-?\s?\d|prodist|resolu|aneel|inmetro|\bnt[-_ ]?\d|\bren\b|iec\s?\d|ieee|lei[-_ ]?\d|portaria|norma|submodulo|\bons\b)/i;

function titulizar(slug) {
  return slug
    .split("-")
    .map((p) => p.charAt(0).toUpperCase() + p.slice(1))
    .join(" ");
}

// Retorna { categoria, fabricante } a partir do path relativo.
function categorizar(path) {
  const partes = path.split("/");
  if (partes[0] === "datasheets" && partes.length >= 2) {
    return { categoria: "datasheet", fabricante: titulizar(partes[1]) };
  }
  if (partes[0] === "normas-web-oficiais") {
    return { categoria: "norma", fabricante: "" };
  }
  if (partes[0] === "artigos-cientificos") {
    return { categoria: "artigo", fabricante: "" };
  }
  if (partes[0] === "buscas-web") {
    return { categoria: "web", fabricante: "" };
  }
  const nome = partes[partes.length - 1];
  if (RE_NORMA.test(nome)) return { categoria: "norma", fabricante: "" };
  return { categoria: "livro", fabricante: "" };
}

const BADGE_CAT = {
  norma: { rotulo: "Norma", cls: "cat-norma" },
  datasheet: { rotulo: "Datasheet", cls: "cat-datasheet" },
  artigo: { rotulo: "Artigo", cls: "cat-artigo" },
  web: { rotulo: "Web", cls: "cat-web" },
  livro: { rotulo: "Livro", cls: "cat-livro" },
};

function formatarTamanho(bytes) {
  if (bytes < 1024) return `${bytes} B`;
  if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`;
  return `${(bytes / (1024 * 1024)).toFixed(1)} MB`;
}

export default function App() {
  const [arquivos, setArquivos] = useState([]);
  const [aba, setAba] = useState("pendente");
  const [filtroCat, setFiltroCat] = useState("todas");
  const [carregando, setCarregando] = useState(true);

  // progresso do RAG
  const [rodando, setRodando] = useState(false);
  const [progresso, setProgresso] = useState(null);
  const [logLinhas, setLogLinhas] = useState([]);
  const pollRef = useRef(null);

  // OCR em background
  const [ocrRodando, setOcrRodando] = useState(false);
  const [ocrProg, setOcrProg] = useState(null);
  const [ocrLog, setOcrLog] = useState([]);
  const ocrPollRef = useRef(null);

  // busca em massa (web)
  const [bRodando, setBRodando] = useState(false);
  const [bProg, setBProg] = useState(null);
  const [bLog, setBLog] = useState([]);
  const bPollRef = useRef(null);
  const [eixosSel, setEixosSel] = useState({ solar: true, subestacoes: true, ee_ampla: false });
  const [usarWeb, setUsarWeb] = useState(false);
  const [maxPorConsulta, setMaxPorConsulta] = useState(30);
  const [temChave, setTemChave] = useState(false);
  const [apiKey, setApiKey] = useState("");
  const [chaveMsg, setChaveMsg] = useState("");

  async function carregar() {
    setCarregando(true);
    try {
      const r = await fetch("/api/arquivos");
      setArquivos(await r.json());
    } finally {
      setCarregando(false);
    }
  }

  useEffect(() => {
    carregar();
    // ao abrir, reflete o status atual (em andamento OU recém-concluído)
    (async () => {
      try {
        const s = await (await fetch("/api/indexar/status")).json();
        if (s.total_arquivos > 0) aplicarStatus(s);
        if (s.rodando) {
          setRodando(true);
          iniciarPolling();
        }
      } catch {
        /* backend ainda subindo */
      }
      // status do OCR (retoma painel se houver job em andamento)
      try {
        const o = await (await fetch("/api/ocr/status")).json();
        if (o.total > 0) aplicarOcr(o);
        if (o.rodando) {
          setOcrRodando(true);
          iniciarPollingOcr();
        }
      } catch {
        /* ignora */
      }
      // config + status da busca em massa
      try {
        const cfg = await (await fetch("/api/busca/config")).json();
        setTemChave(!!cfg.tem_chave);
        const bs = await (await fetch("/api/buscar/status")).json();
        if (bs.total_consultas > 0) aplicarBusca(bs);
        if (bs.rodando) {
          setBRodando(true);
          iniciarPollingBusca();
        }
      } catch {
        /* ignora */
      }
    })();
    return () => {
      pararPolling();
      pararPollingBusca();
      pararPollingOcr();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  function aplicarStatus(s) {
    setProgresso({
      arquivosFeitos: s.arquivos_feitos,
      totalArquivos: s.total_arquivos,
      chunksAcum: s.chunks_acum,
      atual: s.atual,
    });
    if (Array.isArray(s.log)) setLogLinhas(s.log);
  }

  function pararPolling() {
    if (pollRef.current) {
      clearInterval(pollRef.current);
      pollRef.current = null;
    }
  }

  function iniciarPolling() {
    pararPolling();
    pollRef.current = setInterval(async () => {
      try {
        const s = await (await fetch("/api/indexar/status")).json();
        aplicarStatus(s);
        if (!s.rodando) {
          setRodando(false);
          pararPolling();
          if (s.terminado) carregar(); // atualiza status -> indexado
        }
      } catch {
        /* ignora falha pontual de polling */
      }
    }, 1000);
  }

  async function mudarStatus(path, status) {
    await fetch("/api/arquivos/status", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ path, status }),
    });
    setArquivos((prev) =>
      prev.map((a) => (a.path === path ? { ...a, status } : a))
    );
  }

  async function mudarStatusLote(paths, status) {
    if (paths.length === 0) return;
    await fetch("/api/arquivos/status_lote", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ paths, status }),
    });
    const set = new Set(paths);
    setArquivos((prev) =>
      prev.map((a) => (set.has(a.path) ? { ...a, status } : a))
    );
  }

  function aprovarTodos(incluirSemTexto) {
    const alvos = porAba.filter((a) => incluirSemTexto || a.extraivel);
    mudarStatusLote(
      alvos.map((a) => a.path),
      "aprovado"
    );
  }

  // enriquece cada arquivo com categoria/fabricante (derivado do path)
  const arquivosCat = useMemo(
    () => arquivos.map((a) => ({ ...a, ...categorizar(a.path) })),
    [arquivos]
  );

  // arquivos da aba atual, antes do filtro de categoria
  const daAba = useMemo(
    () => arquivosCat.filter((a) => a.status === aba),
    [arquivosCat, aba]
  );

  // após o filtro de categoria (usado na renderização da lista)
  const porAba = useMemo(
    () =>
      filtroCat === "todas"
        ? daAba
        : daAba.filter((a) => a.categoria === filtroCat),
    [daAba, filtroCat]
  );

  // contagem por categoria dentro da aba atual (para os botões de filtro)
  const contagemCat = useMemo(() => {
    const c = { todas: daAba.length, norma: 0, datasheet: 0, artigo: 0, web: 0, livro: 0 };
    daAba.forEach((a) => (c[a.categoria] = (c[a.categoria] || 0) + 1));
    return c;
  }, [daAba]);

  // badges das abas refletem o filtro de categoria atual:
  // ao selecionar "Livros", as abas mostram em qual status eles estão.
  const contagem = useMemo(() => {
    const c = { pendente: 0, aprovado: 0, reprovado: 0, indexado: 0 };
    arquivosCat.forEach((a) => {
      if (filtroCat === "todas" || a.categoria === filtroCat)
        c[a.status] = (c[a.status] || 0) + 1;
    });
    return c;
  }, [arquivosCat, filtroCat]);

  // contagem global por status (independe do filtro) — usada na lógica do botão RAG
  const contagemStatus = useMemo(() => {
    const c = { pendente: 0, aprovado: 0, reprovado: 0, indexado: 0 };
    arquivos.forEach((a) => (c[a.status] = (c[a.status] || 0) + 1));
    return c;
  }, [arquivos]);

  async function dispararRAG() {
    if (rodando) return;
    setProgresso({
      arquivosFeitos: 0,
      totalArquivos: 0,
      chunksAcum: 0,
      atual: null,
    });
    setLogLinhas([]);
    try {
      const j = await (
        await fetch("/api/indexar/iniciar", { method: "POST" })
      ).json();
      if (!j.ok) {
        setLogLinhas([j.erro || "Não foi possível iniciar."]);
        return;
      }
      setRodando(true);
      iniciarPolling();
    } catch (e) {
      setLogLinhas([`Erro ao iniciar: ${e}`]);
    }
  }

  // ---- busca em massa ----
  function pararPollingBusca() {
    if (bPollRef.current) {
      clearInterval(bPollRef.current);
      bPollRef.current = null;
    }
  }

  function aplicarBusca(s) {
    setBProg({
      total: s.total_consultas,
      feitas: s.consultas_feitas,
      baixados: s.baixados,
      atual: s.atual,
    });
    if (Array.isArray(s.log)) setBLog(s.log);
  }

  function iniciarPollingBusca() {
    pararPollingBusca();
    bPollRef.current = setInterval(async () => {
      try {
        const s = await (await fetch("/api/buscar/status")).json();
        aplicarBusca(s);
        if (!s.rodando) {
          setBRodando(false);
          pararPollingBusca();
          if (s.terminado) carregar();
        }
      } catch {
        /* ignora */
      }
    }, 1500);
  }

  async function salvarChave() {
    if (!apiKey.trim()) return;
    await fetch("/api/busca/config", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ provider: "tavily", api_key: apiKey.trim() }),
    });
    setApiKey("");
    setChaveMsg("Chave salva ✓");
    setTemChave(true);
  }

  async function dispararBusca() {
    if (bRodando) return;
    const eixos = Object.keys(eixosSel).filter((k) => eixosSel[k]);
    if (eixos.length === 0) {
      setBLog(["Selecione ao menos um eixo."]);
      return;
    }
    setBProg({ total: 0, feitas: 0, baixados: 0, atual: null });
    setBLog([]);
    try {
      const j = await (
        await fetch("/api/buscar/iniciar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            eixos,
            usar_web: usarWeb,
            max_por_consulta: Number(maxPorConsulta) || 30,
          }),
        })
      ).json();
      if (!j.ok) {
        setBLog([j.erro || "Não foi possível iniciar."]);
        return;
      }
      setBRodando(true);
      iniciarPollingBusca();
    } catch (e) {
      setBLog([`Erro: ${e}`]);
    }
  }

  async function pararBusca() {
    await fetch("/api/buscar/parar", { method: "POST" });
  }

  // ---- OCR ----
  function pararPollingOcr() {
    if (ocrPollRef.current) {
      clearInterval(ocrPollRef.current);
      ocrPollRef.current = null;
    }
  }

  function aplicarOcr(s) {
    setOcrProg({
      total: s.total,
      feitos: s.feitos,
      sucesso: s.sucesso,
      atual: s.atual,
    });
    if (Array.isArray(s.log)) setOcrLog(s.log);
  }

  function iniciarPollingOcr() {
    pararPollingOcr();
    ocrPollRef.current = setInterval(async () => {
      try {
        const s = await (await fetch("/api/ocr/status")).json();
        aplicarOcr(s);
        if (!s.rodando) {
          setOcrRodando(false);
          pararPollingOcr();
          if (s.terminado) carregar(); // recheca extraibilidade (mtime mudou)
        }
      } catch {
        /* ignora */
      }
    }, 2000);
  }

  async function dispararOCR(paths) {
    if (ocrRodando || paths.length === 0) return;
    setOcrProg({ total: paths.length, feitos: 0, sucesso: 0, atual: null });
    setOcrLog([]);
    try {
      const j = await (
        await fetch("/api/ocr/iniciar", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ paths }),
        })
      ).json();
      if (!j.ok) {
        setOcrLog([j.erro || "Não foi possível iniciar o OCR."]);
        return;
      }
      setOcrRodando(true);
      iniciarPollingOcr();
    } catch (e) {
      setOcrLog([`Erro ao iniciar OCR: ${e}`]);
    }
  }

  async function pararOCR() {
    await fetch("/api/ocr/parar", { method: "POST" });
  }

  const ocrPct =
    ocrProg && ocrProg.total > 0
      ? Math.min(100, Math.round((ocrProg.feitos / ocrProg.total) * 100))
      : 0;

  const bPct =
    bProg && bProg.total > 0
      ? Math.min(100, Math.round((bProg.feitas / bProg.total) * 100))
      : 0;

  const fracAtual =
    progresso?.atual?.chunksArq > 0
      ? progresso.atual.chunkNo / progresso.atual.chunksArq
      : 0;
  const pct =
    progresso && progresso.totalArquivos > 0
      ? Math.min(
          100,
          Math.round(
            ((progresso.arquivosFeitos + fracAtual) / progresso.totalArquivos) *
              100
          )
        )
      : 0;

  function textoAtual() {
    const a = progresso?.atual;
    if (!a) return null;
    if (a.fase === "extraindo") {
      return a.paginas
        ? `Extraindo ${a.path} — pág. ${a.pagina}/${a.paginas}`
        : `Extraindo ${a.path}…`;
    }
    return `Indexando ${a.path} — chunk ${a.chunkNo}/${a.chunksArq}`;
  }

  return (
    <div className="app">
      <header>
        <h1>RAG · livros_normas</h1>
        <button className="btn-secundario" onClick={carregar} disabled={carregando}>
          ↻ Recarregar
        </button>
      </header>

      <nav className="abas">
        {ABAS.map((a) => (
          <button
            key={a.id}
            className={`aba ${aba === a.id ? "ativa" : ""}`}
            onClick={() => setAba(a.id)}
          >
            {a.rotulo}{" "}
            {a.id !== "buscar" && (
              <span className="badge">{contagem[a.id] || 0}</span>
            )}
          </button>
        ))}
      </nav>

      {aba !== "buscar" && (
        <nav className="filtros-cat">
          <span className="filtros-label">Categoria:</span>
          {CATEGORIAS.map((c) => (
            <button
              key={c.id}
              className={`chip ${filtroCat === c.id ? "ativo" : ""}`}
              onClick={() => setFiltroCat(c.id)}
            >
              {c.rotulo} <span className="chip-num">{contagemCat[c.id] || 0}</span>
            </button>
          ))}
        </nav>
      )}

      {/* Painel de progresso da indexação — visível só ENQUANTO indexa;
          ao concluir, some e o botão "Disparar RAG" é liberado. */}
      {rodando && progresso && (
        <div className="painel-progresso">
          <div className="painel-progresso-cab">
            <span className="pulso ativo" />
            <strong>Indexando…</strong>
            <span className="pct-grande">{pct}%</span>
          </div>
          <div className="barra">
            <div className="barra-preench" style={{ width: `${pct}%` }} />
          </div>
          <div className="progresso-txt">
            {progresso.arquivosFeitos}/{progresso.totalArquivos} arquivos ·{" "}
            {progresso.chunksAcum} chunks indexados
          </div>
          {textoAtual() && <div className="progresso-atual">{textoAtual()}</div>}
          {logLinhas.length > 0 && (
            <div className="log">
              {logLinhas
                .slice(-40)
                .map((l, i) => (
                  <div key={i} className="log-linha">
                    {l}
                  </div>
                ))}
            </div>
          )}
        </div>
      )}

      {/* Painel de progresso do OCR — fica visível após concluir para mostrar
          quais arquivos foram recuperados e quais falharam. */}
      {aba !== "buscar" && (ocrRodando || (ocrProg && ocrProg.total > 0)) && (
        <div className="painel-progresso estatico">
          <div className="painel-progresso-cab">
            <span className={`pulso ${ocrRodando ? "ativo" : ""}`} />
            <strong>{ocrRodando ? "OCR em andamento…" : "OCR concluído"}</strong>
            {ocrRodando && (
              <button className="btn-rejeitar" onClick={pararOCR}>
                ⛔ Parar
              </button>
            )}
            <span className="pct-grande">{ocrPct}%</span>
          </div>
          <div className="barra">
            <div className="barra-preench" style={{ width: `${ocrPct}%` }} />
          </div>
          <div className="progresso-txt">
            {ocrProg.feitos}/{ocrProg.total} arquivos · {ocrProg.sucesso} com
            sucesso
          </div>
          {ocrProg.atual && (
            <div className="progresso-atual">🔍 OCR: {ocrProg.atual}</div>
          )}
          {ocrLog.length > 0 && (
            <div className="log">
              {ocrLog.slice(-40).map((l, i) => (
                <div key={i} className="log-linha">
                  {l}
                </div>
              ))}
            </div>
          )}
        </div>
      )}

      {aba === "buscar" && (
        <div className="painel-busca">
          <p className="busca-intro">
            Motor de busca em massa — OpenAlex + arXiv (acadêmico, grátis) +
            Tavily (web: normas/datasheets). Os PDFs entram como{" "}
            <strong>pendentes</strong> para revisão.
          </p>

          <div className="busca-bloco">
            <span className="busca-label">Chave Tavily:</span>
            {temChave ? (
              <span className="dica">✓ configurada</span>
            ) : (
              <span className="dica sem-chave">não configurada</span>
            )}
            <input
              className="busca-input"
              type="password"
              placeholder="tvly-..."
              value={apiKey}
              onChange={(e) => setApiKey(e.target.value)}
            />
            <button className="btn-secundario" onClick={salvarChave}>
              Salvar
            </button>
            {chaveMsg && <span className="dica">{chaveMsg}</span>}
          </div>

          <div className="busca-bloco">
            <span className="busca-label">Eixos:</span>
            {EIXOS.map(([k, r]) => (
              <label key={k} className="busca-check">
                <input
                  type="checkbox"
                  checked={!!eixosSel[k]}
                  onChange={(e) =>
                    setEixosSel({ ...eixosSel, [k]: e.target.checked })
                  }
                />{" "}
                {r}
              </label>
            ))}
          </div>

          <div className="busca-bloco">
            <label className={`busca-check ${!temChave ? "desativado" : ""}`}>
              <input
                type="checkbox"
                disabled={!temChave}
                checked={usarWeb}
                onChange={(e) => setUsarWeb(e.target.checked)}
              />{" "}
              incluir busca web (normas/datasheets via Tavily)
            </label>
            <label className="busca-check">
              máx por consulta:
              <input
                className="busca-num"
                type="number"
                min="1"
                max="100"
                value={maxPorConsulta}
                onChange={(e) => setMaxPorConsulta(e.target.value)}
              />
            </label>
          </div>

          <div className="busca-acoes">
            <button className="btn-rag" onClick={dispararBusca} disabled={bRodando}>
              {bRodando ? "Buscando…" : "🔎 Buscar em massa"}
            </button>
            {bRodando && (
              <button className="btn-rejeitar" onClick={pararBusca}>
                ⛔ Parar
              </button>
            )}
          </div>

          {(bRodando || (bProg && bProg.total > 0)) && (
            <div className="painel-progresso estatico">
              <div className="painel-progresso-cab">
                <span className={`pulso ${bRodando ? "ativo" : ""}`} />
                <strong>{bRodando ? "Buscando…" : "Busca concluída"}</strong>
                <span className="pct-grande">{bPct}%</span>
              </div>
              <div className="barra">
                <div className="barra-preench" style={{ width: `${bPct}%` }} />
              </div>
              <div className="progresso-txt">
                {bProg.feitas}/{bProg.total} consultas · {bProg.baixados} PDFs
                baixados
              </div>
              {bProg.atual && (
                <div className="progresso-atual">
                  🔎 {bProg.atual.query} ({bProg.atual.tema})
                </div>
              )}
              {bLog.length > 0 && (
                <div className="log">
                  {bLog.slice(-40).map((l, i) => (
                    <div key={i} className="log-linha">
                      {l}
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
        </div>
      )}

      {aba === "aprovado" && (
        <div className="painel-rag">
          <button
            className="btn-rag"
            onClick={dispararRAG}
            disabled={rodando || contagemStatus.aprovado === 0}
          >
            {rodando ? "Processando…" : "🚀 Disparar RAG"}
          </button>
          {contagemStatus.aprovado > 0 && !rodando && (
            <span className="dica">
              {contagemStatus.aprovado} arquivo(s) aprovado(s) prontos para indexar.
            </span>
          )}
        </div>
      )}

      {aba === "pendente" && porAba.length > 0 && (
        <div className="barra-acoes">
          <button
            className="btn-aprovar"
            onClick={() => aprovarTodos(false)}
            disabled={porAba.filter((a) => a.extraivel).length === 0}
          >
            ✓ Aprovar todos extraíveis ({porAba.filter((a) => a.extraivel).length})
          </button>
          {porAba.some((a) => !a.extraivel) && (
            <>
              <button
                className="btn-secundario"
                onClick={() => {
                  if (
                    window.confirm(
                      `Incluir também ${
                        porAba.filter((a) => !a.extraivel).length
                      } arquivo(s) SEM texto extraível?\n` +
                        "Eles não gerarão chunks no RAG (precisariam de OCR)."
                    )
                  )
                    aprovarTodos(true);
                }}
              >
                Aprovar todos ({porAba.length})
              </button>
              <button
                className="btn-rejeitar"
                onClick={() =>
                  mudarStatusLote(
                    porAba.filter((a) => !a.extraivel).map((a) => a.path),
                    "reprovado"
                  )
                }
              >
                ⛔ Rejeitar sem textos ({porAba.filter((a) => !a.extraivel).length})
              </button>
            </>
          )}
          {porAba.some((a) => !a.extraivel && a.ext === "pdf") && (
            <button
              className="btn-ocr"
              disabled={ocrRodando}
              onClick={() =>
                dispararOCR(
                  porAba
                    .filter((a) => !a.extraivel && a.ext === "pdf")
                    .map((a) => a.path)
                )
              }
            >
              🔍 Tentar OCR nos sem texto (
              {porAba.filter((a) => !a.extraivel && a.ext === "pdf").length})
            </button>
          )}
        </div>
      )}

      {aba === "reprovado" && porAba.length > 0 && (
        <div className="barra-acoes">
          <button
            className="btn-secundario"
            onClick={() =>
              mudarStatusLote(
                porAba.map((a) => a.path),
                "pendente"
              )
            }
          >
            ↩ Restaurar todos ({porAba.length})
          </button>
        </div>
      )}

      {aba !== "buscar" && (
      <main>
        {carregando ? (
          <p className="vazio">Carregando…</p>
        ) : porAba.length === 0 ? (
          <p className="vazio">
            {aba === "pendente"
              ? "Nenhum arquivo pendente. Coloque arquivos em livros_normas/ e recarregue."
              : aba === "aprovado"
              ? "Nenhum arquivo aprovado ainda. Aprove na aba Pendentes."
              : aba === "reprovado"
              ? "Nenhum arquivo reprovado."
              : "Nenhum arquivo indexado ainda."}
          </p>
        ) : (
          <ul className="lista">
            {porAba.map((a) => (
              <li key={a.path} className="item">
                <span className="icone">{ICONE_EXT[a.ext] || "📄"}</span>
                <div className="info">
                  <div className="nome">
                    <span className={`cat-badge ${BADGE_CAT[a.categoria].cls}`}>
                      {BADGE_CAT[a.categoria].rotulo}
                    </span>
                    {a.fabricante && (
                      <span className="fabricante">{a.fabricante}</span>
                    )}
                    {a.nome}
                  </div>
                  <div className="meta">
                    {a.path !== a.nome && <span>{a.path} · </span>}
                    {formatarTamanho(a.tamanho)}
                    {a.status === "indexado" && a.chunks > 0 && (
                      <span> · {a.chunks} chunks</span>
                    )}
                  </div>
                </div>
                <div
                  className={`extr ${a.extraivel ? "extr-ok" : "extr-falha"}`}
                  title={a.motivo_extr}
                >
                  {a.extraivel ? "✅ Extraível" : "⛔ Sem texto"}
                </div>
                <div className="acoes">
                  {a.status === "pendente" && (
                    <button
                      className="btn-aprovar"
                      onClick={() => {
                        if (
                          !a.extraivel &&
                          !window.confirm(
                            `"${a.nome}" não tem texto extraível (${a.motivo_extr}).\n` +
                              "O RAG não conseguirá indexá-lo sem OCR. Aprovar mesmo assim?"
                          )
                        )
                          return;
                        mudarStatus(a.path, "aprovado");
                      }}
                    >
                      ✓ Aprovar
                    </button>
                  )}
                  {a.status === "pendente" && (
                    <button
                      className="btn-rejeitar"
                      onClick={() => mudarStatus(a.path, "reprovado")}
                    >
                      ⛔ Rejeitar
                    </button>
                  )}
                  {a.status === "pendente" &&
                    !a.extraivel &&
                    a.ext === "pdf" && (
                      <button
                        className="btn-ocr"
                        disabled={ocrRodando}
                        title="Roda OCR (ocrmypdf) e substitui pelo PDF pesquisável; o original vai para originais-escaneados/"
                        onClick={() => dispararOCR([a.path])}
                      >
                        🔍 OCR
                      </button>
                    )}
                  {a.status === "reprovado" && (
                    <button
                      className="btn-secundario"
                      onClick={() => mudarStatus(a.path, "pendente")}
                    >
                      ↩ Restaurar
                    </button>
                  )}
                  {a.status === "aprovado" && (
                    <button
                      className="btn-secundario"
                      onClick={() => mudarStatus(a.path, "pendente")}
                    >
                      ↩ Desfazer
                    </button>
                  )}
                  {a.status === "indexado" && (
                    <button
                      className="btn-secundario"
                      onClick={() => mudarStatus(a.path, "aprovado")}
                    >
                      ↻ Reindexar
                    </button>
                  )}
                </div>
              </li>
            ))}
          </ul>
        )}
      </main>
      )}
    </div>
  );
}
