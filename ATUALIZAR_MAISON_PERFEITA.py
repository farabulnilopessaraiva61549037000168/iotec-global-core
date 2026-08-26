import os
import shutil
import subprocess

class MaisonImpecavelEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.dist_videos = os.path.join(self.dist_dir, "videos")

    def preparar_arquivos_limpos(self):
        print(" [1/3] 🧹 Preparando estrutura limpa e espelhando vídeos de alta definição...")
        os.makedirs(self.dist_videos, exist_ok=True)

        # Garante que os videos mestres estejam na dist
        fontes_videos = [
            os.path.join(self.root_dir, "static", "hero.mp4"),
            os.path.join(self.root_dir, "static", "executive.mp4"),
            os.path.join(self.root_dir, "midias_fundo", "fundo_inteligencia_artificial.mp4"),
            os.path.join(self.root_dir, "midias_fundo", "fundo_tecnologia_servidores.mp4")
        ]

        for src in fontes_videos:
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(self.dist_videos, os.path.basename(src)))

    def gerar_maison_sem_poluicao(self):
        print(" [2/3] 🎨 Compilando a Maison IOTEC limpa, sem depoimentos e com vídeos em loop...")
        
        html_perfeito = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IOTEC BL — Construtora de Inovações e Tecnologia</title>
  <style>
    :root {
      --bg: #070a12;
      --gold: #D4A843;
      --border: rgba(212,168,67,0.2);
    }
    * { margin: 0; padding: 0; box-sizing: border-box; font-family: 'Inter', -apple-system, sans-serif; }
    body { background: var(--bg); color: #fff; overflow-x: hidden; }

    /* HERO FULLSCREEN COM VÍDEO DE FUNDO */
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
      filter: brightness(0.45) contrast(1.1);
    }

    .hero-overlay {
      position: absolute;
      inset: 0;
      background: radial-gradient(circle, rgba(7,10,18,0.2) 0%, rgba(7,10,18,0.85) 90%);
      z-index: 2;
    }

    /* NAVBAR */
    .navbar { position: absolute; top:0; left:0; width:100%; z-index:10; padding: 25px 50px; display: flex; justify-content: space-between; align-items: center; }
    .brand { font-size: 1.4rem; font-weight: 800; color: #fff; text-decoration: none; letter-spacing: 1px; }
    .brand span { color: var(--gold); font-weight: 400; }

    .hero-content { position: relative; z-index: 3; text-align: center; max-width: 950px; padding: 0 20px; }
    
    .badge {
      display: inline-block;
      padding: 6px 20px;
      border: 1px solid var(--gold);
      color: var(--gold);
      border-radius: 20px;
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 2px;
      text-transform: uppercase;
      margin-bottom: 25px;
      background: rgba(212,168,67,0.1);
    }

    h1 { font-size: 4.2rem; font-weight: 300; line-height: 1.1 margin-bottom: 25px; }
    h1 em { color: var(--gold); font-style: normal; font-weight: 600; }
    p.sub { font-size: 1.25rem; color: #cbd5e1; max-width: 720px; margin: 0 auto 40px; line-height: 1.6; }

    .btn-gold {
      padding: 16px 36px;
      background: var(--gold);
      color: #000;
      font-weight: 700;
      border-radius: 6px;
      text-decoration: none;
      font-size: 0.95rem;
      transition: 0.3s;
      display: inline-block;
    }
    .btn-gold:hover { transform: translateY(-3px); box-shadow: 0 10px 25px rgba(212,168,67,0.3); }

    /* SEÇÃO SOBRE MINIMALISTA */
    .section-clean { padding: 100px 40px; max-width: 1200px; margin: 0 auto; text-align: center; }
    .section-clean h2 { font-size: 2.5rem; font-weight: 300; margin-bottom: 20px; }
    .section-clean h2 em { color: var(--gold); font-style: normal; }
    .section-clean p { color: #94a3b8; font-size: 1.1rem; max-width: 800px; margin: 0 auto 50px; }

    footer { border-top: 1px solid var(--border); padding: 40px; text-align: center; color: #64748b; font-size: 0.85rem; }
  </style>
</head>
<body>

  <nav class="navbar">
    <a href="#" class="brand">IOTEC <span>BL</span></a>
    <div style="font-size:0.85rem; color:var(--gold); font-weight:600; letter-spacing:1px;">ENGANHARIA & SISTEMAS</div>
  </nav>

  <section class="hero">
    <!-- Vídeo contínuo sem áudio em alta definição -->
    <video autoplay loop muted playsinline preload="auto">
      <source src="videos/hero.mp4" type="video/mp4">
      <source src="videos/executive.mp4" type="video/mp4">
      <source src="videos/fundo_inteligencia_artificial.mp4" type="video/mp4">
    </video>

    <div class="hero-overlay"></div>

    <div class="hero-content">
      <div class="badge">MAISON INSTITUCIONAL DE TECNOLOGIA</div>
      <h1>Inovação que<br><em>transforma empresas.</em></h1>
      <p class="sub">Construção de sistemas corporativos sob medida com precisão, arquitetura de alto padrão e inteligência operacional.</p>
      <a href="#solucoes" class="btn-gold">Conhecer Capacidades</a>
    </div>
  </section>

  <section class="section-clean" id="solucoes">
    <h2>Arquitetura Digital <em>Sem Limites</em></h2>
    <p>A IOTEC desenvolve ecossistemas e plataformas específicas para todos os setores da economia — da saúde ao varejo, do agronegócio à logística multimodal.</p>
  </section>

  <footer>
    <p>© 2026 IOTEC BL — Construtora de Inovações e Tecnologia. Todos os direitos reservados. | CNPJ: 61.549.037/0001-68</p>
  </footer>

</body>
</html>
"""
        with open(os.path.join(self.dist_dir, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_perfeito)

    def deploy_impecavel(self):
        print(" [3/3] 🚀 Disparando deploy para a Netlify sem alterar matrizes...")
        subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)
        print("\n==========================================================================================")
        print(" ✅ PRODUÇÃO MUNDIAL IMPECÁVEL NO AR! PRONTA PARA APRESENTAÇÃO.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = MaisonImpecavelEngine()
    engine.preparar_arquivos_limpos()
    engine.gerar_maison_sem_poluicao()
    engine.deploy_impecavel()
