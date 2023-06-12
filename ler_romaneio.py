import pytesseract
from PIL import Image

# Definir o caminho para o arquivo de dados do idioma 'por'
tessdata_dir = '/usr/share/tesseract-ocr/4.00/tessdata/'

# Carregar a imagem
image_path = 'doc3.png'
image = Image.open(image_path)

# Realizar o reconhecimento de texto usando Tesseract
text = pytesseract.image_to_string(image, lang='por', config=f'--tessdata-dir "{tessdata_dir}"')

# Exibir o texto reconhecido
print(text)
