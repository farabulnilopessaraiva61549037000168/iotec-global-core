import sqlite3
import datetime

class BrainiacValuationTarget:
    def __init__(self):
        self.db_path = "iotec.db"
        self.target_valuation_usd = 1950000.00
        self.usd_brl_rate = 5.50
        self.target_valuation_brl = self.target_valuation_usd * self.usd_brl_rate
        self.multiple = 7.0

    def calculate_targets(self):
        arr_target = self.target_valuation_brl / self.multiple
        mrr_target = arr_target / 12.0
        clients_base_tier = mrr_target / 299.00
        clients_pro_tier = mrr_target / 899.00
        
        print("======================================================================")
        print(" 🧠 BRAINIAC CORE LEVEL 12 | INJEÇÃO DE FÓRMULA DE VALUATION TETO     ")
        print("======================================================================")
        print(f" [VALUATION TETO DÓLAR]  : US$ {self.target_valuation_usd:,.2f}")
        print(f" [VALUATION TETO BRL]    : R$  {self.target_valuation_brl:,.2f}")
        print(f" [MÚLTIPLO DE MERCADO]   : {self.multiple}x ARR")
        print("----------------------------------------------------------------------")
        print(f" 📊 ARR NECESSÁRIO        : R$  {arr_target:,.2f} / ano")
        print(f" 📊 MRR META MENSAL       : R$  {mrr_target:,.2f} / mês")
        print("----------------------------------------------------------------------")
        print(" 🎯 METAS DE BASE ATIVA (EQUAÇÃO DE VOLUME):")
        print(f"    • Plano Standard (R$ 299,00) : {int(clients_base_tier) + 1} clientes ativos")
        print(f"    • Plano High-Ticket (R$ 899,00): {int(clients_pro_tier) + 1} clientes ativos")
        print("======================================================================")

if __name__ == "__main__":
    brainiac = BrainiacValuationTarget()
    brainiac.calculate_targets()
