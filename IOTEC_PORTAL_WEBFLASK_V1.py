import os
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML_PLATAFORMA_DINAMICA = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Command Center & Port Telemetry</title>
    <style>
        :root { --accent: #3a86ff; --green: #10b981; --blue: #38bdf8; --yellow: #f59e0b; --bg: #030712; }
        * { box-sizing: border-box; }
        body, html { margin: 0; padding: 0; min-height: 100vh; font-family: 'Segoe UI', sans-serif; color: #fff; background: var(--bg); overflow-x: hidden; }

        /* VÍDEO MP4 DE FUNDO COM FALLBACK DENSIDADE */
        .v-bg {
            position: fixed; top: 50%; left: 50%;
            min-width: 100%; min-height: 100%; width: auto; height: auto;
            z-index: -2; transform: translateX(-50%) translateY(-50%);
            object-fit: cover; filter: brightness(0.25) contrast(1.2);
        }
        .overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: radial-gradient(circle, rgba(15,23,42,0.4) 0%, rgba(3,7,18,0.95) 100%); z-index: -1; }

        .container { max-width: 1250px; margin: 0 auto; padding: 30px 20px; }
        
        /* HEADER OPERACIONAL COM HORÁRIO EM TEMPO REAL */
        .top-header { display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 20px; margin-bottom: 30px; }
        .logo-title h1 { font-size: 32px; margin: 0; letter-spacing: 2px; text-transform: uppercase; color: #fff; text-shadow: 0 0 20px rgba(58,134,255,0.6); }
        .logo-title p { color: #94a3b8; font-size: 14px; margin: 4px 0 0 0; }
        .clock-box { text-align: right; font-family: monospace; }
        .clock-time { font-size: 22px; font-weight: bold; color: var(--blue); }
        .live-status { font-size: 12px; color: var(--green); font-weight: bold; }

        /* NAVEGAÇÃO ENTRE CAMADAS */
        .nav-tabs { display: flex; gap: 12px; margin-bottom: 24px; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 12px; }
        .tab-btn { background: rgba(30, 41, 59, 0.7); border: 1px solid #334155; color: #94a3b8; padding: 12px 24px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: all 0.2s; }
        .tab-btn.active { background: var(--accent); color: #fff; border-color: var(--accent); box-shadow: 0 0 15px rgba(58,134,255,0.5); }

        /* SEÇÕES / CAMADAS */
        .layer { display: none; background: rgba(15, 23, 42, 0.85); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 28px; backdrop-filter: blur(12px); }
        .layer.active { display: block; animation: fadeIn 0.3s ease; }

        @keyframes fadeIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

        /* METRIC CARDS COM ANIMAÇÃO DINÂMICA */
        .metrics-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-bottom: 28px; }
        .m-card { background: rgba(30, 41, 59, 0.6); border: 1px solid #334155; border-radius: 12px; padding: 20px; }
        .m-card h3 { margin: 0 0 8px 0; font-size: 12px; color: #94a3b8; text-transform: uppercase; }
        .m-value { font-size: 32px; font-weight: bold; color: #fff; font-family: monospace; }
        .pulse-dot { display: inline-block; width: 8px; height: 8px; background: var(--green); border-radius: 50%; box-shadow: 0 0 8px var(--green); margin-right: 6px; }

        /* TABELA DINÂMICA DE RASTREAMENTO */
        table { width: 100%; border-collapse: collapse; text-align: left; font-size: 14px; }
        th, td { padding: 14px 12px; border-bottom: 1px solid #1e293b; }
        th { color: #94a3b8; text-transform: uppercase; font-size: 12px; font-weight: 600; }
        .tag-live { background: rgba(16, 185, 129, 0.2); color: var(--green); padding: 4px 10px; border-radius: 20px; font-size: 12px; font-weight: bold; border: 1px solid rgba(16, 185, 129, 0.3); }
        .coords { font-family: monospace; color: var(--blue); }

        .footer { text-align: center; margin-top: 40px; color: #64748b; font-size: 12px; }
    </style>
</head>
<body>

    <!-- VIDEO CORPORATIVO NATIVO DE FUNDO -->
    <video autoplay muted loop playsinline class="v-bg">
        <source src="https://assets.mixkit.co/videos/preview/mixkit-cargo-ship-entering-a-port-41527-large.mp4" type="video/mp4">
    </video>
    <div class="overlay"></div>

    <div class="container">
        
        <!-- TOPBAR INTEGRADA -->
        <div class="top-header">
            <div class="logo-title">
                <h1>IOTEC COMMAND CENTER</h1>
                <p>Monitoramento e Inteligência Operacional de Portos & Corredores Logísticos</p>
            </div>
            <div class="clock-box">
                <div class="live-status"><span class="pulse-dot"></span>SISTEMA EM TEMPO REAL</div>
                <div class="clock-time" id="utc-clock">00:00:00 UTC</div>
            </div>
        </div>

        <!-- ABAS DE NAVEGAÇÃO ENTRE CAMADAS -->
        <div class="nav-tabs">
            <button class="tab-btn active" onclick="setLayer('c1', this)">🏢 1ª CAMADA: PORTAL FACHADA</button>
            <button class="tab-btn" onclick="setLayer('c2', this)">⚓ 2ª CAMADA: TELEMETRIA PORTO DO PECÉM</button>
            <button class="tab-btn" onclick="setLayer('c3', this)">🏛️ 3ª CAMADA: CIGM V4 SALA DE SITUAÇÃO</button>
        </div>

        <!-- 1ª CAMADA: FACHADA -->
        <div id="c1" class="layer active">
            <h2>Fachadas de Negócios Conectadas</h2>
            <p style="color:#cbd5e1;">Acesse as ferramentas dinâmicas ativas do núcleo:</p>
            <div class="metrics-grid" style="margin-top:20px;">
                <div class="m-card">
                    <h3>Logística & Portos</h3>
                    <div class="m-value" style="color:var(--blue)">Rastreio Pecém</div>
                    <p style="color:#94a3b8; font-size:13px; margin-top:8px;">Controle autônomo de navios cargueiros, contêineres e desembaraço de insumos.</p>
                    <button onclick="setLayer('c2', document.querySelectorAll('.tab-btn')[1])" class="tab-btn" style="width:100%; margin-top:10px;">ABRIR RASTREAMENTO</button>
                </div>
                <div class="m-card">
                    <h3>Gestão Pública</h3>
                    <div class="m-value" style="color:var(--green)">CIGM V4</div>
                    <p style="color:#94a3b8; font-size:13px; margin-top:8px;">Centro Integrado de Governança para Secretarias e Gabinete do Prefeito.</p>
                    <button onclick="setLayer('c3', document.querySelectorAll('.tab-btn')[2])" class="tab-btn" style="width:100%; margin-top:10px;">ABRIR CIGM GOV</button>
                </div>
            </div>
        </div>

        <!-- 2ª CAMADA: RASTREIO PECÉM EM TEMPO REAL -->
        <div id="c2" class="layer">
            <h2 style="color:var(--blue)">⚓ Telemetria do Porto do Pecém & Corredores Internacionais</h2>
            
            <div class="metrics-grid">
                <div class="m-card">
                    <h3>Cargueiros Ativos no Pecém</h3>
                    <div class="m-value" id="ship-count">14</div>
                    <span style="color:var(--green); font-size:12px;">● Fila de espera reduzida em 22%</span>
                </div>
                <div class="m-card">
                    <h3>Volume Processado (TEUs)</h3>
                    <div class="m-value" id="teu-counter">12,450</div>
                    <span style="color:var(--blue); font-size:12px;">↑ Incremento em tempo real</span>
                </div>
                <div class="m-card">
                    <h3>Capacidade do Corredor BR-116</h3>
                    <div class="m-value" style="color:var(--green)">94.2%</div>
                    <span style="color:#94a3b8; font-size:12px;">Fluxo contínuo sem gargalos</span>
                </div>
            </div>

            <h3 style="margin-top:20px; color:#fff;">Embarcações em Operação & Posição GPS Dinâmica</h3>
            <table>
                <thead>
                    <tr>
                        <th>Cargueiro / Navio</th>
                        <th>Origem / Rota</th>
                        <th>Coordenadas GPS (Ao Vivo)</th>
                        <th>Insumo / Carga</th>
                        <th>Status Operacional</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>MSC Rotterdam VII</strong></td>
                        <td>Roterdã &rarr; Pecém</td>
                        <td class="coords" id="gps-1">-3.5489, -38.8051</td>
                        <td>Componentes Industriais</td>
                        <td><span class="tag-live">EM DESCARGA</span></td>
                    </tr>
                    <tr>
                        <td><strong>Maersk Linea C</strong></td>
                        <td>Xangai &rarr; Pecém</td>
                        <td class="coords" id="gps-2">-3.5120, -38.7910</td>
                        <td>Insumos Eletrônicos & Polímeros</td>
                        <td><span class="tag-live" style="background:rgba(56,189,248,0.2); color:var(--blue); border-color:rgba(56,189,248,0.3)">ATRACANDO</span></td>
                    </tr>
                    <tr>
                        <td><strong>Grain Express I</strong></td>
                        <td>Pecém &rarr; Hamburgo</td>
                        <td class="coords" id="gps-3">-3.4901, -38.7554</td>
                        <td>Fruticultura de Exportação</td>
                        <td><span class="tag-live" style="background:rgba(245,158,11,0.2); color:var(--yellow); border-color:rgba(245,158,11,0.3)">EM TRÂNSITO</span></td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- 3ª CAMADA: CIGM GOVERNANÇA -->
        <div id="c3" class="layer">
            <h2 style="color:var(--green)">🏛️ CIGM V4 - Sala de Situação e Governança Executiva</h2>
            <div class="metrics-grid">
                <div class="m-card"><h3>Arrecadação do Mês</h3><div class="m-value">R$ 4.280.450</div></div>
                <div class="m-card"><h3>Frentes de Obras</h3><div class="m-value">18 Ativas</div></div>
                <div class="m-card"><h3>Rede de Saúde (SUS)</h3><div class="m-value">1.420 / dia</div></div>
            </div>
            <table>
                <thead>
                    <tr><th>Módulo de Governança</th><th>Eixo Executivo</th><th>Status Operacional</th></tr>
                </thead>
                <tbody>
                    <tr><td><code>CIGM_V4_PREFEITO_APRESENTACAO.py</code></td><td>Console do Prefeito / Indicadores</td><td><span class="tag-live">CONECTADO</span></td></tr>
                    <tr><td><code>fullscreen_governor.py</code></td><td>Sala de Situação / Projetor Fullscreen</td><td><span class="tag-live">CONECTADO</span></td></tr>
                </tbody>
            </table>
        </div>

        <div class="footer">
            IOTEC Command Center &copy; 2026 | Arquitetura Dinâmica em Tempo Real
        </div>

    </div>

    <script>
        // MUDANÇA DE CAMADAS INSTANTÂNEA
        function setLayer(id, btn) {
            document.querySelectorAll('.layer').forEach(l => l.classList.remove('active'));
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            document.getElementById(id).classList.add('active');
            btn.classList.add('active');
        }

        // RELÓGIO OPERACIONAL DINÂMICO
        function updateClock() {
            const now = new Date();
            document.getElementById('utc-clock').innerText = now.toUTCString().split(' ')[4] + ' UTC';
        }
        setInterval(updateClock, 1000);
        updateClock();

        // SIMULAÇÃO DE TELEMETRIA GPS E CONTADORES EM TEMPO REAL
        let teus = 12450;
        setInterval(() => {
            teus += Math.floor(Math.random() * 3);
            document.getElementById('teu-counter').innerText = teus.toLocaleString();
            
            // Variacao sutil de coordenadas GPS simulando movimento de navios
            let lat = (-3.5489 + (Math.random() * 0.0008 - 0.0004)).toFixed(4);
            let lon = (-38.8051 + (Math.random() * 0.0008 - 0.0004)).toFixed(4);
            document.getElementById('gps-1').innerText = `${lat}, ${lon}`;
        }, 2000);
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_PLATAFORMA_DINAMICA)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)