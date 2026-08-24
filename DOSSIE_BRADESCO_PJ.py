import sqlite3
import datetime
import os

class DossieBradescoPJ:
    def __init__(self):
        self.db_path = "iotec.db"
        self.owner_name = "Farabulini Lopes Saraiva"
        self.cnpj = "61.549.037/0001-68"
        self.target_mrr = 127678.57
        self.valuation_usd = 1950000.00
        self.valuation_brl = self.valuation_usd * 5.50

    def generate_executive_summary(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM leads")
        total_leads = cur.fetchone()[0]
        conn.close()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🏛️  IOTEC & BRADESCO PJ | DOSSIÊ EXECUTIVO DE ESTRUTURAÇÃO PATRIMONIAL                   ")
        print("==========================================================================================")
        print(f" [TITULAR DA OPERAÇÃO : {self.owner_name.upper()}]                                     ")
        print(f" [CNPJ INSTITUCIONAL   : {self.cnpj}]                                                   ")
        print(f" [EMISSÃO E GOVERNANÇA : {now}] | [CANAL DIRECT: IOTEC.BL@proton.me]                   ")
        print("==========================================================================================\n")

        print(" ─── [ 1. RESUMO EXECUTIVO E MÉTRICAS FINANCEIRAS ] ────────────────────────────────────────")
        print(f"  • Valuation Alvo (Modelo 7.0x ARR) : US$ {self.valuation_usd:,.2f} (~R$ {self.valuation_brl:,.2f} BRL)")
        print(f"  • Capacidade de Receita Recorrente : R$ {self.target_mrr:,.2f} / mês")
        print(f"  • Custos Operacionais Fixos        : R$ 0,00 / mês (Infraestrutura Nuvem Marginal Zero)")
        print(f"  • Margem Bruta de Operação          : 100% Líquida\n")

        print(" ─── [ 2. ATIVO DE DADOS E COBERTURA DE MERCADO ] ────────────────────────────────────────")
        print(f"  • Carteira de CNPJs em Custódia    : {total_leads:,} Empresas Mapeadas no iotec.db".replace(",", "."))
        print("  • Perfil dos Alvos B2B             : Construção Civil, Energia, Indústria e Logística")
        print("  • Modelo de Monetização            : Assinaturas B2B (R$ 299/mês Standard | R$ 899/mês Corporate)\n")

        print(" ─── [ 3. OPORTUNIDADES DE PARCERIA COM O BANCO ] ─────────────────────────────────────────")
        print("  • Abertura de Conta Domicílio Bancário com Tração de Receita Recorrente (PJ)")
        print("  • Antecipação de Recebíveis dos Contratos B2B de R$ 899/mês")
        print("  • Linhas de Crédito Garantidas pelo Valuation do Acervo Digital de Software")
        print("==========================================================================================")
        print(" 🌐 DOCUMENTO DE GOVERNANÇA PRONTO PARA APRESENTAÇÃO A GERÊNCIA CORPORATIVA.")
        print("==========================================================================================")

if __name__ == "__main__":
    dossie = DossieBradescoPJ()
    dossie.generate_executive_summary()
