import requests, json

url = 'http://localhost:21465/send-message'
headers = {'Content-Type': 'application/json'}

payload = {
    'phone': '5588993064168',
    'message': 'Sessao WhatsApp restabelecida com sucesso no IOTEC!'
}

try:
    r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
    print('Status HTTP:', r.status_code)
    print('Resposta:', r.text)
except Exception as e:
    print('Erro na conexao:', e)
