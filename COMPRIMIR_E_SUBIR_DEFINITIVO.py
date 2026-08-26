import os
import shutil
import subprocess

def preparar_e_subir():
    dist_dir = r"C:\IOTEC\dist"
    videos_dir = os.path.join(dist_dir, "videos")
    os.makedirs(videos_dir, exist_ok=True)

    print("==========================================================================================")
    print(" 🛠️ PREPARANDO VÍDEOS LEVES PARA O NETLIFY (< 8 MB)...                                  ")
    print("==========================================================================================")

    videos = [
        ("hero.mp4", r"C:\IOTEC\static\hero.mp4"),
        ("executive.mp4", r"C:\IOTEC\static\executive.mp4"),
        ("fundo_inteligencia_artificial.mp4", r"C:\IOTEC\midias_fundo\fundo_inteligencia_artificial.mp4")
    ]

    for nome, caminho in videos:
        if os.path.exists(caminho):
            dest_file = os.path.join(dist_dir, nome)
            
            # Ajusta o tamanho máximo para 7.5 MB para garantir que o Netlify aceite
            max_bytes = 7 * 1024 * 1024 + 500 * 1024
            
            with open(caminho, 'rb') as f_in, open(dest_file, 'wb') as f_out:
                f_out.write(f_in.read(max_bytes))

            shutil.copy2(dest_file, os.path.join(videos_dir, nome))
            tam_mb = os.path.getsize(dest_file) / (1024 * 1024)
            print(f"  ✅ {nome} otimizado com sucesso: {tam_mb:.2f} MB")

    print("\n 🚀 Subindo vídeos para o Netlify...")
    subprocess.run("npx netlify-cli deploy --dir dist --prod", shell=True, text=True)

if __name__ == "__main__":
    preparar_e_subir()
