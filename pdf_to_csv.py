import csv
import PyPDF2

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def convert_pdf_to_csv(pdf_path, csv_path):
    text = extract_text_from_pdf(pdf_path)
    lines = text.split("\n")

    with open(csv_path, "w", newline="") as file:
        writer = csv.writer(file)
        for line in lines:
            row = line.split()  # Separa as palavras da linha
            writer.writerow(row)

# Exemplo de uso
pdf_path = "doc.pdf"
csv_path = "doc_csv.csv"

convert_pdf_to_csv(pdf_path, csv_path)

with open('doc_csv.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Ler todas as linhas do arquivo CSV
    linhas = list(leitor_csv)

# Remover as quatro primeiras linhas
linhas = linhas[4:]

# Abrir o arquivo CSV novamente para escrita e criar um escritor CSV
with open('doc_csv.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    # Escrever as linhas atualizadas no arquivo CSV
    escritor_csv.writerows(linhas)
