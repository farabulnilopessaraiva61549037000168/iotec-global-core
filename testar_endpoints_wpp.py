import requests

url_base = 'http://localhost:21465'
endpoints = [
    '/api/send-message',
    '/api/messages/send',
    '/send-message',
    '/api/sendText',
    '/message/send-text',
    '/api/v1/send-message',
    '/api/iotec/send-message',
    '/sendText'
]

payload = {
    'phone': '5588993064168',
    'number': '5588993064168@c.us',
    'message': 'Teste de conexão IOTEC',
    'text': 'Teste de conexão IOTEC'
}

print('=== VARRENDO ENDPOINTS DE ENVIO DO WPPCONNECT ===\n')

for ep in endpoints:
    url = url_base + ep
    try:
        r = requests.post(url, json=payload, timeout=3)
        print(f'POST {ep} -> Status: {r.status_code} | Resposta: {r.text[:100]}')
    except Exception as e:
        print(f'POST {ep} -> Erro: {e}')
