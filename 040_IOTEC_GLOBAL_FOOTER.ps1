# =========================================================================================
#       USINA IOTEC — ATENDIMENTO POR ANDARES & RODAPÉ GLOBAL (PORTA 8240)
#       CNPJ: 61.549.037/0001-68 | Governança: Farabulini Lopes Saraiva
# =========================================================================================

$port = 8240
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC GLOBAL FOOTER — ATENDIMENTO POR ANDARES ATIVO (PORTA $port)" -ForegroundColor Green
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
    <title>IOTEC — Central Global & Atendimento por Andares</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#040507; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; min-height:100vh; display:flex; flex-direction:column; justify-content:space-between; padding:20px; }
        
        .main-container { max-width:900px; margin:0 auto; width:100%; text-align:center; padding-top:40px; }
        .hero-title { font-family:'Cinzel',serif; font-size:28px; color:#E8D8C8; letter-spacing:4px; margin-bottom:12px; }
        .hero-subtitle { font-size:13px; color:#9AA0AC; max-width:600px; margin:0 auto 30px auto; line-height:1.6; }
        
        /* ESTRUTURA DOS ANDARES TÉCNICOS */
        .floors-grid { display:grid; grid-template-columns:repeat(2, 1fr); gap:14px; margin-bottom:40px; text-align:left; }
        .floor-card { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.25); border-radius:12px; padding:18px; position:relative; overflow:hidden; }
        .floor-card:hover { border-color:#E8D8C8; }
        .floor-number { font-family:'Cinzel',serif; font-size:12px; color:#D4B886; font-weight:800; letter-spacing:1px; margin-bottom:4px; }
        .floor-name { font-size:14px; font-weight:700; color:#FFF; margin-bottom:6px; }
        .floor-desc { font-size:11px; color:#9AA0AC; line-height:1.4; }

        /* BOTÃO WHATSAPP COM NÚMERO EMBUTIDO NO NÚCLEO */
        .btn-whatsapp { display:inline-flex; align-items:center; gap:10px; background:rgba(74,222,128,0.12); border:1px solid #4ADE80; color:#4ADE80; font-size:12px; font-weight:800; padding:14px 28px; border-radius:30px; text-decoration:none; text-transform:uppercase; letter-spacing:1px; transition:all 0.2s; margin-top:10px; }
        .btn-whatsapp:hover { background:#4ADE80; color:#040507; box-shadow:0 0 20px rgba(74,222,128,0.4); }

        /* RODAPÉ GLOBAL OFICIAL */
        footer { border-top:1px solid rgba(232,216,200,0.2); padding-top:24px; margin-top:40px; text-align:center; font-size:10.5px; color:#9AA0AC; line-height:1.8; }
        .footer-brand { font-family:'Cinzel',serif; color:#E8D8C8; font-size:12px; font-weight:800; letter-spacing:2px; margin-bottom:4px; }
        .footer-legal { font-size:10px; color:#D4B886; font-weight:600; }
    </style>
</head>
<body>

    <div class="main-container">
        <div class="hero-title">EDIFÍCIO TÉCNICO IOTEC</div>
        <div class="hero-subtitle">Navegue pelos andares operacionais da plataforma ou inicie o atendimento especializado pelo WhatsApp para ativação de módulos e suporte.</div>

        <div class="floors-grid">
            <div class="floor-card">
                <div class="floor-number">ANDAR 01</div>
                <div class="floor-name">Gastronomia & Delivery Express</div>
                <div class="floor-desc">Marmitarias, Açaíterias e Pizzarias. Trava técnica anti-PIX falso e sincronização de cozinha.</div>
            </div>

            <div class="floor-card">
                <div class="floor-number">ANDAR 02</div>
                <div class="floor-name">Serviços & Agenda Blindada</div>
                <div class="floor-desc">Bronzeamento, Salões de Beleza e Pet Shops. Confirmação de agendamento via sinal bancário real.</div>
            </div>

            <div class="floor-card">
                <div class="floor-number">ANDAR 03</div>
                <div class="floor-name">Eventos, Festas & Conveniência</div>
                <div class="floor-desc">Bares de alto fluxo e casas de show. Fechamento cego de caixa, troco exato e emissão de fichas.</div>
            </div>

            <div class="floor-card">
                <div class="floor-number">ANDAR 04</div>
                <div class="floor-name">Mesa de Investimentos & Cotas Orbitais</div>
                <div class="floor-desc">Portal Café com Economia. Alocação de capital e rentabilidade via contrato Mútuo Conversível (SAFE).</div>
            </div>
        </div>

        <!-- LINK PARA O WHATSAPP DA ATENDENTE (NÚMERO MANTIDO NO MÚCLEO) -->
        <a href="https://wa.me/5500000000000?text=Ol%C3%A1!%20Desejo%20falar%20com%20a%20atendente%20para%20acessar%20os%20andares%20t%C3%A9cnicos%20da%20IOTEC." target="_blank" class="btn-whatsapp">
            <span>💬 Falar com Atendente — Central de Ativação & Andares Técnicos</span>
        </a>
    </div>

    <!-- RODAPÉ OFICIAL MUNDIAL -->
    <footer>
        <div class="footer-brand">IOTEC ENTERPRISE SOFTWARE & FINANCIAL SYSTEMS</div>
        <div class="footer-legal">Corporate Tax ID (CNPJ): 61.549.037/0001-68</div>
        <div>Governance: Farabulini Lopes Saraiva — Founder & Chief Technology Officer</div>
        <div>Executive Support: IOTEC.BL@proton.me</div>
        <div style="margin-top:8px; font-size:9.5px; opacity:0.7;">© 2026 IOTEC Global. All rights reserved. Zero-Downtime B2B Infrastructure & Automated Clearing.</div>
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
