# =========================================================================================
#       USINA IOTEC — QUARTEL GENERAL & SALA DE COMANDO CENTRAL (PORTA 8000)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8000
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC WAR ROOM — SALA DE COMANDO CENTRAL ATIVA (PORTA $port)" -ForegroundColor Green
    Write-Host "     Acesse no seu navegador: http://localhost:$port/" -ForegroundColor Yellow
    Write-Host "=================================================================`n" -ForegroundColor Cyan
} catch {
    Write-Host "[ERRO] Nao foi possivel iniciar na porta $port." -ForegroundColor Red
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
    <title>IOTEC — Central War Room & Dominio Operacional</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#030406; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; height:100vh; display:grid; grid-template-rows:65px 1fr 40px; padding:14px; gap:12px; }
        header { background:rgba(10,12,18,0.9); border:1px solid rgba(212,184,134,0.3); border-radius:12px; display:flex; justify-content:space-between; align-items:center; padding:0 24px; }
        .brand { font-family:'Cinzel',serif; font-size:20px; color:#E8D8C8; letter-spacing:4px; font-weight:800; }
        .badge-hq { background:rgba(212,184,134,0.15); border:1px solid #D4B886; color:#D4B886; padding:5px 14px; border-radius:20px; font-size:10.5px; font-weight:700; letter-spacing:1px; }
        .main-grid { display:grid; grid-template-columns:300px 1fr; gap:12px; height:100%; overflow:hidden; }
        .panel { background:rgba(10,12,18,0.85); border:1px solid rgba(212,184,134,0.25); border-radius:14px; padding:18px; display:flex; flex-direction:column; gap:14px; overflow-y:auto; }
        .title { font-family:'Cinzel',serif; color:#E8D8C8; font-size:14px; border-bottom:1px solid rgba(212,184,134,0.2); padding-bottom:6px; letter-spacing:1px; }
        .module-link { display:flex; justify-content:space-between; align-items:center; background:rgba(212,184,134,0.05); border:1px solid rgba(212,184,134,0.2); padding:10px 12px; border-radius:8px; color:#FFF; text-decoration:none; font-size:11px; font-weight:600; transition:all 0.2s; }
        .module-link:hover { background:rgba(212,184,134,0.18); border-color:#E8D8C8; }
        .metrics-container { display:grid; grid-template-columns:repeat(3, 1fr); gap:10px; }
        .metric-card { background:rgba(6,7,10,0.9); border:1px solid rgba(212,184,134,0.2); border-radius:10px; padding:14px; }
        .m-title { font-size:9.5px; color:#D4B886; text-transform:uppercase; font-weight:700; letter-spacing:1px; }
        .m-val { font-size:20px; font-weight:800; color:#FFF; margin-top:4px; font-family:'Cinzel',serif; }
        .terminal { background:rgba(4,5,7,0.95); border:1px solid rgba(212,184,134,0.25); border-radius:10px; padding:12px; height:100%; font-family:monospace; font-size:11px; color:#E8D8C8; display:flex; flex-direction:column; gap:6px; overflow-y:auto; }
        footer { display:flex; justify-content:space-between; font-size:9px; color:#9AA0AC; text-transform:uppercase; letter-spacing:1px; }
    </style>
</head>
<body>
    <header>
        <div class="brand">IOTEC WAR ROOM — SITES & COMANDO CENTRAL</div>
        <div class="badge-hq">● COMANDO PLANETARIO DE OPERACOES</div>
    </header>

    <div class="main-grid">
        <!-- PAINEL LATERAL DE TERMINAIS E SERVIDORES -->
        <div class="panel">
            <div class="title">Terminais Ativos</div>
            <a href="http://localhost:8170/" target="_blank" class="module-link"><span>8170 - Cafe com Economia</span> <small>→</small></a>
            <a href="http://localhost:8180/" target="_blank" class="module-link"><span>8180 - Delivery Audit</span> <small>→</small></a>
            <a href="http://localhost:8190/" target="_blank" class="module-link"><span>8190 - Rede Multicatalogo</span> <small>→</small></a>
            <a href="http://localhost:8200/" target="_blank" class="module-link"><span>8200 - App Mobile PWA</span> <small>→</small></a>
            <a href="http://localhost:8210/" target="_blank" class="module-link"><span>8210 - Motor de Estorno</span> <small>→</small></a>
            <a href="http://localhost:8220/" target="_blank" class="module-link"><span>8220 - Hub Comercial B2B</span> <small>→</small></a>

            <div class="title" style="margin-top:10px;">Monopolizacao de Carteiras</div>
            <div style="font-size:10px; color:#9AA0AC; line-height:1.4;">
                Cadeias de arrecadacao conectadas via Mútuo Conversível (SAFE). Recolhimento automático de taxas de processamento.
            </div>
        </div>

        <!-- AREA CENTRAL DE VISUALIZACAO E DASHBOARD -->
        <div class="panel">
            <div class="metrics-container">
                <div class="metric-card">
                    <div class="m-title">GMV Auditado (Diario)</div>
                    <div class="m-val">R$ 148.500,00</div>
                </div>
                <div class="metric-card">
                    <div class="m-title">Cotas Orbitais Ativas</div>
                    <div class="m-val">1.250 Lotes</div>
                </div>
                <div class="metric-card">
                    <div class="m-title">Retencao por Aporte</div>
                    <div class="m-val">22,4% a.m.</div>
                </div>
            </div>

            <div class="title" style="margin-top:8px;">Logs Unificados da Cadeia Financeira</div>
            <div class="terminal" id="term">
                <div>[COMANDO CENTRAL INICIALIZADO] Varredura dos 6 terminais concluida com sucesso.</div>
                <div>[MONOPOLIZACAO] Regra de captura de taxa de suporte ativada em todos os modulos.</div>
                <div style="color:#4ADE80;">[GOVERNANCA] CNPJ 61.549.037/0001-68 operando em capacidade nominal sem divergencias.</div>
            </div>
        </div>
    </div>

    <footer>
        <div>© IOTEC — USINA TECHNOLOGICAL PLATFORM</div>
        <div>MESA DE GOVERNANCA: BRUNO (FUNDADOR)</div>
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
