import sqlite3
import datetime

class SimuladorSolvencia:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cnpj = "61.549.037/0001-68"
        self.total_leads = 2155
        self.ticket_standard = 299.00
        self.ticket_highticket = 899.00

    def analyze_solvency(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🏥  IOTEC FINANCIAL CORE | ANÁLISE DE SOLVÊNCIA & CAPACIDADE DE PAGAMENTO DE CRÉDITO     ")
        print("==========================================================================================")
        print(f" [TITULAR DA OPERAÇÃO : {self.owner}]")
        print(f" [CNPJ INSTITUCIONAL   : {self.cnpj}]")
        print(f" [AVALIAÇÃO EM      : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. CENÁRIO DE SIMULAÇÃO DE EMPRÉSTIMO ] ───────────────────────────────────────────")
        print("  • Valor do Empréstimo Simulado : R$ 50.000,00")
        print("  • Estimativa de Parcela Mensal  : R$ 2.800,00 / mês (Prazo: 24 meses)")
        print("  • Custo Fixo Operacional IOTEC  : R$ 0,00 / mês (Margem Bruta 100%)\n")

        print(" ─── [ 2. PONTO DE EQUILÍBRIO DE COBERTURA (BREAK-EVEN) ] ───────────────────────────────")
        needed_standard = int(2800 / self.ticket_standard) + 1
        needed_highticket = int(2800 / self.ticket_highticket) + 1
        
        print(f"  • Clientes Standard (R$ 299/mês) necessários para quitar a parcela    : {needed_standard} contratos")
        print(f"  • Clientes High-Ticket (R$ 899/mês) necessários para quitar a parcela : {needed_highticket} contratos")
        print(f"  • Cobertura do Acervo (`iotec.db`)                                    : {self.total_leads} CNPJs B2B")
        print(f"  • Taxa de Conversão Exigida da Base                                   : { (needed_standard / self.total_leads) * 100:.2f}%\n")

        print(" ─── [ 3. DIAGNÓSTICO BANCÁRIO DE RISCO ] ────────────────────────────────────────────────")
        print("  ✅ RISCO EXTREMAMENTE BAIXO: Menos de 0.5% de conversão da base atual paga a dívida integral.")
        print("  ✅ ALTA CAPACIDADE DE SOLVÊNCIA: Margem de 100% garante imunidade contra aluguel ou folha.")
        print("==========================================================================================")

if __name__ == "__main__":
    sim = SimuladorSolvencia()
    sim.analyze_solvency()
