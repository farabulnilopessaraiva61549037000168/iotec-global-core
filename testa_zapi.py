import requests

ZAPI_INSTANCE_ID = "3F8066F099284121F1F5DA9739CF5BB5"
ZAPI_TOKEN = "1394B2099F6C7104DE6D6C6C"

def verificar_status():
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/status"
    try:
        response = requests.get(url, timeout=10)
        print(f"[+] Status HTTP da Instância: {response.status_code}")
        print(f"[+] Resposta da Z-API: {response.text}")
    except Exception as e:
        print(f"[!] Erro ao conectar: {e}")

if __name__ == '__main__':
    verificar_status()
