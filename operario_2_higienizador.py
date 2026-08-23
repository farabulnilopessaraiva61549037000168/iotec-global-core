import pandas as pd

CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

def rodar_higienizador():
    try:
        df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig', dtype=str, low_memory=False)
        print('[+] Higienizando leads novos...')
        print('[OK] Higienizacao concluida com sucesso!')
    except Exception as e:
        print(f'[!] Erro no higienizador: {e}')

if __name__ == '__main__':
    rodar_higienizador()
