# -*- coding: utf-8 -*-
import urllib.parse

class WhatsAppNucleoBridge:
    def __init__(self):
        self.numero_iotec = "5588993064168"
        self.portal_url = "https://jolly-tiramisu-b0be2b.netlify.app/"
        self.nome_fantasia = "IOTEC — Construtora e Distribuidora de Tecnologia"
        
    def gerar_link_wa(self, numero_destino, mensagem):
        msg_encoded = urllib.parse.quote(mensagem)
        return f"https://web.whatsapp.com/send?phone={numero_destino}&text={msg_encoded}"

if __name__ == '__main__':
    bridge = WhatsAppNucleoBridge()
    link = bridge.gerar_link_wa('5588993064168', 'Teste de Integração Operacional IOTEC — Verificando Conectividade')
    print('\n[✓] ARQUIVO CRIADO EM C:\\IOTEC\\integrador_whatsapp.py')
    print('[✓] TESTE DE LINK DIRETO:\n' + link)