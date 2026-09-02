import csv, time, urllib.parse, subprocess, os

arquivo_csv = r'C:\IOTEC\LOTE_PROSPECCAO_B2B.csv'

print('=== DISPARO DIRETO VIA NAVEGADOR (SISTEMA NATIVO) ===\n')

try:
    with open(arquivo_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        total = 0
        
        for row in reader:
            total += 1
            empresa = row.get('RAZAO_SOCIAL', 'Empresa')
            telefone = row.get('TELEFONE', '').strip().replace('+', '').replace('-', '').replace(' ', '').replace('(', '').replace(')', '')
            
            if not telefone or len(telefone) < 10:
                print(f'[{total}/50] ⚠️ {empresa[:30]}: Telefone ausente/inválido ({telefone})')
                continue
                
            if not telefone.startswith('55'):
                telefone = '55' + telefone
                
            mensagem = f'''Olá! Apresentação comercial IOTEC Platform para a *{empresa}*.

Disponibilizamos a emissão e validação automatizada de Certidões de Compliance B2B com suporte e liquidação 24/7.

🔗 *Acesse o portal e consulte os serviços:*
https://endearing-fudge-3789ac.netlify.app

Dúvidas e Atendimento: (88) 99306-4168 | IOTEC.BL@proton.me'''

            msg_encoded = urllib.parse.quote(mensagem)
            url_wa = f'https://web.whatsapp.com/send?phone={telefone}&text={msg_encoded}'
            
            print(f'[{total}/50] 🚀 Abrindo conversa para {empresa[:30]} ({telefone})...')
            os.system(f'start chrome "{url_wa}"')
            
            # Tempo para carregamento do chat na tela e envio manual/automatizado
            time.sleep(12)
            
except Exception as e:
    print(f'Erro no processamento: {e}')
