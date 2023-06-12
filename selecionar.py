import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('bd_data_norte.db')
cursor = conn.cursor()

    # Executar o comando SQL para inserir os dados na tabela
cursor.execute('''
                SELECT Tomador_Frete,toma_CNPJ, SUM(Fr_Valor)  AS valor_total,COUNT(*) as registros
                FROM ctes
                GROUP BY toma_CNPJ order by registros
                ''') 
linha = cursor.fetchall()
print(linha)
# Fechar a conexão com o banco de dados
conn.commit()
conn.close()

