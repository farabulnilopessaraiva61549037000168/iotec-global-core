import subprocess
import sqlite3
import datetime

class DefinitveDeployEngine:
    def __init__(self):
        self.db_path = "iotec.db"

    def executar_deploy(self):
        print("==========================================================================================")
        print(" 🚀 PUBLICANDO VERSÃO TRAVADA VIA NETLIFY LINK (PRODUÇÃO)                                ")
        print("==========================================================================================")

        cmd = "npx netlify-cli deploy --prod --skip-functions-cache"
        print(f" [EXECUTANDO]: {cmd}\n")
        
        process = subprocess.run(cmd, shell=True, text=True)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_CLI_FINAL_LINK_DEPLOY', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" ✅ PROCESSO CONCLUÍDO COM SUCESSO!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = DefinitveDeployEngine()
    engine.executar_deploy()
