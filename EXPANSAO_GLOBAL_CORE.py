import datetime

class GlobalExpansionEngine:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"

    def exibir_matriz_internacional(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🌐  IOTEC GLOBAL CORE | MATRIZ DE EXPANSÃO CÉU, TERRA E AR                               ")
        print("==========================================================================================")
        print(f" [STAMP DE EXECUÇÃO  : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ MERCADOS PRONTOS PARA ENGAJAMENTO DE RECEITA ] ───────────────────────────────────")
        print("  🇺🇸 ESTADOS UNIDOS  | Moeda: USD | Ticket: $ 199.00 / mês | Gateway: Remessa Swift Direct")
        print("  🇪🇺 UNIÃO EUROPEIA  | Moeda: EUR | Ticket: € 180.00 / mês | Gateway: SEPA / Remessa Online")
        print("  🇺🇾 URUGUAI / CHILE | Moeda: USD | Ticket: $ 299.00 / mês | Gateway: Cross-Border LatAm\n")

        print(" ─── [ ESTRUTURA DE CAPTAÇÃO CÉU, TERRA E AR ] ─────────────────────────────────────────")
        print("  • Camada AR    : Contratos SaaS internacionais com cobrança recorrente em dólar.")
        print("  • Camada TERRA : Integrações B2B locais que usam a IOTEC como ponte no Brasil.")
        print("  • Camada CÉU   : Licenciamento de código e APIs executadas na nuvem global.\n")

        print("==========================================================================================")
        print(" 🚀 CAMADA GLOBAL PRONTA PARA ENTRADA DE RECURSOS EM DÓLAR E EURO.")
        print("==========================================================================================")

if __name__ == "__main__":
    expansion = GlobalExpansionEngine()
    expansion.exibir_matriz_internacional()
