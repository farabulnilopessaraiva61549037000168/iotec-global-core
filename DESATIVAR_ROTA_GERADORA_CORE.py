import sqlite3
import datetime

class DisableLegacyRoutesEngine:
    def __init__(self):
        self.redirects_file = "_redirects"
        self.db_path = "iotec.db"

    def aplicar_redirecionamento_forcado(self):
        print(" [REDIRECT CORE] 🛑 Criando regra de redirecionamento para anular rotas antigas...")

        # Força qualquer requisição de página ou arquivo estático a apontar exclusivamente para o index.html travado
        redirect_rules = """/*    /index.html   200!
"""
        with open(self.redirects_file, "w", encoding="utf-8") as f:
            f.write(redirect_rules)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_REDIRECTS_LOCK_ALL', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("  ✅ Arquivo `_redirects` gerado com regra de sobreposição `/* -> /index.html 200!`.")

if __name__ == "__main__":
    engine = DisableLegacyRoutesEngine()
    engine.aplicar_redirecionamento_forcado()
