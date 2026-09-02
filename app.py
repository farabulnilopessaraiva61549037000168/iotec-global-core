from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# CNPJ Oficial IOTEC para liquidação direta
CNPJ_IOTEC = "61.549.037/0001-68"
EMAIL_CONTATO = "IOTEC.BL@proton.me"

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC Global Enterprise — Checkout de Ativação Real</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { 
            background: #000; 
            color: #FFF; 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            min-height: 100vh; 
            background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.95)), url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920&auto=format&fit=crop'); 
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
        }
        .container { max-width: 900px; margin: 0 auto; padding: 60px 20px; text-align: center; }
        .brand { font-family: 'Cinzel', serif; font-size: 36px; color: #E8D8C8; letter-spacing: 6px; margin-bottom: 8px; text-transform: uppercase; }
        .tagline { font-size: 12px; color: #D4B886; letter-spacing: 3px; margin-bottom: 40px; text-transform: uppercase; font-weight: 600; }
        
        .hero-card { 
            background: rgba(10,10,14,0.88); 
            border: 1px solid rgba(232,216,200,0.3); 
            border-radius: 20px; 
            padding: 45px 35px; 
            backdrop-filter: blur(15px); 
            box-shadow: 0 25px 60px rgba(0,0,0,0.95); 
        }
        .hero-title { font-size: 22px; font-weight: 700; color: #FFF; margin-bottom: 16px; font-family: 'Cinzel', serif; letter-spacing: 2px; }
        .hero-desc { font-size: 13px; color: #D4D4D8; max-width: 650px; margin: 0 auto 30px auto; line-height: 1.8; }
        
        .checkout-box {
            background: rgba(20,20,28,0.9);
            border: 1px solid rgba(212,184,134,0.4);
            border-radius: 16px;
            padding: 30px;
            margin: 30px 0;
            text-align: left;
        }

        .checkout-title { font-size: 14px; font-weight: 700; color: #E8D8C8; font-family: 'Cinzel', serif; margin-bottom: 15px; letter-spacing: 1px; }
        .field-group { margin-bottom: 15px; }
        .field-group label { display: block; font-size: 11px; color: #A1A1AA; text-transform: uppercase; margin-bottom: 6px; letter-spacing: 1px; }
        .field-group input, .field-group select {
            width: 100%; padding: 14px; background: #000; border: 1px solid rgba(255,255,255,0.2); border-radius: 8px; color: #FFF; font-size: 13px;
        }

        .btn-pix { 
            display: block; 
            width: 100%;
            background: #10B981; 
            color: #000; 
            font-size: 13px; 
            font-weight: 800; 
            padding: 18px; 
            border: none;
            border-radius: 10px; 
            text-transform: uppercase; 
            letter-spacing: 2px; 
            cursor: pointer;
            transition: all 0.3s; 
            margin-top: 20px;
        }
        .btn-pix:hover { background: #34D399; box-shadow: 0 0 25px rgba(16,185,129,0.5); }
        
        .pix-display {
            display: none;
            background: rgba(16,185,129,0.1);
            border: 1px solid #10B981;
            border-radius: 12px;
            padding: 20px;
            margin-top: 20px;
            text-align: center;
        }
        .pix-key { font-family: monospace; font-size: 16px; color: #10B981; font-weight: 700; word-break: break-all; margin: 10px 0; }

        footer { margin-top: 50px; font-size: 11px; color: #71717A; line-height: 1.8; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="brand">IOTEC GLOBAL</div>
        <div class="tagline">Enterprise Software & Financial Systems</div>
        
        <div class="hero-card">
            <div class="hero-title">CHECKOUT OFICIAL DE LIQUIDAÇÃO REAL</div>
            <div class="hero-desc">Ativação imediata de módulos B2B e licenciamento de software com trava de segurança direta no CNPJ da empresa.</div>
            
            <div class="checkout-box">
                <div class="checkout-title">🔒 DADOS DA OPERAÇÃO DE COMPRA</div>
                
                <div class="field-group">
                    <label>Selecione o Serviço / Licença</label>
                    <select id="servico">
                        <option value="1.00">Teste de Validação de Sinal — R$ 1,00</option>
                        <option value="150.00">Módulo PWA Bronze/Estética — R$ 150,00</option>
                        <option value="500.00">Licença Enterprise B2B — R$ 500,00</option>
                    </select>
                </div>

                <div class="field-group">
                    <label>Razão Social / Nome do Cliente</label>
                    <input type="text" id="nome_cliente" placeholder="Digite seu nome ou empresa">
                </div>

                <button class="btn-pix" onclick="gerarPix()">⚡ GERAR COBRANÇA PIX REAL</button>

                <div id="pix_box" class="pix-display">
                    <div style="font-size:12px; color:#FFF; font-weight:700;">CHAVE PIX CNPJ PARA PAGAMENTO:</div>
                    <div class="pix-key">61.549.037/0001-68</div>
                    <div style="font-size:11px; color:#A1A1AA;">Titular: IOTEC Enterprise | Destino: Banco do Brasil / Mercado Pago</div>
                    <div style="font-size:11px; color:#10B981; margin-top:10px;">Após o pagamento, a trava de segurança libera o acesso automaticamente.</div>
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
        function gerarPix() {
            var nome = document.getElementById('nome_cliente').value;
            if(!nome) {
                alert('Por favor, digite seu nome ou o nome da sua empresa para prosseguir.');
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
    return render_template_string(HTML_LAYOUT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
