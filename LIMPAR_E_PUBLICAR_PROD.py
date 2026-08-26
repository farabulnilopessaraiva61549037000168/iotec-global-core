import os
import shutil
import subprocess
import sqlite3
import datetime

class CleanAndDeployEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.toml_file = os.path.join(self.root_dir, "netlify.toml")
        self.db_path = os.path.join(self.root_dir, "iotec.db")

    def sanitizar_nomes(self):
        print(" [1/3] 🧹 Sanitizando nomes de arquivos locais com caracteres inválidos (# e ?)...")
        cont = 0
        for root, dirs, files in os.walk(self.root_dir):
            # Ignora a pasta .git
            if ".git" in root:
                continue
            for file in files:
                if "#" in file or "?" in file:
                    old_path = os.path.join(root, file)
                    new_filename = file.replace("#", "_num_").replace("?", "")
                    new_path = os.path.join(root, new_filename)
                    os.rename(old_path, new_path)
                    print(f"  -> Renomeado: {file} -> {new_filename}")
                    cont += 1
        print(f"  ✅ {cont} arquivo(s) sanitizado(s).")

    def preparar_dist(self):
        print(" [2/3] 📦 Preparando diretório isolado 'dist' para publicação limpa...")
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        os.makedirs(self.dist_dir, exist_ok=True)

        # Arquivos essenciais do site estático
        arquivos_essenciais = ["index.html", "_headers", "_redirects"]
        for item in arquivos_essenciais:
            orig = os.path.join(self.root_dir, item)
            if os.path.exists(orig):
                shutil.copy2(orig, os.path.join(self.dist_dir, item))

        # Atualiza netlify.toml para publicar 'dist'
        toml_content = """[build]
  command = ""
  publish = "dist"

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
        print("  ✅ Pasta 'dist' criada e 'netlify.toml' atualizado.")

    def disparar_deploy(self):
        print(" [3/3] 🚀 Disparando Netlify CLI para produção...")
        cmd = "npx netlify-cli deploy --dir dist --prod --skip-functions-cache"
        print(f" [EXECUTANDO]: {cmd}\n")
        
        process = subprocess.run(cmd, shell=True, text=True)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_DIST_CLEAN_DEPLOY', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" ✅ PROCESSO FINALIZADO!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = CleanAndDeployEngine()
    engine.sanitizar_nomes()
    engine.preparar_dist()
    engine.disparar_deploy()
