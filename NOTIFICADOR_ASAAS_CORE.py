import datetime
import sqlite3

class AsaasInstantNotifier:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"

    def registrar_e_notificar_pagamento(self, cliente, valor, produto, forma_pagamento="PIX"):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print("\n==========================================================================================")
        print(" 🔔  ALERT: NOVO PAGAMENTO CONFIRMADO E LIQUIDADO NO ASAAS                                 ")
        print("==========================================================================================")
        print(f" [DATA E HORA EXATA : {now}]")
        print(f" [CLIENTE / COMPRADOR: {cliente}]")
        print(f" [PRODUTO / LICENÇA  : {produto}]")
        print(f" [VALOR LIQUIDADO    : R$ {valor:,.2f}]")
        print(f" [FORMA DE RECEBIMENTO: {forma_pagamento}]")
        print(f" [STATUS DA CONTA PJ : SALDO DISPONÍVEL NA CONTA ASAAS]")
        print("==========================================================================================\n")

if __name__ == "__main__":
    notifier = AsaasInstantNotifier()
    # Simulação de disparo de notificação do Webhook
    notifier.registrar_e_notificar_pagamento(
        cliente="NEXUS DEEP TECH SYSTEMS",
        valor=899.00,
        produto="Licenciamento IOTEC High-Ticket (UTI)"
    )
