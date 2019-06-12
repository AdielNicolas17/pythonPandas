######## bibliotecas 
import urllib.request
import pandas as pd
import datetime
import matplotlib.pyplot as plt


####### downloads dos dados do bcb
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

######## delimitando os ultimos de 5 anos 
data_inicial = datetime.datetime.strptime('2014' + "-" + '01' + "-" + '01', "%Y-%m-%d")

data_final = datetime.datetime.strptime('2019' + "-" + '12' + "-" + '31', "%Y-%m-%d")

df_dolar = df_dolar.loc[data_inicial:data_final]


print(df_dolar)
# gerando o grafico


plt.title('Grafico dolar 2014 - 2019')
df_dolar['Dolar'].plot()
plt.legend(loc=7)
plt.xlabel('Data')
plt.ylabel('Dólar')

#plt.show()

## estatisticas 
#print(df_dolar)

resumo = df_dolar.describe(include ='all')
print (resumo)

media = df_dolar.mean() 
print("Valor médio: ", media, "\n")

media = df_dolar.max() 
print("Valor maximo: ", media, "\n")

media = df_dolar.min() 
print("Valor minimo: ", media, "\n")
