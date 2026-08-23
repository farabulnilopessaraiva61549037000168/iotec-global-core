import pandas as pd
import requests
import time
from datetime import datetime

ZAPI_INSTANCE_ID = "3F8066F099284121F1F5DA9739CF5BB5"
ZAPI_TOKEN = "1394B2099F6C7104DE6D6C6C"
CNPJ_MATRIZ = "61.549.037/0001-68"
WHATSAPP_PRESIDENCIA = "5588993064168"
CSV_PATH = 'C:\\IOTEC\\base_empresas.csv'

def enviar_mensagem_whatsapp(numero_destino, texto_mensagem):
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"
    headers = {"Content-Type": "application/json"}
    payload = {"phone": numero_destino, "message": texto_mensagem}
    try:
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        if response.status_code == 200:
            return True
        else:
            print(f"[!] Resposta Z-API (HTTP {response.status_code}): {response.text}")
            return False
    except Exception as e:
        print(f"[!] Erro de conexão: {e}")
        return False

def processar_disparos_em_lote():
    try:
        df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig', dtype=str)
        print(f"[+] Lendo base com {len(df)} registros cadastrados...")
        
        for index, row in df.iterrows():
            razao = str(row.get('Razao_Social', 'Empresa')).strip()
            telefone = str(row.get('Telefone', '')).strip()
            num_limpo = ''.join(filter(str.isdigit, telefone))
            
            if not num_limpo.startswith('55'):
                num_limpo = '55' + num_limpo

            texto_oferta = f"Olá, responsável pela empresa *{razao}*.\n\n" \
                           f"A *IOTEC Global* identificou a necessidade de atualização/emissão da sua *Certidão CND / Licença Logística*.\n\n" \
                           f"Emitimos o documento oficial autenticado com QR-Code em tempo real.\n\n" \
                           f"💰 *Taxa de Emissão:* R$ 150,00\n" \
                           f"🔑 *Chave Pix CNPJ Matriz:* {CNPJ_MATRIZ}\n\n" \
                           f"Responda esta mensagem para receber a minuta ou acesse o portal IOTEC."

            if enviar_mensagem_whatsapp(num_limpo, texto_oferta):
                print(f"[🚀 PROPOSTA ENVIADA COM SUCESSO] Para: {razao} ({num_limpo})")
            else:
                print(f"[!] Falha na entrega para {num_limpo}")

    except Exception as e:
        print(f"[!] Erro ao processar lote: {e}")

if __name__ == '__main__':
    processar_disparos_em_lote()
