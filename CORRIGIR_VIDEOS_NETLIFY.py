import os
import shutil
import subprocess

class NetlifyVideoFixer:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.dist_videos = os.path.join(self.dist_dir, "videos")

    def reestruturar_assets(self):
        print(" [1/3] 🔍 Mapeando e forçando cópia dos vídeos para a pasta de distribuição `dist/videos`...")
        os.makedirs(self.dist_videos, exist_ok=True)

        # Copia todos os MP4s encontrados no projeto para a dist
        videos_copiados = 0
        for root, dirs, files in os.walk(self.root_dir):
            if "dist" in root or "node_modules" in root or ".git" in root:
                continue
            for f in files:
                if f.lower().endswith(".mp4"):
                    src_path = os.path.join(root, f)
                    dest_path = os.path.join(self.dist_videos, f)
                    try:
                        shutil.copy2(src_path, dest_path)
                        videos_copiados += 1
                        print(f"  ✅ Vídeo acoplado na CDN Netlify: {f}")
                    except Exception:
                        pass
        print(f" Total de {videos_copiados} arquivos de vídeo empacotados.")

    def gerar_html_com_trava_autoplay(self):
        print(" [2/3] 🛠️ Injetando tags de vídeo com suporte total a Autoplay e Fallback...")
        
        html_code = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IOTEC — Showroom Institucional & Mídia</title>
  <style>
    * { margin:0; padding:0; box-sizing:border-box; }
    body { background: #070a12; color: #fff; font-family: system-ui, -apple-system, sans-serif; overflow-x: hidden; }

    /* BACKGROUND VIDEO CONTAINER */
    .hero { position: relative; width: 100vw; height: 100vh; display: flex; align-items: center; justify-content: center; overflow: hidden; }
    
    .hero video {
      position: absolute;
      top: 50%;
      left: 50%;
      min-width: 100%;
      min-height: 100%;
      width: auto;
      height: auto;
      z-index: 1;
      transform: translate(-50%, -50%);
      object-fit: cover;
    }

    .hero-overlay {
      position: absolute;
      inset: 0;
      background: rgba(7, 10, 18, 0.65);
      z-index: 2;
    }

    .hero-content {
      position: relative;
      z-index: 3;
      text-align: center;
      max-width: 900px;
      padding: 20px;
    }

    .badge {
      display: inline-block;
      padding: 6px 16px;
      border: 1px solid #D4A843;
      color: #D4A843;
      border-radius: 20px;
      font-size: 0.8rem;
      letter-spacing: 2px;
      margin-bottom: 20px;
      background: rgba(212,168,67,0.1);
    }

    h1 { font-size: 3.5rem; font-weight: 300; margin-bottom: 20px; }
    h1 em { color: #D4A843; font-style: normal; font-weight: 600; }
    p { font-size: 1.2rem; color: #94a3b8; }
  </style>
</head>
<body>

  <section class="hero">
    <!-- Player com regramento rigoroso para Autoplay do Navegador -->
    <video autoplay loop muted playsinline preload="auto">
      <source src="videos/hero.mp4" type="video/mp4">
      <source src="videos/fundo.mp4" type="video/mp4">
      <source src="videos/executive.mp4" type="video/mp4">
    </video>
    
    <div class="hero-overlay"></div>

    <div class="hero-content">
      <div class="badge">IOTEC GLOBAL SHOWROOM</div>
      <h1>Tecnologia Corporativa e <em>Capacidade Multimodal.</em></h1>
      <p>Acompanhe nossas operações em tempo real através da nossa vitrine institucional de alta definição.</p>
    </div>
  </section>

  <script>
    // Script de segurança para forçar o início do vídeo caso o navegador bloqueie o autoplay inicial
    document.addEventListener('DOMContentLoaded', () => {
      const v = document.querySelector('video');
      if (v) {
        v.muted = true;
        v.play().catch(() => {
          console.log("Autoplay bloqueado pelo navegador. Aguardando interação do usuário.");
        });
      }
    });
  </script>
</body>
</html>
"""
        with open(os.path.join(self.dist_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_code)
        print("  ✅ `index.html` reescrito com script de forçar Autoplay e fallback de mídias.")

    def deploy(self):
        print(" [3/3] 🚀 Enviando atualização estática completa para a Netlify...")
        subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)

if __name__ == "__main__":
    fixer = NetlifyVideoFixer()
    fixer.reestruturar_assets()
    fixer.gerar_html_com_trava_autoplay()
    fixer.deploy()
