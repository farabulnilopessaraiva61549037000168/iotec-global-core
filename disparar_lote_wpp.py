import csv, time, requests, json, os

arquivo_csv = r'C:\IOTEC\LOTE_PROSPECCAO_B2B.csv'
url = 'http://localhost:21465/send-message'
headers = {'Content-Type': 'application/json'}

print('=== INICIANDO DISPAROS VIA WHATSAPP (LOTE B2B) ===\n')

if not os.path.exists(arquivo_csv):
    print(f'❌ ERRO: O arquivo {arquivo_csv} nao foi encontrado!')
    exit()

try:
    with open(arquivo_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        total = 0
        enviados = 0
        
        for row in reader:
            total += 1
            empresa = row.get('RAZAO_SOCIAL', 'Empresa')
            telefone = row.get('TELEFONE', '').strip().replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
            
            if not telefone or len(telefone) < 10:
                print(f'[{total}/50] ⚠️ {empresa[:30]}: Telefone invalido/ausente ({telefone})')
                continue
                
            if not telefone.startswith('55'):
                telefone = '55' + telefone
                
            mensagem = f'''Olá! Apresentação comercial IOTEC Platform para a *{empresa}*.

Disponibilizamos a emissão e validação automatizada de Certidões de Compliance B2B com suporte e liquidação 24/7.

🔗 *Acesse o portal e consulte os serviços:*
https://endearing-fudge-3789ac.netlify.app

Dúvidas e Atendimento: (88) 99306-4168 | IOTEC.BL@proton.me'''

            payload = {'phone': telefone, 'message': mensagem}
            
            try:
                r = requests.post(url, data=json.dumps(payload), headers=headers, timeout=10)
                if r.status_code == 200:
                    enviados += 1
                    print(f'[{total}/50] ✅ {empresa[:30]} -> Enviado para {telefone}')
                else:
                    print(f'[{total}/50] ❌ {empresa[:30]} -> Falha HTTP {r.status_code}: {r.text}')
            except Exception as e:
                print(f'[{total}/50] ❌ {empresa[:30]} -> Erro de conexao HTTP (Servidor offline?)')
                
            # Intervalo de seguranca (5 segundos) para evitar bloqueios de SPAM
            time.sleep(5)
            
    print(f'\n=== DISPAROS CONCLUÍDOS: {enviados}/{total} ENVIADOS ===')

except Exception as e:
    print(f'Erro ao ler arquivo CSV: {e}')
