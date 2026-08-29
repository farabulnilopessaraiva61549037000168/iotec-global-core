$csvPath         = "C:\IOTEC\base_empresas.csv"
$zapiInstance    = "3F8066F099284121F1F5DA9739CF5BB5"
$zapiToken       = "1394B2099F6C7104DE6D6C6C"
$zapiClientToken = "SEU_CLIENT_TOKEN_AQUI" # Substituir pelo token do painel Z-API (Aba Seguranca)

$ciclo = 1

while ($true) {
    Clear-Host
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host "  CENTRO DE OPERACOES IOTEC - AUDITORIA EM TEMPO REAL " -ForegroundColor Cyan
    Write-Host "==================================================" -ForegroundColor Cyan
    Write-Host "[HTTP/REDE] Iniciando varredura em: $(Get-Date -Format 'HH:mm:ss')
" -ForegroundColor White

    # 1. LEITURA DA BASE
    $leadsNovos = $null
    if (Test-Path $csvPath) {
        $base = Import-Csv -Path $csvPath -Delimiter ";"
        $leadsNovos = $base | Where-Object { $_.Status -eq "NOVO" } | Select-Object -First 2
        
        Write-Host "[AGENTE 1/2] Base carregada. Leads aguardando envio: $($leadsNovos.Count)" -ForegroundColor Gray
    } else {
        Write-Host "[ERRO CRITICO] Arquivo $csvPath nao encontrado!" -ForegroundColor Red
    }

    # 2. PROCESSAMENTO E CONFIRMACAO REAL
    if ($leadsNovos) {
        foreach ($lead in $leadsNovos) {
            $nomeEmpresa = $lead.NomeEmpresa
            $telefone    = $lead.Telefone

            Write-Host "
[AGENTE 3] Tentando conexao HTTP com Z-API para $nomeEmpresa..." -ForegroundColor Yellow
            
            $headers = @{ "Client-Token" = $zapiClientToken }
            $body    = @{ phone = $telefone; message = "Ola $nomeEmpresa, certidoes pendentes." } | ConvertTo-Json
            $uri     = "https://api.z-api.io/instances/$zapiInstance/token/$zapiToken/send-text"

            try {
                $response = Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -Body $body -ContentType "application/json"
                
                # CHECAGEM RIGOROSA DA RESPOSTA DO SERVIDOR
                if ($response.zaapId -or $response.messageId -or $response.id) {
                    $lead.Status = "CONTATADO"
                    $lead.DataContato = (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
                    Write-Host "[? DISPARO VERIFICADO REAL] ID da Mensagem: $($response.zaapId)$($response.messageId)" -ForegroundColor Green
                } else {
                    Write-Host "[? ALERTA] Servidor respondeu sem ID de entrega valido. Status mantido como NOVO." -ForegroundColor Red
                }
            }
            catch {
                Write-Host "[? REJEITADO PELA API] Falha de conexao/autenticacao: $_" -ForegroundColor Red
                Write-Host "--> O lead '$nomeEmpresa' NAO teve o status alterado para evitar dados falsos." -ForegroundColor Gray
            }
        }
        # Atualiza a planilha apenas se houverem alteracoes reais
        $base | Export-Csv -Path $csvPath -Delimiter ";" -NoTypeInformation
    } else {
        Write-Host "[AGENTE 3] Nenhum lead pendente para envio." -ForegroundColor Gray
    }

    # CONTAGEM REGRESSIVA DOS CICLOS
    Write-Host "
--------------------------------------------------" -ForegroundColor DarkGray
    Write-Host "Ciclo $ciclo finalizado." -ForegroundColor Gray
    
    for ($i = 60; $i -gt 0; $i--) {
        Write-Host -NoNewline "[*] Reiniciando proximo ciclo em: $i segundos... "
        Start-Sleep -Seconds 1
    }
    
    $ciclo++
}
