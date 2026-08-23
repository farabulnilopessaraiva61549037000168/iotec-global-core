Param(
    [Parameter(Mandatory=$true)]
    [string]$IpVps,
    
    [string]$Usuario = "root"
)

if ($IpVps -eq "SEU_IP_AQUI" -or $IpVps -eq "123.45.67.89" -or [string]::IsNullOrWhiteSpace($IpVps)) {
    Write-Host "❌ ERRO: Substitua o IP pelo IP real fornecido pela sua VPS!" -ForegroundColor Red
    Exit
}

$binDir = "C:\IOTEC\bin"
if (-not (Test-Path $binDir)) { New-Item -ItemType Directory -Path $binDir | Out-Null }

$plink = "$binDir\plink.exe"
$pscp  = "$binDir\pscp.exe"

if (-not (Test-Path $plink)) {
    Write-Host "Baixando utilitário SSH portátil (plink.exe)..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri "https://the.earth.li/~sgtatham/putty/latest/w64/plink.exe" -OutFile $plink
}

if (-not (Test-Path $pscp)) {
    Write-Host "Baixando utilitário SCP portátil (pscp.exe)..." -ForegroundColor Yellow
    Invoke-WebRequest -Uri "https://the.earth.li/~sgtatham/putty/latest/w64/pscp.exe" -OutFile $pscp
}

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host " INICIANDO DEPLOY AUTOMÁTICO DA IOTEC PARA VPS: $IpVps " -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan

# 1. Criar diretório remoto
Write-Host "`n1. Criando diretório /app/IOTEC na VPS..." -ForegroundColor Yellow
& $plink -batch -ssh "${Usuario}@${IpVps}" "mkdir -p /app/IOTEC"

# 2. Enviar arquivos
Write-Host "`n2. Enviando arquivos de C:\IOTEC para a VPS..." -ForegroundColor Yellow
& $pscp -batch -r C:\IOTEC\* "${Usuario}@${IpVps}:/app/IOTEC/"

# 3. Executar setup
Write-Host "`n3. Executando instalação automática do Docker na VPS..." -ForegroundColor Yellow
& $plink -batch -ssh "${Usuario}@${IpVps}" "chmod +x /app/IOTEC/setup_vps.sh && /app/IOTEC/setup_vps.sh"

Write-Host "`n✅ DEPLOY CONCLUÍDO COM SUCESSO!" -ForegroundColor Green
