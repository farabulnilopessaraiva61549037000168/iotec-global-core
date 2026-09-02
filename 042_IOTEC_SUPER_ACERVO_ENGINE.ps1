$port = 8260
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC SUPER ACERVO — VISUAL ULTRA-LUXO ATIVO (PORTA $port)" -ForegroundColor Green
    Write-Host "     Acesse no seu navegador: http://localhost:$port/" -ForegroundColor Yellow
    Write-Host "=================================================================`n" -ForegroundColor Cyan
} catch {
    Write-Host "[ERRO] Não foi possível iniciar na porta $port." -ForegroundColor Red
    exit
}

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $response = $context.Response

    $html = @"
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC — Super Acervo & Design Minimalista Elevado</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Plus+Jakarta+Sans:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#000; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; min-height:100vh; overflow-x:hidden; position:relative; }

        /* VÍDEO DE FUNDO EM LOOP DE ALTO LUXO */
        .video-bg {
            position: fixed;
            top: 50%;
            left: 50%;
            min-width: 100%;
            min-height: 100%;
            width: auto;
            height: auto;
            z-index: -2;
            transform: translate(-50%, -50%);
            filter: grayscale(100%) contrast(120%) brightness(35%);
            object-fit: cover;
        }

        /* OVERLAY MÁSCARA OBSIDIAN */
        .overlay {
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background: radial-gradient(circle, rgba(0,0,0,0.4) 0%, rgba(0,0,0,0.92) 100%);
            z-index: -1;
        }

        .container { max-width: 1000px; margin: 0 auto; padding: 60px 20px; text-align: center; }
        
        .brand { font-family: 'Cinzel', serif; font-size: 32px; color: #E8D8C8; letter-spacing: 8px; margin-bottom: 6px; text-transform: uppercase; text-shadow: 0 0 20px rgba(232,216,200,0.2); }
        .tagline { font-size: 11px; color: #D4B886; letter-spacing: 4px; margin-bottom: 50px; text-transform: uppercase; font-weight: 600; }

        /* CARTÃO EM VIDRO FOSCO (GLASSMORPHISM ELEVADO) */
        .glass-card {
            background: rgba(10, 10, 14, 0.65);
            border: 1px solid rgba(232, 216, 200, 0.25);
            border-radius: 20px;
            padding: 50px 40px;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            box-shadow: 0 30px 80px rgba(0,0,0,0.9);
            margin-bottom: 40px;
        }

        .card-title { font-family: 'Cinzel', serif; font-size: 20px; color: #FFF; margin-bottom: 16px; letter-spacing: 2px; }
        .card-desc { font-size: 13px; color: #A1A1AA; max-width: 680px; margin: 0 auto 35px auto; line-height: 1.8; font-weight: 300; }

        /* GRID DO ACERVO DE LUXO */
        .acervo-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; margin: 30px 0; text-align: left; }
        .acervo-item { 
            background: rgba(255,255,255,0.03); 
            border: 1px solid rgba(255,255,255,0.08); 
            border-radius: 12px; 
            padding: 20px; 
            transition: all 0.3s ease;
        }
        .acervo-item:hover { 
            border-color: #D4B886; 
            background: rgba(212,184,134,0.05); 
            transform: translateY(-3px);
        }
        .item-tag { font-family: 'Cinzel', serif; font-size: 10px; color: #D4B886; font-weight: 700; letter-spacing: 1px; margin-bottom: 6px; }
        .item-name { font-size: 13px; font-weight: 600; color: #FFF; margin-bottom: 6px; }
        .item-desc { font-size: 11px; color: #71717A; line-height: 1.5; }

        footer { border-top: 1px solid rgba(255,255,255,0.1); padding-top: 25px; font-size: 10.5px; color: #71717A; line-height: 1.8; }
        .footer-gold { color: #D4B886; font-weight: 600; }
    </style>
</head>
<body>

    <!-- VÍDEO DE ABSTRATO EM LOOP NO BACKGROUND -->
    <video class="video-bg" autoplay loop muted playsinline>
        <source src="https://assets.mixkit.co/videos/preview/mixkit-abstract-fast-lines-of-light-31742-large.mp4" type="video/mp4">
    </video>
    <div class="overlay"></div>

    <div class="container">
        <div class="brand">IOTEC SUPER ACERVO</div>
        <div class="tagline">Minimalismo Elevado & Design de Alta Resolução</div>

        <div class="glass-card">
            <div class="card-title">GESTOR DE MÍDIAS & AMBIENTAÇÃO VISUAL</div>
            <div class="card-desc">Fundo com movimento abstrato e filtro cinematográfico. O Super Acervo abastece automaticamente o Portal Render, os PWAs dos clientes e as telas de atendimento.</div>

            <div class="acervo-grid">
                <div class="acervo-item">
                    <div class="item-tag">NÍVEL 4 — ULTRA-LUXO</div>
                    <div class="item-name">Loop Abstrato Obsidiana</div>
                    <div class="item-desc">Vídeo de fundo de alta densidade visual para portais de investimento e War Room.</div>
                </div>

                <div class="acervo-item">
                    <div class="item-tag">NÍVEL 3 — LUXO B2B</div>
                    <div class="item-name">Textura P&B Arquitetura</div>
                    <div class="item-desc">Fotografia corporativa internacional em preto e branco para fundo de catálogo.</div>
                </div>

                <div class="acervo-item">
                    <div class="item-tag">NÍVEL 2 — COMERCIAL</div>
                    <div class="item-name">Vinheta de Segurança</div>
                    <div class="item-desc">Efeito de selo de trava de segurança com brilho dourado sutil para os comprovantes.</div>
                </div>
            </div>
        </div>

        <footer>
            <strong>IOTEC Enterprise Software & Financial Systems</strong><br>
            <span class="footer-gold">Corporate Tax ID (CNPJ): 61.549.037/0001-68</span> | Governança: Farabulini Lopes Saraiva (Bruno)<br>
            Executive Contact: IOTEC.BL@proton.me | © 2026 IOTEC Global. All rights reserved.
        </footer>
    </div>

</body>
</html>
"@

    $buffer = [System.Text.Encoding]::UTF8.GetBytes($html)
    $response.ContentLength64 = $buffer.Length
    $response.ContentType = "text/html; charset=utf-8"
    $response.OutputStream.Write($buffer, 0, $buffer.Length)
    $response.OutputStream.Close()
}
