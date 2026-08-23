import pandas as pd
import requests
import time
import os

CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

def consultar_brasil_api(cnpj):
    cnpj_limpo = ''.join(filter(str.isdigit, str(cnpj)))
    url = f"https://brasilapi.com.br/api/cnpj/v1/{cnpj_limpo}"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200:
            data = res.json()
            razao = data.get('razao_social', 'Empresa Comercial')
            ddd_tel = data.get('ddd_telefone_1', '')
            if ddd_tel:
                tel_limpo = ''.join(filter(str.isdigit, str(ddd_tel)))
                if len(tel_limpo) >= 10:
                    return razao, f"55{tel_limpo}"
    except Exception:
        pass
    return None, None

def enriquecer_base():
    print("[+] OPERÁRIO 1: Iniciando varredura e enriquecimento dos CNPJs na rede...")
    
    # CNPJs para consulta e enriquecimento de base
    cnpjs_para_rodar = [
        "00000000000191", "33000167000101", "02558157000162", "06626253000151"
    ]
    
    novos_dados = []
    for cnpj in cnpjs_para_rodar:
        razao, tel = consultar_brasil_api(cnpj)
        if tel:
            print(f"[✓ ENCONTRADO] {razao} -> Tel: {tel}")
            novos_dados.append({"Razao_Social": razao, "Telefone": tel})
        time.sleep(1) # Respeita o limite da API pública
        
    if novos_dados:
        df = pd.DataFrame(novos_dados)
        df.to_csv(CSV_PATH, sep=';', encoding='utf-8-sig', index=False)
        print(f"[SUCCESS] Base C:\\IOTEC\\base_empresas.csv atualizada com {len(df)} contatos enriquecidos!")
    else:
        print("[!] Nenhum telefone novo retornado nesta rodada.")

if __name__ == '__main__':
    enriquecer_base()
