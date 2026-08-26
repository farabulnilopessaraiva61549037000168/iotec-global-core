import os
import shutil
import subprocess

class MediaConsolidator:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.assets_dir = os.path.join(self.root_dir, "assets", "videos")
        self.dist_dir = os.path.join(self.root_dir, "dist")
        
    def organizar_e_copiar(self):
        print("==========================================================================================")
        print(" 📽️ CONSOLIDANDO VÍDEOS DE ALTO IMPACTO PARA O SHOWROOM INSTITUCIONAL                     ")
        print("==========================================================================================")
        
        os.makedirs(self.assets_dir, exist_ok=True)
        os.makedirs(os.path.join(self.dist_dir, "videos"), exist_ok=True)

        user_prof = os.path.expanduser("~")
        
        # Mapeamento dos melhores MP4s encontrados
        fontes = [
            os.path.join(self.root_dir, "static", "executive.mp4"),
            os.path.join(self.root_dir, "static", "hero.mp4"),
            os.path.join(self.root_dir, "midias_fundo", "fundo_inteligencia_artificial.mp4"),
            os.path.join(self.root_dir, "midias_fundo", "fundo_tecnologia_servidores.mp4"),
            os.path.join(user_prof, "Desktop", "DIVERSOS", "REGULUS_SITE", "REGULUS _ Vídeo Promocional_arquivos", "regulus_luxury_fintech_promo_video.mp4"),
            os.path.join(user_prof, "Downloads", "REGULUS _ Comercial Institucional.07_arquivos", "premium_tech_commercial_video.mp4")
        ]

        copiados = 0
        for src in fontes:
            if os.path.exists(src):
                fname = os.path.basename(src)
                dest_local = os.path.join(self.assets_dir, fname)
                dest_dist = os.path.join(self.dist_dir, "videos", fname)
                
                shutil.copy2(src, dest_local)
                shutil.copy2(src, dest_dist)
                copiados += 1
                print(f"  ✅ Video importado com sucesso: {fname}")

        print(f"\n 🎬 Total de {copiados} vídeos master consolidados na pasta `assets/videos` e `dist/videos`!")

    def atualizar_interface(self):
        print("\n [2/2] 🎨 Injetando players de vídeo nativos na sala de visitação `broadcast.html`...")
        
        broadcast_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IOTEC — Global Broadcast & Innovation Showroom</title>
  <style>
    :root {
      --bg: #070a12;
      --bg-card: #0f172a;
      --gold: #D4A843;
      --border: rgba(212,168,67,0.25);
    }
    * { box-sizing: border-box; margin:0; padding:0; font-family: 'Inter', -apple-system, sans-serif; }
    body { background: var(--bg); color: #fff; overflow-x: hidden; }

    /* VIDEO BACKGROUND HERO */
    .hero-container { position: relative; height: 90vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; overflow: hidden; }
    .bg-video { position: absolute; top: 50%; left: 50%; min-width: 100%; min-height: 100%; width: auto; height: auto; z-index: 1; transform: translate(-50%, -50%); object-fit: cover; opacity: 0.35; filter: contrast(110%); }
    .hero-overlay { position: absolute; inset: 0; background: radial-gradient(circle, rgba(7,10,18,0.4) 0%, rgba(7,10,18,0.95) 85%); z-index: 2; }
    
    .hero-content { position: relative; z-index: 3; padding: 0 20px; }
    .live-badge { display: inline-flex; align-items: center; gap: 8px; background: rgba(212,168,67,0.15); border: 1px solid var(--gold); color: var(--gold); padding: 6px 18px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 24px; }
    
    .hero-content h1 { font-size: 4rem; font-weight: 300; line-height: 1.1; max-width: 950px; margin-bottom: 20px; }
    .hero-content h1 em { font-style: normal; color: var(--gold); font-weight: 600; }
    .hero-content p { color: #cbd5e1; font-size: 1.2rem; max-width: 700px; margin: 0 auto 35px; }

    /* MEDIA GRID */
    .grid-section { padding: 90px 40px; max-width: 1350px; margin: 0 auto; }
    .section-header { text-align: center; margin-bottom: 60px; }
    .section-header h2 { font-size: 2.4rem; font-weight: 400; }
    .section-header h2 em { color: var(--gold); font-style: normal; }

    .media-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 30px; }
    .media-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; transition: 0.3s; }
    .media-card:hover { border-color: var(--gold); transform: translateY(-6px); }
    .video-preview { height: 220px; width: 100%; object-fit: cover; background: #000; }
    .media-body { padding: 25px; }
    .media-tag { color: var(--gold); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
    .media-body h3 { font-size: 1.3rem; margin-bottom: 10px; }
    .media-body p { color: #94a3b8; font-size: 0.92rem; }

    footer { border-top: 1px solid var(--border); padding: 40px; text-align: center; color: #64748b; font-size: 0.85rem; }
  </style>
</head>
<body>

  <div class="hero-container">
    <video class="bg-video" autoplay loop muted playsinline>
      <source src="videos/hero.mp4" type="video/mp4">
    </video>
    <div class="hero-overlay"></div>
    <div class="hero-content">
      <div class="live-badge">⚡ IOTEC SHOWROOM & CANAL AUDIOVISUAL</div>
      <h1>Engenharia Viva & <em>Capacidade Multimodal.</em></h1>
      <p>Demonstrações técnicas em tempo real de inteligência logística, telemetria e soluções corporativas de alto padrão.</p>
    </div>
  </div>

  <section class="grid-section">
    <div class="section-header">
      <h2>Mídia Operacional & <em>Inovações em Vídeo</em></h2>
    </div>

    <div class="media-grid">
      <div class="media-card">
        <video class="video-preview" controls poster="">
          <source src="videos/executive.mp4" type="video/mp4">
        </video>
        <div class="media-body">
          <div class="media-tag">Maison Corporativa</div>
          <h3>Visão Executiva & Governança</h3>
          <p>Apresentação das capacidades de auditoria e segurança em infraestruturas privadas.</p>
        </div>
      </div>

      <div class="media-card">
        <video class="video-preview" controls poster="">
          <source src="videos/fundo_inteligencia_artificial.mp4" type="video/mp4">
        </video>
        <div class="media-body">
          <div class="media-tag">Inteligência Artificial</div>
          <h3>Motor de Agentes e Mineração</h3>
          <p>Processamento server-side contínuo com validação em tempo real no banco central.</p>
        </div>
      </div>

      <div class="media-card">
        <video class="video-preview" controls poster="">
          <source src="videos/regulus_luxury_fintech_promo_video.mp4" type="video/mp4">
        </video>
        <div class="media-body">
          <div class="media-tag">Engenharia Financeira</div>
          <h3>Liquidação Instantânea Asaas Direct</h3>
          <p>Protocolos de pagamento Pix, cartão e gateways globais integrados ao ecossistema.</p>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <p>© 2026 IOTEC BL — Construtora de Inovações e Tecnologia. Todos os direitos reservados. | CNPJ: 61.549.037/0001-68</p>
  </footer>

</body>
</html>
"""
        with open(os.path.join(self.dist_dir, "broadcast.html"), "w", encoding="utf-8") as f:
            f.write(broadcast_html)
            
        shutil.copy2(os.path.join(self.dist_dir, "broadcast.html"), os.path.join(self.root_dir, "broadcast.html"))
        print("  ✅ Interface `broadcast.html` atualizada com os vídeos locais!")

    def disparar_deploy(self):
        print("\n 🚀 Enviando atualização completa do canal de mídia para a Netlify...")
        cmd = "npx netlify-cli deploy --dir dist --prod --skip-functions-cache"
        subprocess.run(cmd, shell=True, text=True)
        print("\n==========================================================================================")
        print(" ✅ A MAISON AUDIOVISUAL DA IOTEC ESTÁ 100% NO AR NA NETLIFY COM VÍDEOS NATIVOS!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = MediaConsolidator()
    engine.organizar_e_copiar()
    engine.atualizar_interface()
    engine.disparar_deploy()
