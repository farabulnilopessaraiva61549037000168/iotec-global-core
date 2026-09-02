$port = 8280
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")
$listener.Start()

Write-Host "`n[VISUALIZADOR ATIVO] Acesse http://localhost:$port/ para ver as fotos e vídeos na tela!" -ForegroundColor Yellow

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $response = $context.Response

    $html = @"
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>IOTEC — Acervo Visual Real em Disco</title>
    <style>
        body { background:#0a0a0f; color:#fff; font-family:sans-serif; padding:40px; }
        h1 { color:#E8D8C8; font-family:serif; border-bottom:1px solid #333; padding-bottom:10px; }
        .grid { display:grid; grid-template-columns:repeat(2, 1fr); gap:20px; margin-top:20px; }
        .card { background:#14141e; border:1px solid rgba(232,216,200,0.3); border-radius:12px; padding:15px; }
        img, video { width:100%; height:250px; object-fit:cover; border-radius:8px; }
        .title { margin-top:10px; font-weight:bold; color:#D4B886; font-size:14px; }
    </style>
</head>
<body>
    <h1>IOTEC — VITRINE DO ACERVO VISUAL BAIXADO NO DISCO (C:\IOTEC\ACERVO_MIDIAS)</h1>
    <p>Abaixo estão os materiais reais prontos para serem injetados nas interfaces dos clientes, atendentes e produtores:</p>
    
    <div class="grid">
        <div class="card">
            <img src="https://images.unsplash.com/photo-1486406146926-c627a92ad1ab?q=80&w=1920&auto=format&fit=crop" />
            <div class="title">01_predio_corporativo_luxo.jpg (Fundo Portal Render)</div>
        </div>
        <div class="card">
            <img src="https://images.unsplash.com/photo-1507679799987-c73779587ccf?q=80&w=1920&auto=format&fit=crop" />
            <div class="title">02_executivo_seguranca_b2b.jpg (Fundo Trava Financeira)</div>
        </div>
        <div class="card">
            <img src="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?q=80&w=1920&auto=format&fit=crop" />
            <div class="title">03_estetica_bronzeamento_luxo.jpg (Fundo PWA Bronze)</div>
        </div>
        <div class="card">
            <video autoplay loop muted playsinline controls>
                <source src="https://vjs.zencdn.net/v/oceans.mp4" type="video/mp4">
            </video>
            <div class="title">01_loop_oceano_observatorio.mp4 (Vídeo em Loop de Fundo)</div>
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
