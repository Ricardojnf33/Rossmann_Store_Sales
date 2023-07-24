# Projeto de Previsão de Vendas - Rede de Farmácias Rossmann
## _Rossmann Sales Predict Project_

___

Este repositório contém código e análises para um projeto de previsão de vendas das lojas Rossmann. O objetivo é prever com precisão as vendas de cada loja ao longo de um período de 6 semanas, auxiliando no planejamento orçamentário e na alocação de recursos.

## Problema de Negócio
A Rossmann opera mais de 4.000 drogarias em 8 países europeus, com cerca de 56.000 funcionários. A empresa disponibilizou seus dados de vendas por meio da plataforma de competições Kaggle. Os dados contêm 1.017.209 registros de vendas feitas pelas subsidiárias da empresa, com 18 características únicas para cada venda.

O departamento financeiro precisa de previsões precisas de vendas para cada loja nas próximas 6 semanas. Atualmente, cada gerente de loja fornece suas próprias previsões manualmente, resultando em resultados inconsistentes. Uma solução automatizada e confiável é necessária para ajudar o CFO a tomar decisões mais informadas para o planejamento orçamentário e alocar recursos para melhorias nas lojas.

## Dados
Os dados utilizados no projeto estão disponíveis na competição Kaggle Rossmann Store Sales. Eles contêm os seguintes atributos:

___

| Atributo     | Descrição |
| ----------- | ----------- |
| Store      | Identificador único de cada loja (Id)      |
| Date   | Data em que ocorreu o evento de venda        |
| DayOfWeek      | Variável numérica que representa o dia da semana que ocorreu o evento de venda       |
| Sales   | Valor de Vendas do dia        |
| Customers      | Quantidade de clientes na loja no dia       |
| StateHoliday   | Indica se o dia em análise é feriado. a = Feriado público, b = Feriado de páscoa, c = Natal, 0 = Não há feriado       |
| SchoolHoliday      | Indica se a loja foi ou não fechada durante o feriado escolar.       |
| StoreType   | Indica o modelo de lojas. Pode variar entre as váriaveis categóricas a, b, c, d        |
| Assortment      | Indica o nível de variedade de produtos: a = básico, b = extra, c = estendido       |
| CompetitionDistance   | Distância (em metros) para o competidor mais próximo        |
| CompetitionOpenSince [Month/Year]      | Indica o ano e mês em que o competidor mais próximo abriu       |
| Promo  |Indica se a loja está com alguma promoção ativa no dia     |
| Promo2     | Indica se a loja deu continuidade na promoção: 0 = loja não está participando, 1 = loja participando       |
| Promo2Since [Year/Week]   | Descreve o ano e semana de quando a loja começa a a promoção extendida        |
| PromoInterval      | Descreve os meses em que a loja iniciou a promo2, ex.: "Feb,May,Aug,Nov" significa que a loja iniciou as promoções estendidas em cada um desses meses     |

## Abordagem

O processo CRISP-DM foi utilizado para entregar uma solução inicial rapidamente, que fornece valor ao negócio. As etapas incluem:

- Definição do problema de negócio
- Compreensão do negócio
- Coleta de dados
- Limpeza dos dados
- Exploração dos dados e geração de hipóteses
- Preparação dos dados para modelagem
- Aplicação de algoritmos de aprendizado de máquina
- Avaliação do modelo
- Implantação do modelo

##### Em cada ciclo completo, o modelo é refinado e reavaliado para melhorar o desempenho do negócio.

## Insights

Testes de hipóteses revelaram que as lojas não vendem mais quando abertas nos feriados de Natal em comparação com outros feriados. Esse insight ajuda a guiar a estratégia de marketing.
As lojas tendem a vender mais após o décimo dia de cada mês. A equipe de marketing pode utilizar esse insight para o planejamento de promoções.
Verificou-se que as lojas vendem menos na segunda metade do ano, contrariando as crenças iniciais. Isso sugere que podem ser necessárias mudanças para impulsionar o desempenho na segunda metade do ano.

## Modelagem

Vários modelos de regressão foram testados:

- Modelo Médio
- Regressão Linear
- Regressão LASSO
- Random Forest Regressor
- XGBoost Regressor

___

# Performance Real com Cross Validation: 


|        Model Name       | 	  MAE CV	        |    MAPE CV	    |       RMSE CV      |
| ----------------------- | ------------------- | --------------- | ------------------ |
|    Linear Regression    |	2081.73 +/- 295.63	|  0.3 +/- 0.02	  | 2952.52 +/- 468.37 |
|	         Lasso     	    | 2116.38 +/- 341.5   |  0.29  +/- 0.01	| 3057.75 +/- 504.26 |
|	Random Forest Regressor	| 837.47 +/- 218.61	  |  0.12 +/- 0.02	| 1257.22 +/- 319.82 |
|	   XGBoost Regressor   	| 928.15 +/- 129.72   |	 0.13 +/- 0.01	| 1322.73 +/- 176.6  |

O modelo XGBoost foi selecionado, pois apresentou a melhor combinação de desempenho e nível de performance. A sintonização dos hiperparâmetros melhorou ainda mais a precisão.

#### Resultado Modelo Final:

|     Model Name    |   	MAE    |   	MAPE    |	    RMSE    |
| ----------------- | ---------- | ---------- | ----------- |
| XGBoost Regressor |	775.156519 |	0.114113	| 1132.319847 |

## Resultados

O modelo retorna previsões de vendas para uma loja solicitada. Isso é fornecido por meio de um bot do Telegram para fácil acesso pela equipe financeira.

Para as 5 melhores lojas em termos de desempenho, a precisão MAPE variou de 0,0635 a 0,0684. As 5 piores lojas mostraram oportunidades de melhoria, com MAPE variando de 0,7664 a 0,9116.

Vendas totais previstas para todas as lojas:

___
## Tradução e Interpretação do erro na performance de negócio: 

|	store	|  predictions   |	worst_scenario |	best_scenario |	   MAE      |	  MAPE   |
| ----- | -------------- | --------------- | -------------- | ----------  | -------- |
|  292 	|  111192.921875 | 107684.256219   |	114701.587531 |	3508.665656 |	0.640044 |
|  909  |  221007.890625 | 213136.024584	 |  228879.756666	| 7871.866041	| 0.517736 |
|  286  |  177835.609375 | 176716.998350	 |  178954.220400	| 1118.611025	| 0.398606 |
|  425  |  157305.312500 | 156217.601444	 |  158393.023556	| 1087.711056	| 0.378163 |
|  902  |  199823.593750 | 198420.469542	 |  201226.717958	| 1403.124208	| 0.352660 |

## Performance de todas as lojas juntas:

|    Cenário      |    Valores      |
| --------------- | --------------- |
|    Previsão     | $282,423,488.00 |
|   Pior cenário  | $281,556,067.09 |
|  Melhor cenário | $283,290,932.74 |

## Próximos Passos

Ciclos futuros se concentrarão em:

1. **Identificar as causas do baixo desempenho de algumas lojas
2. **Testar novos algoritmos
3. **Criar um aplicativo web para acesso dos gerentes de loja
4. **Implementar testes unitários
5. **Criar novas features
6. **Melhorar o desempenho do modelo por meio de técnicas de programação

## Ferramentas Utilizadas

##### Python, Pandas, Matplotlib, Seaborn, Scikit-Learn
##### Jupyter Notebook, Flask, Telegram API
##### Heroku, Render, GitHub
##### Análise Exploratória de Dados
##### Técnicas estatísticas como testes de hipóteses, validação cruzada
##### Algoritmos de aprendizado de máquina, incluindo regressão linear, LASSO, Random Forest e XGBoost
##### Métricas de desempenho como MAE, MAPE e RMSE

# Trabalho de Conslusão de Curso da Pós-Graduação em Engenharia e Análise de Dados
link PDF : https://drive.google.com/drive/folders/1GZyiIwfy7Z1fZd1yLSyHEPfxgEytPtNR?usp=sharing
