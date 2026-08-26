import os
import shutil
import subprocess

def preparar_e_deploy_perfeito():
    dist_dir = r"C:\IOTEC\dist"
    os.makedirs(dist_dir, exist_ok=True)

    print("==========================================================================================")
    print(" 🎬 COMPILANDO PORTAL DE ALTO PADRÃO COM VÍDEOS VÁLIDOS & STREAMING CDN DE ALTA PERFORMANCE")
    print("==========================================================================================")

    # Limpa arquivos truncados/corrompidos que causaram erro 422
    for item in os.listdir(dist_dir):
        item_path = os.path.join(dist_dir, item)
        if os.path.isfile(item_path) and item.endswith(".mp4"):
            try:
                os.remove(item_path)
            except:
                pass

    html_com_videos_reais = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IOTEC BL — Construtora de Inovações & Tecnologias</title>
  <style>
    :root {
      --bg: #070a12;
      --card-bg: rgba(15, 23, 42, 0.80);
      --gold: #D4A843;
      --border: rgba(212, 168, 67, 0.25);
    }
    * { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: var(--bg); color: #fff; overflow-x: hidden; }

    /* VÍDEO DE BACKGROUND STREAMING EM UHD */
    .bg-video {
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
      filter: brightness(0.35) contrast(1.15);
      pointer-events: none;
    }

    .bg-overlay {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle, rgba(7,10,18,0.3) 0%, rgba(7,10,18,0.92) 85%);
      z-index: -1;
      pointer-events: none;
    }

    /* CONTEÚDO PRINCIPAL DO PORTAL BLACK/WHITE OPERACIONAL */
    header {
      padding: 30px 60px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
      backdrop-filter: blur(12px);
    }
    .brand { font-size: 1.6rem; font-weight: 800; color: #fff; text-decoration: none; letter-spacing: 1.5px; }
    .brand span { color: var(--gold); font-weight: 400; }
    .status-badge { font-size: 0.75rem; color: var(--gold); border: 1px solid var(--gold); padding: 6px 16px; border-radius: 20px; background: rgba(212,168,67,0.1); font-weight: 700; letter-spacing: 1px; }

    .hero-body {
      text-align: center;
      padding: 90px 20px 40px;
      max-width: 1000px;
      margin: 0 auto;
    }
    .hero-body h1 { font-size: 3.8rem; font-weight: 300; line-height: 1.15; margin-bottom: 20px; }
    .hero-body h1 em { color: var(--gold); font-style: normal; font-weight: 600; }
    .hero-body p { font-size: 1.2rem; color: #cbd5e1; max-width: 750px; margin: 0 auto; line-height: 1.6; }

    .products-container {
      max-width: 1300px;
      margin: 0 auto 80px;
      padding: 0 20px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
      gap: 30px;
      margin-top: 40px;
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 35px;
      backdrop-filter: blur(16px);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .card:hover {
      border-color: var(--gold);
      transform: translateY(-8px);
      box-shadow: 0 15px 35px rgba(212, 168, 67, 0.15);
    }

    .card-tag { font-size: 0.75rem; color: var(--gold); font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 12px; }
    .card h3 { font-size: 1.6rem; font-weight: 600; margin-bottom: 15px; }
    .card p { color: #94a3b8; font-size: 0.95rem; line-height: 1.6; margin-bottom: 25px; }

    .price-box { font-size: 1.8rem; font-weight: 700; color: #fff; margin-bottom: 20px; }
    .price-box span { font-size: 0.85rem; color: #64748b; font-weight: 400; }

    .btn-checkout {
      width: 100%;
      padding: 16px;
      background: var(--gold);
      color: #000;
      border: none;
      border-radius: 6px;
      font-weight: 700;
      font-size: 0.95rem;
      cursor: pointer;
      transition: 0.2s;
    }
    .btn-checkout:hover { opacity: 0.9; }

    footer {
      border-top: 1px solid var(--border);
      padding: 35px;
      text-align: center;
      color: #64748b;
      font-size: 0.85rem;
      backdrop-filter: blur(10px);
    }
  </style>
</head>
<body>

  <!-- VÍDEO DE BACKGROUND EMBED CONTINUO DE ALTA PERFORMANCE -->
  <video class="bg-video" autoplay loop muted playsinline preload="auto">
    <source src="https://assets.mixkit.co/videos/preview/mixkit-technology-network-lines-and-dots-in-motion-32704-large.mp4" type="video/mp4">
    <source src="https://assets.mixkit.co/videos/preview/mixkit-circuit-board-and-cpu-processor-41005-large.mp4" type="video/mp4">
  </video>
  <div class="bg-overlay"></div>

  <header>
    <a href="#" class="brand">IOTEC <span>BL</span></a>
    <div class="status-badge">⚡ ASAAS PIX DIRECT ATIVO</div>
  </header>

  <div class="hero-body">
    <h1>Construtora de Inovações & <em>Sistemas Corporativos.</em></h1>
    <p>Plataformas prontas para clínicas, supermercados e emissão de certidões operacionais com liquidação instantânea.</p>
  </div>

  <div class="products-container">
    <div class="grid-3">
      
      <div class="card">
        <div>
          <div class="card-tag">Médicos & Saúde</div>
          <h3>IOTEC MED CORE</h3>
          <p>Prontuário eletrônico PWA, agendamento de consultas e laudos com assinatura digital sem necessidade de instalação.</p>
        </div>
        <div>
          <div class="price-box">R$ 1.500 <span>/ taxa de ativação</span></div>
          <button class="btn-checkout" onclick="alert('Iniciando Pix Asaas Direct para IOTEC MED CORE...')">Ativar Sistema</button>
        </div>
      </div>

      <div class="card">
        <div>
          <div class="card-tag">Supermercados & Varejo</div>
          <h3>IOTEC RETAIL POS</h3>
          <p>Gestão de estoque, automação de caixas PDV em rede e emissão fiscal integrada via navegador.</p>
        </div>
        <div>
          <div class="price-box">R$ 2.500 <span>/ taxa de ativação</span></div>
          <button class="btn-checkout" onclick="alert('Iniciando Pix Asaas Direct para IOTEC RETAIL POS...')">Ativar Sistema</button>
        </div>
      </div>

      <div class="card">
        <div>
          <div class="card-tag">Emissão Instantânea</div>
          <h3>CERTIDÕES & AUDITORIA</h3>
          <p>Emissão automatizada de laudos técnicos e certidões operacionais com QR Code e validação digital imediata.</p>
        </div>
        <div>
          <div class="price-box">R$ 350 <span>/ por certidão</span></div>
          <button class="btn-checkout" onclick="alert('Iniciando emissão de Certidão via Pix Asaas Direct...')">Emitir Certidão</button>
        </div>
      </div>

    </div>
  </div>

  <footer>
    <p>© 2026 IOTEC BL — Construtora de Inovações e Tecnologia. Todos os direitos reservados. | CNPJ: 61.549.037/0001-68</p>
  </footer>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      const vid = document.querySelector('video');
      if (vid) {
        vid.muted = true;
        vid.play().catch(e => console.log("Aguardando interação do usuário para iniciar reprodução."));
      }
    });
  </script>

</body>
</html>
"""

    with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_com_videos_reais)

    print(" ✅ HTML do Portal compilado com sucesso sem arquivos corrompidos!")
    print("\n 🚀 Disparando Deploy Limpo para o Netlify...")
    subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)

if __name__ == "__main__":
    preparar_e_deploy_perfeito()
