import requests, json

url = 'http://localhost:21465/api/iotec-session/send-message'
headers = {'Content-Type': 'application/json'}

mensagem_teste = '''*IOTEC Platform - Teste de Disparo Comercial*

Olá! A infraestrutura de envio via WhatsApp está ativa e conectada.

🔗 *Link do Checkout Nuvem (24/7):*
https://endearing-fudge-3789ac.netlify.app

Suporte IOTEC: (88) 99306-4168'''

payload = {
    'phone': '5588993064168',
    'message': mensagem_teste
}

try:
    response = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
    print('HTTP Status:', response.status_code)
    print('Resposta:', response.text)
except Exception as e:
    print('Erro ao enviar mensagem:', e)
