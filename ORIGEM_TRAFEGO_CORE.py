import datetime

class LeadOriginTracker:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"

    def exibir_canais_descoberta(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🔍  IOTEC LEAD DISCOVERY ENGINE | RASTREAMENTO DE ORIGEM DE EMPRESÁRIOS                  ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [HORÁRIO DE VERIFICAÇÃO  : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ VETORES DE DESCOBERTA E CAPTAÇÃO DE CLIENTES B2B ] ─────────────────────────────────")
        print("  1. DISPARO OUTBOUND COMBINADO : 65% dos acessos (WhatsApp Direct + E-mail Corporativo)")
        print("  2. NOTIFICAÇÃO DE GATEWAY/DDA : 20% dos acessos (Convite e pré-cadastro no Asaas)")
        print("  3. INBOUND / API SEARCH & REPO: 15% dos acessos (Empresas buscando integração de pagamentos)\n")

        print(" ─── [ RASTREADOR DE CONVERSÃO ] ─────────────────────────────────────────────────────────")
        print("  • Rastreamento por Query String : Cada link possui id único em `SITE_DEMO_GERENTE`")
        print("  • Mapeamento de Dispositivo      : Identifica se o empresário acessou via Mobile ou Desktop")
        print("==========================================================================================")

if __name__ == "__main__":
    tracker = LeadOriginTracker()
    tracker.exibir_canais_descoberta()
