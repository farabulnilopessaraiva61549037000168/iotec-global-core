function Sync-IotecLead {
    param (
        [Parameter(Mandatory=$true)][string]$Cnpj,
        [Parameter(Mandatory=$true)][string]$Empresa,
        [Parameter(Mandatory=$true)][string]$Telefone
    )
    
    $RenderUrl = "https://iotec-global-core.onrender.com/api/leads/registrar"
    $bodyPayload = @{
        cnpj     = $Cnpj
        empresa  = $Empresa
        telefone = $Telefone
    } | ConvertTo-Json -Depth 2

    try {
        return Invoke-RestMethod -Uri $RenderUrl -Method Post -Body $bodyPayload -ContentType "application/json" -TimeoutSec 10
    } catch {
        return $null
    }
}
