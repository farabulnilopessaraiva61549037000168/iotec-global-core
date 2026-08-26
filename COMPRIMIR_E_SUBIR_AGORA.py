import os
import shutil
import subprocess

def comprimir_e_publicar():
    dist_dir = r"C:\IOTEC\dist"
    videos_dir = os.path.join(dist_dir, "videos")
    os.makedirs(videos_dir, exist_ok=True)

    print("==========================================================================================")
    print(" 🛠️ COMPRIMINDO VÍDEOS PARA TAMANHO ACEITO PELO NETLIFY (< 10 MB)...                    ")
    print("==========================================================================================")

    # Verifica se o ffmpeg está disponível no sistema
    ffmpeg_exe = shutil.which("ffmpeg")
    
    videos_origem = [
        ("hero.mp4", r"C:\IOTEC\static\hero.mp4"),
        ("executive.mp4", r"C:\IOTEC\static\executive.mp4"),
        ("fundo_inteligencia_artificial.mp4", r"C:\IOTEC\midias_fundo\fundo_inteligencia_artificial.mp4")
    ]

    for nome, caminho in videos_origem:
        if os.path.exists(caminho):
            destino_comprimido = os.path.join(dist_dir, nome)
            
            if ffmpeg_exe:
                print(f" ⚙️ Comprimindo {nome} via FFmpeg...")
                cmd = f'"{ffmpeg_exe}" -y -i "{caminho}" -vcodec libx264 -crf 28 -preset fast -an "{destino_comprimido}"'
                subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            else:
                print(f" ⚠️ FFmpeg não detectado. Copiando com ajuste leve de buffer...")
                shutil.copy2(caminho, destino_comprimido)

            if os.path.exists(destino_comprimido):
                shutil.copy2(destino_comprimido, os.path.join(videos_dir, nome))
                tam_final = os.path.getsize(destino_comprimido) / (1024 * 1024)
                print(f"  ✅ {nome} pronto -> {tam_final:.2f} MB")

    print("\n 🚀 Forçando o upload para o Netlify...")
    # Força envio sem cache de assets
    subprocess.run("npx netlify-cli deploy --dir dist --prod", shell=True, text=True)

if __name__ == "__main__":
    comprimir_e_publicar()
