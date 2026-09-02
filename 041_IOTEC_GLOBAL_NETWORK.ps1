# =========================================================================================
#       USINA IOTEC — MALHA DE COMUNICAÇÃO GLOBAL & COLUNAS DE VISIBILIDADE (PORTA 8250)
#       CNPJ: 61.549.037/0001-68 | Governança: Farabulini Lopes Saraiva
# =========================================================================================

$port = 8250
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC GLOBAL NETWORK — TORRES & COLUNAS ATIVAS (PORTA $port)" -ForegroundColor Green
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
    <title>IOTEC — Central Global de Comunicação & Visibilidade</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#030406; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; min-height:100vh; padding:20px; }
        
        .main-container { max-width:900px; margin:0 auto; width:100%; text-align:center; padding-top:20px; }
        .hero-title { font-family:'Cinzel',serif; font-size:26px; color:#E8D8C8; letter-spacing:4px; margin-bottom:10px; }
        .hero-subtitle { font-size:12px; color:#9AA0AC; max-width:600px; margin:0 auto 30px auto; line-height:1.6; }
        
        /* ESTRUTURA DAS TORRES DE COMUNICAÇÃO */
        .towers-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:14px; margin-bottom:40px; text-align:left; }
        .tower-card { background:rgba(12,14,20,0.85); border:1px solid rgba(212,184,134,0.25); border-radius:12px; padding:18px; position:relative; overflow:hidden; }
        .tower-card:hover { border-color:#D4B886; box-shadow:0 0 15px rgba(212,184,134,0.1); }
        .tower-fuso { font-family:'Cinzel',serif; font-size:11px; color:#D4B886; font-weight:800; letter-spacing:1px; margin-bottom:4px; }
        .tower-name { font-size:13px; font-weight:700; color:#FFF; margin-bottom:6px; text-transform:uppercase; }
        .tower-info { font-size:10.5px; color:#9AA0AC; line-height:1.4; }

        /* COLUNAS DE EXISTÊNCIA & PORTÕES DE VISIBILIDADE */
        .colunas-title { font-family:'Cinzel',serif; font-size:18px; color:#E8D8C8; letter-spacing:2px; margin-bottom:15px; }
        .colunas-grid { display:grid; grid-template-columns:repeat(3, 1fr); gap:12px; margin-bottom:30px; }
        .btn-coluna { display:inline-flex; align-items:center; justify-content:center; gap:8px; background:rgba(212,184,134,0.05); border:1px solid rgba(212,184,134,0.25); color:#E8D8C8; font-size:11px; font-weight:700; padding:14px; border-radius:10px; text-decoration:none; text-transform:uppercase; letter-spacing:1px; transition:all 0.2s; }
        .btn-coluna:hover { background:rgba(212,184,134,0.18); border-color:#E8D8C8; color:#FFF; }

        /* RODAPÉ GLOBAL OFICIAL */
        footer { border-top:1px solid rgba(232,216,200,0.2); padding-top:20px; margin-top:30px; text-align:center; font-size:10.5px; color:#9AA0AC; line-height:1.8; }
        .footer-brand { font-family:'Cinzel',serif; color:#E8D8C8; font-size:12px; font-weight:800; letter-spacing:2px; margin-bottom:4px; }
    </style>
</head>
<body>

    <div class="main-container">
        <div class="hero-title">MALHA DE COMUNICAÇÃO GLOBAL IOTEC</div>
        <div class="hero-subtitle">Erguendo as torres de comando regionalizadas por fuso horário e integrando as colunas de visibilidade comercial para o escalonamento perpétuo da usina.</div>

        <!-- TORRES DE COMUNICAÇÃO (HANGAR LOCAL) -->
        <div class="towers-grid">
            <div class="tower-card">
                <div class="tower-fuso">GMT-3 | AMÉRICAS</div>
                <div class="tower-name">Hangar São Paulo</div>
                <div class="tower-info">Ativo 24/7. Central de Ativação WhatsApp, Auditoria B2B e Trava Anti-Fraude.</div>
            </div>

            <div class="tower-card">
                <div class="tower-fuso">GMT+1 | EUROPA</div>
                <div class="tower-name">Hangar Londres</div>
                <div class="tower-info">Ativo 24/7. Gestão de Cotas Orbitais, Jurídico SAFE e Compensação SAFE.</div>
            </div>

            <div class="tower-card">
                <div class="tower-fuso">GMT+9 | ÁSIA</div>
                <div class="tower-name">Hangar Tóquio</div>
                <div class="tower-info">Ativo 24/7. Arbitragem de Milhas, Liquidação Internacional e Central WeChat.</div>
            </div>
        </div>

        <!-- COLUNAS DE EXISTÊNCIA & PORTÕES DE VISIBILIDADE -->
        <div class="colunas-title">PORTÕES DE VISIBILIDADE COMERCIAL</div>
        <div class="colunas-grid">
            <a href="#" class="btn-coluna"><span>💬 WhatsApp (Nativo-BR)</span></a>
            <a href="#" class="btn-coluna"><span>📊 LinkedIn (B2B Global)</span></a>
            <a href="#" class="btn-coluna"><span>📱 WeChat (Ásia)</span></a>
            <a href="#" class="btn-coluna"><span>📧 E-mail (Europa)</span></a>
            <a href="#" class="btn-coluna"><span>☕ Café com Economia</span></a>
            <a href="#" class="btn-coluna"><span>🌐 Portal Web IOTEC</span></a>
        </div>
    </div>

    <!-- RODAPÉ OFICIAL MUNDIAL -->
    <footer>
        <div class="footer-brand">IOTEC ENTERPRISE SOFTWARE & FINANCIAL SYSTEMS</div>
        <div>CNPJ: 61.549.037/0001-68 | Governança: Farabulini Lopes Saraiva</div>
        <div style="margin-top:6px; font-size:9.5px; opacity:0.7;">© 2026 IOTEC Global. Malha de Satélites & Torres Orbitais. All rights reserved.</div>
    </footer>

</body>
</html>
"@

    $buffer = [System.Text.Encoding]::UTF8.GetBytes($html)
    $response.ContentLength64 = $buffer.Length
    $response.ContentType = "text/html; charset=utf-8"
    $response.OutputStream.Write($buffer, 0, $buffer.Length)
    $response.OutputStream.Close()
}
