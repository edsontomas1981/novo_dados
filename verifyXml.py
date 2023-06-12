import openpyxl
import pandas as pd
from utils import analisa_frete,consolidado_totais
from utils import gera_dict,cria_aba_frete_consolidado

def verify_xml(caminho_pasta,nome_planilha):
    dados_totais,dados_cte=gera_dict(caminho_pasta)       

    # Criar um novo DataFrame com os totais por remetente
    df_totais = pd.DataFrame(dados_totais)

    frete_total = df_totais['frete'].sum()
    peso_total = df_totais['peso'].sum()
    vlr_nf_total = df_totais['vlr_nfs'].sum()

    totais = {'frete_total':float(frete_total),
            'peso_total':float(peso_total),
            'vlr_nfs_total':float(vlr_nf_total)}

    consolidado=consolidado_totais(dados_cte)
   
    workbook = openpyxl.Workbook()        
    analisa_frete(dados_cte, workbook,totais)
    cria_aba_frete_consolidado(consolidado,workbook,totais)
    workbook.save(nome_planilha+'.xlsx')
