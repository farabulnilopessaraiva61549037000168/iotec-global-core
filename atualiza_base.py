import pandas as pd

CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

# Substitua pelos números reais de clientes, contadores ou parceiros que você deseja contatar
empresas_reais = [
    {"Razao_Social": "TRANSPORTES CEARA LTDA", "Telefone": "5585999998888", "Email": "comercial@transceara.com.br", "Tipo_alvo": "Transporte"},
    {"Razao_Social": "LOGISTICA NORDESTE S/A", "Telefone": "5588988887777", "Email": "contato@lognordeste.com.br", "Tipo_alvo": "Logística"}
]

df = pd.DataFrame(empresas_reais)
df.to_csv(CSV_PATH, sep=';', encoding='utf-8-sig', index=False)
print('[SUCCESS] Base atualizada com sucesso no arquivo base_empresas.csv!')
