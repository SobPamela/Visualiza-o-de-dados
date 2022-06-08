# importando bibliotecas
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# carregar dados para analise.
URL = 'https://raw.githubusercontent.com/SobPamela/visualizacao_dados/fa5d67ddc7eba21894c048509ae3b82b35c26488/HIST_PAINEL_COVIDBR_2022_Parte1_06jun2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

# definir campo 'casosAcumulado' como inteiro
df['casosAcumulado'] = df['casosAcumulado'].astype(int)

# criar novos campos de mês e ano para filtrar as informações
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month


sudeste = df.query('regiao == "Sudeste" and ano == 2022')

#substuindo Nan por 0
sudeste = sudeste.replace(np.nan, 0)

#agupar valores de casos por estado e mês.
dt_agrupado_sudeste = sudeste.groupby(['estado','mes'])['casosNovos', 'obitosNovos'].sum().reset_index()

# filtrando e agrupando por região e mês
itens_estados = dt_agrupado_sudeste['estado'].unique()


# Plot series
for estado in itens_estados:
  set_estado = dt_agrupado_sudeste.loc[dt_agrupado_sudeste['estado']== estado]
  plt.plot(set_estado['mes'], set_estado['casosNovos'], label= estado,
          linewidth=2, marker="o",  linestyle="-")


plt.title('NÚMERO DE CASOS DE COVID NOS ESTADOS DO SUDESTE EM 2022')
plt.xlabel('MESES')

plt.ylabel('N° DE CASOS')
plt.legend()
plt.tight_layout()
plt.show()