$base = "C:\IOTEC\IOTEC_RENDER_READY\static"
$saida = "C:\IOTEC\RELATORIO_INTERFACE.txt"

"===== ANALISE IOTEC =====" | Out-File $saida

Get-ChildItem $base -Filter *.html | ForEach-Object {

    "`n📄 ARQUIVO: $($_.Name)" | Add-Content $saida

    $c = Get-Content $_.FullName -Raw

    # extrair botões
    ($c | Select-String "<button.*?>.*?</button>" -AllMatches).Matches.Value | ForEach-Object {
        "[BOTAO] $_" | Add-Content $saida
    }

    # extrair links
    ($c | Select-String "<a.*?>.*?</a>" -AllMatches).Matches.Value | ForEach-Object {
        "[LINK] $_" | Add-Content $saida
    }

    # extrair forms
    ($c | Select-String "<form.*?>.*?</form>" -AllMatches).Matches.Value | ForEach-Object {
        "[FORM] $_" | Add-Content $saida
    }
}

# analisar JS
$js = "$base\main.js"
if (Test-Path $js) {

    "`n📜 MAIN.JS" | Add-Content $saida

    $c = Get-Content $js -Raw

    ($c | Select-String "function .*?\(" -AllMatches).Matches.Value | ForEach-Object {
        "[FUNCAO] $_" | Add-Content $saida
    }

    ($c | Select-String "fetch\(.*?\)" -AllMatches).Matches.Value | ForEach-Object {
        "[API] $_" | Add-Content $saida
    }

    ($c | Select-String "addEventListener.*" -AllMatches).Matches.Value | ForEach-Object {
        "[EVENTO] $_" | Add-Content $saida
    }
}

Write-Host "✅ RELATÓRIO GERADO EM: $saida" -ForegroundColor Green
