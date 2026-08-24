import sqlite3
import datetime

class EngineRetiradas:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cnpj = "61.549.037/0001-68"
        self.salario_minimo = 1518.00  # Projeção de piso nacional
        self.parcela_emprestimo = 2800.00

    def processar_distribuicao(self, receita_bruta):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 💰  IOTEC AUTOMATED CASH ENGINE | MÓDULO DE DISTRIBUIÇÃO E RETIRADAS AUTOMÁTICAS        ")
        print("==========================================================================================")
        print(f" [TITULAR DO BENEFÍCIO : {self.owner}]")
        print(f" [CNPJ PAGADOR         : {self.cnpj}]")
        print(f" [PROCESSADO EM        : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. BALANÇO DE ENTRADAS DA CONTA PJ ] ──────────────────────────────────────────────")
        print(f"  • Receita Bruta Processada no Mês : R$ {receita_bruta:,.2f}")
        
        # Cobertura do Crédito
        saldo_pos_emprestimo = receita_bruta - self.parcela_emprestimo
        print(f"  • Dedução de Trava de Crédito PJ   : -R$ {self.parcela_emprestimo:,.2f} (Parcela do Empréstimo)")
        print(f"  • Saldo Operacional Líquido        : R$ {saldo_pos_emprestimo:,.2f}\n")

        # Divisão de Retiradas CPF
        if saldo_pos_emprestimo <= 0:
            print("  ⚠️ ALERTA: Receita insuficiente para iniciar a esteira de retiradas.")
            return

        pro_labore = min(self.salario_minimo, saldo_pos_emprestimo)
        lucro_isento = max(0, saldo_pos_emprestimo - pro_labore)

        print(" ─── [ 2. ROTEAMENTO DE TRANSFERÊNCIAS PARA O CPF ] ──────────────────────────────────────")
        print(f"  • Pró-Labore Fixo (DECORE / INSS)   : R$ {pro_labore:,.2f} (Transferência em Conta Corrente)")
        print(f"  • Dividendos Isentos (Lucro Limpo)  : R$ {lucro_isento:,.2f} (Isento de IRPF)")
        print(f"  👉 TOTAL RETIRADO PARA O CPF        : R$ {(pro_labore + lucro_isento):,.2f}")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = EngineRetiradas()
    # Simulação considerando 15 clientes High-Ticket (R$ 899/mês)
    faturamento_simulado = 15 * 899.00
    engine.processar_distribuicao(faturamento_simulado)
