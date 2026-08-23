$base = "C:\IOTEC\IOTEC_RENDER_READY\static"

Write-Host "🚀 REANIMANDO INTERFACE" -ForegroundColor Cyan

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    # Corrigir links mortos
    $c = $c -replace 'href="#"', 'href="/"'

    # Corrigir botões com onclick vazio
    $c = $c -replace 'onclick=""', ''

    # Ativar formulários
    if ($c -match "<form" -and $c -notmatch "action=") {
        $c = $c -replace "<form", '<form action="/enviar" method="post"'
        Write-Host "✔ Form ativado: $($_.Name)"
    }

    Set-Content $_.FullName $c
}

Write-Host "🔧 Criando script JS universal..." -ForegroundColor Yellow

$js = @"
document.addEventListener("DOMContentLoaded", function() {

    console.log("IOTEC MOTOR ATIVO");

    // Corrigir botões que não fazem nada
    document.querySelectorAll("button").forEach(btn => {
        btn.addEventListener("click", function() {
            console.log("Botão clicado:", btn.innerText);
        });
    });

    // Corrigir links mortos
    document.querySelectorAll("a").forEach(link => {
        if (link.getAttribute("href") === "#") {
            link.setAttribute("href", "/");
        }
    });

});
"@

$js | Out-File "$base\iotec_fix.js" -Encoding UTF8

Write-Host "🔗 Injetando JS nas páginas..." -ForegroundColor Yellow

Get-ChildItem $base -Filter *.html | ForEach-Object {

    $c = Get-Content $_.FullName -Raw

    if ($c -notmatch "iotec_fix.js") {
        $c = $c -replace "</body>", '<script src="/iotec_fix.js"></script></body>'
    }

    Set-Content $_.FullName $c
}

Write-Host "✅ INTERFACE REATIVADA" -ForegroundColor Green
