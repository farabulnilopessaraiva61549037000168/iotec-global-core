# =========================================================================================
#           USINA IOTEC — AGENTE CONSTRUTOR DE NOVOS AGENTES (METAGESTOR)
# =========================================================================================

$dbPath = "C:\IOTEC\iotec_kernel.db"

Write-Host "`n=========================================================================================" -ForegroundColor Cyan
Write-Host "     USINA IOTEC — ACTIVATING AGENT BUILDER & DYNAMIC SYSTEM EXPANSION     " -ForegroundColor Cyan
Write-Host "=========================================================================================`n" -ForegroundColor Cyan

$initDbScript = @"
import sqlite3
conn = sqlite3.connect(r'$dbPath')
c = conn.cursor()
c.execute('''
    CREATE TABLE IF NOT EXISTS iotec_system_agents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_agente TEXT UNIQUE,
        funcao_descricao TEXT,
        linguagem TEXT,
        caminho_script TEXT,
        status TEXT DEFAULT 'QUARENTENA',
        data_criacao DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()
conn.close()
"@

$pyInitPath = "C:\IOTEC\temp_init_agents.py"
Set-Content -Path $pyInitPath -Value $initDbScript -Encoding UTF8
python $pyInitPath
Remove-Item -Path $pyInitPath -ErrorAction SilentlyContinue

Write-Host "[CARTÓRIO] Tabela 'iotec_system_agents' verificada no iotec_kernel.db." -ForegroundColor Yellow

function New-IotecAgent {
    param (
        [string]$NomeAgente,
        [string]$FuncaoDescricao,
        [string]$Linguagem,
        [string]$CodigoFonte
    )

    Write-Host "`n[CONSTRUTOR] Processando nova demanda funcional: $NomeAgente..." -ForegroundColor Green

    $extensao = if ($Linguagem -eq "Python") { "py" } else { "ps1" }
    $caminhoArquivo = "C:\IOTEC\${NomeAgente}.${extensao}"

    Set-Content -Path $caminhoArquivo -Value $CodigoFonte -Encoding UTF8
    Write-Host "[OK] Código gerado e salvo em: $caminhoArquivo" -ForegroundColor Cyan

    $registerPy = @"
import sqlite3
conn = sqlite3.connect(r'$dbPath')
c = conn.cursor()
c.execute('''
    INSERT OR REPLACE INTO iotec_system_agents (nome_agente, funcao_descricao, linguagem, caminho_script, status)
    VALUES (?, ?, ?, ?, 'QUARENTENA')
''', ('$NomeAgente', '$FuncaoDescricao', '$Linguagem', r'$caminhoArquivo'))
conn.commit()
conn.close()
"@

    $pyRegPath = "C:\IOTEC\temp_reg_agent.py"
    Set-Content -Path $pyRegPath -Value $registerPy -Encoding UTF8
    python $pyRegPath
    Remove-Item -Path $pyRegPath -ErrorAction SilentlyContinue

    Write-Host "[REGISTRO] Agente '$NomeAgente' catalogado no kernel com status: QUARENTENA." -ForegroundColor Yellow
    Write-Host "[GOVERNANÇA] Aguardando aprovação manual do fundador Bruno para promoção a PRODUÇÃO.`n" -ForegroundColor DarkGray
}

Write-Host "=========================================================================================" -ForegroundColor Cyan
Write-Host " [USINA IOTEC] Agente Construtor Pronto para Receber Novas Instruções." -ForegroundColor Cyan
Write-Host "=========================================================================================`n" -ForegroundColor Cyan
