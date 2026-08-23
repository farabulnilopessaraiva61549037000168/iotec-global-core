"""
===================================================================================
                       IOTEC NUCLEUS - DISPARADOR LOCAL WHATSAPP
===================================================================================
 Arquiteto-Chefe: Farabulini Lopes Saraiva
 Canal Corporativo Oficial: (88) 99930-6416
 CNPJ: 61.549.037/0001-68
===================================================================================
"""

import pywhatkit as pwk
import time
from typing import List, Dict

class DisparadorLocalWhatsApp:
    def __init__(self):
        self.canal_origem = "(88) 99930-6416"

    def enviar_mensagem_direta(self, numero_destino: str, mensagem: str):
        """
        Abre o WhatsApp Web no navegador local e envia a mensagem programada.
        O número deve conter o DDD (ex: '+5588999306416').
        """
        num_formatado = numero_destino.strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
        if not num_formatado.startswith("+55"):
            num_formatado = f"+55{num_formatado}"

        print(f"[+] Preparando envio via WhatsApp Web para {num_formatado}...")
        try:
            # Envia instantaneamente (aguarda 15 segundos para carregar a página e fecha a aba após 3s)
            pwk.sendwhatmsg_instantly(
                phone_no=num_formatado,
                message=mensagem,
                wait_time=15,
                tab_close=True,
                close_time=3
            )
            print(f"[✓] Mensagem enviada com sucesso para {num_formatado}!")
            return True
        except Exception as e:
            print(f"[!] Erro no disparo para {num_formatado}: {e}")
            return False

if __name__ == "__main__":
    disparador = DisparadorLocalWhatsApp()
    
    # Exemplo de teste interno para o WhatsApp Business Oficial IOTEC:
    numero_teste = "88999306416"
    texto_abertura = (
        "IOTEC NUCLEUS - Notificação Interna de Sistema\n"
        "----------------------------------------------\n"
        "Canal de Atendimento Comercial ativado com sucesso.\n"
        "Titular: Farabulini Lopes Saraiva\n"
        "CNPJ: 61.549.037/0001-68"
    )
    
    # Para rodar o teste de bancada no seu WhatsApp Web, descomente a linha abaixo:
    # disparador.enviar_mensagem_direta(numero_teste, texto_abertura)