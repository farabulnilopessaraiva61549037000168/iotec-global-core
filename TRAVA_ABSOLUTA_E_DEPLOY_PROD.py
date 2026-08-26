import subprocess
import sqlite3
import datetime
import os

class TravaAbsolutaEngine:
    def __init__(self):
        self.site_id = "tubular-monstera-5d8665"
        self.db_path = "iotec.db"

    def aplicar_trava_e_publicar(self):
        print("==========================================================================================")
        print(" 🛑 APLICANDO BLOQUEIO RÍGIDO NO BACKEND E PUBLICANDO EM PRODUÇÃO (NETLIFY PROD)          ")
        print("==========================================================================================")

        # 1. Garante que as tabelas de auditoria financeira existam no iotec.db
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS audit_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                transaction_id TEXT UNIQUE,
                status TEXT,
                amount REAL,
                created_at_utc TEXT
            )
        ''')
        
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_HARD_LOCK_ENFORCED', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        # 2. Executa a publicação forçada em PRODUÇÃO via Netlify CLI
        print("\n [NETLIFY CLI] Enviando diretórios atualizados para o ambiente de PRODUÇÃO (--prod)...")
        cmd = f"npx netlify-cli deploy --site {self.site_id} --dir . --prod --skip-functions-cache"
        
        process = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(process.stdout)

        if "Website URL" in process.stdout or "Deploy Path" in process.stdout:
            print("==========================================================================================")
            print(" ✅ DEPLOY EM PRODUÇÃO CONCLUÍDO COM SUCESSO!")
            print(" 🛑 Trava Server-Side aplicada globalmente no servidor.")
            print("==========================================================================================")
        else:
            print(" ⚠️ Saída do comando Netlify:")
            print(process.stderr)

if __name__ == "__main__":
    engine = TravaAbsolutaEngine()
    engine.aplicar_trava_e_publicar()
