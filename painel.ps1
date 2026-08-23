function Exibir-Menu {
    Clear-Host
    Write-Host "==============================================================" -ForegroundColor DarkCyan
    Write-Host "                  IOTEC - PAINEL OPERACIONAL                  " -ForegroundColor Cyan
    Write-Host "==============================================================" -ForegroundColor DarkCyan
    Write-Host " [1] Operário 1 - Coletor de Leads (Scraper)" -ForegroundColor Yellow
    Write-Host " [2] Operário 2 - Minerador & Sanitizador de E-mails" -ForegroundColor Yellow
    Write-Host " [3] Operário 3 - Disparador de Primeiras Abordagens (B2B)" -ForegroundColor Yellow
    Write-Host " [4] Operário 4 - Disparador de Follow-up (Re-engajamento)" -ForegroundColor Yellow
    Write-Host " [5] Relatório de Métricas Consolidado" -ForegroundColor Green
    Write-Host " [6] Sair" -ForegroundColor Red
    Write-Host "==============================================================" -ForegroundColor DarkCyan
}

do {
    Exibir-Menu
    $opcao = Read-Host "Escolha uma opção (1-6)"

    switch ($opcao) {
        "1" {
            Write-Host "`n[+] Executando Operário 1 (Coletor)..." -ForegroundColor Cyan
            python C:\IOTEC\operario_1_coletor.py
            Pause
        }
        "2" {
            Write-Host "`n[+] Executando Operário 2 (Minerador)..." -ForegroundColor Cyan
            python C:\IOTEC\operario_2_minerador.py
            Pause
        }
        "3" {
            Write-Host "`n[+] Executando Operário 3 (Primeiras Abordagens)..." -ForegroundColor Cyan
            python C:\IOTEC\operario_3_contatador.py
            Pause
        }
        "4" {
            Write-Host "`n[+] Executando Operário 4 (Follow-up)..." -ForegroundColor Cyan
            python C:\IOTEC\operario_4_followup.py
            Pause
        }
        "5" {
            python C:\IOTEC\relatorio.py
            Pause
        }
        "6" {
            Write-Host "`nSaindo do painel IOTEC... Até logo!" -ForegroundColor Green
            break
        }
        default {
            Write-Host "`nOpção inválida! Tente novamente." -ForegroundColor Red
            Start-Sleep -Seconds 1
        }
    }
} while ($opcao -ne "6")