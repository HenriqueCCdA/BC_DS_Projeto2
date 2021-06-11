# Estudo da Cobertura Vacinal (Bootcamp: Data Science Aplicada 2: Projeto 2)

---
## Estrututa do Repositorio

Os dados estão dividos em duas pastas: 

* [Dados brutos](https://github.com/HenriqueCCdA/BC_DS_Projeto2/tree/main/Dados/Bruto) - Estes dados foram retirados diretamente do [DATASUS](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def) sem nenhuma tratamento.

* [Dados tratados](BC_DS_Projeto2/Dados/Tratados/) - Os dados aqui são os dados brutos tratados e prontos para usar no notebook de analise.


Os notebooks foram dividos em dois tipo: os exploratorios e de explanatorios.

Os notebooks explaratorios tem tem como o objetivo ser um primeiro contanto e a seleção dos dados que serão utilizados. Os notebooks exploratorios são:

* [exploracao_BCG.ipynb](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Notebooks/Exploratorios/exploracao_BCG.ipynb) - Neste notebook é feito um primeiro contato com os dados da **Cobertura Vacinal** do **DataSUS** 

* [limpando_os_dados.ipynb](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Notebooks/Exploratorios/limpando_os_dados.ipynb) - Neste notebook é uma limpeza e seleção de dados que serão utilizados. E gerado o arquivo [bcg.csv](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Dados/Tratados/bcg.csv)

Os notebooks explanatorio são onde a analise propriamente é feita. O notebook é:

* [analise_bcg_cobertura_vacinal](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Notebooks/Explanatorios/analise_bcg_cobertura_vacinal.ipynb) -  Neste notebook é feito a analise da **Cobertura Vacinal** da **BCG**. 



---
# Estudo

---
# 1) Introdução

Neste notebook será estuda a cobertura vacinal desde de **1995** a **2018** no pais da Vacina **BCG**. Vacina BCG previne contra as formas graves da tuberculose, como a meningite tuberculosa e a tuberculose miliar [[1]](http://blog.saude.mg.gov.br/2019/07/02/bcg-tire-suas-duvidas-sobre-essa-vacina/). Os dados foram retirados do [DATASUS-Tabnet [2]](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def) por região do Brasil.

A metrica utilizada para avaliar a vacinação no Brasil é a **Cobertura Vacinal**. Este número é calculado pela A fórmula de **cálculo da cobertura** é o **número de doses** aplicadas da dose indicada (1ª, 2ª, 3ª dose ou dose única, conforme a vacina) dividida pela **população alvo**, **multiplicado por 100** [[3]](http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf). A **Cobertura Vacinal** tenta ser um indicativo da porcentacem para população alvo vacina.

Os dados de 2019 e 2020 ainda não forram consolidade na base de dados, por isso não estão presentes na análise.

## 1.1) Motivação

O Brasil sempre foi conhecio pela sua excelente cobertura de vacinas passibilitade pelo maior sistema de saúde público do mundo. Porém nos ultimos anos e comum ver noticias na impressa que o indices de vacinação no Brasil vem caindo nos ultimos anos. Neste trabalho tentaremos ver algum indicios disso no dados

## 1.2) Objetivos

* Verifica se realmente a indicios da queda da cobertura vacinal nos ultimos anos
* Analisar verificar a ditribuição de vacinação por região

## 1.3) Metodologia

Analisar os dados de **cobertura vacinal** na regiões Sudeste, Sul, Norte, Nordeste e Centro-Oeste no perido de **1995** a **2018**.

---

# 2) Analise

![GrafLinha](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/e8edd7e043e1b13146d1045bbd2cb4395086fa4d/Fig/Geradas/BCG_linha.png)

![GrafBar](https://github.com/HenriqueCCdA/BC_DS_Projeto2/blob/main/Fig/Geradas/BCG_bar.png)

---
# 3) Conclusões
---

A ditribuição entre os estado da cobertura vacinal de **BCG** para ser bem uniforme não parecendo haver diferença sistematica. 

Apartir de **2016** o porcentatual de vacinação parenta **cair** em todos os Estados. Isso pode indicar que um fenomeno generalizado do sistema de saúde do Brasil. O que corrobora a informações apresentado na imprenssa.

Nesse estudo só voi analisada a cobertura da vacina **BCG**

---
# 6) Referências
---

[1]        http://blog.saude.mg.gov.br/2019/07/02/bcg-tire-suas-duvidas-sobre-essa-vacina/

[2] DATA_SUS - Tabnet http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def

[3] http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf