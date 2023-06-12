import xmltodict
from datetime import datetime

def extrair_dados_xml(arquivo_xml):
    with open(arquivo_xml, 'r') as file:
        xml_data = file.read()

    dados_dict = xmltodict.parse(xml_data)

    # Acessar os dados desejados do dicionário convertido
    dados = {}
    dados['data_emissao'] = dados_dict['mdfeProc']['MDFe']['infMDFe']['ide']['dhEmi']
    dados['tpAmb'] = dados_dict['mdfeProc']['MDFe']['infMDFe']['ide']['tpAmb']
    dados['tpEmit'] = dados_dict['mdfeProc']['MDFe']['infMDFe']['ide']['tpEmit']
    # Continuar para outros dados que você deseja extrair

    return dados

# Exemplo de uso
dados_xml = extrair_dados_xml('MDFe.xml')



data_string = "2023-06-07T21:15:01-03:00"
data_formatada = datetime.strptime(dados_xml['data_emissao'], "%Y-%m-%dT%H:%M:%S%z")

print(data_formatada)
