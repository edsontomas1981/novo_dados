from tkinter import Tk, Button, Entry, Label,filedialog,messagebox
from tkinter.filedialog import askdirectory
from verifyXml import verify_xml
from tkinter import ttk
from utils import gera_dict

caminho_pasta=''

def seleciona_pasta():
    global caminho_pasta
    caminho_pasta = askdirectory()
    return caminho_pasta


def gera_xls():
    global caminho_pasta
    nome_planilha = nome_xls.get()
    verify_xml(caminho_pasta, nome_planilha)
    # Exibe um alerta
    messagebox.showinfo("Alerta", "Arquivo gerado com sucesso !")

def gera_dados():
    global caminho_pasta
    caminho_pasta = seleciona_pasta()
    dados,dados_cte = gera_dict(caminho_pasta)
    gerar_treeview(dados)

def cabecalho_treeview():
    # Criação do TreeView
    treeview.pack(side='top')

    # Configuração das colunas
    colunas = ["CNPJ Tomador", "Tomador", "Frete", "Valor NFs", "Volumes", "Peso", "Dt Emissão"]
    widths = [120, 150, 80, 100, 80, 80, 120]  # Larguras desejadas para cada coluna

    for i, coluna in enumerate(colunas):
        treeview.heading(coluna, text=coluna)
        treeview.column(i, width=widths[i])

    # Cria a barra de rolagem
    scrollbar = ttk.Scrollbar(janela, orient="vertical", command=treeview.yview)
    scrollbar.pack(side="right", fill="y")

    # Configura a associação entre o Treeview e a barra de rolagem
    treeview.configure(yscrollcommand=scrollbar.set)

      

def gerar_treeview(dados):

    # Preenchimento dos dados da tabela
    for registro in dados:
        valores = [
            registro.get("cnpj_tomador", ""),
            registro.get("tomador", ""),
            registro.get("frete", ""),
            registro.get("vlr_nfs", ""),
            registro.get("volumes", ""),
            registro.get("peso", ""),
            registro.get("data_emissao", "")

        ]
        treeview.insert("", "end", values=valores)


# Cria a janela
janela = Tk()
# Define a geometria da janela para preencher toda a tela
largura = janela.winfo_screenwidth()
altura = janela.winfo_screenheight()
janela.geometry(f"{largura}x{altura}")

# Cria o Notebook
notebook = ttk.Notebook(janela)

# Cria as abas
aba1 = ttk.Frame(notebook)
aba2 = ttk.Frame(notebook)
aba3 = ttk.Frame(notebook)

# Adiciona as abas ao Notebook
notebook.add(aba1, text="Aba 1")
notebook.add(aba2, text="Aba 2")
notebook.add(aba3, text="Aba 3")

treeview = ttk.Treeview(aba1, columns=("CNPJ Tomador", "Tomador",  "Frete", "Valor NFs", "Volumes", "Peso",'Dt Emissão'), show="headings")

cabecalho_treeview()

# Cria o campo de entrada
nome_xls = Entry(aba2)
nome_xls.pack()

# Cria o rótulo para o campo de entrada
label_nome_xls = Label(aba2, text="Nome do Arquivo:")
label_nome_xls.pack()

# Cria o botão para gerar o arquivo
botao_gerar = Button(aba1, text="Selecionar pasta", command=gera_dados)
botao_gerar.pack(side='left')
# Cria o rótulo para o campo de entrada
label_nome_treeview = Label(aba1, text="Motorista:")
label_nome_treeview.pack()
# Cria o botão para gerar o arquivo
botao_seleciona_pasta = Button(aba2, text="Selecionar pasta", command=seleciona_pasta)
botao_seleciona_pasta.pack()

# Cria o botão para gerar o arquivo
botao_gerar_xls = Button(aba2, text="Gerar Xls", command=gera_xls)
botao_gerar_xls.pack()

# Exibe o Notebook na janela
notebook.pack()

# Executa o loop principal da janela
janela.mainloop()
