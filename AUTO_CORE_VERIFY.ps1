Clear-Host

Write-Host ""
Write-Host "========================================="
Write-Host "IOTEC AUTO CORE VERIFY"
Write-Host "========================================="
Write-Host ""

# =====================================================
# ESCOLHER PASTA
# =====================================================

$ROOT = Read-Host "Digite o caminho do núcleo"

if (!(Test-Path $ROOT)) {

    Write-Host ""
    Write-Host "Pasta não encontrada."
    pause
    exit
}

# =====================================================
# IGNORAR
# =====================================================

$IGNORE = @(
    "node_modules",
    ".git",
    "__pycache__",
    "dist",
    "build",
    ".next",
    ".cache",
    "venv",
    ".venv"
)

# =====================================================
# ASSINATURAS
# =====================================================

$SIGNATURES = @{

    "IA_SYSTEM" = @(
        "openai",
        "gpt",
        "agent",
        "langchain",
        "embedding",
        "rag"
    )

    "CHAT_SYSTEM" = @(
        "chat",
        "conversation",
        "whatsapp",
        "telegram",
        "discord"
    )

    "PAYMENT_SYSTEM" = @(
        "stripe",
        "payment",
        "checkout",
        "paypal"
    )

    "CRM_SYSTEM" = @(
        "crm",
        "lead",
        "pipeline",
        "sales"
    )

    "AUTH_SYSTEM" = @(
        "auth",
        "login",
        "jwt",
        "token"
    )

    "API_SYSTEM" = @(
        "api",
        "router",
        "endpoint",
        "fastapi",
        "flask",
        "express"
    )

    "DASHBOARD_SYSTEM" = @(
        "dashboard",
        "panel",
        "admin",
        "analytics"
    )

    "AUTOMATION_SYSTEM" = @(
        "automation",
        "workflow",
        "trigger",
        "cron"
    )

    "ENGINE_SYSTEM" = @(
        "engine",
        "core",
        "processor",
        "runtime"
    )

    "DATABASE_SYSTEM" = @(
        "mongodb",
        "postgres",
        "mysql",
        "sqlite",
        "redis"
    )

    "FRONTEND_SYSTEM" = @(
        "react",
        "next",
        "vue",
        "component"
    )

    "BACKEND_SYSTEM" = @(
        "backend",
        "server",
        "service",
        "controller"
    )
}

# =====================================================
# RESULTADOS
# =====================================================

$Results = @{}

foreach ($key in $SIGNATURES.Keys) {
    $Results[$key] = @()
}

# =====================================================
# INVESTIGAÇÃO
# =====================================================

Write-Host ""
Write-Host "Investigando núcleo..."
Write-Host ""

$files = Get-ChildItem -Path $ROOT -Recurse -File -ErrorAction SilentlyContinue

foreach ($file in $files) {

    $skip = $false

    foreach ($ignoreDir in $IGNORE) {

        if ($file.FullName -like "*\$ignoreDir\*") {
            $skip = $true
            break
        }
    }

    if ($skip) {
        continue
    }

    $lower = $file.Name.ToLower()

    foreach ($system in $SIGNATURES.Keys) {

        foreach ($pattern in $SIGNATURES[$system]) {

            if ($lower.Contains($pattern)) {

                $Results[$system] += $file.FullName
                break
            }
        }
    }
}

# =====================================================
# RELATÓRIO
# =====================================================

$output = @()

$output += "====================================="
$output += "IOTEC VERIFIED CORE REPORT"
$output += "====================================="
$output += ""

$output += "Projeto:"
$output += $ROOT
$output += ""

# =====================================================
# DIAGNÓSTICO
# =====================================================

$output += "====================================="
$output += "DIAGNÓSTICO FINAL"
$output += "====================================="
$output += ""

foreach ($system in $Results.Keys) {

    $count = ($Results[$system] | Select-Object -Unique).Count

    if ($count -gt 100) {

        $level = "MUITO FORTE"

    } elseif ($count -gt 40) {

        $level = "FORTE"

    } elseif ($count -gt 10) {

        $level = "MODERADO"

    } elseif ($count -gt 0) {

        $level = "EXISTE"

    } else {

        $level = "NÃO DETECTADO"
    }

    $output += "$system -> $level ($count)"
}

# =====================================================
# SALVAR
# =====================================================

$REPORT = "VERIFIED_CORE_REPORT.txt"

$output | Out-File $REPORT -Encoding UTF8

Write-Host ""
Write-Host "========================================="
Write-Host "VERIFICAÇÃO CONCLUÍDA"
Write-Host "========================================="
Write-Host ""

Write-Host "Relatório salvo:"
Write-Host $REPORT

# =====================================================
# ABRIR AUTOMATICAMENTE
# =====================================================

Start-Process notepad.exe $REPORT