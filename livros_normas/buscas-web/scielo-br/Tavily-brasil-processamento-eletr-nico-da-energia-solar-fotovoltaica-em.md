# Brasil - Processamento eletrônico da energia solar fotovoltaica em sistemas conectados à rede elétrica Processamento eletrônico da energia solar fotovoltaica em sistemas conectados à rede elétrica

**Fonte:** https://www.scielo.br/j/ca/a/LzxvkKP5YDqBzxtWx9js75q?lang=pt

Menu

* [English](/set_locale/en/)
* [Español](/set_locale/es/)

Sba: Controle & Automação Sociedade Brasileira de Automatica 


* [info Sobre o periódico](/journal/ca/about/#about)
* [help\_outline Política editorial](/journal/ca/about/#item2)
* [people Corpo Editorial](/journal/ca/about/#editors)
* [help\_outline Instruções aos autores](/journal/ca/about/#instructions)
* [email Contato](/journal/ca/about/#contact)
* [show\_chart Métricas](http://analytics.scielo.org/?journal=0103-1759&collection=scl)



[home](/j/ca/)   [Sumário](/j/ca/i/2010.v21n2/)   [navigate\_before Anterior](/j/ca/a/fZRQ6hgLMdS4cdYPP4ZyYNh/?lang=pt)   [Atual](#)   [Seguinte navigate\_next](/j/ca/a/dsZ9ZmJ9V6vnyBbvGMSK7CS/?lang=pt)

* [Resumo (Português)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/abstract/?lang=pt)
* [Resumo (Inglês)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/abstract/?lang=en)

* [Texto (Português)](#)

* [Download PDF (Português)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/?format=pdf&lang=pt)

* [Resumo (Português)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/abstract/?lang=pt)
* [Resumo (Inglês)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/abstract/?lang=en)
* [Texto (Português)](#)
* [Download PDF (Português)  (abre em nova aba)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/?format=pdf&lang=pt)

[home](/j/ca/)   [Sumário](/j/ca/i/2010.v21n2/) 

* Whatsapp
* BlueSky
* Mastodon
* Facebook
* [Mais](https://www.addtoany.com/share)

* [Resumo (Português)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/abstract/?lang=pt)
* [Resumo (Inglês)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/abstract/?lang=en)

* [Texto (Português)](#)

* [Download PDF (Português)  (abre em nova aba)](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/?format=pdf&lang=pt)

Eletrônica de Potência • Sba Controle & Automação 21 (2)  • Abr 2010 • <https://doi.org/10.1590/S0103-17592010000200005> [linkcopiar](javascript:;)

# Processamento eletrônico da energia solar fotovoltaica em sistemas conectados à rede elétrica

## Electronic processing of the photovoltaic solar energy in grid connected systems

AutoriaSCIMAGO INSTITUTIONS RANKINGS

## Resumo

Este artigo apresenta um sistema fotovoltaico conectado à rede elétrica comercial em configuração centralizada e construído com um inversor trifásico de dois estágios capaz de extrair a máxima potência do arranjo de painéis fotovoltaicos. O algoritmo P&O é adotado como técnica de MPPT. O isolamento é realizado por um transformador de alta frequência. O conversor que compõe o estágio CC-CC dispensa a estrutura de controle, pois funciona com razão cíclica e frequência constantes ao longo de toda a faixa de operação. Isto viabiliza o uso de conversores CC-CC ressonantes, cujo rendimento é elevado em altas frequências, favorecendo a compactação da estrutura de potência. Assim, o conversor trifásico série ressonante é escolhido para compor este estágio. O MPPT é transferido para o estágio CC-CA, que, invariavelmente, possui um controlador para a corrente injetada na rede elétrica. O inversor trifásico PWM alimentado em tensão, que compõe o estágio CC-CA, é controlado e modulado vetorialmente. O controle vetorial impõe a transformação de Park as correntes de linha, de onde resulta a corrente de eixo direto. O MPPT utiliza as mesmas variáveis do controlador de corrente e maximiza a corrente de eixo direto, a qual reflete a potência extraída do arranjo fotovoltaico. Assim, nenhuma medição específica para o MPPT é realizada, resultando em economia de sensores.

sistema fotovoltaico; inversor trifásico de dois estágios; conversor CC-CC trifásico série ressonante; MPPT

---

## Abstract

This paper presents a grid-connected photovoltaic system in centralized configuration and constructed with a three-phase dual-stage inverter able to extract the maximum power of the PV modules. The P&O algorithm is adopted as MPPT technique. The isolation is achieved by a high-frequency transformer. The converter used in the DC-DC stage dispenses control-loop, its duty-cycle and switching frequency are constants throughout the power operation range. This enables the application of DC-DC resonant converters, whose efficiency is high at high frequencies, favoring compaction of the power circuit. Thus, the three-phase series resonant converter is chosen to integrate this stage. The MPPT is transferred to the DC-AC stage, which, invariably, has a grid current controller. The three-phase PWM voltage-source inverter, in the DC-AC stage, uses vector control and space vector modulation. The vector control requires a Park's transformation from the grid-currents which yield the direct axis current. The MPPT uses the same variables of the grid current controller and maximize the direct axis current which reflects the power flux from the PV array. Thus, any specific measurement to realize the MPPT is not needed, resulting in a small count of sensors.

photovoltaic system; three-phase dual-stage inverter; three-phase series ressonant converter; MPPT

---

**ELETRÔNICA DE POTÊNCIA**

**Processamento eletrônico da energia solar fotovoltaica em sistemas conectados à rede elétrica**

**Electronic processing of the photovoltaic solar energy in grid connected systems**

**Marcio Mendes CasaroI; Denizar Cruz MartinsII**

IUniversidade Tecnológica Federal do Paraná Av. Monteiro Lobato, km 04, Ponta Grossa, Paraná - CEP: 84.016-210 [casaro@utfpr.edu.br](mailto:casaro@utfpr.edu.br)

IIUniversidade Federal de Santa Catarina, INEP Caixa postal 5119, Florianópolis, Santa Catarina - CEP: 88.040-970 [denizar@inep.ufsc.br](mailto:denizar@inep.ufsc.br)

**RESUMO**

Este artigo apresenta um sistema fotovoltaico conectado à rede elétrica comercial em configuração centralizada e construído com um inversor trifásico de dois estágios capaz de extrair a máxima potência do arranjo de painéis fotovoltaicos. O algoritmo P&O é adotado como técnica de MPPT. O isolamento é realizado por um transformador de alta frequência. O conversor que compõe o estágio CC-CC dispensa a estrutura de controle, pois funciona com razão cíclica e frequência constantes ao longo de toda a faixa de operação. Isto viabiliza o uso de conversores CC-CC ressonantes, cujo rendimento é elevado em altas frequências, favorecendo a compactação da estrutura de potência. Assim, o conversor trifásico série ressonante é escolhido para compor este estágio. O MPPT é transferido para o estágio CC-CA, que, invariavelmente, possui um controlador para a corrente injetada na rede elétrica. O inversor trifásico PWM alimentado em tensão, que compõe o estágio CC-CA, é controlado e modulado vetorialmente. O controle vetorial impõe a transformação de Park as correntes de linha, de onde resulta a corrente de eixo direto. O MPPT utiliza as mesmas variáveis do controlador de corrente e maximiza a corrente de eixo direto, a qual reflete a potência extraída do arranjo fotovoltaico. Assim, nenhuma medição específica para o MPPT é realizada, resultando em economia de sensores.

**Palavras-chave:** sistema fotovoltaico, inversor trifásico de dois estágios, conversor CC-CC trifásico série ressonante, MPPT.

**ABSTRACT**

This paper presents a grid-connected photovoltaic system in centralized configuration and constructed with a three-phase dual-stage inverter able to extract the maximum power of the PV modules. The P&O algorithm is adopted as MPPT technique. The isolation is achieved by a high-frequency transformer. The converter used in the DC-DC stage dispenses control-loop, its duty-cycle and switching frequency are constants throughout the power operation range. This enables the application of DC-DC resonant converters, whose efficiency is high at high frequencies, favoring compaction of the power circuit. Thus, the three-phase series resonant converter is chosen to integrate this stage. The MPPT is transferred to the DC-AC stage, which, invariably, has a grid current controller. The three-phase PWM voltage-source inverter, in the DC-AC stage, uses vector control and space vector modulation. The vector control requires a Park's transformation from the grid-currents which yield the direct axis current. The MPPT uses the same variables of the grid current controller and maximize the direct axis current which reflects the power flux from the PV array. Thus, any specific measurement to realize the MPPT is not needed, resulting in a small count of sensors.

**Keywords:** photovoltaic system, three-phase dual-stage inverter, three-phase series ressonant converter, MPPT.

**1 INTRODUÇÃO**

Neste trabalho é apresentado um inversor de dois estágios modificado usado no processamento da energia solar fotovoltaica em sistemas conectados à rede elétrica. Trata-se de um equipamento inovador em vários aspectos, cuja concepção enfatizou a redução de custos, volume e peso. Nesta concepção, foram abordadas somente questões comercialmente viáveis, embora esta aplicação ainda não esteja regulamentada no Brasil.

A conversão direta da energia solar em elétrica é realizada por módulos fotovoltaicos. O custo destes equipamentos é o principal fator que define a opção por outras fontes geradoras. Um sistema fotovoltaico não produz lixo tóxico como as usinas nucleares, não polui o meio ambiente como as termoelétricas a gás ou a carvão e não envolve nenhum impacto ambiental ou social como as hidrelétricas. Assim, a justificativa fundamental para o desenvolvimento deste trabalho é a grande expectativa pela redução do custo de fabricação das células solares, projetado para algo abaixo dos US$0,40/watt contra os atuais US$4,00/watt (Burger, 2008). É de se observar que esta redução elevará proporcionalmente o peso que o inversor exerce no custo total do sistema. A figura 1 mostra um gráfico elaborado a partir da consulta a diversos revendedores de inversores para o mercado europeu e norte americano, a exemplo de Alter Systems (2008).

Tendo em vista que o custo médio para geração de hidroeletricidade é de US$1,00/watt, mesma relação de investimento/watt verificada para um inversor de 10kW, fica evidente a necessidade do aperfeiçoamento tecnológico dos inversores conectados à rede, a fim de tornar esta modalidade de energia alternativa competitiva no Brasil.

**1.1 Contexto Energético Brasileiro**

O sistema de produção e transmissão de energia elétrica do Brasil é um sistema hidrotérmico de grande porte, com forte predominncia de usinas hidrelétricas que respondem atualmente por aproximadamente 80% da energia elétrica gerada no Brasil.

Para compensar a falta de investimentos em usinas hidrelétricas, o governo federal criou um programa de construção de usinas termoelétricas a gás. Em períodos de condições hidrológicas desfavoráveis, estas contribuem para o atendimento ao mercado consumidor de maneira complementar (Agência, 2005).

No ano de 2007, registrou-se o maior aumento no consumo de energia elétrica da década, cerca de 5%. Credita-se este aumento ao crescimento sustentável do Brasil. Porém, o racionamento, devido ao baixo nível dos reservatórios de água, foi evitado graças ao acionamento das termoelétricas (Consumo, 2007). Mas a maior parte do gás disponível no mercado esta comprometido com empresas que, nos últimos anos, passaram a usar o insumo, e com uma crescente frota de veículos movidos a gás. Testes recentes feitos pelo Operador Nacional do Sistema Elétrico Brasileiro mostraram que cerca da metade da capacidade instalada das termoelétricas não podia ser usada por falta de combustível (O Racionamento, 2007).

Só haverá desenvolvimento sustentável com investimentos na geração de energia vinda de fontes renováveis, ou seja, aquelas que não consomem combustíveis e não produzem resíduos prejudiciais. Assim, a conservação da energia proveniente das usinas hidrelétricas, papel desempenhado pelas termoelétricas, poderia ser auxiliada por sistemas solares fotovoltaicos, bastante adequados à integração com o meio urbano.

O Brasil exibe um alto índice médio diário de radiação solar, chegando a mais de 5kWh/m2 por dia em algumas regiões (Agência, 2005). Utilizando módulos fotovoltaicos com 40% de eficiência, que estão em fase inicial de industrialização (Célula, 2007), seriam gerados 2kWh/m2 por dia. Assim, menos de 10m2, em média, seriam suficientes para abastecer uma unidade consumidora de Santa Catariana, cujo consumo médio é de 503kWh/mês, o maior do sul do país (Celesc, 2008). Este Estado possui uma média de 2,7 habitantes por unidade consumidora, ou seja, por ponto de medição.

**1.2 Sistemas Fotovoltaicos**

Sistemas fotovoltaicos usam inversores de tensão chaveados para o condicionamento e sincronismo da saída do arranjo fotovoltaico com a rede de energia elétrica. O controle exerce duas funções principais, rastrear o ponto de operação de máxima potência (MPPT) do arranjo fotovoltaico e injetar uma corrente senoidal na rede, com fator de potência próximo ao unitário.

São três as topologias de inversores conectados à rede elétrica (Carrasco *et alii*, 2006):

>  Inversor de um estágio: em um único estágio de processamento são realizados o MPPT e o controle da corrente injetada na rede.
>
>  Inversor de dois estágios: um conversor CC-CC realiza o MPPT enquanto um conversor CC-CA é responsável pelo controle da corrente injetada na rede.
>
>  Inversor de múltiplos estágios: vários conversores CCCC respondem pelo MPPT e um único conversor CCCA cuida da corrente injetada na rede.

As maneiras como os módulos fotovoltaicos são combinados com as topologias de inversores se apresentam em quatro configurações diferentes.

>  Inversor centralizado: módulos fotovoltaicos são ligados em série para formar uma fileira. Fileiras são conectadas em paralelo para formar o arranjo, que fornece energia ao barramento CC de um inversor. Apresentado na figura 5.
>
>  CC paralelo: fileiras ou arranjos são conectados a conversores CC-CC. Um único barramento CC interno alimenta um conversor CC-CA. Apresentado na figura 6.
>
>  CA paralelo: fileiras ou arranjos são conectados a inversores individuais. As saídas destes inversores são ligadas internamente em paralelo do lado CA. Apresentado na figura 7.
>
>  Inversor integrado: cada módulo fotovoltaico tem um pequeno inversor. Esses inversores são ligados em paralelo do lado CA. Apresentado na figura 8.

A tabela 1 relaciona as topologias de inversores conectados à rede com as possíveis configurações de sistemas fotovoltaicos.

Thumbnail

**1.3 Considerações**

Em alguns países, a exemplo dos Estados Unidos, o isolamento galvnico entre o arranjo fotovoltaico e a rede de energia elétrica é obrigatório. Por isso, modernos inversores tendem a usar um transformador de alta freqüência (Carrasco *et alii*, 2006). Isso ocorre porque o transformador de baixa freqüência é maior, mais pesado, mais caro e apresenta me-nor eficiência (Rashid, 2001). Para que um transformador de alta freqüência possa integrar a topologia do inversor usado em um sistema fotovoltaico, o estágio CC-CC se torna imprescindível.

Segundo Carrasco *et alii* (2006), em suas considerações sobre tendências futuras, para que haja uma redução no custo por watt de inversores conectados à rede elétrica é indicada a adoção da configuração centralizada. Além disso, esta configuração é apontada como a mais apropriada para potências superiores a 10kW, por ser de alta eficiência e de baixo custo específico.

A partir destas considerações, pode-se direcionar a atenção para o inversor de dois estágios com isolamento em alta freqüência e configurado em uma planta centralizada de média potência. Conforme Carletti *et alii* (2005), uma planta de média potência vai de 10kW até 500kW. A seguir se faz uma abordagem sobre as estruturas a serem empregadas nos dois estágios do inversor.

Carrasco *et alii* (2006) apresentam o conversor Full-Bridge como o representante do estágio CC-CC mais empregado em potências acima de 750W, devido ao seu bom fator de utilização do transformador. Porém, em Ziogas *et alii* (1988) é demonstrado que a conversão trifásica é vantajosa quando comparada com a monofásica. De um modo geral, verifica-se uma melhor distribuição das perdas em estruturas trifásicas, tal que os componentes são submetidos a um esforço relativamente menor. Filtros capacitivos ou indutivos têm seu volume sensivelmente reduzido, pois a corrente que os atravessa tem frequência superior aquela que teria em um conversor monofásico. Falando especificamente do estágio CCCC, em Ziogas *et alii* (1988) ficou demonstrada uma redução no volume do transformador trifásico de alta frequência em comparação ao utilizado no Full-Bridge. A combinação dessas vantagens leva a uma melhora no comportamento dinmico, com respostas mais rápidas.

A tabela 2 foi elaborada através da consulta aos catálogos de alguns dos principais representantes do mercado de inversores conectados à rede no mundo. Sua finalidade é manter estreita a relação deste trabalho com a linha comercial.

Thumbnail

A partir de 8kW todos os inversores são trifásicos. Até 10kW predominam equipamentos não isolados. São leves e compactos. De 5 a 10kW a configuração CC paralelo é a preferida. Com dois a três conversores CC-CC na entrada, esta oferece mais flexibilidade na montagem do arranjo fotovoltaico. Acima de 10kW, todas as estruturas tendem a ser isoladas. Os transformadores de baixa frequência são os mais comuns, instalados em volumosos e pesados inversores. A configuração CA paralelo é bastante adotada para permitir o uso de transformadores de alta frequência. Alguns fabricantes chegam a usar quinze conversores CC-CA em configuração CA paralelo. Porém, a configuração centralizada com o isolamento em alta frequência é a combinação que conduz aos equipamentos mais leves.

O MPPT é realizado no estágio CC-CC em todos os inversores conectados à rede que possuem um estágio CC-CC, especialmente os isolados em alta frequência.

A potência de 15kW aparenta ser a mais promissora no Brasil. Embora o custo/watt tenda a diminuir, há duas limitações práticas para potências maiores. Poderia haver dificuldade para encontrar áreas grandes o suficiente para a instalação dos módulos fotovoltaicos (estima-se em 130m2 a área necessária para 15kW de painéis da atual tecnologia) e não se-ria qualquer secundário de transformador de distribuição trifásico que aceitaria a conexão do inversor (os menores transformadores trifásicos instalados pelas concessionárias são de 15kVA, normalmente). Vale salientar que o inversor proposto neste trabalho é destinado a áreas urbanas, integrado a construções. O uso de telhados e janelas de prédios públicos seria um interessante ponto de partida.

Como conclusão, este trabalho busca propor um inversor de dois estágios com isolamento em alta freqüência, configurado em uma planta centralizada, adequado ao processamento de 15kW de potência e que emprega conversores trifásicos tanto no estágio CC-CC como no estágio CC-CA.

**2 INVERSOR DE DOIS ESTÁGIOS MODIFICADO**

Embora se possa computar como contribuição o desenvolvimento do que foi proposto até o momento, ainda não foram tratadas questões relativas ao controle. Neste assunto, o presente trabalho também elenca propostas que valorizem o inversor em relação ao estado da arte.

Em primeiro lugar, deve-se ter em mente que tanto o MPPT quanto o controle da corrente injetada na rede são implementados em um processador digital de sinais, o que favorece a utilização do controle vetorial e da modulação vetorial. A realização do MPPT frequentemente passa por um dos dois métodos fundamentais conhecidos como perturbação e observação (P&O) e condutncia incremental (IncCond). Destes, o P&O é preferível, especialmente em sistemas conectados à rede e de potência elevada (Hua *et alii*, 1998; Jing *et alii*, 2005).

Neste trabalho, se propõem que o P&O seja executado no estágio CC-CA, a fim de aproveitar a capacidade de processamento envolvida no controle da corrente injetada na rede elétrica, dando origem ao Inversor de Dois Estágios Modificado, ilustrado na figura 9.

Este inversor de dois estágios modificado emprega as mesmas variáveis usadas no controle da corrente injetada na rede para executar o P&O, propiciando uma sensível economia de sensores. Assim, sem que se façam medições específicas para o P&O, pode-se maximizar a potência de saída do inversor e forçar o arranjo fotovoltaico a operar no ponto de máxima potência, MPP.

A estratégia para que isto funcione está fundamentada em uma característica que pode ser observada em conversores CC-CC que os faz reproduzir em seus terminais de saída o mesmo comportamento do arranjo fotovoltaico, quando a eles estão conectados. Um aspecto muito interessante é que para o conversor CC-CC ter um comportamento correspondente ao do arranjo fotovoltaico ele deve operar com freqüência e razão cíclica constantes. Demonstra-se que este aspecto leva conversores, em princípio inviáveis, a funcionarem com extrema eficiência ao longo de toda a faixa de operação do MPPT.

**2.1 Estágio CC-CC**

Os conversores CC-CC trifásicos mais atrativos são aqueles que apresentam comutação suave, pois podem operar com elevadas frequências de chaveamento, o que leva a uma significativa redução em elementos magnéticos e capacitivos. Não são muitos os conversores CC-CC trifásicos com comutação suave disponíveis na literatura. Alguns deles (Doncker *et alii*, 1991; Prasad *et alii*, 1991; Bhat e Zheng, 1996; Oliveira Júnior e Barbi, 2005; Jacobs *et alii*, 2004) foram avaliados quanto a sua eficiência, número de componentes, emissão de interferência eletromagnética, desempenho em condições assimétricas de funcionamento e aptidão a potências elevadas. A estrutura apresentada na figura 10, SRC3, obtida de Jacobs *et alii* (2004), se mostrou insuperável em todos os quesitos. O transformador foi substituído pelas suas indutncias de dispersão (*Ld*).

Os transistores de um mesmo braço são disparados de forma complementar. Entre os braços há uma defasagem de 120º nos pulsos de comando. Quando a frequência de chaveamento, f1, é igual a de ressonncia, *fr*, o conversor opera em ZCS. Se f1 > *fr*, o conversor opera em ZVS. Neste modo de operação, uma redução na potência de entrada, condição normal de funcionamento do arranjo fotovoltaico, reduz bruscamente a eficiência do conversor (Jacobs *et alii*, 2004). Assim, para o modo ZCS, pode-se deduzir (1) e (2).

Onde:

Iin*av, V*in*av* - Corrente e tensão média na entrada do conversor CC-CC.

I*pa*- Corrente nos terminais de saída do arranjo fotovoltaico.

Vdcav'- Tensão média na saída do conversor CC-CC, referida ao primário do transformador.

*Rloss* - Representante de todas as perdas no SRC3.

Apesar das muitas vantagens, o SRC3 possui uma deficiência que o torna inapto a realização do MPPT. Sua frequência de chaveamento e sua razão cíclica são variáveis fixas (Jacobs *et alii*, 2004). Por isso, concentrar todas as malhas de controle no estágio CC-CA é um dos grandes méritos deste trabalho. Esta técnica permite que tais deficiências sejam desprezadas.

**2.2 Estágio CC-CA**

Os arranjos fotovoltaicos têm um comportamento próximo ao de uma fonte de corrente. Por isso, a grande maioria dos conversores CC-CA conectados à rede são alimentados em tensão (Rashid, 2001), ou seja, possuem um barramento CC na entrada, conforme o apresentado na figura 11. A elevada tensão do barramento normalmente impõe o uso de IGBTs na composição da ponte de transistores.

A modulação vetorial, SVM, é empregada no disparo dos transistores a fim de minimizar a THD da corrente de linha. É utilizada a sequência simétrica para geração dos pulsos de gatilho. Com isso, só aparecem componentes harmônicas significativas a partir da frequência de chaveamento. O li-mite de 5% da THD estabelecido por normas internacionais é atendido com o filtro L de primeira ordem na conexão com a rede elétrica. A combinação da modulação vetorial com o uso do filtro L acarretou em maior compactação e menor custo, pois os indutores de linha foram construídos com núcleo de ferro-silício. O ferrite é mais caro e possui baixa densidade de fluxo magnético.

Da figura 11, verifica-se que a transformação de Park (controle vetorial) é usada na modelagem do conversor, de onde resulta a corrente de eixo direto, Id.

**3 ESTRATÉGIA DE CONTROLE**

A corrente de eixo direto *Id* representa a potência média injetada na rede elétrica, que é maximizada através do algoritmo P&O. Neste, a tensão do barramento CC, *V*dc, é perturbada enquanto a corrente *Id* é observada. A lógica de funcionamento do algoritmo P&O é descrita na tabela 3, cuja representação matemática está em (3).

Thumbnail

A grandeza Δ*V* corresponde a amplitude da perturbação aplicada em Vdc. Esta perturbação, bem como o período de sua aplicação, são adequadamente dimensionados a fim de evitar a instabilidade do controle (Femia *et alii*, 2005). A função *sign*, que aparece em (3), extrai apenas o sinal da conta feita em seu argumento.

O sistema da figura 11 possui mais de uma entrada de controle, o que levou ao abandono da teoria de controle clássico em favor da teoria de controle baseada no espaço de estados. Assim, foi desenvolvido o projeto de um servossistema com realimentação de estados e controle integral (Ogata, 2003). As variáveis de estado são geradas a partir de apenas dois sensores de corrente e um de tensão. Para o MPPT, nenhuma medição adicional é necessária.

Apresenta-se o modelo dinmico do conversor da figura 11 em (4) a fim de melhor evidenciar as variáveis de estado.

Onde:

*Id, Iq, Vdc* - variáveis de estado.

*Iq* - corrente de eixo em quadratura.

*Dd*, *Dq* - entradas de controle.

*Vg* - Tensão de fase eficaz da rede elétrica.

 frequência angular da rede elétrica.

L, R - indutncia e resistência intrínseca dos indutores de linha.

*C2* - capacitor do barramento CC.

*Idc* - corrente resultante da divisão entre a potência entregue ao barramento CC e sua tensão, *Vdc*.

**4 PROCEDIMENTO DE PROJETO**

A figura 12 apresenta a estrutura de potência do inversor de dois estágios modificado posicionado entre o arranjo fotovoltaico e a rede elétrica trifásica.

Embora se tenha concluído que a potência nominal de 15kW é a mais adequada para o contexto energético brasileiro, projeta-se um protótipo de 4kW em função da disponibilidade de módulos fotovoltaicos no labortatório. O arranjo fotovoltaico é composto por 20 módulos (duas fileiras) KC200GT da Kyocera, totalizando 4kWp. A unidade kWp representa a máxima potência que pode ser extraída do arranjo fotovoltaico, ou seja, a potência em STC (standard test conditions -radiação solar de 1kW/m2 , espectro de 1,5 de massa de ar e temperatura das células fotovoltaicas de 25ºC).

As especificações para o projeto do inversor são dadas a seguir:

Onde:

*Pin* - Potência nominal de entrada do estágio CC-CC.

*f2* - Frequência de chaveamento do estágio CC-CA.

Δ*Vin* - Ondulação de tensão nos terminais do arranjo fotovoltaico.

Estima-se a eficiência do SRC3 em η1 = 0,97 (Jacobs *et alii*, 2004). Daí, pode-se calcular a potência entregue ao barramento CC, bem como o valor de sua tensão, conforme (5) e (6). Vdc*av* é elevada a 816V pela relação de espiras do transformador.

O capacitor acoplado ao arranjo fotovoltaico é calculado por (7). Utilizou-se um capacitor de poliéster de 680nF.

De (8), obtém-se o valor do capacitor do barramento CC, *C*2. A ondulação sobre este capacitor, ΔV*C2* = 0,2V, corresponde a um percentual de Δ*V* . Adota-se *C*2 = 333µF. Este é o valor comercial resultante da associação série de três capacitores eletrolíticos de 1.000µF. Vale ressaltar que a tensão neste barramento pode se aproximar dos 1.000V.

Do transformador trifásico, construído a partir de três monofásicos, resultou uma dispersão *Ld* = 1,64µH. Assim, cada capacitor ressonante vale *Cr* = 9,9µF. Este valor, calculado em (1), é obtido pela associação paralela de três capacitores de filme de polipropileno de 3,3µF.

Os indutores de linha são calculados por (9), resultando em *L* = 9,3mH. A ondulação na corrente de linha vale Δ*I*L = 0,42A, correspondente a 5% da corrente de linha de pico.

**5 RESULTADOS TEÓRICOS**

As perdas no estágio CC-CC são calculadas em 0,32 isolando *Rloss* em (2). Substituindo *Rloss* e (6) em (2), pode-se traçar a característica de entrada do SRC3, mostrada na figura 13. Os parmetros que definem esta característica são a sua inclinação e sua posição. A inclinação depende das perdas. A posição, de *Vdc*. Esta tensão, por sua vez, é controlada pelo conversor CC-CA. Assim, o deslocamento na característica I-V de entrada do conversor CC-CC é realizado pelo conversor CC-CA.

A figura 14 mostra que os cruzamentos entre as curvas características do conversor CC-CC e a do arranjo fotovoltaico de 4kWp ocorrem praticamente sobre os pontos de máxima potência para vários níveis de radiação.

Se a temperatura variar, o conversor CC-CA, através do algoritmo P&O, reposiciona a característica I-V do SRC3 até extrair a máxima potência do arranjo fotovoltaico novamente. A corrente *Id* reflete a potência extraída do arranjo. Esta ação de controle é ilustrada na figura 15. A tensão *Vdc* é perturbada em 4V a cada 50ms. A figura 16 mostra o comportamento da potência de saída do arranjo fotovoltaico (*PMPPT*) mediante os ajustes na tensão Vdc, apresentados na figura 15. O erro de rastreamento relativo, ER, praticamente vai a zero em regime permanente. Isto ocorre devido a aproximação entre a característica I-V de entrada do SRC3 e o MPP do arranjo fotovoltaico.

**6 RESULTADOS EXPERIMENTAIS**

O conversor CC-CA trifásico PWM alimentado em tensão, adotado neste trabalho, é o conversor mais utilizado no mundo quando se trata de injetar a energia proveniente de um arranjo fotovoltaico na rede elétrica trifásica (Burger *et alii*, 2008). Dentre os trabalhos que utilizam este conversor com esta finalidade, alguns são nacionais (Schonardie e Martins, 2007; Cavalcanti *et alii*, 2006). Há estudos que apontam vantagens na sua substituição por outras estrutaras como o conversor CC-CA trifásico PWM alimentado em corrente (Sahan *et alii*, 2008) ou por inversores multiníveis (Selvaraj e Rahim, 2009). São empregadas as mais variadas técnicas de controle da corrente injetada na rede e de MPPT. O filtro LCL na interface com a rede pode tornar sua estrutura mais compacta (Blaabjerg *et alii*, 2004). Como se verifica, esta é uma vertente bastante produtiva para pesquisadores deste assunto. Porém, a aplicação do conversor CC-CC trifásico série ressonante num inversor de dois estágios é o foco e a principal contribuição deste trabalho. Por isso, esta seção é dedicada a apresentação de resultados experimentais referentes ao estágio CC-CC do inversor de dois estágios.

A figura 17 apresenta o protótipo de 4kW implementado em laboratório.

Foram usados os módulos SK20GD065 e SK10GD123 da Semikron. Cada módulo possui seis IGBTs de 600V e de 1200V, respectivamente. Dois circuitos de comando SKHI 61, também da Semikron, levam os pulsos de gatilho a esses transistores. A ponte retificadora foi implementada com seis diodos ultra rápidos FFPF05U120S de 1200V e 5A. A placa de condicionamento possui dois sensores de corrente LA 25-NP e um de tensão LV 25-P, todos da LEM, a fim de monitorar as variáveis de estado. Nela também é gerado o sinal de sincronismo, necessário ao controlador. O DSP TMS320F2812 responde pelo controle da corrente injetada na rede, pelo MPPT e pela proteção de falta de fase, que impede o inversor de continuar operando quando a rede elétrica é desenergizada. Simultaneamente, o DSP aciona o estágio CC-CC através de seis saídas PWM. São gerados pulsos de gatilho com 40kHz de frequência, razão cíclica de 50% e tempo morto de 640ns.

A figura 18 apresenta as correntes ressonantes em condições nominais de operação. Essas correntes fluem pelo transformador trifásico, constituído por três trasnformadores monofásicos artesanais. Obviamente, as indutncias de dispersão de cada fase não são exatamente iguais. Isso provoca pequenas diferenças nas amplitudes das correntes ressonantes, o que não prejudica a operação do SRC3 e não leva o risco de saturação ao transformador. Aliás, em condições normais de operação, as tensões contínuas que poderiam saturar o transformador são bloqueadas pelos capacitores ressonantes.

As figuras 19 e 20 apresentam as correntes de entrada e saída do SRC3, antes dos respectivos filtros. Essas correntes têm frequência seis vezes maior que a de chaveamento e baixa ondulação, resultando em um fluxo contínuo de potência. Essas não são características comuns entre os conversores CC-CC, principalmente entre os monofásicos. Dessas características é que resulta o valor atípico de 680nF para o capacitor de entrada, C1.

As figuras 20 e 21 favorecem a visualização das assimetrias provocadas na corrente Iin e na tensão Vin pelas diferenças nas indutncias de dispersão. O uso de transformadores comerciais certamente reduziria tais assimetrias.

A comutação ZCS é mostrada na figura 22. Em baixas potências essa comutação torna-se dissipativa, conforme figura 23. A eficiência, ilustrada na figura 24, ficou em torno de 97,5% em condições nominais. Assim, as perdas no SRC3 podem ser recalculadas através de (6) e (2), resultando em *Rloss* = 0,26.

Substituindo o novo valor de *Rloss* em (10), equação derivada de (2), obtém-se a inclinação da característica I-V de entrada do SRC3 para diferentes valores de tensão do barramento CC. A figura 25 confirma este resultado.

A característica de entrada do SRC3 favorece o MPPT. Isto se torna evidente quando a figura 25 (Vdc = 816V) é sobreposta as curvas características do arranjo fotovoltaico para uma dada temperatura, resultando na figura 26. Para cada valor de radiação solar, é estabelecido um ponto de cruzamento entre as características do arranjo e do conversor. Ocorre que a inclinação definida em (10) faz com que esses cruzamentos fiquem sempre muito próximos aos MPPs, dispensando a atuação do MPPT em caso de rápidas variações das condições atmosféricas. A temperatura varia lentamente.

A tensão nominal do barramento CC corresponde a 816V e seu valor mínimo de operação está em torno de 600V. O inversor necessita de tensões acima deste valor mínimo para poder injetar corrente na rede elétrica.

**7 CONCLUSÃO**

Neste trabalho foi proposta uma alteração conceitual na topologia do inversor de dois estágios empregado no processamento da energia solar fotovoltaica em sistemas conectados à rede elétrica. Tal alteração conceitual, que consiste em concentrar toda a estrutura de controle no estágio CC-CA, dá origem ao chamado Inversor de Dois Estágios Modificado. Nele, nenhuma ação de controle atua sobre o estágio CC-CC, ou seja, frequência e razão cíclica são constantes ao longo de toda a faixa de operação. Por isso, foi possível aplicar o conversor trifásico série ressonante na sua composição. Dentre as muitas vantagens oferecidas por este conversor, se destaca a ondulação máxima de apenas 1% na tensão de saída do arranjo fotovoltaico, obtida com um capacitor de poliéster de apenas 680nF, cujo custo é inexpressivo. Comercialmente, fabricantes adotam ondulações de 2% em potências superiores a 100kW e até 10% para potências abaixo de 10kW. Esses valores normalmente são atingidos por meio de bancos capacitivos que chegam a alguns mili farads.

O baixo número de sensores requeridos pelo Inversor de Dois Estágios Modificado é reduzido ainda mais pela forma inovadora como o algoritmo P&O é executado, perturbando a tensão no barramento CC e observando a variação da corrente de eixo direto. Essas variáveis foram geradas como parte do controle da corrente injetada na rede elétrica. Isto significa que nenhuma medição específica para o MPPT foi feita.

Os algoritmos de MPPT tendem a ficar mais lentos a medida que se tornam mais precisos. Rápidas mudanças nas condições atmosféricas ocorrem com frequência. Portanto, variações bruscas na radiação solar normalmente causam perdas importantes. Neste inversor, a característica de entrada do conversor trifásico série ressonante compensa quase que integralmente os deslocamentos do MPP. O tempo de atuação é limitado pelo tempo de resposta do conversor CC-CC, que é muito mais rápido que a malha de MPPT.

**AGRADECIMENTOS**

Os autores agradecem à FINEP e ao CNPq pelo suporte financeiro destinado ao desenvolvimento desta pesquisa.

Artigo submetido em 29/10/2008 (Id.: 00914)

Revisado em 19/03/2009, 05/08/2009

Aceito sob recomendação do Editor Associado Prof. Darizon Alves de Andrade

## Referências bibliográficas

* Agência Nacional de Energia Elétrica (2005). Atlas de Energia Elétrica do Brasil, 2. ed., Brasília
* Alter Systems: Alternative energy products and services. Berkeley, CA. Disponível em: . Acesso em: 16 ago. 2008.
* Bhat, A.K.S. and L. Zheng (1996). Analysis and Design of a Three-Phase LCC Type Resonant Converter. *IEEE Power Electronics Specialists Conference*, Baveno, pp. 252-258.
* Blaabjerg, F., R. Teodorescu, Z. Chen and M. Lissere (2004). Power Converters and Control of Renewable Energy System. *Proc. of ICPE'04*, pp. I2-I20.
* Burger, A.K. Next Generation Dye Sensitive & Organic PV, Part 1. RenewableEnergyWorld.com, Cadiz, Spain, 24 jul. 2008. Disponível em: . Acesso em: 16 ago. 2008.
* Burger, B., B. Goeldi, D. Kranzer and H. Schmidt (2008). 98.8% Inverter Efficiency with SIC Transistor. *23rd European Photovoltaic Solar Energy Conference*, Valencia, pp. 2688-2692.
* Carletti, R.L., L.C.G. Lopes and P.G. Barbosa (2005). Active & Reactive Powers Control Scheme for a Grid-Connected Photovoltaic Generation System Based on VSI with Selective Harmonic Elimination. *Brazilian Power Electronics Conference*, Recife, pp. 129-134.
* Carrasco, J.M., L.G. Franquelo, J.T. Bialaziewicz, E. Galván, R.C.P. Guisado, M.A.M. Prats, J.I. León and N.M. Alfonso (2006). Power-Electronic Systems for the Grid Integration of Renewable Energy Sources: A Survey. *IEEE Transactions on Industrial Electronics*, v. 53, n. 4, pp. 1002-1016.
* Cavalcanti, M.C., G.M.S. Azevedo, B.A. Amaral, F.A.S. Neves, D.C. Moreira and K.C. Oliveira (2006). A Grid Connected Photovoltaic Generation System with Compensation of Current Harmonics and Voltage Sags. *Eletrônica de Potência*, v. 11, n. 2, pp. 93-101.
* Celesc: Centrais Elétricas de Santa Catarina. Perfil. Disponível em: . Acesso em 16 ago. 2008.
* Célula solar bate recorde de eficiência e pode viabilizar energia solar. Redação do Site Inovação Tecnológica. Campinas, SP, 26 jul. 2007. Disponível em: . Acesso em: 16 ago. 2008.
* Consumo bate recorde e é o maior da década. InvestNews - Tempo Real (Brasil), São Paulo, 23 nov. 2007. Energia. Disponível em: . Acesso em: 16 ago. 2008.
* Doncker, R.W.A.A. de, D.M. Divan and M.H.A. Kheraluwala (1991). Three-Phase Soft-Switched HighPower-Density dc/dc Converter for High-Power Applications. *IEEE Transactions on Industry Applications*, v. 27, n. 1, pp. 63-73.
* Femia, N., G. Petrone, G. Spagnuolo and M. Vitelli (2005). Optimization of Perturb and Observe Maximum Power Point Tracking Method. *IEEE Transactions on Power Electronics*, v. 20, n. 4, pp. 963-973.
* Hua, C., J. Lin and C. Shen (1998). Implementation of a DSP-Controlled Photovoltaic System with Peak Power Tracking. *IEEE Transactions on Industrial Electronics*, v. 45, n. 1, pp. 99-107.
* Jacobs, J., A. Averberg and R. de Doncker (2004). A Novel Three-Phase DC/DC Converter for High-Power Applications. *IEEE Power Electronics Specialists Conference*, Aachen, pp. 1861-1867.
* Jing, L., D. Wei, X. Zheng-guo, P. Yan-chang and X. Honghua (2005). Evaluation on MPPT Methods of Photovoltaic Power Systems. *International Photovoltaic Science & Engineering Conference*, Shanghai, pp. 925-926.
* O Racionamento bate à porta. O Estado de S.Paulo, São Paulo, 01 nov. 2007. Disponível em: . Acesso em: 16 ago. 2008.
* Oliveira Júnior, D.S. and I. Barbi (2005). A Three-Phase ZVS PWM DC/DC Converter with Asymmetrical Duty Cycle Associated with a Three-Phase Version of the Hybridge Rectifier. *IEEE Transactions on Power Electronics*, v. 20, n. 2, pp. 354-360.
* Ogata, K. (2003). *Engenharia de Controle Moderno*, 4.ed. Prentice Hall, São Paulo.
* Prasad, A.R., P.D. Ziogas and S. Manias (1991). A Three-Phase Resonant PWM DC-DC Converter. *IEEE Power Electronics Specialists Conference*, Cambridge, pp. 463-473.
* Rashid, M.H. (2001). *Power Electronics Handbook* Academic Press, San Diego.
* Sahan, B., A.N. Vergara, N. Henze, A. Engler and P. Zacharias (2008). A Single-Stage PV Module Integrated Converter Based on a Low-Power Current-Source Inverter. *IEEE Transactions on Industrial Electronics*, v. 55, n.7, pp. 2602-2609.
* Schonardie, M.F. and D.C. Martins (2007). Grid-Connected Photovoltaic Three-Phase System Using Park Transformation with Active and Reactive Power Control and Input Voltage Clamped. 9ş *Congresso Brasileiro de Eletrônica de Potência*, Blumenau, pp. 485-489.
* Selvaraj, J. and N.A. Rahim (2009). Multilevel Inverter For Grid-Connected PV System Employing Digital PI Controller. *IEEE Transactions on Industrial Electronics*, v. 56, n. 1, pp. 149-158.
* Ziogas, P.D., A.R. Prasad and S. Manias (1988). Analysis and Design of a Three-Phase Off-Line DC/DC Converter with High Frequency Isolation. *IEEE Industry Applications Conference*, pp. 813-820.

## Datas de Publicação

* **Publicação nesta coleção**  
  26 Abr 2010
* **Data do Fascículo**  
  Abr 2010

## Histórico

* **Revisado**  
  19 Mar 2009
* **Recebido**  
  29 Out 2008

[This work is licensed under a Creative Commons Attribution-NonCommercial 4.0 International License.](http://creativecommons.org/licenses/by-nc/4.0/)

##### Autoria

person Marcio Mendes Casaro

schoolUniversidade Tecnológica Federal do Paraná, Ponta Grossa, Paraná, BrazilUniversidade Tecnológica Federal do ParanáBrazilPonta Grossa, Paraná, BrazilUniversidade Tecnológica Federal do Paraná, Ponta Grossa, Paraná, Brazil

person Denizar Cruz Martins

schoolUniversidade Tecnológica Federal do Paraná, INEP , Florianópolis, Santa CatarinaUniversidade Tecnológica Federal do ParanáFlorianópolis, Santa CatarinaUniversidade Tecnológica Federal do Paraná, INEP , Florianópolis, Santa Catarina

##### SCIMAGO INSTITUTIONS RANKINGS

Universidade Tecnológica Federal do Paraná, Ponta Grossa, Paraná, BrazilUniversidade Tecnológica Federal do ParanáBrazilPonta Grossa, Paraná, BrazilUniversidade Tecnológica Federal do Paraná, Ponta Grossa, Paraná, Brazil

Universidade Tecnológica Federal do Paraná, INEP , Florianópolis, Santa CatarinaUniversidade Tecnológica Federal do ParanáFlorianópolis, Santa CatarinaUniversidade Tecnológica Federal do Paraná, INEP , Florianópolis, Santa Catarina

##### Figuras | Tabelas | Fórmulas

* [Figuras (23)](#figures)
* [Tabelas (3)](#tables)
* [Fórmulas (2)](#schemes)

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

Thumbnail

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/57d1ef6d17d0f1588a5791fc1d78c4dde411fd6a.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/311f24663b9d141681078813139f48564ca741fa.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/12ddd3d986cb43c98b9e51f7919012060b06512f.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/abee9d6c8d00986c73bf16b334de01c751c94c44.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/533e0950ccb51c219c4451d5f63401519de718c7.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/49b05bba5a23b968b879a180312b97ae8515b742.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/634bae17ee89f2c315b44d80e2c685a836106b17.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/ce90e5463e8e7dadeb8451fc4e8ae44f3211013e.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/a490262caaa64e489be47c075eac47026f1b2a87.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/ccadd270e18988b7a0fff502c2dbbef06bd498f2.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/807827cdf64d60600ec1f6d779e345e9bb45bb3f.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/678beebbfa1cbe777c71027dcf7328dab0e82d2b.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/5d2a95a29ea849a87655a5faca775489c0625b23.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/30f4ed5060c075c66157f924cb890e24a2116726.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/627dd09f662309bbb4be247c446e61832c951afa.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/6b22a902ffbafe03376fa9e8840c1bd318ba7ecc.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/c2e460373ea7f980901db6f7335fae1539851bae.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/0d3d0a3c2a35b97a54401498f764e3935321d9b6.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/31d566b0ee6844f38349d1fd14dd3ec25c4b657d.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/3c2eba87bf6827c89cf8242eeeef830661f2a98f.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/0247ac76dd33415ce0b076cd91633e761e827323.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/957728c797a87bf8442bbcc22977e9f0664a9c0f.gif "Abrir em nova janela")

##### image[open\_in\_new](https://minio.scielo.br/documentstore/0103-1759/LzxvkKP5YDqBzxtWx9js75q/2fe24cf8d0ae7cdda72457769a4c99d3fcb177e8.gif "Abrir em nova janela")

##### table\_chart

##### table\_chart

##### table\_chart

##### Como citar

Casaro, Marcio Mendes e Martins, Denizar Cruz. Processamento eletrônico da energia solar fotovoltaica em sistemas conectados à rede elétrica. Sba: Controle & Automação Sociedade Brasileira de Automatica [online]. 2010, v. 21, n. 2 [Acessado 4 Junho 2026], pp. 159-172. Disponível em: . Epub 26 Abr 2010. ISSN 0103-1759. https://doi.org/10.1590/S0103-17592010000200005.

linkcopiar

## Ferramentas do artigo

* [file\_download PDFs](#)
* [show\_chart Métricas](#)
* [image Figuras e tabelas](#)
* [translate Versões e traduções](#)
* [link Como citar este artigo](#)
* [article Artigos relacionados](#)

location\_on

**Sociedade Brasileira de Automática** Secretaria da SBA, FEEC - Unicamp, BLOCO B - LE51, Av. Albert Einstein, 400, Cidade Universitária Zeferino Vaz, Distrito de Barão Geraldo, 13083-852 - Campinas - SP - Brasil, Tel.: (55 19) 3521 3824, Fax: (55 19) 3521 3866 - Campinas - SP - Brazil   
 **E-mail:** revista\_sba@fee.unicamp.br

[rss\_feed](/journal/ca/feed/ "RSS do número mais recente do periódico")  Acompanhe os números deste periódico no seu leitor de RSS

## Versão para download de PDF

### PDF

* [Português](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/?lang=pt&format=pdf)

## Artigos relacionados

Lista de links para artigos relacionados. Os links abrem em nova aba.

* [Google  (abre em nova aba)](https://www.google.com/search?q=)
* [Google Scholar  (abre em nova aba)](https://scholar.google.com/scholar?q=)

## Versões e tradução automática

Escolha a versão original do texto ou utilize um serviço de tradução automática.

### Versão original do texto

* [Português](/j/ca/a/LzxvkKP5YDqBzxtWx9js75q/?lang=pt)

### Tradução automática

* [Google Translator  (abre serviço externo de tradução)](#)
* [Microsoft Translator  (abre serviço externo de tradução)](#)

## Como citar

Escolha um formato para exportar ou selecione um estilo de citação. O conteúdo abaixo pode ser atualizado após a seleção.

[Baixar em RIS](/citation/export/LzxvkKP5YDqBzxtWx9js75q/?format=ris)

[Baixar em BIBTEX](/citation/export/LzxvkKP5YDqBzxtWx9js75q/?format=bib)

  [vertical\_align\_top  Ir para o topo](#top) 

[SciELO Analytics](http://analytics.scielo.org/w/accesses?document=S0103-17592010000200005&collection=scl)

[Processamento eletrônico da energia solar fotovoltaica em sistemas conectados à rede elétrica](https://plu.mx/scielo/a/?doi=10.1590/S0103-17592010000200005)

## Mensagem

## Mensagem

[Reportar erro](#)

Este site usa cookies para garantir que você obtenha uma melhor experiência de navegação. Leia nossa Política de Privacidade.OK
