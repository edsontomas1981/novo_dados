import pandas as pd

def consolidado_totais(dados):
    df = pd.DataFrame(dados)
    dados_totais = []
    for coluna in df.columns:
        tomador_cnpj = df[coluna]['tomador']['CNPJ']
        tomador_nome = df[coluna]['tomador']['Nome']
        peso = df[coluna]['peso']
        frete = df[coluna]['frete']
        total_nf = df[coluna]['valor']
        dados_totais.append({
            tomador_cnpj: {
                'tomador': tomador_cnpj,
                'nome': tomador_nome,
                'peso': peso,
                'frete': frete,
                'vlr_nf': total_nf
            }
        })

    consolidado = {}
    for item in dados_totais:
        for tomador, dados_tomador in item.items():
            if tomador in consolidado:
                consolidado[tomador]['dados']['frete'] = round(float(dados_tomador['frete'])+float(consolidado[tomador]['dados']['frete']),2)
                consolidado[tomador]['dados']['peso'] = round(float(dados_tomador['peso'])+float(consolidado[tomador]['dados']['peso']),2)
                consolidado[tomador]['dados']['vlr_nf'] = round(float(dados_tomador['vlr_nf'])+float(consolidado[tomador]['dados']['vlr_nf']),2)
            else:
                consolidado[tomador] = {'dados': dados_tomador}
                consolidado[tomador]['dados']['frete'] = round(float(consolidado[tomador]['dados']['frete']),2)
                consolidado[tomador]['dados']['peso'] = round(float(consolidado[tomador]['dados']['peso']),2)
                consolidado[tomador]['dados']['vlr_nf'] = round(float(consolidado[tomador]['dados']['vlr_nf']),2)                

    consolidado_df = pd.DataFrame(consolidado)
    return consolidado



    
    