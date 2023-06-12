import pandas as pd

dados = pd.read_excel('04052022.xls')

# Criar um DataFrame com os totais por cliente
df_totais = pd.DataFrame(dados)


total_pedidos_cliente = df_totais.groupby('frete_total').sum()

for x in total_pedidos_cliente.items(): 
    print('X:', x)
    # print('Y:', y)
    # print('Z:', z)


# # Agrupar os dados por cliente e calcular os totais
# totais_por_cliente = dados.groupby('Toma CNPJ')['Frete Total'].sum()

# print(totais_por_cliente)



# for cliente in totais_por_cliente.items():
#     print(cliente)
    