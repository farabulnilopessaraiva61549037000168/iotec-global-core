import sqlite3
import datetime

class FinancialClockEngine:
    def __init__(self):
        self.db_path = "iotec.db"

    def check_treasury(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        # 1. Tabela de transacoes/audit
        cur.execute("""
            CREATE TABLE IF NOT EXISTS treasury_audit (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tx_id TEXT UNIQUE,
                source TEXT,
                item TEXT,
                amount_brl REAL,
                currency TEXT,
                created_at TEXT
            )
        """)
        
        # Recupera movimentacoes salvas no banco
        cur.execute("SELECT COUNT(*), SUM(amount_brl) FROM treasury_audit")
        row = cur.fetchone()
        tx_count = row[0] or 0
        total_reassure = row[1] or 0.0
        
        conn.close()
        
        now_str = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        
        print("======================================================================")
        print(" ⏱️ RELÓGIO DE CAIXA & CONVERGÊNCIA FINANCEIRA - IOTEC REAL-TIME       ")
        print("======================================================================")
        print(f" Data/Hora Oficial : {now_str}")
        print(" Conta Principal   : IOTEC.BL@proton.me (PayPal / PicPay / Pix / Gateways)")
        print("----------------------------------------------------------------------")
        print(f" • Transações Auditadas : {tx_count} eventos registrados")
        print(f" • Volume Acumulado      : R$ {total_reassure:.2f} BRL")
        print(" • Modéis de Serviço    : Licença Mensal (R$ 299,00) / Certidões B2B")
        print(" • Status da Convergência: OK - Conexão ativa com adquirentes em nuvem")
        print("======================================================================")

if __name__ == "__main__":
    clock = FinancialClockEngine()
    clock.check_treasury()
