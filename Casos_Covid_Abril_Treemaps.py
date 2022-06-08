#importando bibliotecas
import matplotlib.pyplot as plt
import pandas as pd
import squarify
import numpy as np

# carregar dados para analise.
URL = 'https://raw.githubusercontent.com/SobPamela/visualizacao_dados/fa5d67ddc7eba21894c048509ae3b82b35c26488/HIST_PAINEL_COVIDBR_2022_Parte1_06jun2022.csv'
df = pd.read_csv(URL, sep=';', parse_dates=['data'])

#definir campo 'casosAcumulado' como inteiro
df['casosAcumulado'] = df['casosAcumulado'].astype(int)

# criar novos campos para facilitar filtro dos dados
df['ano'] = df['data'].dt.year
df['mes'] = df['data'].dt.month

#agupar valores de casos por estado e mês.
sudeste_mes_4 = df.query('regiao == "Sudeste" and ano == 2022 and mes == 4').groupby(['estado',
                                    'mes'])['casosNovos', 'obitosNovos'].sum().reset_index()

#substuindo Nan por 0
sudeste_mes_4 = sudeste_mes_4.replace(np.nan, 0)

volume = sudeste_mes_4['casosNovos']
labels = sudeste_mes_4['estado']
l =[]
for index in range(len(labels)):
    l.append(labels[index]+"\n N° casos "+str(volume[index]))

plt.rc('font', size=12)
squarify.plot(sizes=volume, label=l, pad=True,
               alpha=0.3)
plt.axis('off')
plt.title("Região Sudeste do Brasil - Casos do mês de Abril", pad=True, loc='left')
plt.show()