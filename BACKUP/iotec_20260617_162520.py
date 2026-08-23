import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
param(

    [string]$Command

)



$Base = "C:\IOTEC"



function Log {

    param($msg)

    $logPath = "$Base\LOGS\iotec_command.log"

    Add-Content -Path $logPath -Value "$(Get-Date) - $msg"

}



function Run-Python {

    param($script)



    $full = Join-Path $Base $script



    if (-not (Test-Path $full)) {

        Write-Host "ERRO: Script nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o encontrado: $script" -ForegroundColor Red

        return

    }



    Write-Host "Executando: $script" -ForegroundColor Cyan

    Log "EXEC $script"



    python $full

}



switch ($Command) {



    "miner" {

        Run-Python "CORE\runtime\run_demo_cycle.py"

    }



    "full" {

        Run-Python "CORE\runtime\run_demo_cycle.py"

    }



    "api" {

        Run-Python "CORE\gateway\visible_core_api.py"

    }



    "repair" {

        & "$Base\repair_nucleus.ps1"

    }



    "status" {

        Write-Host "Nucleo IOTEC ativo" -ForegroundColor Green

        Write-Host "Base: $Base"

    }



    default {

        Write-Host "Comando invalido" -ForegroundColor Red

        Write-Host "Use:"

        Write-Host "  iotec miner"

        Write-Host "  iotec full"

        Write-Host "  iotec api"

        Write-Host "  iotec repair"

        Write-Host "  iotec status"

    }

}





