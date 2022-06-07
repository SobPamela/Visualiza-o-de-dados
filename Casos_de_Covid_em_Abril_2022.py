# importando bibliotecas
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# carregar dados para analise.
URL = 'https://raw.githubusercontent.com/SobPamela/visualizacao_dados/fa5d67ddc7eba21894c048509ae3b82b35c26488/HIST_PAINEL_COVIDBR_2022_Parte1_06jun2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

# definir campo 'casosAcumulado' como inteiro
df['casosAcumulado'] = df['casosAcumulado'].astype(int)

# criar novos campos para facilitar a consulta e construção da representação gráfica
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

# filtrando e agrupando por região e mês
sudeste_mes_4 = df.query('regiao == "Sudeste" and ano == 2022 and mes == 4').groupby(['estado',
                                                                                      'mes'])[
    'casosNovos', 'obitosNovos'].sum().reset_index()

# colocando Nan por 0 para facilitar a analise das informações
sudeste_mes_4 = sudeste_mes_4.replace(np.nan, 0)
sudeste_mes_4

# criação gráfico
titulo = 'Numero de casos e obitos do Sudeste do Brasil no mês de Abril de 2022'
fig2 = go.Figure()
fig2.add_trace(go.Bar(x=sudeste_mes_4['estado'], y=sudeste_mes_4['casosNovos'],
                      text=sudeste_mes_4['casosNovos'], name='CASOS'))
fig2.add_trace(go.Bar(x=sudeste_mes_4['estado'], y=sudeste_mes_4['obitosNovos'],

                      text=sudeste_mes_4['obitosNovos'], name='OBITOS'))

fig2.update_layout(title_text=titulo, xaxis_title='Estados',
                   yaxis_title=' ',
                   template='plotly_white')

fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',
                  showline=True, linewidth=1, linecolor='black')
fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray',
                  showline=True, linewidth=1, linecolor='black')

fig2.show()
