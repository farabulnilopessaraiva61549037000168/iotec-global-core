import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


import os
import pandas as pd
from PyPDF2 import PdfReader

# Define a pasta onde estÃƒÆ'Ã†â€™o os dados
pasta_dados = r'C:\CerebroDigital\DadosBrutos'

# Lista todos os arquivos na pasta
for raiz, diretorios, arquivos in os.walk(pasta_dados):
    for arquivo in arquivos:
        caminho_arquivo = os.path.join(raiz, arquivo)

        if arquivo.endswith('.pdf'):
            print(f'Lendo PDF: {arquivo}')
            reader = PdfReader(caminho_arquivo)
            texto = ""
            for page in reader.pages:
                texto += page.extract_text()
            print(texto)

        elif arquivo.endswith('.csv'):
            print(f'Lendo CSV: {arquivo}')
            df = pd.read_csv(caminho_arquivo)
            print(df.head())

        elif arquivo.endswith('.xlsx'):
            print(f'Lendo Excel: {arquivo}')
            df = pd.read_excel(caminho_arquivo)
            print(df.head())

        elif arquivo.endswith('.txt'):
            print(f'Lendo TXT: {arquivo}')
            with open(caminho_arquivo, 'r', encoding='utf-8') as f:
                texto = f.read()
                print(texto)

        else:
            print(f'Arquivo nÃƒÆ'Ã†â€™o suportado (ainda): {arquivo}')


