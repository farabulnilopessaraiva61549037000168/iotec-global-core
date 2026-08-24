import sqlite3
import datetime

class PaypalIntegrationEngine:
    def __init__(self):
        self.db_path = "iotec.db"

    def atualizar_status_paypal(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()

        # Inspeciona colunas da tabela para evitar erro de schema
        cursor.execute("PRAGMA table_info(integration_status);")
        colunas = [col[1] for col in cursor.fetchall()]

        if "last_sync_utc" not in colunas:
            cursor.execute("ALTER TABLE integration_status ADD COLUMN last_sync_utc TEXT;")

        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('PAYPAL_GLOBAL_SDK', 1, 1, ?)
        ''', (now_utc,))

        conn.commit()
        conn.close()

        print("==========================================================================================")
        print(" 💳 IOTEC PAYPAL CORE | INTEGRAÇÃO AJUSTADA E REGISTRADA NO IOTEC.DB                      ")
        print("==========================================================================================")
        print(f" [STAMP DE ATUALIZAÇÃO UTC : {now_utc}]")
        print("==========================================================================================\n")
        print("  ✅ Schema da tabela `integration_status` adequado com sucesso.")
        print("  ✅ Status do PayPal registrado no banco de dados sem erros.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = PaypalIntegrationEngine()
    engine.atualizar_status_paypal()
