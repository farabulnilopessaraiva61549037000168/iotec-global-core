import sqlite3
import datetime

class DossieCreditoBradesco:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cnpj = "61.549.037/0001-68"
        self.target_mrr = 127678.57
        self.leads_total = 2155

    def print_credit_proposal(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🏦  IOTEC × BRADESCO PJ | PROPOSTA DE ESTRUTURAÇÃO DE CRÉDITO & DOMICÍLIO BANCÁRIO        ")
        print("==========================================================================================")
        print(f" [PROPRIETÁRIO : {self.owner}]")
        print(f" [CNPJ         : {self.cnpj}]")
        print(f" [DATA EMISSÃO : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. CONTRAPARTIDA INSTITUCIONAL (O QUE O BRADESCO RECEBE) ] ─────────────────────────")
        print("  • Domicílio Bancário Exclusivo para liquidação de boletos e faturamento da IOTEC.")
        print("  • Processamento do fluxo de caixa previsto de até R$ 127.678,57 / mês.")
        print("  • Fidelização de conta corporativa de Tecnologia com Custo Fixo R$ 0,00 e Margem 100%.\n")

        print(" ─── [ 2. SOLICITAÇÃO DE CRÉDITO ESTRUTURADO (O QUE A IOTEC SOLICITA) ] ────────────────────")
        print("  • Linha de Capital de Giro / Pronampe / FGI PEAC para aceleração de aquisição.")
        print("  • Limite de Antecipação Automática de Recebíveis sobre os Contratos High-Ticket (R$ 899).")
        print("  • Conta Garantida para liquidez operacional do ecossistema.\n")

        print(" ─── [ 3. GARANTIA OPERACIONAL E ATIVO EM CUSTÓDIA ] ───────────────────────────────────────")
        print(f"  • Base Ativa de Dados  : {self.leads_total:,} CNPJs B2B qualificados no iotec.db".replace(",", "."))
        print("  • Código-Fonte Core    : Registrado e hospedado em repositório seguro GitHub / Render.")
        print("==========================================================================================")
        print(" 🌐 DOCUMENTO DE SOLICITAÇÃO DE CRÉDITO PRONTO PARA REUNIÃO BANCÁRIA.")
        print("==========================================================================================")

if __name__ == "__main__":
    credit = DossieCreditoBradesco()
    credit.print_credit_proposal()
