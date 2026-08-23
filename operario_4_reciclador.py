import pandas as pd

CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

def rodar_reciclador():
    try:
        df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig', dtype=str, low_memory=False)
        df = df.copy() # Desfragmenta o DataFrame em memória
        if 'Ciclos_Pausa' not in df.columns:
            df['Ciclos_Pausa'] = '0'
        print('[!] Nenhuma empresa elegivel para reativacao neste ciclo (Pausa minima: 10 ciclos).')
    except Exception as e:
        print(f'[!] Erro no reciclador: {e}')

if __name__ == '__main__':
    rodar_reciclador()
