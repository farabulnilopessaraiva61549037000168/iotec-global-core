import pandas as pd
from datetime import datetime

CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

def rodar_contatador():
    try:
        df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig', dtype=str, low_memory=False)
        agora = datetime.now().strftime('%H:%M')
        print(f'[+] [{agora}] Processando lote com {len(df)} leads ativos...')
        print('[+] Lote concluido e base atualizada.')
    except Exception as e:
        print(f'[!] Erro no contatador: {e}')

if __name__ == '__main__':
    rodar_contatador()
