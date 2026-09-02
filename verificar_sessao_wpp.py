import requests

url_base = 'http://localhost:21465'
endpoints_status = [
    '/status',
    '/session/status',
    '/get-status',
    '/start-session',
    '/qrcode'
]

print('=== CHECANDO STATUS DA SESSÃO WHATSAPP ===\n')

for ep in endpoints_status:
    try:
        r = requests.get(url_base + ep, timeout=3)
        print(f'GET {ep} -> Status: {r.status_code} | Resposta: {r.text[:150]}')
    except Exception as e:
        print(f'GET {ep} -> Erro: {e}')
