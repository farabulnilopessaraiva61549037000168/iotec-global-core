import sqlite3
import datetime

class NetlifyFixBuildEngine:
    def __init__(self):
        self.toml_file = "netlify.toml"
        self.db_path = "iotec.db"

    def corrigir_toml(self):
        print(" [NETLIFY FIX] 🛠️ Ajustando netlify.toml para garantir build com sucesso...")

        # Configuracao direta e limpa para evitar erro de comando no Linux do Netlify
        toml_content = """[build]
  publish = "."

[[headers]]
  for = "/*"
  [headers.values]
    Cache-Control = "no-cache, no-store, must-revalidate"
    Pragma = "no-cache"
    Expires = "0"
"""
        with open(self.toml_file, "w", encoding="utf-8") as f:
            f.write(toml_content)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_TOML_BUILD_FIXED', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("  ✅ Arquivo `netlify.toml` simplificado.")
        print("  ✅ Status registrado no `iotec.db`.")

if __name__ == "__main__":
    engine = NetlifyFixBuildEngine()
    engine.corrigir_toml()
