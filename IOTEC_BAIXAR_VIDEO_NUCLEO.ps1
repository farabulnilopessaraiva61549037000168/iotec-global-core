# ============================================================
# IOTEC_BAIXAR_VIDEO_NUCLEO.ps1
# ============================================================

param(
    [string]$Url,
    [string]$Nome = "video_iotec.mp4",
    [string]$Categoria = "institucional"
)

$Base = "C:\IOTEC"
$DirVideos = Join-Path $Base "MEDIA\VIDEOS"
$DirCatalogo = Join-Path $Base "CATALOGO"
$JsonCatalogo = Join-Path $DirCatalogo "videos.json"

New-Item -ItemType Directory -Force -Path $DirVideos | Out-Null
New-Item -ItemType Directory -Force -Path $DirCatalogo | Out-Null

if ([string]::IsNullOrWhiteSpace($Url)) {
    Write-Host "ERRO: informe a URL do vídeo."
    exit 1
}

$Destino = Join-Path $DirVideos $Nome

try {
    Invoke-WebRequest -Uri $Url -OutFile $Destino -UseBasicParsing
} catch {
    Write-Host "ERRO ao baixar vídeo: $($_.Exception.Message)"
    exit 1
}

$item = [PSCustomObject]@{
    nome = $Nome
    categoria = $Categoria
    caminho = $Destino
    url_origem = $Url
    data_importacao = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
    pronto_para_front = $true
}

$catalogo = @()
if (Test-Path $JsonCatalogo) {
    try {
        $conteudo = Get-Content $JsonCatalogo -Raw -Encoding UTF8
        if (-not [string]::IsNullOrWhiteSpace($conteudo)) {
            $lido = $conteudo | ConvertFrom-Json
            if ($lido -is [System.Array]) {
                $catalogo = @($lido)
            } else {
                $catalogo = @($lido)
            }
        }
    } catch {
        $catalogo = @()
    }
}

$catalogo += $item
$catalogo | ConvertTo-Json -Depth 6 | Set-Content -Path $JsonCatalogo -Encoding UTF8

Write-Host "=============================================="
Write-Host "VÍDEO BAIXADO E INTEGRADO AO NÚCLEO"
Write-Host "ARQUIVO : $Destino"
Write-Host "CATÁLOGO: $JsonCatalogo"
Write-Host "=============================================="