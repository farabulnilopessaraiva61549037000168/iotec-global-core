import pandas as pd
import os

folder = 'C:\\IOTEC'
if not os.path.exists(folder):
    os.makedirs(folder)

csv_path = os.path.join(folder, 'base_empresas.csv')

if not os.path.exists(csv_path):
    data = {
        'Razao_Social': ['TRANSPORTADORA EXEMPLO LTDA', 'LOGISTICA GLOBAL SA', 'DISTRIBUIDORA NORDESTE LTDA'],
        'Telefone': ['5588993064168', '5588993064168', '5588993064168'],
        'Email': ['contato@exemplo.com', 'logistica@exemplo.com', 'vendas@exemplo.com'],
        'Tipo_alvo': ['Transporte', 'Logística', 'Comércio']
    }
    df = pd.DataFrame(data)
    df.to_csv(csv_path, sep=';', encoding='utf-8-sig', index=False)
    print('[OK] Arquivo base_empresas.csv criado com sucesso!')
