import os

class VideoArcheologist:
    def __init__(self):
        self.user_profile = os.path.expanduser("~")
        self.root_dir = r"C:\IOTEC"
        self.video_exts = ('.mp4', '.mov', '.avi', '.mkv', '.webm', '.m4v')

    def buscar_todos_os_videos(self):
        print("==========================================================================================")
        print(" 📽️ INICIANDO BUSCA PROFUNDA DE VÍDEOS EM TODOS OS NÚCLEOS E PASTAS INTERNAS             ")
        print("==========================================================================================")

        pastas_alvo = [
            self.root_dir,
            os.path.join(self.user_profile, "Downloads"),
            os.path.join(self.user_profile, "Desktop"),
            os.path.join(self.user_profile, "Videos"),
            os.path.join(self.user_profile, "Documents")
        ]

        videos_encontrados = []

        for pasta in pastas_alvo:
            if not os.path.exists(pasta):
                continue
            print(f" 🔍 Varendo diretório: {pasta}...")
            for root, dirs, files in os.walk(pasta):
                # Ignora pastas de ambiente virtual pesadas
                if "node_modules" in root or ".git" in root or "venv" in root:
                    continue
                for f in files:
                    if f.lower().endswith(self.video_exts):
                        caminho_completo = os.path.join(root, f)
                        try:
                            tamanho_mb = os.path.getsize(caminho_completo) / (1024 * 1024)
                            videos_encontrados.append((f, round(tamanho_mb, 2), caminho_completo))
                        except Exception:
                            pass

        print("\n==========================================================================================")
        print(f" 🎬 TOTAL DE VÍDEOS LOCALIZADOS NO SISTEMA: {len(videos_encontrados)}")
        print("==========================================================================================\n")

        if videos_encontrados:
            for nome, tam, local in videos_encontrados:
                print(f" 📹 [{tam} MB] {nome}")
                print(f"    └─ Caminho: {local}\n")
        else:
            print(" ⚠️ Nenhum arquivo de vídeo nativo (.mp4, .mov, etc.) foi encontrado nessas pastas.")

        print("==========================================================================================")

if __name__ == "__main__":
    archeologist = VideoArcheologist()
    archeologist.buscar_todos_os_videos()
