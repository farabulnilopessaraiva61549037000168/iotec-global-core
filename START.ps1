###############################################################################
#
# IOTEC OPERATING CORE
# START.PS1
#
# BOOT LOADER
#
###############################################################################

Clear-Host

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "==============================================================="
Write-Host "               IOTEC OPERATING CORE"
Write-Host "                    BOOT LOADER"
Write-Host "==============================================================="
Write-Host ""

$Root = "C:\IOTEC"

$DB = "$Root\DB"

$Backup = "$DB\BACKUP"

$DatabaseFile = "$DB\IOTEC_DATABASE.json"

###############################################################

$Folders = @(

    $Root,

    $DB,

    $Backup,

    "$Root\CORE",

    "$Root\MODULES",

    "$Root\REPORTS",

    "$Root\SERVICES",

    "$Root\LOGS",

    "$Root\CONFIG"

)

foreach($Folder in $Folders){

    if(!(Test-Path $Folder)){

        New-Item `
            -ItemType Directory `
            -Force `
            -Path $Folder | Out-Null

    }

}

###############################################################

$Global:IOTEC = @{

    Project="IOTEC OPERATING CORE"

    Version="1.0.0"

    Started=Get-Date

    Status="ONLINE"

    Database=@{

        File=$DatabaseFile

        Folder=$DB

        Backup=$Backup

    }

    Engines=@{}

    Services=New-Object System.Collections.ArrayList

    EventBus=New-Object System.Collections.ArrayList

    Notifications=New-Object System.Collections.ArrayList

    Events=New-Object System.Collections.ArrayList

    Commercial=@{

        Opportunities=New-Object System.Collections.ArrayList

        Statistics=@{

            Total=0

            PipelineValue=0

            Forecast=0

        }

    }

}

###############################################################
# RESTAURA DATABASE
###############################################################

if(Test-Path $DatabaseFile){

    Write-Host "[DATABASE] Restaurando..." -ForegroundColor Yellow

    try{

        $Restore = Get-Content `
            $DatabaseFile `
            -Raw |
            ConvertFrom-Json

        #######################################################
        # EVENTOS
        #######################################################

        if($Restore.EventBus){

            foreach($item in $Restore.EventBus){

                [void]$Global:IOTEC.EventBus.Add($item)

            }

        }

        #######################################################
        # NOTIFICATIONS
        #######################################################

        if($Restore.Notifications){

            foreach($item in $Restore.Notifications){

                [void]$Global:IOTEC.Notifications.Add($item)

            }

        }

        #######################################################
        # OPORTUNIDADES
        #######################################################

        if($Restore.Commercial){

            if($Restore.Commercial.Opportunities){

                foreach($item in $Restore.Commercial.Opportunities){

                    [void]$Global:IOTEC.Commercial.Opportunities.Add($item)

                }

            }

            $Global:IOTEC.Commercial.Statistics.Total =
                $Restore.Commercial.Statistics.Total

            $Global:IOTEC.Commercial.Statistics.PipelineValue =
                $Restore.Commercial.Statistics.PipelineValue

            $Global:IOTEC.Commercial.Statistics.Forecast =
                $Restore.Commercial.Statistics.Forecast

        }

        Write-Host "[OK] Banco restaurado." -ForegroundColor Green

    }
    catch{

        Write-Host "[ERRO] Banco corrompido." -ForegroundColor Red

    }

}
else{

    Write-Host "[INFO] Primeiro Boot." -ForegroundColor Yellow

}

###############################################################
# REGISTRO DE SERVIÇOS
###############################################################

function Register-IOTService{

    param(

        [string]$Name,

        [string]$Type="CORE"

    )

    $Service=[PSCustomObject]@{

        Id=[guid]::NewGuid()

        Name=$Name

        Type=$Type

        Status="ONLINE"

        Started=Get-Date

        Health=100

    }

    [void]$Global:IOTEC.Services.Add($Service)

}

Register-IOTService "Kernel"

Register-IOTService "Database" "DATABASE"

Register-IOTService "Commercial" "COMMERCIAL"

Register-IOTService "Event Bus"

Register-IOTService "Notification Center"

###############################################################
# DASHBOARD
###############################################################

Write-Host ""
Write-Host "==============================================================="
Write-Host "KERNEL STATUS"
Write-Host "==============================================================="
Write-Host ""

Write-Host ("Projeto..............: {0}" -f $Global:IOTEC.Project)

Write-Host ("Versão...............: {0}" -f $Global:IOTEC.Version)

Write-Host ("Status...............: {0}" -f $Global:IOTEC.Status)

Write-Host ""

Write-Host ("Serviços.............: {0}" -f $Global:IOTEC.Services.Count)

Write-Host ("Eventos..............: {0}" -f $Global:IOTEC.EventBus.Count)

Write-Host ("Notificações.........: {0}" -f $Global:IOTEC.Notifications.Count)

Write-Host ("Oportunidades........: {0}" -f $Global:IOTEC.Commercial.Statistics.Total)

Write-Host ("Pipeline.............: R$ {0}" -f $Global:IOTEC.Commercial.Statistics.PipelineValue)

Write-Host ("Forecast.............: R$ {0}" -f $Global:IOTEC.Commercial.Statistics.Forecast)

Write-Host ""

Write-Host "==============================================================="
Write-Host "BOOT FINALIZADO COM SUCESSO"
Write-Host "==============================================================="