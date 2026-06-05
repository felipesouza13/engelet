# Wiki de Engenharia Elétrica — Schema e Convenções

Este repositório é uma **LLM Wiki**: uma base de conhecimento de engenharia elétrica, persistente e interligada, mantida por você (o agente LLM). O usuário cura as fontes, dirige a análise e faz as perguntas. Você faz todo o trabalho de leitura, resumo, cross-referencing, arquivamento e manutenção.

Foco do projeto: **trabalho profissional de engenharia elétrica** — normas técnicas (NBR/IEC/IEEE), projetos, componentes/datasheets, especificações e documentação técnica.

> ⚠️ **Regra de ouro:** o usuário (quase) nunca escreve a wiki. Você escreve e mantém todas as páginas em `wiki/`. As fontes em `raw/` são **imutáveis** — você lê delas, mas nunca as modifica.

---

## Arquitetura (3 camadas)

1. **`raw/`** — Fontes brutas e curadas. Imutáveis. Sua fonte de verdade.
2. **`wiki/`** — Páginas markdown geradas por você. Você é dono total desta camada.
3. **Este arquivo (`CLAUDE.md`)** — O schema. Define a estrutura, as convenções e os workflows. Co-evolui com o usuário ao longo do tempo.

---

## Estrutura de diretórios

```
engelet/
├── CLAUDE.md              # este arquivo (schema)
├── index.md              # catálogo de conteúdo de toda a wiki
├── log.md                # registro cronológico (append-only)
├── raw/                  # FONTES BRUTAS (imutáveis)
│   ├── pdfs/             # papers, livros, normas em PDF
│   ├── artigos/          # artigos web salvos em markdown
│   ├── datasheets/       # datasheets de componentes
│   ├── notas/            # notas manuais, transcrições
│   └── assets/           # imagens, diagramas, esquemáticos, fotos
└── wiki/                 # PÁGINAS GERADAS (você é dono)
    ├── overview.md       # visão geral / ponto de entrada da wiki
    ├── sintese.md        # síntese / tese evolutiva do conhecimento
    ├── fontes/           # uma página de resumo por fonte ingerida
    ├── conceitos/        # páginas de conceitos técnicos
    ├── entidades/        # páginas de entidades (fabricantes, projetos, equipamentos)
    ├── normas/           # páginas por norma técnica (NBR, IEC, IEEE, etc.)
    └── componentes/      # páginas por componente / família de componentes
```

---

## Convenções de páginas

- **Idioma:** todo o conteúdo em **PT-BR**, com acentuação correta. Termos técnicos e identificadores podem ficar no original.
- **Links internos:** use o estilo Obsidian `[[nome-da-pagina]]`. Linke com generosidade — um link para uma página que ainda não existe é aceitável; marca algo a escrever depois.
- **Nomes de arquivo:** kebab-case, sem acentos no nome do arquivo (ex.: `dimensionamento-condutores.md`). O título dentro da página pode ter acentos.
- **Frontmatter YAML** no topo de cada página da wiki:

```yaml
---
titulo: Título Legível da Página
tipo: conceito | entidade | norma | componente | fonte | overview | sintese
tags: [potencia, protecao, baixa-tensao]
atualizado: 2026-06-01
fontes: [nome-da-fonte-1, nome-da-fonte-2]   # quais fontes embasam esta página
---
```

- **Citações:** ao afirmar algo derivado de uma fonte, referencie a página da fonte: `(ver [[fontes/nbr-5410]])`.
- **Contradições:** quando uma nova fonte contradisser uma afirmação existente, **não apague silenciosamente**. Sinalize com um bloco:

```markdown
> ⚠️ **Contradição:** [[fontes/fonte-a]] afirma X, mas [[fontes/fonte-b]] (mais recente) afirma Y. <razão / resolução>.
```

---

## Página de fonte (`wiki/fontes/<slug>.md`)

Uma página por fonte ingerida. Template:

```markdown
---
titulo: <título da fonte>
tipo: fonte
tipo_fonte: pdf | artigo | datasheet | nota | norma
tags: [...]
atualizado: 2026-06-01
arquivo_raw: raw/pdfs/arquivo.pdf
---

# <Título da fonte>

**Origem:** <autor / fabricante / URL / órgão> · **Data:** <data> · **Arquivo:** `raw/...`

## Resumo
<2-5 parágrafos com os pontos-chave>

## Pontos principais
- ...

## Dados / valores relevantes
<tabelas, fórmulas, especificações>

## Conexões
- Atualiza: [[conceitos/...]], [[normas/...]]
- Relacionado: [[entidades/...]]
```

---

## Operações (workflows)

### 1. Ingest (ingerir fonte)
Quando o usuário colocar uma fonte em `raw/` e pedir para processar:
1. Leia a fonte por completo. Se for PDF, leia o texto; se houver imagens/diagramas relevantes em `raw/assets/`, visualize-as separadamente.
2. Discuta os pontos-chave com o usuário (breve).
3. Crie a página de resumo em `wiki/fontes/<slug>.md`.
4. Atualize/crie páginas de `conceitos/`, `entidades/`, `normas/`, `componentes/` afetadas. Uma fonte pode tocar 10-15 páginas.
5. Atualize cross-references nas páginas relacionadas.
6. Atualize `index.md`.
7. Revise `sintese.md` se a fonte mudar o panorama.
8. Acrescente uma entrada em `log.md`.

### 2. Query (consultar)
Quando o usuário fizer uma pergunta:
1. Leia `index.md` primeiro para localizar páginas relevantes.
2. Leia as páginas, sintetize a resposta com citações `[[...]]`.
3. **Se a resposta for valiosa, arquive-a de volta na wiki** como nova página (ex.: uma comparação, um cálculo, uma análise). Explorações devem compor a base, não sumir no chat.
4. Registre a query em `log.md`.

### 3. Lint (revisão de saúde)
Quando o usuário pedir um lint:
- Contradições entre páginas.
- Afirmações obsoletas superadas por fontes mais novas.
- Páginas órfãs (sem links de entrada).
- Conceitos importantes mencionados mas sem página própria.
- Cross-references faltando.
- Lacunas de dados que uma busca web poderia preencher.
- Sugira novas perguntas a investigar e novas fontes a buscar.

---

## index.md e log.md

- **`index.md`** é orientado a conteúdo: catálogo de todas as páginas, organizado por categoria, cada uma com link e resumo de uma linha. Atualize a cada ingest. Leia-o primeiro ao responder queries.
- **`log.md`** é cronológico, append-only. Cada entrada começa com prefixo consistente:
  `## [AAAA-MM-DD] ingest | <título>` · `## [AAAA-MM-DD] query | <pergunta>` · `## [AAAA-MM-DD] lint`
  Assim `grep "^## \[" log.md` extrai a timeline.

---

## Notas para o agente

- A data atual deve ser usada nos campos `atualizado:` e nas entradas de log (converta datas relativas para absolutas).
- Prefira ingerir uma fonte por vez e manter o usuário envolvido, salvo pedido de batch.
- Mantenha consistência: ao renomear um conceito, atualize todos os links.
- Quando faltar uma norma/valor e fizer sentido, ofereça buscar na web (WebSearch/WebFetch).
- Esta é a versão inicial do schema. Evolua-o com o usuário conforme o domínio amadurece.
