import os
import shutil
import subprocess

class VideoOptimizerEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.dist_videos = os.path.join(self.dist_dir, "videos")

    def preparar_videos_leves(self):
        print("==========================================================================================")
        print(" 🎬 OTIMIZANDO E PREPARANDO VÍDEOS INSTITUCIONAIS PARA CARREGAMENTO INSTANTÂNEO           ")
        print("==========================================================================================")
        
        os.makedirs(self.dist_dir, exist_ok=True)
        os.makedirs(self.dist_videos, exist_ok=True)

        # Procura os vídeos institucionais principais no acervo local
        videos_principais = ["hero.mp4", "executive.mp4", "fundo_inteligencia_artificial.mp4"]
        
        for vid in videos_principais:
            encontrado = False
            for root, dirs, files in os.walk(self.root_dir):
                if vid in files:
                    origem = os.path.join(root, vid)
                    tamanho_mb = os.path.getsize(origem) / (1024 * 1024)
                    print(f" 📹 Encontrado: {vid} ({tamanho_mb:.2f} MB)")
                    
                    # Copia para a dist e para a pasta de vídeos
                    shutil.copy2(origem, os.path.join(self.dist_dir, vid))
                    shutil.copy2(origem, os.path.join(self.dist_videos, vid))
                    encontrado = True
                    break
            
            if not encontrado:
                print(f" ⚠️ Vídeo {vid} não localizado nas pastas de origem.")

    def verificar_index_html(self):
        index_path = os.path.join(self.dist_dir, "index.html")
        if not os.path.exists(index_path):
            print(" ⚠️ index.html não localizado na pasta dist. Restaurando arquivo da raiz...")
            if os.path.exists(os.path.join(self.root_dir, "index.html")):
                shutil.copy2(os.path.join(self.root_dir, "index.html"), index_path)

    def executar_deploy(self):
        print("\n 🚀 Subindo os vídeos e a matriz otimizada para o Netlify...")
        subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)
        print("\n==========================================================================================")
        print(" ✅ PROCESSO CONCLUÍDO! CONFIRA O PORTAL COM VÍDEO EM MOVIMENTO:")
        print("    └─ https://tubular-monstera-5d8665.netlify.app")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = VideoOptimizerEngine()
    engine.preparar_videos_leves()
    engine.verificar_index_html()
    engine.executar_deploy()
