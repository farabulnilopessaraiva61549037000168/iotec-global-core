
Clear-Host

Write-Host ""
Write-Host "==============================================="
Write-Host "IOTEC ORCHESTRATOR DETECTOR"
Write-Host "==============================================="
Write-Host ""

$ROOT = Read-Host "Digite a pasta do núcleo"

if (!(Test-Path $ROOT)) {

    Write-Host ""
    Write-Host "Pasta não encontrada."
    pause
    exit
}

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

$PATTERNS = @(
    "orchestrator",
    "workflow",
    "pipeline",
    "scheduler",
    "dispatcher",
    "taskmanager",
    "coordinator",
    "runtime",
    "executor",
    "queue",
    "worker",
    "agent",
    "automation",
    "monitor",
    "controller",
    "router",
    "integration",
    "trigger",
    "state",
    "manager"
)

$results = @()

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

    foreach ($pattern in $PATTERNS) {

        if ($lower.Contains($pattern)) {

            $results += $file.FullName
            break
        }
    }
}

$results = $results | Select-Object -Unique

$output = @()

$output += "======================================="
$output += "ORCHESTRATOR ANALYSIS"
$output += "======================================="
$output += ""

$output += "TOTAL DE ARQUIVOS:"
$output += $results.Count
$output += ""

foreach ($item in $results[0..([Math]::Min(50, $results.Count)-1)]) {

    $output += $item
}

$output += ""
$output += "======================================="
$output += "DIAGNÓSTICO"
$output += "======================================="
$output += ""

if ($results.Count -gt 100) {

    $output += "ORQUESTRADOR AVANÇADO DETECTADO"

} elseif ($results.Count -gt 30) {

    $output += "ESTRUTURA DE ORQUESTRAÇÃO MODERADA"

} elseif ($results.Count -gt 0) {

    $output += "INDÍCIOS DE ORQUESTRAÇÃO"

} else {

    $output += "ORQUESTRADOR NÃO DETECTADO"
}

$output += ""
$output += "O núcleo pode possuir:"
$output += "- automações"
$output += "- pipelines"
$output += "- agentes"
$output += "- workers"
$output += "- controladores"
$output += "- módulos fragmentados"

$REPORT = "ORCHESTRATOR_ANALYSIS.txt"

$output | Out-File $REPORT -Encoding UTF8

Write-Host ""
Write-Host "==============================================="
Write-Host "ANÁLISE FINALIZADA"
Write-Host "==============================================="
Write-Host ""

Write-Host "Relatório salvo:"
Write-Host $REPORT

Start-Process notepad.exe $REPORT

Write-Host ""
Write-Host "Pressione ENTER para sair..."
Read-Host

