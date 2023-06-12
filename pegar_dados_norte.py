import pandas as pd
import sqlite3

# Função para gravar os dados no banco de dados
def gravar_dados_bd(row):
    # Conectar ao banco de dados
    conn = sqlite3.connect('bd_data_norte.db')
    cursor = conn.cursor()

    # Extrair os valores de cada coluna
    ctrc = row['CTRC']
    pedido = row['Pedido']
    dt_emissao = row['Dt.Emissao']
    remetente = row['Remetente']
    rem_cnpj = row['Rem CNPJ']
    destinatario = row['Destinatario']
    des_cnpj = row['Des CNPJ']
    des_cep = row['Des CEP']
    tomador_frete = row['Tomador do Frete']
    toma_cnpj = row['Toma CNPJ']
    redespachante = row['Redespachante']
    redesp_cnpj = row['Redesp CNPJ']
    rota = row['Rota']
    duplicata = row['Duplicata']
    fr_valor = row['Fr Valor']
    advalorem = row['Advalorem']
    despacho = row['Despacho']
    gris = row['GRIS']
    pedagio = row['Pedagio']
    outros = row['Outros']
    aliq_icms = row['ICMS']
    frete_total = row['Frete Total']
    volumes = row['Volumes']
    m3 = row['m3']
    peso_real = row['Peso Real']
    peso_cub = row['Peso Cub']
    peso_fatur = row['Peso Fatur']
    valor_nfs = row['Valor NFs']
    origem = row['Origem']
    destino = row['Destino']
    dt_ultima_ocorrencia = row['Dt.Ultima Ocorrencia']
    ultima_ocorrencia = row['Ultima Ocorrencia']
    obs_ocorrencia = row['Obs Ocorrencia']
    dt_entrega = row['Dt Entrega']
    viagem = row['Viagem']
    placa = row['Placa']
    manifesto = row['Manifesto']
    averbacao = row['Averbacao']
    natureza = row['Natureza']
    vendedor = row['Vendedor']

    # Executar o comando SQL para inserir os dados na tabela
    cursor.execute('''INSERT INTO ctes (CTRC, Pedido, Dt_Emissao, Remetente, 
                    Rem_CNPJ, Destinatario, Des_CNPJ, Des_CEP, Tomador_Frete, 
                    Toma_CNPJ, Redespachante, Redesp_CNPJ, Rota, Duplicata, 
                    Fr_Valor, Advalorem, Despacho, GRIS, Pedagio, Outros, ICMS, 
                    Frete_Total, Volumes, m3, Peso_Real, Peso_Cub, Peso_Fatur, 
                    Valor_NFs, Origem, Destino, Dt_Ultima_Ocorrencia, 
                    Ultima_Ocorrencia, Obs_Ocorrencia, Dt_Entrega, Viagem, 
                    Placa, Manifesto, Averbacao, Natureza, Vendedor) 
                    VALUES (
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
                        ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                  (ctrc, pedido, dt_emissao, remetente, 
                   rem_cnpj, destinatario, des_cnpj, des_cep, 
                   tomador_frete, toma_cnpj, redespachante, redesp_cnpj, 
                   rota, duplicata, fr_valor, advalorem, 
                   despacho, gris, pedagio, outros, 
                   aliq_icms, frete_total, volumes, m3, 
                   peso_real, peso_cub, peso_fatur, valor_nfs, 
                   origem, destino, dt_ultima_ocorrencia, ultima_ocorrencia, 
                   obs_ocorrencia, dt_entrega, viagem, placa, 
                   manifesto, averbacao, natureza, vendedor))

    # Fechar a conexão com o banco de dados
    conn.commit()
    conn.close()

# Ler o arquivo Excel com o pandas
df = pd.read_excel('ctrcs.xlsx')

# Iterar pelas linhas do DataFrame
for index, row in df.iterrows():
    gravar_dados_bd(row)
