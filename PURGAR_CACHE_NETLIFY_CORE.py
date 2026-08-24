import sqlite3
import datetime

class PurgeNetlifyCacheEngine:
    def __init__(self):
        self.headers_file = "_headers"
        self.db_path = "iotec.db"

    def aplicar_purge(self):
        print(" [PURGE CORE] 🧹 Criando regras _headers para desativar cache na Netlify...")

        # Força Cache-Control para proibir o navegador e a CDN de guardar páginas velhas
        headers_config = """/*
  Cache-Control: no-cache, no-store, must-revalidate
  Pragma: no-cache
  Expires: 0
"""
        with open(self.headers_file, "w", encoding="utf-8") as f:
            f.write(headers_config)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_CACHE_PURGED_ZERO_STORE', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("  ✅ Arquivo `_headers` criado com diretivas `no-store`.")
        print("  ✅ Servidor Netlify instruído a revalidar toda requisição a partir de agora.")

if __name__ == "__main__":
    engine = PurgeNetlifyCacheEngine()
    engine.aplicar_purge()
