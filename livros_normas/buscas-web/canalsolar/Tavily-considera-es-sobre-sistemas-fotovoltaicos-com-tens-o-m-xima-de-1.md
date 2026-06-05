# Considerações sobre sistemas fotovoltaicos com tensão máxima de 1500 V

**Fonte:** https://canalsolar.com.br/sistemas-fotovoltaicos-com-tensao-maxima-de-1500-v

![logo site canal solar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20846%20179'%3E%3C/svg%3E)
![logo site canal solar](https://canalsolar.com.br/wp-content/uploads/2024/01/LOGO-CANAL-SOLAR-VERSAO-5-copiar.svg)
![logo site canal solar](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20846%20179'%3E%3C/svg%3E)
![logo site canal solar](https://canalsolar.com.br/wp-content/uploads/2024/01/LOGO-CANAL-SOLAR-VERSAO-5-copiar.svg)

# Considerações sobre sistemas fotovoltaicos com tensão máxima de 1500 V

![Foto de Mateus Vinturini](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20100%20100'%3E%3C/svg%3E)
![Foto de Mateus Vinturini](https://canalsolar.com.br/wp-content/uploads/2021/10/Vinturini-100x100.jpeg)
![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20768%20511'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2020/12/placas-solares-instaladas-com-arvores-de-fundo-768x511-1.jpg) 





![](https://canalsolar.com.br/wp-content/uploads/2020/12/placas-solares-instaladas-com-arvores-de-fundo-768x511-1.jpg)

Os padrões de tensão de isolação dos cabos, módulos e conexões fotovoltaicos evoluíram com o tempo. Os primeiros sistemas fotovoltaicos comercialmente aplicados tinham como padrão a tensão de isolação de 600 V, que depois mudou para 1000 V e, mais recentemente, para 1500 V. A evolução das tensões admissíveis nos sistemas fotovoltaicos foi acompanhada do aumento das tensões máximas tipicamente suportadas pelos inversores. Logo, o projetista tem cada vez mais opções de trabalhar com strings de 1000 V a 1500 V. De maneira geral, quando aumentamos a tensão de trabalho das strings, a questão que merece mais atenção é a garantia do nível de isolação dos componentes (cabos,  módulos, chaves e fusíveis, por exemplo). Já quando aumentamos a corrente, via de regra,  precisamos aumentar a seção dos condutores e adequá-los para as temperaturas de operação. Então, se imaginarmos um conjunto de módulos a serem arranjados em série e paralelo, ao escolhermos trabalhar com tensões maiores (strings mais longas e menos strings em paralelo), tendemos a trabalhar com cabos de seção menor e menos fusíveis, disjuntores e barramentos, uma vez que temos menos strings em paralelo. Para ilustrar a vantagem de se trabalhar com strings de 1500 V de tensão máxima em vez de 1000 V, vamos comparar o dimensionamento de um sistema fotovoltaico com dois modelos de inversores diferentes. Vamos tomar como base para este exemplo os inversores 125K-HV-5G (1000 V) e o 125K-EHV-5G (1500 V), ambos produzidos pela Solis[Solis](https://novo.canalsolar.com.br/portfolio/solis/) e de mesma potência nominal, porém com tensões máximas distintas. Importante notar que este comparativo não é realizado em termos de energia produzida, uma vez que os inversores selecionados têm números de entradas de MPPT diferentes, podendo produzir resultados diferentes conforme a aplicação. Este será um comparativo de complexidade e custo do cabeamento. Para deixar o comparativo entre topologias de 1000 V e 1500 V menos dependente do modelo específico do inversor do exemplo, vamos imaginar que seja necessário paralelizar todas as strings em uma string-box e sair com um par de cabos CC para o inversor. Para compor este sistema utilizaremos módulos de 400 Wp da [Risen](https://novo.canalsolar.com.br/risen/), conforme os dados abaixo:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20223'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2020/12/tabela-electrical-data-498x302-1-300x182.jpg)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20368%20223'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2020/12/tabela-electrical-data-498x302-1-300x182.jpg)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20103'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2020/12/tabela-electrical-data-559x149-1-300x80.jpg)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20386%20103'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2020/12/tabela-electrical-data-559x149-1-300x80.jpg)

Vamos compor um sistema de 150 kWp, deixando os inversores de 125 kW levemente sobrecarregados. Para atingir 150 kW de potência CC precisaremos de 375 módulos de 400 W. Iniciaremos determinando o número máximo de módulos em série, considerando uma temperatura ambiente mínima pelas manhãs de 10ºC. Para isto, precisaremos realizar o cálculo do Voc corrigido para esta temperatura:

Variação do Voc = (Temp. Ambiente – Temp. STC) x coeficiente de variação de Voc

Variação = (10-25) x -0,29 = + 4,35%

Voc corrigido pela temperatura = Voc\_STC x (1+ 4,35%) = 50,7 V

O número máximo de módulos em série para o inversor de 1000 V será então:

1000 / 50,7 = 19 unidades (arredondando para baixo)

E para o inversor de 1500 V:

1500 V / 50,7 = 29 unidades (arredondando para baixo)

Para chegarmos ao número de strings em paralelo necessárias, podemos dividir o número total de módulos pelo número de módulos por string para cada uma das situações: Para o sistema de 1000 V:

375 / 19 = 20 strings em paralelo (arredondando para cima)

Para o sistema de 1500V:

375 / 29 = 13 strings em paralelo (arredondando para cima)

Como todas as strings estão paralelas, é obrigatório o uso de fusíveis em pelo menos um dos condutores. O sistema de 1000 V precisará então de 20 fusíveis, enquanto o sistema de 1500 V necessitará de somente 13 fusíveis. Isto permite a escolha de string-boxes fisicamente menores e com menor custo por unidade.

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20308'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2020/12/esquema-sistema-das-string-box-653x583-1-300x223.jpg)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20415%20308'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2020/12/esquema-sistema-das-string-box-653x583-1-300x223.jpg)

Vamos imaginar que exista uma distância média de 10 m entre os módulos e a string-box. Desta forma, o sistema de 1000 V precisaria de 200 m de condutor positivo e mais 200 m de condutor negativo para conectar as strings à string-box. Já no sistema de 1500 V, precisamos somente de 130 m para o positivo e 130 m para o negativo. Utilizando os critérios de dimensionamento de condutores das normas NBR 16690 e NBR 16612, também percebemos outra diferença importante entre os sistemas: o condutor para o sistema de 1000 V precisa ser de 95 mm² e o condutor do sistema de 1500 V pode ser o de 50 mm². Dependendo da distância da string-box até o inversor a diferença de custo pode ser considerável. Você pode ler mais sobre o dimensionamento de cabos no artigo [Dimensionamento de cabos e proteções em sistemas fotovoltaicos](/dimensionamento-de-cabos-e-protecao). A seguir apresenta-se a Tabela C.3 da norma NBR 16612:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20485%20433'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2020/12/capacidade-de-conducao-de-corrente-para-cabos-instalados-em-temp-ambiente-453x404-1-300x268.jpg)

Com base nas orientações normativas e nas características do projeto, temos os seguintes resultados:

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20426%20182'%3E%3C/svg%3E)![](https://canalsolar.com.br/wp-content/uploads/2020/12/fig-5-449x192-1-300x128.jpg)

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20426%20182'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2020/12/fig-5-449x192-1-300x128.jpg)

Neste exemplo, comparamos sistemas de 1000 V e 1500 V para uma potência de 150 kWp (e 125 kW de inversor). Se considerássemos uma usina de maior escala (como 6,5 MWp, por exemplo), teríamos diferenças muito mais significativas: 303 fusíveis e 6000 m de cabo a menos para a solução de 1500 V em relação à solução de 1000 V. Isto sem considerar a facilidade de instalação, projeto e manuseio de menos cabos na obra.

## Cuidados com sistemas de 1500 V

Como estamos trabalhando com um nível de tensão maior, a intensidade de arcos elétricos no caso de falhas é maior. Logo, precisamos garantir que todos os componentes sejam compatíveis com os 1500V, sendo eles: módulos, cabos, fusíveis, porta-fusíveis, disjuntores, chaves, barramentos, protetores de surto (DPS) e inversores. Utilizando os componentes corretos, não há riscos maiores no uso de sistemas de 1500 V em vez de 1000 V. Os componentes próprios para 1500 V podem ter um custo maior do que os componentes para sistemas de 1000 V, mas a experiência do mercado mostra que esta diferença é facilmente encoberta pelo benefício de ter menos strings, fusíveis, cabos e mão-de-obra nos sistemas de tensão maior. A vantagem de se utilizar sistemas de 1500 V é proporcional ao tamanho do sistema. Para sistemas de pequeno porte não há diferença significativa no custo de fusível, string-box e cabos em relação a sistemas de 1000 V. Do ponto de vista da segurança das instalações, os dois tipos de sistemas fotovoltaicos, com 1000 V e 1500 V, são idênticos. Como comentado anteriormente, os componentes devem ser especificados corretamente, de acordo com o nível de tensão empregado. Aliado a isso, a norma NBR 5410, que rege os circuitos de baixa tensão (categoria na qual se enquadram os sistemas fotovoltaicos), diz que os sistemas que trabalham acima de 1000 V só podem ser acessados por pessoas classificadas como qualificadas, como mostrado na tabela abaixo:

## Conclusão

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20446%20318'%3E%3C/svg%3E)
![](https://canalsolar.com.br/wp-content/uploads/2020/12/tabla-copetencia-das-pessoas-556x396-1-300x214.jpg)

Sistemas fotovoltaicos de 1000 V e 1500 V coexistem no mercado. Todos os componentes devem ser compatíveis com o nível de tensão escolhido. Do ponto de vista da segurança é indiferente a escolha do nível de tensão, tanto para o funcionamento dos sistemas como para as pessoas. De acordo com a NBR 5410, a mesma qualificação é exigida para pessoas que trabalham em sistemas com qualquer tensão acima de 1000 V. Nos sistemas de pequeno porte a diferença entre se trabalhar com 1000 V ou 1500 V quase não pode ser notada. Em grande escala, por outro lado, a escolha da tensão pode ter um impacto grande nos comprimentos dos circuitos e nos custos da instalação. Um sistema de 1500 V, como foi exemplificado neste artigo, permite a formação de strings mais longas e o emprego de um número reduzido de strings paralelas. Com menos circuitos de strings a quantidade de cabos é reduzida e são necessários cabos de menor bitola nas ligações entre as string-boxes e os inversores. Fabricantes de inversores disponibilizam equipamentos adequados para operar com tensões de 1000 V e 1500 V. A tensão máxima suportada pelo inversor afeta diretamente a quantidade de módulos em cada string, que deve ser determinada com base na tensão de circuito aberto dos módulos fotovoltaicos (corrigida de acordo com a menor temperatura do local em que vão operar).

![Foto de Mateus Vinturini](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20300%20300'%3E%3C/svg%3E)
![Foto de Mateus Vinturini](https://canalsolar.com.br/wp-content/uploads/2021/10/Vinturini-300x300.jpeg)

## Uma resposta

![](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2042%2042'%3E%3C/svg%3E)![](https://secure.gravatar.com/avatar/640044040a0e32604da01ab24bc7c2f20b9fd3e309ca2e53efddb88638098076?s=42&d=mm&r=g) **Tássio** disse: 
![](https://secure.gravatar.com/avatar/640044040a0e32604da01ab24bc7c2f20b9fd3e309ca2e53efddb88638098076?s=42&d=mm&r=g)

Boa tarde.  
Acredito que exista um erro no cálculo da tensão corrigida.  
Considerando o funcionamento do painel, é intuitivo entender que a tensão de funcionamento dele irá diminuir com o aumento da temperatura ambiente.  
Analisando o cálculo, da para notar que no momento de considerar a temperatura (da placa e do ambiente) houve uma subtração (10 – 25), quando deveria ter acontecido um acréscimo (10 + 25). Esse acrescimento deve ser considerado pois em condições de teste, o ambiente fica a 0 graus e a temperatura na placa fica 25, então quanto mais quente o ambiente, maior a temperatura na placa. Com essas considerações feitas, é possível recalcular a equação considerando que agora o termo (10+25)\*(-0,0029), que é a variação da tensão de saída (Voc) em relação a temperatura, fica como -0,1015 o que representa uma queda de 10,15% no valor de Voc.

## Deixe um comentário [Cancelar resposta](/sistemas-fotovoltaicos-com-tensao-maxima-de-1500-v/#respond)

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

![ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos? ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos?](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos? ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos?](https://canalsolar.com.br/wp-content/uploads/2026/06/Canal-Solar-SO-55001-aplicada-a-energia-solar-como-prolongar-a-vida-util-de-sistemas-fotovoltaicos-1.webp)

### [ISO 55001 aplicada à energia solar: como prolongar a vida útil de sistemas fotovoltaicos?](https://canalsolar.com.br/iso-55001-solar-vida-util-sistemas-fotovoltaicos/)

![Assentamento Irmã Dorothy receberá kits de energia solar no RJ](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![Assentamento Irmã Dorothy receberá kits de energia solar no RJ](https://canalsolar.com.br/wp-content/uploads/2026/05/Canal-Solar-Sudene-destina-R-120-mi-do-FDNE-para-complexo-fotovoltaico-em-Pernambuco-1.webp)

### [Assentamento Irmã Dorothy receberá kits de energia solar no RJ](https://canalsolar.com.br/assentamento-irma-dorothy-energia-solar/)

![Canal Solar - Oito estados ainda terão reajuste na conta de luz até o fim de abril](data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%20850%20566'%3E%3C/svg%3E)
![Canal Solar - Oito estados ainda terão reajuste na conta de luz até o fim de abril](https://canalsolar.com.br/wp-content/uploads/2026/04/Canal-Solar-Oito-estados-ainda-terao-reajuste-na-conta-de-luz-ate-o-fim-de-abril.webp)

### [Oito estados ainda terão reajuste na conta de luz até o fim de abril](https://canalsolar.com.br/oito-estados-ainda-terao-reajuste-conta-de-luz-abril/)

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
