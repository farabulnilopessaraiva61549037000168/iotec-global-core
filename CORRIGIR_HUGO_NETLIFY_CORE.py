import subprocess
import sqlite3
import datetime

class FixHugoConfigEngine:
    def __init__(self):
        self.toml_file = "netlify.toml"
        self.db_path = "iotec.db"

    def corrigir_e_publicar(self):
        print("==========================================================================================")
        print(" 🛠️ DESATIVANDO COMANDO HUGO NO NETLIFY.TOML E FORÇANDO DEPLOY                            ")
        print("==========================================================================================")

        # Sobrescreve o netlify.toml anulando explicitamente o build command
        toml_content = """[build]
  command = ""
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "no-cache, no-store, must-revalidate"
    Pragma = "no-cache"
    Expires = "0"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200
  force = true
"""
        with open(self.toml_file, "w", encoding="utf-8") as f:
            f.write(toml_content)

        print("  ✅ Arquivo `netlify.toml` atualizado (command = '').")

        # Dispara o deploy com a flag --build=false para pular o script do Hugo da interface do Netlify
        cmd = "npx netlify-cli deploy --prod --skip-functions-cache"
        print(f" [EXECUTANDO]: {cmd}\n")
        
        process = subprocess.run(cmd, shell=True, text=True)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_HUGO_COMMAND_DISABLED', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" ✅ PROCESSO CONCLUÍDO!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = FixHugoConfigEngine()
    engine.corrigir_e_publicar()
