import os
from utils import extract_numeros_nfe,extract_destinatario,extract_remetente
from utils import extract_informacoes_carga,extract_terceiro_tomador,extract_valor_mercadoria
from utils.extract_data_emissao_cte import extract_data_cte
import pandas as pd
import xml.etree.ElementTree as ET


def gera_dict(pasta):
        # Especificar o caminho da pasta contendo os arquivos XML
    dados_cte={}
    # Iterar sobre todos os arquivos na pasta
    for arquivo in os.listdir(pasta):
        # Verificar se o arquivo tem extensão XML
        if arquivo.endswith('.xml'):
            # Obter o caminho completo do arquivo
            caminho_arquivo = os.path.join(pasta, arquivo)

            try:
                # Fazer o parsing do arquivo XML
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()
                namespace = {'cte': 'http://www.portalfiscal.inf.br/cte'}

                destinatario=extract_destinatario(root,namespace)
                remetente=extract_remetente(root,namespace)
                infCarga = extract_informacoes_carga(root, namespace)
                ncte = root.find('.//{http://www.portalfiscal.inf.br/cte}nCT').text
                total_prest = root.find('.//{http://www.portalfiscal.inf.br/cte}vTPrest').text
                tomador = root.find('.//{http://www.portalfiscal.inf.br/cte}toma').text
                numeros_nfe = extract_numeros_nfe(root)
                valor_nfs = extract_valor_mercadoria(root,namespace)
                data_emissao = extract_data_cte(root,namespace)
                
                if tomador == '4':
                    terceiro_tomador = extract_terceiro_tomador(root,namespace)

                if tomador == '0':
                    dados_cte[ncte]={'rem':remetente,'peso':infCarga['peso_faturado'],
                                    'volumes':infCarga['volumes'],'frete':total_prest,
                                    'nf':numeros_nfe,'dest':destinatario,'notas':numeros_nfe,
                                    'valor':valor_nfs,'tomador':remetente,'data_emissao':data_emissao}
                elif tomador == '4':
                    dados_cte[ncte]={'rem':remetente,'peso':infCarga['peso_faturado'],
                                    'volumes':infCarga['volumes'],'frete':total_prest,
                                    'nf':numeros_nfe,'dest':destinatario,'notas':numeros_nfe,
                                    'valor':valor_nfs,'tomador':terceiro_tomador,'data_emissao':data_emissao}
                else:
                    dados_cte[ncte]={'rem':remetente,'peso':infCarga['peso_faturado'],
                                    'volumes':infCarga['volumes'],'frete':total_prest,
                                    'nf':numeros_nfe,'dest':destinatario,'notas':numeros_nfe,
                                    'valor':valor_nfs,'tomador':destinatario,'data_emissao':data_emissao}
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {str(e)}")

    df=pd.DataFrame(dados_cte)
    
    dados_totais = []
    for coluna in df.columns:
        remetente = df[coluna]['rem']['Nome']
        cnpj_remetente = df[coluna]['rem']['CNPJ']
        destinatario = df[coluna]['dest']['Nome']
        cnpj_destinatario = df[coluna]['dest']['CNPJ']
        tomador = df[coluna]['tomador']['Nome']
        cnpj_tomador = df[coluna]['tomador']['CNPJ'] 
        vlr_nfs = float(df[coluna]['valor'])
        volumes = float(df[coluna]['volumes'])
        peso = float(df[coluna]['peso'])
        data_emissao_cte = df[coluna]['data_emissao']

    
        frete = float(df[coluna]['frete'])
        dados_totais.append({'cnpj_tomador': cnpj_tomador,'tomador': tomador,
                            'cnpj_rem': cnpj_remetente,'remetente': remetente,
                            'cnpj_dest': cnpj_destinatario,'destinatario': destinatario,
                            'frete': frete,'vlr_nfs':vlr_nfs,'volumes':volumes,'peso':peso,
                            'data_emissao':data_emissao_cte})
    print(dados_totais)

    return dados_totais,dados_cte
        

