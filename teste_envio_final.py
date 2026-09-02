import requests, json

url = 'http://localhost:21465/send-message'
headers = {'Content-Type': 'application/json'}

payload = {
    'phone': '5588993064168',
    'message': '''*IOTEC Platform - Autenticação Confirmada*

A API de WhatsApp local está ativa na porta 21465.

🔗 *Portal de Vendas Nuvem (24/7):*
https://endearing-fudge-3789ac.netlify.app'''
}

try:
    r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=15)
    print('Status HTTP:', r.status_code)
    print('Resposta:', r.text)
except Exception as e:
    print('Erro:', e)
