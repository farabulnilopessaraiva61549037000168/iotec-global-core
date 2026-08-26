import os
import re
import subprocess

class MatrixVideoEnhancer:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.dist_index = os.path.join(self.dist_dir, "index.html")

    def injetar_player_e_estilos(self):
        print("==========================================================================================")
        print(" 📽️ INJETANDO SEQUÊNCIA DE VÍDEOS INSTITUCIONAIS NA MATRIZ OPERACIONAL                    ")
        print("==========================================================================================")

        if not os.path.exists(self.dist_index):
            print(" ⚠️ index.html não encontrado na pasta dist.")
            return

        with open(self.dist_index, "r", encoding="utf-8") as f:
            html = f.read()

        # CSS para tornar o fundo dinâmico sem quebrar elementos existentes
        css_inject = """
  <!-- ESTILOS VÍDEO DE FUNDO INSTITUCIONAL IOTEC -->
  <style>
    .iotec-bg-video {
      position: fixed;
      top: 50%;
      left: 50%;
      min-width: 100%;
      min-height: 100%;
      width: auto;
      height: auto;
      z-index: -2;
      transform: translate(-50%, -50%);
      object-fit: cover;
      filter: brightness(0.30) contrast(1.15);
      pointer-events: none;
    }
    .iotec-bg-overlay {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle, rgba(7,10,18,0.4) 0%, rgba(7,10,18,0.88) 90%);
      z-index: -1;
      pointer-events: none;
    }
    body {
      background: #070a12 !important;
      color: #ffffff !important;
    }
  </style>
"""

        # HTML do player de vídeo com regras estritas de autoplay
        player_html = """
  <!-- PLAYER VÍDEO INSTITUCIONAL DE FUNDO -->
  <video class="iotec-bg-video" autoplay loop muted playsinline preload="auto">
    <source src="videos/hero.mp4" type="video/mp4">
    <source src="hero.mp4" type="video/mp4">
    <source src="videos/executive.mp4" type="video/mp4">
    <source src="executive.mp4" type="video/mp4">
    <source src="videos/fundo_inteligencia_artificial.mp4" type="video/mp4">
  </video>
  <div class="iotec-bg-overlay"></div>
"""

        # Injeta CSS antes do </head>
        if "</head>" in html and "iotec-bg-video" not in html:
            html = html.replace("</head>", f"{css_inject}\n</head>")

        # Injeta Player de Vídeo logo após o <body>
        if "<body" in html and "iotec-bg-video" not in html:
            # Encontra onde fecha a tag <body ...>
            html = re.sub(r'(<body[^>]*>)', r'\1\n' + player_html, html, count=1)

        with open(self.dist_index, "w", encoding="utf-8") as f:
            f.write(html)

        print(" ✅ Sequência de vídeos e camadas visuais de alta definição aplicadas com sucesso no `index.html`!")

    def publicar_netlify(self):
        print("\n 🚀 Enviando a versão operacional turbinada com vídeos para a Netlify...")
        subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)
        print("\n==========================================================================================")
        print(" ✅ PORTAL OPERACIONAL DE ALTO PADRÃO COM VÍDEOS INSTITUCIONAIS NO AR!")
        print("    └─ Acesse: https://tubular-monstera-5d8665.netlify.app")
        print("==========================================================================================")

if __name__ == "__main__":
    enhancer = MatrixVideoEnhancer()
    enhancer.injetar_player_e_estilos()
    enhancer.publicar_netlify()
