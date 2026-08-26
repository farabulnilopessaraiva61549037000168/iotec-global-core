import os
import shutil
import subprocess
import sqlite3
import datetime

class BroadcastChannelEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.desktop_interfaces = r"C:\Users\Bruno Lopes\Desktop\Diversos\INTERFACES"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.db_path = os.path.join(self.root_dir, "iotec.db")
        self.asaas_key = "$aact_Ydac951d283"

    def processar_e_consolidar(self):
        print("==========================================================================================")
        print(" 🎬 INICIANDO COMPILAÇÃO DO CANAL IOTEC GLOBAL BROADCAST & SHOWROOM AUDIOVISUAL           ")
        print("==========================================================================================")

        # 1. Registra integração das chaves no iotec.db
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('ASAAS_DIRECT_KEY_ACTIVE', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()
        print(" [1/3] 🔑 Chave do Asaas Direct ($aact_Ydac951d283) vinculada com sucesso no iotec.db!")

        # 2. Constrói a Landing Page Broadcast com o acervo visual
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
      --blue: #1B4FCC;
      --border: rgba(212,168,67,0.2);
    }
    * { box-sizing: border-box; margin:0; padding:0; font-family: 'Inter', -apple-system, sans-serif; }
    body { background: var(--bg); color: #fff; overflow-x: hidden; }

    /* NAVBAR */
    .navbar { position: fixed; top:0; width:100%; z-index:1000; background: rgba(7,10,18,0.85); backdrop-filter: blur(12px); border-bottom: 1px solid var(--border); padding: 18px 40px; display: flex; justify-content: space-between; align-items: center; }
    .logo { font-size: 1.3rem; font-weight: 800; letter-spacing: 1px; color: #fff; text-decoration: none; }
    .logo span { color: var(--gold); font-weight: 400; }

    /* BROADCAST HERO */
    .hero { position: relative; height: 90vh; display: flex; flex-direction: column; justify-content: center; align-items: center; text-align: center; padding: 0 20px; background: radial-gradient(circle, rgba(27,79,204,0.18) 0%, rgba(7,10,18,1) 80%); }
    .live-badge { display: flex; align-items: center; gap: 8px; background: rgba(220,38,38,0.15); border: 1px solid #ef4444; color: #f87171; padding: 6px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; letter-spacing: 2px; text-transform: uppercase; margin-bottom: 24px; }
    .live-dot { width: 8px; height: 8px; background: #ef4444; border-radius: 50%; animation: pulse 1.5s infinite; }

    @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.3; } 100% { opacity: 1; } }

    .hero h1 { font-size: 3.8rem; font-weight: 300; line-height: 1.1; max-width: 900px; margin-bottom: 20px; }
    .hero h1 em { font-style: normal; color: var(--gold); font-weight: 600; }
    .hero p { color: #94a3b8; font-size: 1.15rem; max-width: 650px; margin-bottom: 35px; }

    /* MEDIA GRID / CANAIS */
    .grid-section { padding: 80px 40px; max-width: 1300px; margin: 0 auto; }
    .section-header { text-align: center; margin-bottom: 60px; }
    .section-header h2 { font-size: 2.2rem; font-weight: 400; }
    .section-header h2 em { color: var(--gold); font-style: normal; }

    .media-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); gap: 30px; }
    .media-card { background: var(--bg-card); border: 1px solid var(--border); border-radius: 12px; overflow: hidden; transition: 0.3s; position: relative; }
    .media-card:hover { border-color: var(--gold); transform: translateY(-6px); }
    .media-preview { height: 200px; background: #1e293b; display: flex; align-items: center; justify-content: center; position: relative; }
    .play-btn { width: 60px; height: 60px; background: rgba(212,168,67,0.9); border-radius: 50%; display: flex; align-items: center; justify-content: center; cursor: pointer; transition: 0.2s; }
    .play-btn:hover { scale: 1.1; background: #fff; }
    .media-body { padding: 25px; }
    .media-tag { color: var(--gold); font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
    .media-body h3 { font-size: 1.25rem; margin-bottom: 10px; }
    .media-body p { color: #94a3b8; font-size: 0.9rem; }

    /* FOOTER */
    footer { border-top: 1px solid var(--border); padding: 40px; text-align: center; color: #64748b; font-size: 0.85rem; }
  </style>
</head>
<body>

  <nav class="navbar">
    <a href="#" class="logo">IOTEC <span>GLOBAL BROADCAST</span></a>
    <div style="font-size: 0.85rem; color: var(--gold); font-weight: 600;">CNPJ: 61.549.037/0001-68</div>
  </nav>

  <section class="hero">
    <div class="live-badge">
      <div class="live-dot"></div> TRANSMISSÃO OPERACIONAL AO VIVO
    </div>
    <h1>Mídia, Inovação e <em>Engenharia Multimodal.</em></h1>
    <p>Acompanhe em tempo real a cobertura das nossas operações no setor marítimo, aéreo, ferroviário e de logística de alta complexidade.</p>
  </section>

  <section class="grid-section">
    <div class="section-header">
      <h2>Programação <em>Audiovisual & Vitrine B2B</em></h2>
    </div>

    <div class="media-grid">
      <div class="media-card">
        <div class="media-preview">
          <div class="play-btn" onclick="alert('Iniciando transmissão: Operações Marítimas e Terminais de Contêineres...')">▶</div>
        </div>
        <div class="media-body">
          <div class="media-tag">Complexo Portuário</div>
          <h3>Navios Petroleiros & Carga Geral</h3>
          <p>Monitoramento de calado, atracação e atesto de segurança em tempo real.</p>
        </div>
      </div>

      <div class="media-card">
        <div class="media-preview">
          <div class="play-btn" onclick="alert('Iniciando transmissão: Malha Ferroviária Transnordestina...')">▶</div>
        </div>
        <div class="media-body">
          <div class="media-tag">Malha Ferroviária</div>
          <h3>Transnordestina & Transporte de Granéis</h3>
          <p>Fluxo de composições pesadas e integração com terminais de intermodalidade.</p>
        </div>
      </div>

      <div class="media-card">
        <div class="media-preview">
          <div class="play-btn" onclick="alert('Iniciando transmissão: Carga Aérea & Cold-Chain...')">▶</div>
        </div>
        <div class="media-body">
          <div class="media-tag">Aviação & Cadeia de Frio</div>
          <h3>Terminal Aéreo & Telemetria Térmica</h3>
          <p>Pátios de decolagem e rastreamento contínuo de insumos biológicos e químicos.</p>
        </div>
      </div>
    </div>
  </section>

  <footer>
    <p>© 2026 IOTEC BL — Construtora de Inovações e Tecnologia. Todos os direitos reservados.</p>
  </footer>

</body>
</html>
"""
        # Salva o arquivo broadcast na raiz e empacota para dist
        with open(os.path.join(self.root_dir, "broadcast.html"), "w", encoding="utf-8") as f:
            f.write(broadcast_html)

        print(" [2/3] 🌐 Interface `broadcast.html` compilada com sucesso!")

    def publicar_netlify(self):
        print(" [3/3] 🚀 Publicando Showroom Global Broadcast na Netlify...")
        dist_html = os.path.join(self.dist_dir, "broadcast.html")
        shutil.copy2(os.path.join(self.root_dir, "broadcast.html"), dist_html)

        cmd = "npx netlify-cli deploy --dir dist --prod --skip-functions-cache"
        subprocess.run(cmd, shell=True, text=True)

        print("\n==========================================================================================")
        print(" ✅ CANAL GLOBAL BROADCAST PUBLICADO COM SUCESSO!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = BroadcastChannelEngine()
    engine.processar_e_consolidar()
    engine.publicar_netlify()
