# =========================================================================================
#       USINA IOTEC — TRANSMISSÃO DE SINAL E HOMOLOGAÇÃO REMOTA (PORTA 8230)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8230
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC SIGNAL HOMOLOGATION — PONTE ATIVA NA PORTA $port" -ForegroundColor Green
    Write-Host "     Acesse no seu navegador: http://localhost:$port/" -ForegroundColor Yellow
    Write-Host "=================================================================`n" -ForegroundColor Cyan
} catch {
    Write-Host "[ERRO] Não foi possível iniciar a porta $port." -ForegroundColor Red
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
    <title>IOTEC — Central de Sinal & Homologação Remota</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#040507; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; height:100vh; display:flex; justify-content:center; align-items:center; padding:16px; }
        .card { background:#0B0E14; border:1px solid #D4B886; border-radius:16px; padding:24px; max-width:500px; width:100%; box-shadow:0 10px 30px rgba(0,0,0,0.8); }
        .title { font-family:'Cinzel',serif; color:#E8D8C8; font-size:16px; margin-bottom:12px; border-bottom:1px solid rgba(212,184,134,0.2); padding-bottom:8px; }
        .status-box { background:rgba(74,222,128,0.1); border:1px solid #4ADE80; color:#4ADE80; padding:10px; border-radius:8px; font-size:11px; font-weight:700; margin-bottom:14px; text-align:center; }
        .info { font-size:11px; color:#9AA0AC; line-height:1.5; margin-bottom:10px; }
    </style>
</head>
<body>
    <div class="card">
        <div class="title">IOTEC — PONTE DE SINAL & AJUSTE DE FOCO REMOTO</div>
        <div class="status-box">● TRANSMISSÃO ESTÁVEL E HOMOLOGADA</div>
        
        <div class="info">
            <strong>CNPJ:</strong> 61.549.037/0001-68 | <strong>Governança:</strong> Bruno (Fundador)<br>
            <strong>Status de Conexão:</strong> O terminal do cliente está conectado à central. Os produtos contratados foram transmitidos e acomodados nas interfaces do sistema.<br>
            <strong>Ajuste de Foco:</strong> Sincronização remota em andamento pela equipe de operações até atingir 100% de nitidez.
        </div>
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
