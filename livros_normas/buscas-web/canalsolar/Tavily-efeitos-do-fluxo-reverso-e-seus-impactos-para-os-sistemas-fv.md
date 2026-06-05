# Efeitos do fluxo reverso e seus impactos para os sistemas FV

**Fonte:** https://canalsolar.com.br/efeitos-do-fluxo-reverso-e-seus-impactos-para-os-sistemas-fotovoltaicos

![logo site canal solar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20846%20179'%3E%3C/svg%3E)
![logo site canal solar](https://canalsolar.com.br/wp-content/uploads/2024/01/LOGO-CANAL-SOLAR-VERSAO-5-copiar.svg)
![logo site canal solar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20846%20179'%3E%3C/svg%3E)
![logo site canal solar](https://canalsolar.com.br/wp-content/uploads/2024/01/LOGO-CANAL-SOLAR-VERSAO-5-copiar.svg)

# Efeitos do fluxo reverso e seus impactos para os sistemas fotovoltaicos

![Foto de Rodolfo Barreto](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)
![Foto de Rodolfo Barreto](https://secure.gravatar.com/avatar/43f78dbf35265e4c45be5081b4c71117aed2346e30feed6bb41df76a77388b2f?s=96&d=mm&r=g)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2024/01/Energia-solar-Canal-Solar-Efeitos-do-fluxo-reverso-e-seus-impactos-para-os-sistemas-fotovoltaicos.jpg) 

Foto: Rafael Lopes


![](https://canalsolar.com.br/wp-content/uploads/2024/01/Energia-solar-Canal-Solar-Efeitos-do-fluxo-reverso-e-seus-impactos-para-os-sistemas-fotovoltaicos.jpg)

*Autoria de Rodolfo Barreto, assistente de Projetos Fotovoltaicos Amara NZero com colaboração de Thiago Mingareli, gerente Técnico Amara NZero*

Nos últimos meses muito se falou sobre o fluxo reverso devido às reprovações principalmente da CEMIG/MG, mas que já se estendeu para outras concessionárias de energia pelo Brasil.

Tal fato gerou insatisfação e apreensão nas solicitações de parecer de acesso pelos integradores do setor fotovoltaico, sendo a principal justificativa das distribuidoras de que a rede elétrica está incapacitada de receber energia injetada pelos novos sistemas fotovoltaicos (inversão de fluxo).

Em suas justificativas, a concessionária se embasa na resolução normativa Art. 73 da REN 1000. Em suas disposições, diz que:

Sendo necessário para recusa, o cumprimento das exigências do Art. 73 da REN 1000 por parte da concessionária.

Com isso, mostraremos neste artigo o ponto de vista técnico onde o fluxo reverso pode ocorrer DE FATO, muito longe do que as concessionárias de energia têm aplicado, atestando fluxo reverso sem justificativas plausíveis ou critérios.

O que fazer para evitar a recusa do seu parecer, e também evitar ou mitigar o fluxo reverso? Neste artigo, você vai entender o que é a inversão de fluxo, como funciona na prática e o que pode ser feito nessas situações.

## O que é seria o fluxo reverso, e quais seus impactos?

Este fenômeno tem se tornado cada vez mais comum no atual cenário da geração distribuída, com maior destaque aos sistemas fotovoltaicos.

Seu efeito ocorre devido à alta inserção de potência ativa na linha de transmissão (em horários que é observado um maior pico de irradiação/geração de energia nos sistemas FV), que são, por coincidência, os períodos de baixa demanda de consumo hoje em dia – intervalo entre 10h e 16h, mais ou menos.

Este comportamento vem acarretando alguns impactos na topologia da rede de distribuição, afetando seus padrões de qualidade de energia.

Dentre os impactos observados diariamente nos sistemas fotovoltaicos, o que mais se destaca é a flutuação de tensão, porém existem algumas outras interferências que podem ocorrer, como por exemplo: alteração no fator de potência, regulação de frequência e distorções harmônicas.

## O que fazer para mitigar esses efeitos e evitar o fluxo reverso?

Um dos fatores possíveis para mitigação deste efeito, com intuito de prevenção, seria a utilização de software pelas concessionárias com o objetivo de verificação dos impactos que podem causar em sua infraestrutura, utilizando componentes já presentes em sua rede e fazendo inserções aos poucos da geração distribuída em seus ramais de conexão.

Pois  o que temos visto, na prática, são concessionárias alegando inversão de fluxo mas sem realizar os estudos de forma aprofundada e principalmente PROPOR SOLUÇÕES ALTERNATIVAS para a conexão, conforme exige a resolução normativa.

Atualmente, isto já é possível e visível em alguns softwares de código livre, um exemplo disto seria o OpenDss, tendo várias redes disponíveis, simulando grandes ou reduzidos ramais de distribuição, tornando possível realizar a inserção e compensação da geração distribuída.

Nessas simulações é possível notar diferentes comportamentos no nível de tensão de acordo ao local onde se é definido a conexão da geração distribuída.

Outra solução possível seria o controle de injeção de potência ativa dos inversores fotovoltaicos, fazendo a compensação através do ajuste do seu fator de potência, ou então a utilização de sistemas de armazenamento nestes horários, realizando a compensação em horário posterior, com maior consumo.

Uma última opção é a utilização de sistemas zero-grid, sem injeção de energia na rede, atendendo ao consumo interno do local.

#### Veja na prática como acontece a variação do perfil de tensão quando se tem uma alta injeção de potência ativa na rede.

Para fins de verificação, foi realizada uma simulação no software OpenDss considerando a rede de teste IEEE 13 barras. Mesmo caracterizando um sistema pequeno, a rede IEEE 13 barras apresenta configurações diversificadas que permitem as mais variadas análises em um sistema de distribuição e seus componentes.

Este circuito opera em uma tensão de 4,16KV e composto por trechos de linhas trifásicas aéreas e subterrâneas desbalanceadas, ramais bifásicos e monofásicos, dois bancos de capacitores shunts, um regulador de tensão na subestação, dois transformadores de distribuição e cargas desequilibradas.

Cargas com perfil residencial e comercial são conectadas nas barras localizadas após o secundário do transformador abaixador (4.160/220V) conforme pode-se visualizar na Tabela 1.

As potências nominais dos bancos de capacitores, assim como as suas barras de conexão são apresentadas na Tabela 2. O diagrama unifilar completo do sistema de distribuição pode ser observado na Figura 1.

#### Tabela 1 – Cargas conectadas na rede IEEE 13 Barras

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20820%20329'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/01/Tabela-1.jpg)

#### Tabela 2 – Banco de capacitores conectados à rede IEEE 13 Node Test Feeder

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20651%20157'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/01/Tabela-2.jpg)
![Figura 1: Diagrama unifilar da rede teste IEEE 13 barras. Fonte: Autor](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20322'%3E%3C/svg%3E)
![Figura 1: Diagrama unifilar da rede teste IEEE 13 barras. Fonte: Autor](https://server2.canalsolar.com.br/wp-content/uploads/2024/01/unnamed-11.jpg)

Na análise a seguir são apresentados gráficos onde se verifica o comportamento da tensão na rede sem inserção da geração distribuída e com a inserção de 180% de injeção da potência ativa proveniente da geração distribuída, considerando o consumo das cargas. 

Pode-se  observar e analisar, a partir dos gráficos expostos, o perfil de tensão e consumo de potência ativa ao longo do dia em cada barra do sistema de distribuição simulado. Para tal, considerou-se um limite aceitável na variação da tensão nominal de 5%, de acordo com que se recomenda no módulo 8 dos procedimentos de distribuição – PRODIST.

![Gráfico de tensão da fase A sem geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20364'%3E%3C/svg%3E)
![Gráfico de tensão da fase A sem geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-tensao-da-fase-A-sem-geracao-distribuida.png)
![Gráfico de tensão da fase A com 180% de geração distribuíd](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20353'%3E%3C/svg%3E)
![Gráfico de tensão da fase A com 180% de geração distribuíd](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-tensao-da-fase-A-com-180-de-geracao-distribuid.png)
![Gráfico de tensão da fase B sem geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20369'%3E%3C/svg%3E)
![Gráfico de tensão da fase B sem geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-tensao-da-fase-B-sem-geracao-distribuida.png)
![Gráfico de tensão da fase B com 180% de geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20358'%3E%3C/svg%3E)
![Gráfico de tensão da fase B com 180% de geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-tensao-da-fase-B-com-180-de-geracao-distribuida.png)
![Gráfico de tensão da fase C sem geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20358'%3E%3C/svg%3E)
![Gráfico de tensão da fase C sem geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-tensao-da-fase-C-sem-geracao-distribuida.png)
![Gráfico de tensão da fase C com 180% de geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20357'%3E%3C/svg%3E)
![Gráfico de tensão da fase C com 180% de geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-tensao-da-fase-C-com-180-de-geracao-distribuida.png)

Um ponto importante a se observar, é a variação no perfil de tensão quando se tem uma injeção de potência ativa entre os horários das 10h às 16h nas barras de conexão, em algumas delas de maneira acentuada.

## Por que isso acontece?

Tal comportamento pode se justificar devido a sua maior distância em relação ao transformador que alimenta a rede de distribuição, um exemplo disto é a barra 611 mostrada no gráfico de tensão da fase C, analisando no diagrama unifilar, podemos perceber que ela está em uma posição mais afastada do regulador, fazendo com que tenha uma maior impedância, e no momento de uma alta inserção da geração distribuída, mostra uma elevação da tensão.

Ao final do dia, é possível notar uma queda no perfil de tensão a partir das 17h, de acordo com a curva típica de consumo residencial adotada que considera uma maior sobrecarga na demanda da rede entre os horários de 17h até 21h, comportamento que provoca uma significativa queda de tensão nas barras de conexão.

## Em que momento é possível visualizar a inversão de fluxo?

A seguir, plotou-se gráficos onde podemos ver o comportamento da potência em situações sem geração distribuída e com a inserção da geração distribuída, podendo ser visível o comportamento do fluxo reverso.

![Gráfico de Potência da fase A sem geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20372'%3E%3C/svg%3E)
![Gráfico de Potência da fase A sem geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-Potencia-da-fase-A-sem-geracao-distribuida.png)
![Gráfico de potência da fase A com 180% de geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20368'%3E%3C/svg%3E)
![Gráfico de potência da fase A com 180% de geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-potencia-da-fase-A-com-180-de-geracao-distribuida.png)
![Gráfico de Potência da fase B sem geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20321'%3E%3C/svg%3E)
![Gráfico de Potência da fase B sem geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-Potencia-da-fase-B-sem-geracao-distribuida.png)
![Figura 11: Gráfico de potência da fase B com 180% de geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20335'%3E%3C/svg%3E "Figura 11: Gráfico de potência da fase B com 180% de geração distribuída")
![Figura 11: Gráfico de potência da fase B com 180% de geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-potencia-da-fase-B-com-180-de-geracao-distribuida.png "Figura 11: Gráfico de potência da fase B com 180% de geração distribuída")
![Gráfico de Potência da fase C sem geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20404'%3E%3C/svg%3E)
![Gráfico de Potência da fase C sem geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-Potencia-da-fase-C-sem-geracao-distribuida.png)
![Gráfico de potência da fase C com 180% de geração distribuída](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20404'%3E%3C/svg%3E)
![Gráfico de potência da fase C com 180% de geração distribuída](https://canalsolar.com.br/wp-content/uploads/2024/01/Grafico-de-potencia-da-fase-C-com-180-de-geracao-distribuida.png)

Nos gráficos comparativos de injeção de potência ativa, é evidente o comportamento do fluxo reverso nos horários em que se tem uma maior injeção de potência ativa na rede de distribuição, vendo claramente a diferença dos gráficos com e sem geração distribuída, refletindo nas curvas de potência das fases A, B e C, nos horários das 9h às 16h, sendo visível o que ocorre atualmente em alguns trechos da rede.

Tal efeito é uma das principais causas dos distúrbios que ocorrem nos sistemas fotovoltaicos, sendo o mais visto, a sobretensão.

## Conclusão

O objetivo do artigo foi mostrar tecnicamente em que situações o fluxo reverso pode de fato ocorrer, até mesmo para auxiliar o embasamento dos nossos parceiros em contestações a serem feitas junto a concessionária de energia em situações que aleguem inadequadamente ou sem a devida justificativa as razões para apontar inversão de fluxo e negar o parecer de acesso.

Discordamos veementemente da forma arbitrária em que isso tem sido aplicado pelas concessionárias de energia, e é nosso dever contra-argumentar e exigir que demonstrem onde (e se) isso ocorre, a partir de um estudo técnico detalhado.

Como soluções alternativas para evitar o fluxo reverso e consequentemente a sobretensão aos sistemas fotovoltaicos já instalados, temos o ajuste nos parâmetros de tensão do inversor (evidenciando sempre que é necessário seguir todas as novas leis vigentes), evitando atuação do equipamento por sobretensão.

Esta intervenção é apenas um paliativo para minimizar os impactos trazidos pela forte inserção na conexão de GD fotovoltaico à rede de distribuição, porém, outra alternativa viável seria a regulação do fator de potência dos inversores fazendo o uso da própria GD para correção do perfil de tensão através da injeção de reativos, bem como banco de baterias para armazenar o excesso de energia produzida, e a utilização de carregadores elétricos, com a carga e descarga de veículos, podendo ser utilizados como artifício no suprimento excessivo de potência ativa na rede.

Infelizmente este fato é tem sido recorrente no dia a dia dos nossos parceiros integradores, que aconselhamos resolver o problema através da abertura de reclamações com a concessionária ou em último caso em situações de reprovações de pareceres de acesso, contatar a ouvidoria da Agência Nacional de Energia Elétrica ou até mesmo buscar soluções por meios judiciais pois como podemos ver no artigo, existe sim a possibilidade de ocorrer situações de fluxo reverso, porém é obrigação da concessionária realizar estudos e propor alternativas para a conexão do cliente – e não simplesmente recusar o pedido.

### Referências Bibliográficas

[1] AGÊNCIA NACIONAL DE ENERGIA ELÉTRICA. Procedimentos de Distribuição de Energia Elétrica – PRODIST. Módulo 8 – Qualidade da Energia Elétrica. 2021.

[2] ANEEL. Agência Nacional de Energia Elétrica. Resolução Normativa nº 482, de 17 de abril de 2012.

[3] BATISTA, Rodolfo Barreto. Análise dos Impactos Causados pelo Aumento dos Sistemas Fotovoltaicos Conectados à Rede de Distribuição.2023.

![Foto de Rodolfo Barreto](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%200%200'%3E%3C/svg%3E)
![Foto de Rodolfo Barreto](https://secure.gravatar.com/avatar/43f78dbf35265e4c45be5081b4c71117aed2346e30feed6bb41df76a77388b2f?s=200&d=mm&r=g)

## Uma resposta

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)![](https://secure.gravatar.com/avatar/4f8d2ba613f3cb3ec16ce2c8daf47768c3c373e991cec72457b240a8a8a8c70a?s=42&d=mm&r=g) **MURILO CÂMARA SILVA** disse: 
![](https://secure.gravatar.com/avatar/4f8d2ba613f3cb3ec16ce2c8daf47768c3c373e991cec72457b240a8a8a8c70a?s=42&d=mm&r=g)

A corrente elétrica sempre flui da fonte para a carga. Se por motivos diversos, está acontecendo fluxo reverso no posto de transformação, não significa que a demanda após este posto está maior que antes dele? Ou seja, de qualquer forma essa energia está sendo utilizada em algum ponto do sistema ( na sua maioria interligado em anel).

Outra questão é como alegar que um determinado gerador solar que é responsável por essa inversão? Não poderia ser de outra fonte, até mesmo geração de usinas da própria Cemig?

O que vemos hoje são alegações infundadas que como sempre prejudicamos consumidores. No mínimo, uma transmissão da responsabilidade de quem detém a obrigação (concessão) e exploração dos serviços de eletrificação aos seus clientes finais, que nem opção de escolha desse prestador é possível.

Os órgãos reguladores fazem vista grossa e nada está sendo resolvido.

É muito comum observar desde antes do bull da geração distribuída, localidades com níveis de tensão de 250 Vca fase-fase. Na verdade deveria ser 220 Vca. Isso por si só, demonstra que nosso sistema elétrico vem carecendo de melhorias a muito tempo. A Cemig faz isso a muito tempo para não recapacitar as redes e não tinha problema algum. Porem, nessas mesmas localidade algum cliente quiser inserir um gerador solar, o parecer virá com a tal inversão de fluxo.

## Deixe um comentário [Cancelar resposta](/efeitos-do-fluxo-reverso-e-seus-impactos-para-os-sistemas-fotovoltaicos/#respond)

O seu endereço de e-mail não será publicado. Campos obrigatórios são marcados com \*

Comentário \*

Nome \*

E-mail \*

Site

Salvar meus dados neste navegador para a próxima vez que eu comentar.

Os comentários devem ser respeitosos e contribuir para um debate saudável. Comentários ofensivos poderão ser removidos. As opiniões aqui expressas são de responsabilidade dos autores e não refletem, necessariamente, a posição do Canal Solar.

### Notícias do Canal Solar no seu E-mail

### Relacionados

![Canal Solar - Do debate regulatório à contratação de potência o armazenamento de energia e os primeiros leilões de baterias no Brasil](https://canalsolar.com.br/wp-content/uploads/2026/06/Canal-Solar-Do-debate-regulatorio-a-contratacao-de-potencia-o-armazenamento-de-energia-e-os-primeiros-leiloes-de-baterias-no-Brasil.webp)

[Do debate regulatório à contratação de potência: o armazenamento de energia e os primeiros leilões de baterias no Brasil](https://canalsolar.com.br/debate-regulatorio-contratacao-potencia-armazenamento-energia/)

![ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos? ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos?](https://canalsolar.com.br/wp-content/uploads/2026/06/Canal-Solar-SO-55001-aplicada-a-energia-solar-como-prolongar-a-vida-util-de-sistemas-fotovoltaicos-1.webp)

[ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos?](https://canalsolar.com.br/iso-55001-solar-vida-util-sistemas-fotovoltaicos/)

## [Mais Notícias](/category/noticias)

![Comissão da Câmara dos Deputados fará auditoria pública sobre inversão de fluxo](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![Comissão da Câmara dos Deputados fará auditoria pública sobre inversão de fluxo](https://canalsolar.com.br/wp-content/uploads/2025/04/Comissao-da-Camara-dos-Deputados-fara-auditoria-publica-sobre-inversao-de-fluxo.webp)

### [Comissão da Câmara dos Deputados fará auditoria pública sobre inversão de fluxo](https://canalsolar.com.br/comissao-camara-deputados-auditoria-publica-inversao-fluxo/)

![Empreendedores desistem de projetos solares no Nordeste](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![Empreendedores desistem de projetos solares no Nordeste](https://canalsolar.com.br/wp-content/uploads/2025/03/Empreendedores-desistem-de-projetos-solares-no-Nordeste.webp)

### [Empreendedores desistem de projetos solares no Nordeste](https://canalsolar.com.br/empreendedores-desistem-projetos-solares-nordeste/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2025/03/BNDES-e-Ministerio-de-Meio-Ambiente-querem-ampliar-certificadoras-de-carbono-no-Brasil.webp)

### [BNDES e Ministério de Meio Ambiente querem ampliar certificadoras de carbono no Brasil](https://canalsolar.com.br/certificadoras-de-carbono-no-brasil/)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20558%20342'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/05/LOGO-CANAL-SOLAR-VERSAO-2-copiar.webp)

É um canal de notícias e informações sobre o setor de energia solar fotovoltaica. O conteúdo do canal é protegido pela lei de direitos autorais. É proibida a reprodução parcial ou total deste site em qualquer meio.

[Mapa do Site](https://canalsolar.com.br/mapa-do-site/)

Categorias

Canais

Associação e certificações

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20332'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/01/ABGD.webp)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20332'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/01/IEEE-copiar.webp)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20332'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/01/Cigre.webp)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%201024%20332'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/01/CREA-SP.webp)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%202452%202452'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2024/04/SELO_ABSOLAR_PORTUGUES_PNG-min-1-copiar.webp)

## Assine nosso boletim informativo semanal

Preencha os dados acima e receba seu exemplar gratuito da revista canal solar
