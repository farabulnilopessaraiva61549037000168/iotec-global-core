from flask import Flask, render_template_string

app = Flask(__name__)

HTML_LAYOUT = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC Global Enterprise Software</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { 
            background: #000; 
            color: #FFF; 
            font-family: 'Plus Jakarta Sans', sans-serif; 
            min-height: 100vh; 
            background-image: linear-gradient(rgba(0,0,0,0.85), rgba(0,0,0,0.92)), url('https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920&auto=format&fit=crop'); 
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed; 
        }
        .container { max-width: 1100px; margin: 0 auto; padding: 60px 20px; text-align: center; }
        .brand { font-family: 'Cinzel', serif; font-size: 38px; color: #E8D8C8; letter-spacing: 6px; margin-bottom: 8px; text-transform: uppercase; }
        .tagline { font-size: 13px; color: #A1A1AA; letter-spacing: 3px; margin-bottom: 40px; text-transform: uppercase; font-weight: 300; }
        
        .hero-card { 
            background: rgba(10,10,12,0.85); 
            border: 1px solid rgba(232,216,200,0.3); 
            border-radius: 16px; 
            padding: 45px 30px; 
            backdrop-filter: blur(12px); 
            box-shadow: 0 20px 50px rgba(0,0,0,0.9); 
        }
        .hero-title { font-size: 24px; font-weight: 700; color: #FFF; margin-bottom: 16px; font-family: 'Cinzel', serif; letter-spacing: 2px; }
        .hero-desc { font-size: 13.5px; color: #D4D4D8; max-width: 750px; margin: 0 auto 35px auto; line-height: 1.8; }
        
        .features-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin: 40px 0; text-align: left; }
        .feature-item { background: rgba(20,20,25,0.7); border: 1px solid rgba(255,255,255,0.12); border-radius: 12px; padding: 22px; }
        .feature-title { font-size: 13px; font-weight: 700; color: #E8D8C8; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 1px; }
        .feature-txt { font-size: 11px; color: #A1A1AA; line-height: 1.6; }
        
        .btn-atendimento { 
            display: inline-flex; 
            align-items: center; 
            gap: 12px; 
            background: #E8D8C8; 
            color: #000; 
            font-size: 12px; 
            font-weight: 800; 
            padding: 16px 36px; 
            border-radius: 30px; 
            text-decoration: none; 
            text-transform: uppercase; 
            letter-spacing: 2px; 
            transition: all 0.3s; 
        }
        .btn-atendimento:hover { background: #FFF; box-shadow: 0 0 25px rgba(232,216,200,0.5); transform: translateY(-2px); }
        
        footer { margin-top: 60px; font-size: 11px; color: #71717A; line-height: 1.8; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="brand">IOTEC GLOBAL</div>
        <div class="tagline">Enterprise Software & Financial Systems</div>
        
        <div class="hero-card">
            <div class="hero-title">INFRAESTRUTURA B2B DE ALTA RESOLUÇÃO</div>
            <div class="hero-desc">Sistemas adaptáveis para comércio, estética, gastronomia e grandes eventos. Conexão direta com APIs bancárias reais, emissão de travas de segurança e suporte via sinal ativo.</div>
            
            <div class="features-grid">
                <div class="feature-item">
                    <div class="feature-title">🔒 Trava Anti-Fraude</div>
                    <div class="feature-txt">Liberação imediata de acesso somente após confirmação do saldo na conta do CNPJ.</div>
                </div>
                <div class="feature-item">
                    <div class="feature-title">📱 App Adaptável</div>
                    <div class="feature-txt">Cadastro flexível por setor acionado diretamente pela atendente interna da IOTEC.</div>
                </div>
                <div class="feature-item">
                    <div class="feature-title">🌐 Cobertura 24/7</div>
                    <div class="feature-txt">Operação contínua por fuso horário com sinal de transmissão totalmente homologado.</div>
                </div>
            </div>

            <a href="https://wa.me/5500000000000?text=Ol%C3%A1!%20Desejo%20falar%20com%20a%20atendente%20para%20cadastrar%20meu%20setor%20no%20ecossistema%20IOTEC." target="_blank" class="btn-atendimento">
                💬 Solicitar Ativação de Setor com Atendente
            </a>
        </div>

        <footer>
            <strong>IOTEC Enterprise Software & Financial Systems</strong><br>
            Corporate Tax ID (CNPJ): 61.549.037/0001-68 | Governance: Farabulini Lopes Saraiva (Bruno)<br>
            Executive Contact: IOTEC.BL@proton.me | © 2026 IOTEC Global. All rights reserved.
        </footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_LAYOUT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
