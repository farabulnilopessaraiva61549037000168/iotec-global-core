import os
import shutil
import sqlite3
import datetime

class BackupSystemEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.backup_dir = os.path.join(self.root_dir, "BACKUP_ESTAVEL_OFICIAL")
        self.db_path = os.path.join(self.root_dir, "iotec.db")

    def executar_backup(self):
        print("==========================================================================================")
        print(" 🔒 INICIANDO PROCEDIMENTO DE BACKUP COMPLETO E ISOLAMENTO DE VERSÃO ESTÁVEL               ")
        print("==========================================================================================")

        # 1. Limpa e cria diretório de backup
        if os.path.exists(self.backup_dir):
            shutil.rmtree(self.backup_dir)
        os.makedirs(self.backup_dir, exist_ok=True)

        # 2. Copia os arquivos mestres que compõem a versão perfeita do portal
        arquivos_mestres = [
            "index.html",
            "netlify.toml",
            "_headers",
            "_redirects",
            "RESTAURAR_PORTAL_COMPLETO.py"
        ]

        for arq in arquivos_mestres:
            origem = os.path.join(self.root_dir, arq)
            if os.path.exists(origem):
                shutil.copy2(origem, os.path.join(self.backup_dir, f"ORIGINAL_{arq}"))
                print(f"  -> Arquivo protegido e salvo em backup: ORIGINAL_{arq}")

        # 3. Cria snapshot das pastas dist e static/assets
        for pasta in ["dist", "assets", "static"]:
            origem = os.path.join(self.root_dir, pasta)
            if os.path.exists(origem):
                shutil.copytree(origem, os.path.join(self.backup_dir, pasta), dirs_exist_ok=True)
                print(f"  -> Pasta de estilo/dist isolada em backup: {pasta}")

        # 4. Registra no banco iotec.db o ponto de restauração
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('SNAPSHOT_ESTAVEL_GERADO', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" ✅ BACKUP CONCLUÍDO COM SUCESSO!")
        print(f" 📂 Todos os arquivos mestres foram isolados na pasta: {self.backup_dir}")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = BackupSystemEngine()
    engine.executar_backup()
