# ============================================================
# IOTEC_TRIAGEM_DOWNLOADS.ps1
# ============================================================

$DOWNLOADS = "$env:USERPROFILE\Downloads"
$DESTINO = "C:\IOTEC\MINA_IMPORTADA"

$HTML = Join-Path $DESTINO "HTML"
$PY = Join-Path $DESTINO "PYTHON"
$JS = Join-Path $DESTINO "JS"
$IMG = Join-Path $DESTINO "IMAGENS"
$OUTROS = Join-Path $DESTINO "OUTROS"

$pastas = @($DESTINO, $HTML, $PY, $JS, $IMG, $OUTROS)

foreach ($p in $pastas) {
    New-Item -ItemType Directory -Force -Path $p | Out-Null
}

Write-Host ">> VARRENDO DOWNLOADS..."

$arquivos = Get-ChildItem -Path $DOWNLOADS -File -Recurse -ErrorAction SilentlyContinue

foreach ($arq in $arquivos) {

    $destinoFinal = ""

    switch ($arq.Extension.ToLower()) {
        ".html" { $destinoFinal = $HTML }
        ".htm"  { $destinoFinal = $HTML }
        ".py"   { $destinoFinal = $PY }
        ".js"   { $destinoFinal = $JS }
        ".png"  { $destinoFinal = $IMG }
        ".jpg"  { $destinoFinal = $IMG }
        ".jpeg" { $destinoFinal = $IMG }
        ".webp" { $destinoFinal = $IMG }
        default { $destinoFinal = $OUTROS }
    }

    try {
        Copy-Item $arq.FullName -Destination $destinoFinal -Force
    } catch {}
}

Write-Host "======================================="
Write-Host "TRIAGEM FINALIZADA"
Write-Host "Arquivos organizados em:"
Write-Host "C:\IOTEC\MINA_IMPORTADA"
Write-Host "======================================="