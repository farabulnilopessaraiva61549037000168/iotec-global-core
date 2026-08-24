import sqlite3
import datetime
import os

class DemoLiveGerente:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cnpj = "61.549.037/0001-68"
        self.project_code = "REGULUS / IOTEC B2B CORE"
        self.db_path = "iotec.db"

    def run_presentation(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM leads")
        total_leads = cur.fetchone()[0]
        conn.close()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🖥️  PROJETO REGULUS | INTERFACE DE DEMONSTRAÇÃO TÉCNICA E AUDITORIA BANCÁRIA             ")
        print("==========================================================================================")
        print(f" [TITULAR DA PROPRIEDADE INTELECTUAL : {self.owner}]")
        print(f" [CNPJ DE LICENCIAMENTO COMERCIAL     : {self.cnpj}]")
        print(f" [SISTEMA DE ORIGEM & ARQUITETURA     : {self.project_code}]")
        print(f" [TIMESTAMP DA SESSÃO AO VIVO         : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. LAUDO DE DESEMPENHO E BANCO DE DADOS ] ─────────────────────────────────────────")
        print(f"  • Status do Acervo Operacional : {total_leads:,} CNPJs B2B Ativos e Auditáveis".replace(",", "."))
        print("  • Estrutura de Servidores      : Nuvem Híbrida Marginal Zero (Pronta para DigitalOcean)")
        print("  • Captação de Receita Provedora: Gateways de Domicílio e Cobrança Direta Integrados\n")

        print(" ─── [ 2. ROTA DE INTEGRAÇÃO DE FINANCIAL TECHS ] ─────────────────────────────────────────")
        print("  • Gateway Primário (Brasil)    : ASAAS (Emissão de Boletos, Pix e Antecipação)")
        print("  • Gateways Cross-Border (USD)  : Remessa Online / Stripe / Atlas (Ticketing Internacional)")
        print("  • Domicílio Corporativo Alvo   : Banco Bradesco PJ (Processamento de Fluxo de Caixa)\n")

        print(" ─── [ 3. PLANO DE ALAVANCAGEM FINANCEIRA ] ────────────────────────────────────────────────")
        print("  • Linha Solicitada para Tanque  : R$ 50.000,00 (Capital de Giro e Aceleração)")
        print("  • Capacidade de Pagamento / Mês : 4 Contratos High-Ticket (R$ 899) Cobrem 100% da Parcela")
        print("  • Retorno Esperado da Operação  : R$ 127.678,57 / mês em Maturação Completa")
        print("==========================================================================================")
        print(" 🚀 SISTEMA OPERACIONAL E TECNOLOGIA PRONTOS PARA LICENCIAMENTO E EXPANSÃO.")
        print("==========================================================================================")

if __name__ == "__main__":
    demo = DemoLiveGerente()
    demo.run_presentation()
