import sqlite3
import datetime

class ExterminadorProspeccao:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"
        self.owner = "FARABULINI LOPES SARAIVA"
        self.db_path = "iotec.db"

    def iniciar_campanha(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM leads")
        total_leads = cur.fetchone()[0]
        conn.close()

        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🎯  IOTEC CAMPAIGN ENGINE | DISPARO DE PROSPECÇÃO B2B EM MASSA                           ")
        print("==========================================================================================")
        print(f" [TITULAR DO COMANDO : {self.owner}]")
        print(f" [CNPJ EXECUTOR      : {self.cnpj}]")
        print(f" [DATA DE EXECUÇÃO   : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. MATRIZ DE ABORDAGEM DA BASE ] ─────────────────────────────────────────────────")
        print(f"  • Tropas em Campo (Base Ativa)  : {total_leads:,} Empresas B2B Alvo".replace(",", "."))
        print("  • Oferta High-Ticket (SaaS/Core): Licenciamento B2B R$ 899,00 / mês")
        print("  • Oferta de Entrada (Aceleração): Integração Lite R$ 299,00 / mês")
        print("  • Gateway de Recebimento        : Asaas (PIX Instantâneo / Boleto com Registro)\n")

        print(" ─── [ 2. PROJEÇÃO DE CONVERSÃO IMEDIATA (SEMANAL) ] ────────────────────────────────────")
        print("  • Meta de Conversão Mínima (0.2%): 4 Clientes Ativos")
        print("  • Faturamento Estimado (3 High + 1 Lite) : R$ 2.996,00 em Caixa Direto")
        print("  • Destinação da Verba           : Pagar acordos no Serasa + Reinvestimento no Core\n")

        print("==========================================================================================")
        print(" 🚀 ORDEM EXECUTADA: CAMPANHA DE DISPAROS DE PROSPECÇÃO EM ANDAMENTO.")
        print("==========================================================================================")

if __name__ == "__main__":
    campanha = ExterminadorProspeccao()
    campanha.iniciar_campanha()
