from flask import Flask, render_template_string, request, jsonify
import json, time

app = Flask(__name__)

# GOVERNANÇA E IDENTIDADE IOTEC
CNPJ_IOTEC = "61.549.037/0001-68"
EMAIL_CONTATO = "IOTEC.BL@proton.me"

# MATRIZ DE SETORES E AMBIENTES SUBSEQUENTES
SETORES = {
    "estetica": {
        "nome": "Bronze da Lu & Estética Blindada",
        "bg_img": "https://images.unsplash.com/photo-1560750588-73207b1ef5b8?q=80&w=1920&auto=format&fit=crop",
        "desc": "PWA de agendamento com trava financeira obrigatória de sinal.",
        "rota": "http://localhost:8200"
    },
    "gastronomia": {
        "nome": "Gastronomia & Delivery Express",
        "bg_img": "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?q=80&w=1920&auto=format&fit=crop",
        "desc": "Cardápio interativo e emissão direta para impressora da cozinha.",
        "rota": "http://localhost:8220"
    },
    "atacarejo": {
        "nome": "Checkout Autônomo Atacarejo",
        "bg_img": "https://images.unsplash.com/photo-1578916171728-46686eac8d58?q=80&w=1920&auto=format&fit=crop",
        "desc": "Tótem anti-fila, validação expressa e coordenadas de coleta.",
        "rota": "http://localhost:8240"
    },
    "postos": {
        "nome": "Self-Fueling & Mobilidade",
        "bg_img": "https://images.unsplash.com/photo-1527018601619-a508a2be00d6?q=80&w=1920&auto=format&fit=crop",
        "desc": "Liberação autônoma de bombas e cancelas free-flow.",
        "rota": "http://localhost:8240"
    },
    "investimentos": {
        "nome": "Mesa de Cotas SAFE (Café com Economia)",
        "bg_img": "https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920&auto=format&fit=crop",
        "desc": "Participação no fluxo telemétrico de taxas do ecossistema.",
        "rota": "http://localhost:8000"
    }
}

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC Global — Produtora de Tecnologia B2B</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background: #050508; color: #FFF; font-family: 'Plus Jakarta Sans', sans-serif; min-height: 100vh; }
        
        .hero-container {
            position: relative; min-height: 100vh; padding: 40px 20px;
            background-size: cover; background-position: center; transition: background 0.5s ease-in-out;
            display: flex; flex-direction: column; justify-content: space-between; align-items: center;
        }
        .hero-overlay { position: absolute; inset: 0; background: linear-gradient(180deg, rgba(5,5,8,0.85) 0%, rgba(5,5,8,0.96) 100%); z-index: 1; }
        .content { position: relative; z-index: 2; max-width: 1000px; width: 100%; text-align: center; }

        .brand { font-family: 'Cinzel', serif; font-size: 36px; color: #E8D8C8; letter-spacing: 6px; }
        .tagline { font-size: 11px; color: #10B981; letter-spacing: 3px; font-weight: 700; text-transform: uppercase; margin-bottom: 30px; }

        .glass-card { background: rgba(18, 18, 26, 0.75); border: 1px solid rgba(232, 216, 200, 0.2); border-radius: 20px; padding: 30px; backdrop-filter: blur(15px); }
        .grid-setores { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 15px; margin: 25px 0; }
        
        .setor-item { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); padding: 18px; border-radius: 12px; cursor: pointer; text-align: left; transition: all 0.3s; }
        .setor-item:hover, .setor-item.active { border-color: #10B981; background: rgba(16,185,129,0.1); transform: translateY(-2px); }

        .checkout-box { background: rgba(0,0,0,0.5); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; margin-top: 20px; text-align: left; }
        .btn-pay { width: 100%; background: #10B981; color: #000; font-weight: 800; padding: 16px; border: none; border-radius: 8px; cursor: pointer; text-transform: uppercase; letter-spacing: 2px; margin-top: 15px; }

        .brand-signature { font-family: 'Cinzel', serif; font-size: 12px; color: #D4B886; letter-spacing: 2px; text-align: center; margin-top: 30px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }
    </style>
</head>
<body>
    <div class="hero-container" id="bgContainer" style="background-image: url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920&auto=format&fit=crop');">
        <div class="hero-overlay"></div>
        
        <div class="content">
            <div class="brand">IOTEC GLOBAL</div>
            <div class="tagline">Indústria & Produtora de Tecnologia B2B</div>

            <div class="glass-card">
                <h2 style="font-family:'Cinzel',serif; font-size:18px; color:#E8D8C8;">SELECIONE A PROGRAMAÇÃO SETORIAL</h2>
                <div class="grid-setores">
                    {% for key, s in setores.items() %}
                    <div class="setor-item {% if loop.first %}active{% endif %}" onclick="trocarSetor('{{key}}', '{{s.bg_img}}')">
                        <strong style="color:#FFF; display:block; font-size:14px;">{{s.nome}}</strong>
                        <span style="font-size:11px; color:#A1A1AA;">{{s.desc}}</span>
                    </div>
                    {% endfor %}
                </div>

                <div class="checkout-box">
                    <label style="font-size:11px; color:#A1A1AA; text-transform:uppercase;">Razão Social / Estabelecimento</label>
                    <input type="text" id="empresa" placeholder="Nome da sua empresa" style="width:100%; padding:12px; background:#0A0A0F; border:1px solid #333; color:#FFF; border-radius:6px; margin-top:5px;">
                    <button class="btn-pay" onclick="ativarPix()">⚡ ATIVAR PROGRAMAÇÃO PÓS-PAGAMENTO VIA PIX</button>

                    <div id="pixArea" style="display:none; margin-top:15px; background:rgba(16,185,129,0.1); border:1px solid #10B981; padding:15px; border-radius:8px; text-align:center;">
                        <span style="font-size:12px; color:#FFF; font-weight:700;">CHAVE PIX CNPJ IOTEC:</span>
                        <div style="font-family:monospace; font-size:18px; color:#10B981; margin:5px 0;">61.549.037/0001-68</div>
                        <span style="font-size:10px; color:#A1A1AA;">A Camada Subsequente abrirá o painel privado em menos de 2s após o sinal bancário.</span>
                    </div>
                </div>

                <div class="brand-signature">
                    <strong>IOTEC ENTERPRISE SOFTWARE & FINANCIAL SYSTEMS</strong><br>
                    Soberania Operacional • CNPJ: 61.549.037/0001-68 • IOTEC.BL@proton.me
                </div>
            </div>
        </div>
    </div>

    <script>
        function trocarSetor(key, imgUrl) {
            document.getElementById('bgContainer').style.backgroundImage = "url('" + imgUrl + "')";
            var items = document.querySelectorAll('.setor-item');
            items.forEach(i => i.classList.remove('active'));
            event.currentTarget.classList.add('active');
        }

        function ativarPix() {
            var emp = document.getElementById('empresa').value;
            if(!emp) { alert('Informe a razão social para emitir o sinal.'); return; }
            document.getElementById('pixArea').style.display = 'block';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, setores=SETORES)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
