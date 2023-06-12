import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('bd_data_norte.db')
cursor = conn.cursor()

# Criar a tabela
cursor.execute('''CREATE TABLE ctes (
                    CTRC TEXT,
                    Pedido TEXT,
                    Dt_Emissao TEXT,
                    Remetente TEXT,
                    Rem_CNPJ TEXT,
                    Destinatario TEXT,
                    Des_CNPJ TEXT,
                    Des_CEP TEXT,
                    Tomador_Frete TEXT,
                    Toma_CNPJ TEXT,
                    Redespachante TEXT,
                    Redesp_CNPJ TEXT,
                    Rota TEXT,
                    Duplicata TEXT,
                    Fr_Valor REAL,
                    Advalorem REAL,
                    Despacho REAL,
                    GRIS REAL,
                    Pedagio REAL,
                    Outros REAL,
                    ICMS REAL,
                    Frete_Total REAL,
                    Volumes INTEGER,
                    m3 REAL,
                    Peso_Real REAL,
                    Peso_Cub REAL,
                    Peso_Fatur REAL,
                    Valor_NFs REAL,
                    Origem TEXT,
                    Destino TEXT,
                    Dt_Ultima_Ocorrencia TEXT,
                    Ultima_Ocorrencia TEXT,
                    Obs_Ocorrencia TEXT,
                    Dt_Entrega TEXT,
                    Viagem TEXT,
                    Placa TEXT,
                    Manifesto TEXT,
                    Averbacao TEXT,
                    Natureza TEXT,
                    Vendedor TEXT
                    )''')

# Fechar a conexão com o banco de dados
conn.commit()
conn.close()