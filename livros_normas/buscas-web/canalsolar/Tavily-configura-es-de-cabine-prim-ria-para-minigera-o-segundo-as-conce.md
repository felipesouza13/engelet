# Configurações de cabine primária para minigeração segundo as concessionárias de energia

**Fonte:** https://canalsolar.com.br/configuracoes-de-cabine-primaria-para-minigeracao-segundo-as-concessionarias-de-energia

![logo site canal solar](https://canalsolar.com.br/wp-content/uploads/2024/01/LOGO-CANAL-SOLAR-VERSAO-5-copiar.svg)
![logo site canal solar](https://canalsolar.com.br/wp-content/uploads/2024/01/LOGO-CANAL-SOLAR-VERSAO-5-copiar.svg)

# Configurações de cabine primária para minigeração segundo as concessionárias de energia

![Foto de Dirceu Ferreira](https://canalsolar.com.br/wp-content/uploads/2023/01/dirceu-100x100.jpg)

De acordo com a norma NBR 14039 – Instalações Elétricas em Média Tensão, uma cabine de média tensão (MT) deve ter os seguintes equipamentos de proteção, em função da capacidade instalada:

#### a) Capacidade instalada menor ou igual a 300 kVA

#### b) Capacidade instalada maior que 300 kVA

Nesta configuração é exigido que a proteção seja por meio de disjuntor acionado por relés secundários com funções 50 e 51 de fase e de neutro. Com o emprego de disjuntor na média tensão subentende-se a necessidade de um local apropriado para abrigá-lo, além dos componentes periféricos como relé, transformadores de corrente e de potencial.

Com o advento da resolução 482/2012 da ANEEL que trata dos agentes que operam no modo de compensação de energia, surgiu uma nova classificação de consumidores em micro e minigeração. Esta classificação é bem definida como:

E dentro deste contexto é que as distribuidoras de energia no Brasil admitem várias concepções de configuração para a conexão de um cliente no sistema de média tensão, chamado A4. Percorrendo as diversas normas das concessionárias, observa-se que não há um consenso para uso de uma configuração comum, ainda que se preservem as características de cada região do país. Mas podemos destacar ao menos duas vertentes:

Outra questão importante é a respeito do sistema de medição de faturamento dos clientes A4. De acordo com a NBR 14039, a medição pode ser na baixa tensão se a capacidade instalada for de até 300 kVA. Acima deste valor, a medição deve ser na média tensão.

Assim, a localização do setor de medição é outro fator importante na configuração de uma cabine primária. Trataremos aqui dos aspectos de proteção utilizando as concepções típicas de 2 concessionárias para minigeração – Celesc e CPFL – de acordo com as suas normas técnicas:

## **Diagramas Referenciais**

Para tratar das 2 configurações típicas são apresentados os esquemas adotados pela CELESC e pela CPFL, apresentados nas Figuras 1 e 2.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20512%20415'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2021/08/configuracao-de-cabine-primaria-de-acordo-com-a-Celesc-512x415-1.jpg)

Figura 1: Configuração de cabine primária de acordo com a Celesc

![](https://canalsolar.com.br/wp-content/uploads/2021/08/configuracao-de-cabine-primaria-de-acordo-com-a-Celesc-512x415-1.jpg)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20358%20512'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2021/08/configuracao-de-cabine-primaria-de-acordo-com-a-CPFL-358x512-1.jpg)

## Comparações

Observando os diagramas, nota-se que as empresas já apresentam diferenças com relação à forma de classificação. Enquanto a Celesc trata em termos de potência aparente, a CPFL trata como potência ativa. A norma da Celesc não faz qualquer menção no texto quanto ao uso de chave fusível no lado de média tensão, mas a configuração adotada indica o uso de chave fusível (Figura 1).

Por outro lado, a CPFL não permite o uso de chave fusível entre o ponto de conexão e a geração, baseada na norma técnica GED 33 (Ligação de Autoprodutores em Paralelo com o Sistema de Distribuição da CPFL), item 6.1: *“…Ressalva-se que não é permitido o uso de fusíveis nem de seccionadores monopolares entre o interruptor de entrada e o gerador, ou geradores.” Este requisito é ratificado na configuração mostrada na Figura 2.*

A mesma restrição é também exigida pelo Módulo 3 do Prodist, seção 3.3: *“5.4.8 Não devem ser utilizados fusíveis ou seccionadores monopolares entre o disjuntor de entrada e os geradores.”*

No entanto, este item não é evidenciado na seção 3.7 que trata dos procedimentos de micro e minigeração. Tratando-se especificamente das funções de proteção, particularmente sobre geração fotovoltaica, os diagramas mostrados nas Figuras 1 e 2 indicam que elas devem atuar nos respectivos disjuntores, apesar de algumas proteções poderem ser executadas pelos inversores.

A Tabela 1 apresenta as proteções exigidas pelo Módulo 3 e que podem ser habilitadas no relé e/ou inversores.

##### Tabela: Funções de proteção dos relés ou inversores

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Proteção** | **Função** | **Descrição** | **Habilitação** | |
| **Relé** | **Inversor** |
| ***Convencional*** | 50/51 | Sobrecorrente de fase | X |  |
| 50N/51N | Sobrecorrente de neutro | X |  |
| ***Complementares*** | 59N ou | Sobretensão de neutro | X |  |
| 67N | Sobrecorrente direcional de neutro | X |  |
| 32 | Direcional de potência | X | X |
| 25 | Sincronismo |  | X |
| 27 | Subtensão | X | X |
| 59 | Sobretensão de neutro | X | X |
| 46 | Desbalanço de corrente | X |  |
| 47 | Desbalanço de tensão | X |  |
| 51V | Sobrecorrente com restrição de tensão | X |  |
| 67 | Sobrecorrente direcional de fase | X |  |
| 78 | Medição de ângulo de fase | X |  |
| 81 O/U | Sobre e sub frequência | X | X |
| s/n | Anti-ilhamento |  | X |

Quando as proteções são executadas pelos relés, há necessidade de instalação de transformadores de corrente (TCs) e de potencial (TPs) instalados adequadamente para detectar sinais no lado de média tensão. Por exemplo, a função 59N exige o uso de três TPs no lado de média tensão, bem como as funções de sobrecorrente necessitam de 3 TCs.

Essas necessidades implicam na existência de um ambiente adequado, ou seja, uma cabine de média tensão. De uma forma geral, a Tabela 2 apresenta as principais características entre as configurações das duas concessionárias.

##### Tabela 2: Características das configurações de cabine primária para duas concessionárias

|  |  |  |  |
| --- | --- | --- | --- |
| Dispositivo | Celesc | | CPFL |
| P ≤ 300 kVA | P > 300 kVA | P > 75 kW |
| Chave fusível na MT | Sim | Sim | Não |
| Disjuntor na MT | Não | Sim | Sim |
| Atuações das Proteções | BT | MT | MT |

Verifica-se que a CPFL, para qualquer minigeração, exige o uso de disjuntor de MT.

## Comentários

Este artigo tratou de configurações adotadas por duas concessionárias e as duas linhas de configurações sofrem ainda variantes em algumas concessionárias. Pode-se dizer que a configuração adotada pela CPFL é semelhante à da Elektro e à da Roraima Energia. Já a configuração adotada pela Celesc, com algumas variações, é seguida pela Copel e pela Cemig.

Na Copel e na Cemig existem variações com relação ao uso de inversores e em função da potência e do tipo de subestações. De toda forma, essas variantes afetam a especificação da cabine, refletindo no custo de implantação da usina. Em se tratando de geração fotovoltaica, seria oportuno que houvesse um mesmo procedimento entre as concessionárias e algumas otimizações poderiam ser avaliadas:

### Bibliografia

![Foto de Dirceu Ferreira](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20200%20200'%3E%3C/svg%3E)
![Foto de Dirceu Ferreira](https://canalsolar.com.br/wp-content/uploads/2023/01/dirceu.jpg)

## Respostas de 6

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)![](https://secure.gravatar.com/avatar/c1694d2fe16f435b23c94fc064218413959ffc08e1b657f2825809ce59f8878f?s=42&d=mm&r=g) **Douglas Pereira Ramos** disse: 
![](https://secure.gravatar.com/avatar/c1694d2fe16f435b23c94fc064218413959ffc08e1b657f2825809ce59f8878f?s=42&d=mm&r=g)

O meu caso é uma cabine simplificada de 300kVA Poste único e a concessionaria aprovou o sistema de geração em média tensão, mas com algumas resalvas de regularização.  
se possivel me ajudar agradeço…  
Avredito que é o mesmo procedimento…

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)
![](https://secure.gravatar.com/avatar/c1694d2fe16f435b23c94fc064218413959ffc08e1b657f2825809ce59f8878f?s=42&d=mm&r=g)

Neste caso também serveria para a EDP São Paulo/SP.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)
![](https://secure.gravatar.com/avatar/eee89fb043c66f7834a3407eb1278b769666101e604c6f565cf5798cf4dab7e8?s=42&d=mm&r=g)

Ótimo artigo, estou estudando a norma Selesc : I-432.0004 e me ajudou bastante estes esclarecimentos.

![Beatriz Baquiega](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2034%2042'%3E%3C/svg%3E)
![Beatriz Baquiega](https://canalsolar.com.br/wp-content/uploads/2022/05/canal-solar-Beatriz-Baquiega.jpg)

Agradecemos o reconhecimento, Eduardo!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)
![](https://secure.gravatar.com/avatar/70abc99e0c616f183d741adccbdbb2431b389939ee8a74e62133eb1c1d32edc7?s=42&d=mm&r=g)

Parabéns e obrigado pelo artigo!

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)
![](https://secure.gravatar.com/avatar/7fd57a4c74e6ba722183cca529269a9d4325b37fc937aeff6602cc9c41ffc3b9?s=42&d=mm&r=g)

Oi boa noite já estou na espectativa do treinamento

## Deixe um comentário [Cancelar resposta](/configuracoes-de-cabine-primaria-para-minigeracao-segundo-as-concessionarias-de-energia/#respond)

O seu endereço de e-mail não será publicado. Campos obrigatórios são marcados com \*

Comentário \*

Nome \*

E-mail \*

Site

Salvar meus dados neste navegador para a próxima vez que eu comentar.

Os comentários devem ser respeitosos e contribuir para um debate saudável. Comentários ofensivos poderão ser removidos. As opiniões aqui expressas são de responsabilidade dos autores e não refletem, necessariamente, a posição do Canal Solar.

### Notícias do Canal Solar no seu E-mail

### Relacionados

![Entenda na prática como dimensionar sistemas híbridos com bateria](https://canalsolar.com.br/wp-content/uploads/2026/04/Canal-Solar-Estudo-recomenda-que-bares-e-restaurantes-apostem-em-energia-solar-na-copa-do-mundo-para-aumentarem-faturamento-1.webp)

[Entenda na prática como dimensionar sistemas híbridos com bateria](https://canalsolar.com.br/entenda-dimensionar-sistemas-hibridos-bateria/)

![ESG na Energia Solar Fotovoltaica Brasileira: Governança, Regulação e Engenharia de Projetos](https://canalsolar.com.br/wp-content/uploads/2026/04/Canal-Solar-ESG-na-Energia-Solar-Fotovoltaica-Brasileira-Governanca-Regulacao-e-Engenharia-de-Projetos.webp)

[ESG na energia solar fotovoltaica brasileira: governança, regulação e engenharia de projetos](https://canalsolar.com.br/esg-energia-solar-regulacao-engenharia-projetos/)

## [Mais Notícias](/category/noticias)

![Canal Solar - Falta de qualificação em cabine primária aumenta riscos em projetos de GD](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![Canal Solar - Falta de qualificação em cabine primária aumenta riscos em projetos de GD](https://canalsolar.com.br/wp-content/uploads/2025/07/Canal-Solar-Falta-de-qualificacao-em-cabine-primaria-aumenta-riscos-em-projetos-de-GD.webp)

### [Falta de qualificação em cabine primária aumenta riscos em projetos de GD](https://canalsolar.com.br/falta-qualificacao-cabine-primaria-riscos-projetos/)

![Dimensionamento das proteções em cabines primárias para usinas solares](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![Dimensionamento das proteções em cabines primárias para usinas solares](https://canalsolar.com.br/wp-content/uploads/2025/01/Dimensionamento-das-protecoes-em-cabines-primarias-para-usinas-solares.webp)

### [Dimensionamento das proteções em cabines primárias para usinas solares](https://canalsolar.com.br/dimensionamento-protecoes-cabines-primarias-usinas-solares/)

![11-08-23-canal-solar-Alarme de falha de isolação em inversores do tipo string](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![11-08-23-canal-solar-Alarme de falha de isolação em inversores do tipo string](https://canalsolar.com.br/wp-content/uploads/2023/08/11-08-23-canal-solar-Alarme-de-falha-de-isolacao-em-inversores-do-tipo-string.jpg)

### [Alarme de falha de isolação em inversores do tipo string](https://canalsolar.com.br/alarme-de-falha-de-isolacao-em-inversores-do-tipo-string/)

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
