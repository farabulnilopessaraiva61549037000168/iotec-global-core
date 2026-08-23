import pandas as pd

CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

# Insira aqui contatos reais com DDD + 9 dígitos para os disparos comerciais
empresas_externas = [
    {"Razao_Social": "LOGISTICA NORDESTE EXPRESS", "Telefone": "5585999998888"},
    {"Razao_Social": "TRANSPORTE E CARGAS S/A", "Telefone": "5588988887777"}
]

df = pd.DataFrame(empresas_externas)
df.to_csv(CSV_PATH, sep=';', encoding='utf-8-sig', index=False)
print('[SUCCESS] Base atualizada com telefones externos em C:\\IOTEC\\base_empresas.csv')
