import os
import subprocess

def corrigir_fundo():
    dist_dir = r"C:\IOTEC\dist"
    os.makedirs(dist_dir, exist_ok=True)

    print("==========================================================================================")
    print(" 🛠️ APLICANDO FUNDO TECNOLÓGICO DINÂMICO 3D (DESEMPENHO MÁXIMO & ZERO BLOQUEIOS)        ")
    print("==========================================================================================")

    html_perfeito = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>IOTEC BL — Construtora de Inovações & Tecnologias</title>
  <style>
    :root {
      --bg: #050811;
      --card-bg: rgba(10, 16, 30, 0.75);
      --gold: #D4A843;
      --border: rgba(212, 168, 67, 0.3);
    }
    * { margin:0; padding:0; box-sizing:border-box; font-family: 'Inter', system-ui, -apple-system, sans-serif; }
    body { background: var(--bg); color: #fff; overflow-x: hidden; min-height: 100vh; position: relative; }

    /* CANVAS 3D/BG ANIMADO DE ALTA TECNOLOGIA */
    #bg-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      z-index: -2;
      pointer-events: none;
    }

    .bg-overlay {
      position: fixed;
      inset: 0;
      background: radial-gradient(circle at center, rgba(5,8,17,0.2) 0%, rgba(5,8,17,0.85) 90%);
      z-index: -1;
      pointer-events: none;
    }

    header {
      padding: 25px 50px;
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
      padding: 80px 20px 30px;
      max-width: 1000px;
      margin: 0 auto;
    }
    .hero-body h1 { font-size: 3.8rem; font-weight: 300; line-height: 1.15; margin-bottom: 20px; text-shadow: 0 0 30px rgba(0,0,0,0.8); }
    .hero-body h1 em { color: var(--gold); font-style: normal; font-weight: 600; }
    .hero-body p { font-size: 1.2rem; color: #cbd5e1; max-width: 750px; margin: 0 auto; line-height: 1.6; }

    .products-container {
      max-width: 1300px;
      margin: 0 auto 60px;
      padding: 0 20px;
    }
    .grid-3 {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(330px, 1fr));
      gap: 30px;
      margin-top: 40px;
    }

    .card {
      background: var(--card-bg);
      border: 1px solid var(--border);
      border-radius: 12px;
      padding: 35px;
      backdrop-filter: blur(20px);
      transition: all 0.3s ease;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    .card:hover {
      border-color: var(--gold);
      transform: translateY(-8px);
      box-shadow: 0 15px 35px rgba(212, 168, 67, 0.2);
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
      padding: 30px;
      text-align: center;
      color: #64748b;
      font-size: 0.85rem;
      backdrop-filter: blur(10px);
    }
  </style>
</head>
<body>

  <!-- BACKGROUND DINÂMICO REDE NEURAL & REDE DE SERVIDORES -->
  <canvas id="bg-canvas"></canvas>
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
    // ENGINE VISUAL DE FUNDO 60FPS
    const canvas = document.getElementById('bg-canvas');
    const ctx = canvas.getContext('2d');

    let width, height, particles;

    function init() {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
      particles = [];
      const particleCount = Math.floor((width * height) / 12000);

      for (let i = 0; i < particleCount; i++) {
        particles.push({
          x: Math.random() * width,
          y: Math.random() * height,
          vx: (Math.random() - 0.5) * 0.8,
          vy: (Math.random() - 0.5) * 0.8,
          radius: Math.random() * 2 + 1,
          alpha: Math.random() * 0.5 + 0.2
        });
      }
    }

    function animate() {
      ctx.clearRect(0, 0, width, height);

      for (let i = 0; i < particles.length; i++) {
        let p = particles[i];
        p.x += p.vx;
        p.y += p.vy;

        if (p.x < 0 || p.x > width) p.vx *= -1;
        if (p.y < 0 || p.y > height) p.vy *= -1;

        ctx.beginPath();
        ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(212, 168, 67, ${p.alpha})`;
        ctx.fill();

        for (let j = i + 1; j < particles.length; j++) {
          let p2 = particles[j];
          let dx = p.x - p2.x;
          let dy = p.y - p2.y;
          let dist = Math.sqrt(dx * dx + dy * dy);

          if (dist < 120) {
            ctx.beginPath();
            ctx.moveTo(p.x, p.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.strokeStyle = `rgba(212, 168, 67, ${0.25 * (1 - dist / 120)})`;
            ctx.lineWidth = 0.6;
            ctx.stroke();
          }
        }
      }

      requestAnimationFrame(animate);
    }

    window.addEventListener('resize', init);
    init();
    animate();
  </script>

</body>
</html>
"""

    with open(os.path.join(dist_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_perfeito)

    print(" ✅ Fundo dinâmico compilado com sucesso sem dependência de MP4 travado!")
    print("\n 🚀 Enviando para o Netlify...")
    subprocess.run("npx netlify-cli deploy --dir dist --prod --skip-functions-cache", shell=True, text=True)

if __name__ == "__main__":
    corrigir_fundo()
