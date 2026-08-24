import sqlite3
import datetime

class CrossBorderTicketing:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cnpj = "61.549.037/0001-68"
        self.target_mrr_brl = 127678.57
        self.usd_rate = 5.50

    def calculate_multicurrency_matrix(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🌎  IOTEC GLOBAL CORE | MATRIZ DE TICKETING NACIONAL E INTERNACIONAL (MULTIMOEDA)       ")
        print("==========================================================================================")
        print(f" [TITULAR DA OPERAÇÃO : {self.owner}]")
        print(f" [CNPJ INSTITUCIONAL   : {self.cnpj}]")
        print(f" [DATA DE MATURAÇÃO    : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. MATRIZ DE CONVERSÃO COMBINADA (BR / INT) ] ────────────────────────────────────")
        ticket_usd = 1000.00
        ticket_brl_converted = ticket_usd * self.usd_rate
        needed_usd_clients = int(self.target_mrr_brl / ticket_brl_converted) + 1

        print(f"  • Contrato Padrão Internacional : US$ {ticket_usd:,.2f} / mês (~R$ {ticket_brl_converted:,.2f} BRL)")
        print(f"  • Clientes Exigidos (100% USD)  : Apenas {needed_usd_clients} contratos internacionais batem a meta.")
        print(f"  • Impacto no Valuation          : Múltiplo ARR sobe de 7.0x para 10.0x em dólares.\n")

        print(" ─── [ 2. EQUAÇÃO DE MIX DE RECEITA RECOMENDADA ] ────────────────────────────────────────")
        print("  • 100 Contratos Standard BR (R$ 299/mês)   = R$ 29.900,00")
        print("  • 30 Contratos Corporate BR (R$ 899/mês)   = R$ 26.970,00")
        print("  • 12 Contratos Enterprise USD (US$ 1,100)  = R$ 72.600,00")
        print(f"  👉 TOTAL COMBINADO : R$ 129.470,00 / mês (Meta de R$ 127.6k Superada!)")
        print("==========================================================================================")

if __name__ == "__main__":
    cb = CrossBorderTicketing()
    cb.calculate_multicurrency_matrix()
