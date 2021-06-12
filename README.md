![](https://img.shields.io/github/last-commit/HenriqueCCdA/bootCampAluraDataScience?style=plasti&ccolor=blue)
![](https://img.shields.io/badge/Autor-Henrique%20C%20C%20de%20Andrade-blue)

![](https://play-lh.googleusercontent.com/E5OY3A9Nf-XieZN5Ah6KfPIDbFpLR_j5fFOLbl-aYDrRiFAvensqRJjZpWFRA_yyNg)

# Estudo da Cobertura Vacinal (Data Science Aplicada 2: Projeto 2)

---
# 1) Introdução 

Neste notebook será estudo a **Cobertura Vacinal** desde de **1995** a **2018** da vacina **BCG** no Brasil. A vacina BCG previne contra as formas graves da tuberculose, como a meningite tuberculosa e a tuberculose miliar [[1]](http://blog.saude.mg.gov.br/2019/07/02/bcg-tire-suas-duvidas-sobre-essa-vacina/). Os dados foram retirados do [DATASUS-Tabnet [2]](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def) por região.

A métrica utilizada para avaliar a vacinação no Brasil é a **Cobertura Vacinal**. A fórmula de **Cálculo da Cobertura** é o **número de doses** aplicadas da dose indicada (1ª, 2ª, 3ª dose ou dose única, conforme a vacina) dividida pela **população alvo**, **multiplicado por 100** [[3]](http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf). A **Cobertura Vacinal** tenta ser um indicativo da porcentacem para população alvo vacina.

Os dados de 2019 e 2020 ainda não foram consolidas na base de dados, por isso não estão presentes na análise.

## 1.1) Motivação

O Brasil sempre foi conhecio pela sua excelente cobertura de vacinas possibilita pelo maior sistema de saúde público do mundo. Porém nos ultimos anos e comum ver notícias na impressa que o índices de vacinação no Brasil vem caindo nos últimos anos. Neste trabalho tentaremos ver algum indícios disso nos dados do **DATASUS**. 

## 1.2) Objetivos

* Verificar se realmente a indícios da queda da *Cobertura Vacinal** nos últimos anos
* Verificar a distribuição de vacinação por região

## 1.3) Metodologia

Analisar os dados de **Cobertura Vacinal** na regiões Sudeste, Sul, Norte, Nordeste e Centro-Oeste no período de **1995** a **2018**.

---
# 2) Analise
---

![GrafLinha](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/e8edd7e043e1b13146d1045bbd2cb4395086fa4d/Fig/Geradas/BCG_linha.png)

> A figura acima mostra a **Cobertura Vacinal** por região no periodo de **1995 a 2018**. A primeira coisa que chama atenção é que muitos valores estão **acima de 100%** (curva tracejada preta horizontal) o que indica que os valores de **Cobertura Vacinal** devem estar superestimados. Isto provavelemente é uma limitação da metodologia utilizada. Uma fonte da incuracia pode ser as estimativa da população alvo utitilizada para o cálculo **Cobertura Vacinal**. Porém o ponto mais importante é a **queda** da **Cobertura Vacional** a partir de **2016** (curva tracejada vermelha vertical). A queda aconteceu em todas as regiões, isso indica que é uma problema do sistema de saúde de uma forma geral.

![GrafBar](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Fig/Geradas/BCG_bar.png)

> O gráfico mostra a **Cobertura Vacional** por **região** nos anos de **2000**, **2010**, **2015** e **2018**. Aqui vemos melhor ainda como os resultados de **2018** estão bem abaixo dos anos anteriores.


---
# 3) Conclusões
---

A distribuição entre os estado da cobertura vacinal de **BCG** é bem uniforme não parecendo haver diferença sistemática entre os estados. 

A partir de **2016** o porcentatual de vacinação aparenta **cair** em todas as regiões. Isso pode indicar que um fenômeno generalizado do sistema de saúde brasileiro. O que corrobora a informações apresentado na imprenssa sobre a queda da **Cobertura Vacinal** nos últimos anos.

Nesse estudo só foi analisada a cobertura da vacina **BCG** em estudos futuros pode-se verificar os outros imunizantes.

---
# 4) Referências
---

[1]        http://blog.saude.mg.gov.br/2019/07/02/bcg-tire-suas-duvidas-sobre-essa-vacina/

[2] DATA_SUS - Tabnet http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def

[3] http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf

---
# Estrututa do Repositório
---

Os dados estão dividos em duas pastas: 

> * [Dados brutos](https://github.com/HenriqueCCdA/BC_DS_Projeto2/tree/main/Dados/Bruto) - Estes dados foram retirados diretamente do [DATASUS](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def) sem nenhum tratamento.

> * [Dados tratados](https://github.com/HenriqueCCdA/BC_DS_Projeto2/tree/main/Dados/Tratados) - Os dados aqui são os dados brutos tratados e prontos para usar no notebook de análise.


Os notebooks foram dividos em dois tipo: os exploratorios e de explanatorios.

No notebook explanatório é onde a análise é feita. O notebook é:

> * [analise_bcg_cobertura_vacinal.ipynb](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Notebooks/Explanatorios/analise_bcg_cobertura_vacinal.ipynb) -  Neste notebook é feito a analise da **Cobertura Vacinal** da **BCG**. 


Os notebooks explaratorios tem tem como o objetivo ser um primeiro contanto e a seleção dos dados que serão utilizados. Os notebooks exploratorios são:

> * [exploracao_BCG.ipynb](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Notebooks/Exploratorios/exploracao_BCG.ipynb) - Neste notebook é feito um primeiro contato com os dados da **Cobertura Vacinal** do **DataSUS** 

> * [limpando_os_dados.ipynb](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Notebooks/Exploratorios/limpando_os_dados.ipynb) - Neste notebook é feito uma limpeza e seleção de dados que serão utilizados. E gerado o arquivo [bcg.csv](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Dados/Tratados/bcg.csv)


[<img src="https://img.shields.io/badge/mail-EA4335?style=flat-square&logo=Gmail&logoColor=white" />](henrique.ccda@gmail.com)
