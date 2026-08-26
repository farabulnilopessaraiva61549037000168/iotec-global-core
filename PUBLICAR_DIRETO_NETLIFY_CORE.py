import subprocess
import sqlite3
import datetime

class DirectNetlifyDeployEngine:
    def __init__(self):
        self.site_id = "tubular-monstera-5d8665"
        self.db_path = "iotec.db"

    def subir_producao_direta(self):
        print("==========================================================================================")
        print(" 🚀 DEPLOY DIRETO DE EMERGÊNCIA | FORÇANDO SOBREPOSIÇÃO NO NETLIFY                        ")
        print("==========================================================================================")

        try:
            # Comando oficial do Netlify CLI para enviar os arquivos da pasta atual direto para producao
            cmd = f"npx netlify-cli deploy --site {self.site_id} --dir . --prod --skip-functions-cache"
            print(f" [EXECUTANDO]: {cmd}\n")
            
            # Executa no terminal
            process = subprocess.run(cmd, shell=True, text=True)

            # Log de seguranca no banco local
            now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
                VALUES ('NETLIFY_DIRECT_CLI_OVERRIDE', 1, 1, ?)
            ''', (now_utc,))
            conn.commit()
            conn.close()

            print("\n==========================================================================================")
            print(" ✅ PROCESSO FINALIZADO!")
            print("==========================================================================================")

        except Exception as e:
            print(f" ❌ Erro ao publicar: {e}")

if __name__ == "__main__":
    engine = DirectNetlifyDeployEngine()
    engine.subir_producao_direta()
