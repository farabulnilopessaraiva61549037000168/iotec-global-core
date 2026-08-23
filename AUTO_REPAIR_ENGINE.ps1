$ErrorActionPreference = "Stop"

$target = "C:\IOTEC\FROZEN\visible_core_router.py"
$backup = "C:\IOTEC\FROZEN\visible_core_router.AUTO_BACKUP.py"

Write-Host "[IOTEC] AUTO REPAIR ENGINE iniciado"

# 1. BACKUP OBRIGATÓRIO
Copy-Item $target $backup -Force
Write-Host "[OK] Backup criado"

# 2. LER ARQUIVO
$content = Get-Content $target -Raw

# 3. REMOVER BOM INVISÍVEL
$content = $content -replace "^\uFEFF", ""

# 4. CORREÇÃO AUTOMÁTICA DE CONFIG (segura)
$content = $content -replace `
"self\.config\s*\[\s*['`"]paths['`"]\s*\]\s*\[\s*['`"]logs_dir['`"]\s*\]", `
'self.config.get("paths", {}).get("logs_dir", "logs")'

# 5. GARANTIR PROTEÇÃO DE CONFIG NO INIT (injeção controlada)
if ($content -notmatch "setdefault\(") {
    $inject = @"
        if getattr(self, "config", None) is None:
            self.config = {}

        self.config.setdefault("paths", {})
        self.config["paths"].setdefault("logs_dir", "logs")
        self.config["paths"].setdefault("snapshots_dir", "snapshots")
"@

    $content = $content -replace "def __init__\([^)]*\):", "`$&`n$inject"
}

# 6. VALIDAÇÃO BÁSICA DE PARENTESES
$open = ($content.ToCharArray() | Where-Object { $_ -eq '(' }).Count
$close = ($content.ToCharArray() | Where-Object { $_ -eq ')' }).Count

if ($open -ne $close) {
    Write-Host "[ERRO] Parênteses não balanceados - abortando escrita"
    exit 1
}

# 7. VALIDAR KEY ERROR CRÍTICO
if ($content -match "\['paths'\]\['logs_dir'\]") {
    Write-Host "[WARN] padrão inseguro ainda presente"
}

# 8. GRAVAR ARQUIVO LIMPO
[System.IO.File]::WriteAllText(
    $target,
    $content,
    (New-Object System.Text.UTF8Encoding $false)
)

Write-Host "[OK] AUTO PATCH CONCLUÍDO COM SUCESSO"