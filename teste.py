import pandas as pd

# Ler o arquivo Excel com o pandas
df = pd.read_excel('ctrcs.xlsx')

# Converter a coluna de valor para o tipo numérico
df['Valor'] = df['Valor'].astype(float)

# Agrupar os registros pelo toma_CNPJ e calcular a soma das colunas de valor
agrupado = df.groupby('Toma_CNPJ').sum()

# Converter o resultado para um dicionário
dados_agrupados = agrupado.to_dict()

# Exibir o dicionário
print(dados_agrupados)
