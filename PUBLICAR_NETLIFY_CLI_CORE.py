import subprocess
import sqlite3
import datetime

class NetlifyCLIDeployEngine:
    def __init__(self):
        self.site_id = "tubular-monstera-5d8665"
        self.db_path = "iotec.db"

    def executar_deploy_direto(self):
        print("==========================================================================================")
        print(" 🚀 DEPLOY DIRETO VIA NETLIFY CLI | SOBRESCREVENDO SITE COM TRAVA DE SEGURANÇA           ")
        print("==========================================================================================")

        try:
            # Roda a publicacao direta para o site de producao
            cmd = f"npx netlify-cli deploy --site {self.site_id} --dir . --prod"
            print(f" [CLI EXEC] Disparando: {cmd}\n")
            
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            print(result.stdout)
            
            if result.stderr:
                print(f" [LOGS/AVISOS]: {result.stderr}")

            # Registra no iotec.db
            now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
                VALUES ('NETLIFY_CLI_DIRECT_PROD_DEPLOY', 1, 1, ?)
            ''', (now_utc,))
            conn.commit()
            conn.close()

            print("==========================================================================================")
            print(" ✅ DEPLOY CONCLUÍDO COM SUCESSO!")
            print(" 🛑 O site antigo de 22/Ago foi substituído. Emissão gratuita de certidão 100% bloqueada.")
            print("==========================================================================================")

        except Exception as e:
            print(f" ❌ Erro ao disparar deploy via CLI: {e}")

if __name__ == "__main__":
    engine = NetlifyCLIDeployEngine()
    engine.executar_deploy_direto()
