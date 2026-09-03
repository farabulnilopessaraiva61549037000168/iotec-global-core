from flask import Flask, render_template_string, request, jsonify
import json, time

app = Flask(__name__)

# CONFIGURAÇÕES DE GOVERNANÇA IOTEC
CNPJ_IOTEC = "61.549.037/0001-68"
EMAIL_CONTATO = "IOTEC.BL@proton.me"

# BARRAMENTO CENTRAL DE SETORES E ROTAS DA ECONOMIA
MATRIZ_SETORES = {
    "estetica": {
        "nome": "Bronze da Lu & Estética Blindada",
        "porta_local": "http://localhost:8200",
        "descricao": "PWA de agendamento com trava de sinal bancário e gestão de horários.",
        "icone": "💈"
    },
    "gastronomia": {
        "nome": "Gastronomia & Delivery Express",
        "porta_local": "http://localhost:8220",
        "descricao": "Cardápio digital, comanda eletrônica e envio direto para impressora da cozinha.",
        "icone": "🍕"
    },
    "atacarejo": {
        "nome": "Checkout Autônomo & Atacarejo Anti-Fila",
        "porta_local": "http://localhost:8240",
        "descricao": "Tótem telemétrico de validação rápida e liberação de baia de coleta.",
        "icone": "🛒"
    },
    "postos": {
        "nome": "Self-Fueling & Mobilidade",
        "porta_local": "http://localhost:8240",
        "descricao": "Automação de liberação de bombas de combustível e cancelas free-flow.",
        "icone": "⛽"
    },
    "investimentos": {
        "nome": "Mesa de Cotas SAFE (Café com Economia)",
        "porta_local": "http://localhost:8000",
        "descricao": "Portal de alocação de capital e participação no fluxo telemétrico de taxas.",
        "icone": "📊"
    }
}

HTML_ORCHESTRATOR = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC Global — Entidade Técnica Integradora & Central B2B</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { 
            background: #050508; 
            color: #FFF; 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            min-height: 100vh; 
            background-image: linear-gradient(rgba(0,0,0,0.88), rgba(0,0,0,0.95)), url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920&auto=format&fit=crop'); 
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
        }
        .container { max-width: 1050px; margin: 0 auto; padding: 40px 20px; }
        .brand { font-family: 'Cinzel', serif; font-size: 32px; color: #E8D8C8; letter-spacing: 6px; text-align: center; }
        .tagline { font-size: 11px; color: #D4B886; letter-spacing: 3px; text-align: center; margin-bottom: 30px; text-transform: uppercase; font-weight: 600; }
        
        .status-bar { 
            background: rgba(16,185,129,0.12); 
            border: 1px solid #10B981; 
            border-radius: 12px; 
            padding: 14px 20px; 
            font-size: 11px; 
            color: #10B981; 
            font-weight: 700; 
            margin-bottom: 30px; 
            display: flex; 
            justify-content: space-between; 
            align-items: center; 
        }

        .main-card { 
            background: rgba(12,12,18,0.92); 
            border: 1px solid rgba(232,216,200,0.25); 
            border-radius: 20px; 
            padding: 35px; 
            backdrop-filter: blur(15px); 
            box-shadow: 0 25px 60px rgba(0,0,0,0.95); 
        }

        .grid-setores { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; margin: 25px 0; }
        
        .setor-card { 
            background: rgba(22,22,30,0.8); 
            border: 1px solid rgba(212,184,134,0.25); 
            border-radius: 14px; 
            padding: 20px; 
            cursor: pointer; 
            transition: all 0.3s; 
        }
        .setor-card:hover { border-color: #10B981; background: rgba(16,185,129,0.08); transform: translateY(-2px); }
        .setor-card.selected { border-color: #10B981; background: rgba(16,185,129,0.15); box-shadow: 0 0 15px rgba(16,185,129,0.3); }

        .setor-header { font-size: 15px; font-weight: 700; color: #FFF; margin-bottom: 6px; display: flex; align-items: center; gap: 8px; }
        .setor-desc { font-size: 11px; color: #A1A1AA; line-height: 1.5; }

        .checkout-box { background: rgba(0,0,0,0.6); border: 1px solid rgba(255,255,255,0.1); border-radius: 14px; padding: 25px; margin-top: 25px; }
        .field-group { margin-bottom: 15px; text-align: left; }
        .field-group label { display: block; font-size: 11px; color: #A1A1AA; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 1px; }
        .field-group input, .field-group select { width: 100%; padding: 14px; background: #0A0A0F; border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; color: #FFF; font-size: 13px; }

        .btn-pix { display: block; width: 100%; background: #10B981; color: #000; font-size: 13px; font-weight: 800; padding: 18px; border: none; border-radius: 10px; text-transform: uppercase; letter-spacing: 2px; cursor: pointer; transition: all 0.3s; margin-top: 15px; }
        .btn-pix:hover { background: #34D399; box-shadow: 0 0 25px rgba(16,185,129,0.5); }

        .pix-display { display: none; background: rgba(16,185,129,0.1); border: 1px solid #10B981; border-radius: 12px; padding: 20px; margin-top: 20px; text-align: center; }
        .pix-key { font-family: monospace; font-size: 16px; color: #10B981; font-weight: 700; margin: 10px 0; }

        footer { margin-top: 40px; text-align: center; font-size: 11px; color: #71717A; line-height: 1.8; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="brand">IOTEC GLOBAL</div>
        <div class="tagline">Enterprise Software & Financial Systems — Kernel Integrador</div>

        <div class="status-bar">
            <span>⚙️ BARRAMENTO CENTRAL: CONECTADO E TELEMETRIA ATIVA</span>
            <span>CNPJ: 61.549.037/0001-68</span>
        </div>

        <div class="main-card">
            <h2 style="font-family:'Cinzel',serif; font-size:18px; color:#E8D8C8; margin-bottom:10px;">1. SELECIONE O SETOR DA SUA OPERAÇÃO</h2>
            <p style="font-size:12px; color:#A1A1AA; margin-bottom:20px;">A Entidade Técnica liberará o acesso ao programa específico do seu ramo assim que a Camada Subsequente confirmar o pagamento.</p>

            <div class="grid-setores">
                <div class="setor-card selected" onclick="selecionarSetor('estetica', this)">
                    <div class="setor-header">💈 Estética & Spas</div>
                    <div class="setor-desc">PWA com trava de sinal financeiro obrigatório e controle de agenda.</div>
                </div>
                <div class="setor-card" onclick="selecionarSetor('gastronomia', this)">
                    <div class="setor-header">🍕 Gastronomia & Delivery</div>
                    <div class="setor-desc">Cardápio interativo e disparo de comandas direto para a cozinha.</div>
                </div>
                <div class="setor-card" onclick="selecionarSetor('atacarejo', this)">
                    <div class="setor-header">🛒 Atacarejo & Supermercados</div>
                    <div class="setor-desc">Tótem autônomo anti-fila e liberação de baia de coleta.</div>
                </div>
                <div class="setor-card" onclick="selecionarSetor('postos', this)">
                    <div class="setor-header">⛽ Postos & Free-Flow</div>
                    <div class="setor-desc">Self-fueling e liberação instantânea de bombas e cancelas.</div>
                </div>
            </div>

            <div class="checkout-box">
                <h3 style="font-family:'Cinzel',serif; font-size:14px; color:#E8D8C8; margin-bottom:15px;">2. ATIVAÇÃO DO MÓDULO VIA PIX</h3>
                
                <div class="field-group">
                    <label>Valor da Operação / Licença</label>
                    <select id="valor_op">
                        <option value="1.00">Teste de Validação de Sinal — R$ 1,00</option>
                        <option value="150.00">Licença Mensal PWA Setorial — R$ 150,00</option>
                        <option value="500.00">Módulo Enterprise B2B Anti-Fila — R$ 500,00</option>
                    </select>
                </div>

                <div class="field-group">
                    <label>Razão Social / Nome da Empresa</label>
                    <input type="text" id="nome_cliente" placeholder="Digite o nome do seu estabelecimento">
                </div>

                <button class="btn-pix" onclick="gerarPix()">⚡ GERAR COBRANÇA E DISPARAR CAMADA SUBSEQUENTE</button>

                <div id="pix_box" class="pix-display">
                    <div style="font-size:12px; color:#FFF; font-weight:700;">CHAVE PIX CNPJ PARA PAGAMENTO:</div>
                    <div class="pix-key">61.549.037/0001-68</div>
                    <div style="font-size:11px; color:#A1A1AA;">Titular: IOTEC Enterprise | Destino: Banco do Brasil / Mercado Pago</div>
                    <div style="font-size:11px; color:#10B981; margin-top:12px; font-weight:700;">
                        🔄 Aguardando confirmação do banco... A Camada Subsequente liberará a porta do seu setor automaticamente.
                    </div>
                </div>
            </div>
        </div>

        <footer>
            <strong>IOTEC Enterprise Software & Financial Systems</strong><br>
            Corporate Tax ID (CNPJ): 61.549.037/0001-68 | Governança: Farabulini Lopes Saraiva (Bruno)<br>
            Executive Contact: IOTEC.BL@proton.me | © 2026 IOTEC Global. All rights reserved.
        </footer>
    </div>

    <script>
        var setorSelecionado = 'estetica';

        function selecionarSetor(setor, el) {
            setorSelecionado = setor;
            var cards = document.querySelectorAll('.setor-card');
            cards.forEach(c => c.classList.remove('selected'));
            el.classList.add('selected');
        }

        function gerarPix() {
            var nome = document.getElementById('nome_cliente').value;
            if(!nome) {
                alert('Por favor, informe o nome do seu estabelecimento para prosseguir.');
                return;
            }
            document.getElementById('pix_box').style.display = 'block';
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_ORCHESTRATOR)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
