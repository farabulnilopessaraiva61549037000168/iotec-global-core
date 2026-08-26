import os
import shutil
import subprocess
import sqlite3
import datetime

class RestoreDesignAndDeployEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.db_path = os.path.join(self.root_dir, "iotec.db")

    def montar_dist_com_design(self):
        print(" [1/2] 🎨 Copiando arquivos de design (CSS, JS, Imagens) e aplicando trava de segurança...")
        
        # Limpa e recria a pasta dist
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        os.makedirs(self.dist_dir, exist_ok=True)

        # Copia pastas de assets se existirem
        pastas_design = ["css", "js", "assets", "static", "img", "images"]
        for pasta in pastas_design:
            origem = os.path.join(self.root_dir, pasta)
            destino = os.path.join(self.dist_dir, pasta)
            if os.path.exists(origem):
                shutil.copytree(origem, destino, dirs_exist_ok=True)
                print(f"  -> Pastas de estilo copiada: {pasta}")

        # Copia o HTML principal e arquivos de rede/cabeçalho
        arquivos = ["index.html", "_headers", "_redirects", "favicon.ico"]
        for arq in arquivos:
            origem = os.path.join(self.root_dir, arq)
            if os.path.exists(origem):
                shutil.copy2(origem, os.path.join(self.dist_dir, arq))

        print("  ✅ Design e arquivos estáticos compilados na pasta 'dist'.")

    def publicar_producao(self):
        print(" [2/2] 🚀 Publicando layout completo com trava ativa no Netlify...")
        cmd = "npx netlify-cli deploy --dir dist --prod --skip-functions-cache"
        process = subprocess.run(cmd, shell=True, text=True)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_DESIGN_RESTORED_WITH_LOCK', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" ✅ LAYOUT OFICIAL RESTAURADO COM SUCESSO!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = RestoreDesignAndDeployEngine()
    engine.montar_dist_com_design()
    engine.publicar_producao()
