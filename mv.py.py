######## bibliotecas 
import urllib.request
import pandas as pd
import datetime
import matplotlib.pyplot as plt


####### downloads dos dados do bcb no formato '.csv'
origem = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=csv'
arquivo = 'dolar_bcb_api.csv'

urllib.request.urlretrieve(origem, arquivo)

###### para cada linha x está transformando de string em data 
dateparse = lambda x: pd.datetime.strptime(x, '%d/%m/%Y') # dia - mes - ano 
df_dolar = pd.read_csv(arquivo, encoding = "utf-8", delimiter=';', index_col=0, parse_dates=['data'], date_parser=dateparse)

# trocando o nome da coluna 
df_dolar.index.names = ['Data'] 
df_dolar.columns = ['Dolar']

# trocando as virgulas por ponto - transformando em float
df_dolar['Dolar'] = df_dolar['Dolar'].str.replace(',', '.').astype(float) 

######## delimitando os ultimos 10 anos 
data_inicial = datetime.datetime.strptime('2009' + "-" + '01' + "-" + '01', "%Y-%m-%d")

data_final = datetime.datetime.strptime('2019' + "-" + '12' + "-" + '31', "%Y-%m-%d")

df_dolar = df_dolar.loc[data_inicial:data_final]


plt.title('Grafico dolar 2009 - 2019')
df_dolar['Dolar'].plot()
plt.legend(loc=7)
plt.xlabel('Data')
plt.ylabel('Dólar')

medmov = df_dolar.rolling(window = 30)
plt.plot(df_dolar ,'k-', alpha = 0.10)
plt.plot(medmov.mean() , 'r-' )

plt.show()