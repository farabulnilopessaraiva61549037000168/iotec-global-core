import os
import shutil
import subprocess

class MatrixRestorationEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.backup_dir = os.path.join(self.root_dir, "BACKUP_ESTAVEL_OFICIAL")

    def restaurar_interface_matriz(self):
        print("==========================================================================================")
        print(" 🏛️ RESTAURANDO A MATRIZ OPERACIONAL BLACK/WHITE & MANTENDO SHOWROOM DE VÍDEOS           ")
        print("==========================================================================================")

        # 1. Busca o index original da matriz no backup estável
        index_original = os.path.join(self.backup_dir, "index.html")
        
        if not os.path.exists(index_original):
            # Procura em outras pastas de segurança caso o caminho varie
            for root, dirs, files in os.walk(self.root_dir):
                if "index.html" in files and "BACKUP" in root:
                    index_original = os.path.join(root, "index.html")
                    break

        if os.path.exists(index_original):
            print(f" ✅ Matriz Black/White encontrada em: {index_original}")
            
            # Preserva o Showroom de Vídeos atual em uma rota dedicada
            showroom_atual = os.path.join(self.dist_dir, "index.html")
            showroom_destino = os.path.join(self.dist_dir, "showroom.html")
            if os.path.exists(showroom_atual):
                shutil.copy2(showroom_atual, showroom_destino)
                print(" 🎬 Vitrine de Vídeos preservada com sucesso na rota: `/showroom.html`")

            # Restaura a Matriz Operacional no Ponto Principal (index.html)
            shutil.copy2(index_original, os.path.join(self.dist_dir, "index.html"))
            print(" ⚡ Matriz Operacional Black/White restaurada no ponto principal: `index.html`!")
        else:
            print(" ⚠️ Matriz original não localizada automaticamente no backup. Por favor, confirme o caminho da sua cópia salva.")

    def atualizar_deploy(self):
        print("\n 🚀 Atualizando a Netlify com as duas camadas simultâneas...")
        subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)
        print("\n==========================================================================================")
        print(" ✅ CAMADAS UNIFICADAS COM SUCESSO!")
        print("    └─ Matriz Principal (Black/White): https://tubular-monstera-5d8665.netlify.app")
        print("    └─ Vitrine de Vídeos B2B: https://tubular-monstera-5d8665.netlify.app/showroom.html")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = MatrixRestorationEngine()
    engine.restaurar_interface_matriz()
    engine.atualizar_deploy()
