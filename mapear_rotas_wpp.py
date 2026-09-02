import requests

base_url = 'http://localhost:21465'
endpoints_teste = [
    '/',
    '/api/sessions',
    '/status',
    '/api/iotec-session',
    '/api/iotec-session/status-session',
    '/api/iotec/send-message'
]

print('=== MAPEANDO ENDPOINTS DO WPPCONNECT ===\n')
for ep in endpoints_teste:
    url = base_url + ep
    try:
        r = requests.get(url, timeout=3)
        print(f'GET {ep} -> Status: {r.status_code} | Resposta: {r.text[:120]}')
    except Exception as e:
        print(f'GET {ep} -> Erro: {e}')
