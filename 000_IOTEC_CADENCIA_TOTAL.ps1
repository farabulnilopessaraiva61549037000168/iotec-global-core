# ==============================================================================
# IOTEC CORE ENGINE — ORQUESTRADOR NATIVO EM POWERSHELL (24 HORAS)
# CNPJ MATRIZ: 61.549.037/0001-68 | DOMÍNIO: https://deft-choux-097d84.netlify.app/
# ==============================================================================

$PathJson = "C:\IOTEC\contatos_base.json"

function Obter-Mensagem ($categoria, $nome, $empresa, $url) {
    switch ($categoria) {
        "DESPACHANTES"     { return "Olá, $nome! Tudo bem? Vimos a atuação da $empresa em desembaraço aduaneiro. A IOTEC automatizou a emissão de DTA, DTC e DUIMP com chancela ICP-Brasil instantânea. Teste ao vivo: $url" }
        "COMISSARIAS"      { return "Olá, $nome! Para a ${empresa}: a IOTEC oferece emissão e validação de chancelas em lote para liberar contêineres sem fila. Acesse: $url" }
        "TI_ERPS"          { return "Boa tarde, $nome! Disponibilizamos a API REST da IOTEC para integração direta no sistema da ${empresa}. Emita certidões White-Label com recorrência B2B. Documentação: $url" }
        "LOGISTICA_CARGAS" { return "Olá, $nome! A IOTEC simplificou as licenças AFE/AE Anvisa e IBAMA para transporte de cargas perigosas da ${empresa}. Verificação 100% online: $url" }
        "TRADING_COMPANIES"{ return "Prezado(a) $nome, a IOTEC automatiza a emissão de Certificados OEA para a ${empresa}, acelerando a liberação de canal verde nas alfândegas: $url" }
        "INVESTIDORES_B2B" { return "Olá, $nome! Apresentamos o Jornal de Oportunidades IOTEC (CNPJ 61.549.037/0001-68) para investimentos em infraestrutura de certidões com Yield estimado de 18% a 22% a.a. Confira: $url" }
        "FOLLOW_UP"        { return "Olá, $nome! Vi que você visitou o simulador IOTEC hoje. Ficou com alguma dúvida sobre a chancela ICP-Brasil para a ${empresa}? Fale direto no atendimento: https://wa.me/5588993064168" }
        Default            { return "Conheça a plataforma IOTEC: $url" }
    }
}

function Executar-DisparoLote ($categoria) {
    if (!(Test-Path $PathJson)) { Write-Host "❌ Arquivo contatos_base.json não encontrado!" -ForegroundColor Red; return }
    
    $dados = Get-Content $PathJson -Raw -Encoding UTF8 | ConvertFrom-Json
    $contatos = $dados.BASE_CONTATOS.$categoria
    $url = $dados.DOMINIO_OFICIAL

    if ($null -eq $contatos -or $contatos.Count -eq 0) {
        Write-Host "⚠️ Nenhum contato encontrado para a categoria [$categoria]" -ForegroundColor Yellow
        return
    }

    Write-Host "`n⚡ [JANELA ATIVA: $categoria] — Processando $($contatos.Count) contatos..." -ForegroundColor Cyan

    foreach ($c in $contatos) {
        $msg = Obter-Mensagem -categoria $categoria -nome $c.nome -empresa $c.empresa -url $url
        $horaEnvio = (Get-Date).ToString("HH:mm:ss")

        Write-Host "  └── 📲 [DISPARO PREPARADO] $($c.nome) ($($c.empresa)) às $horaEnvio" -ForegroundColor Green
        Write-Host "      💬 '$msg'" -ForegroundColor DarkCyan

        # Intervalo humano aleatório entre 3 e 7 minutos para simular digitação real
        $tempoPausa = Get-Random -Minimum 180 -Maximum 420
        Write-Host "      ⏳ Pausa de segurança anti-SPAM: ${tempoPausa}s..." -ForegroundColor Gray
        Start-Sleep -Seconds $tempoPausa
    }
}

Clear-Host
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host "🤖 NÚCLEO IOTEC — MOTOR DE CADÊNCIA EXPANDIDA (POWERSHELL 24H)" -ForegroundColor Cyan
Write-Host "==================================================================" -ForegroundColor Cyan

while ($true) {
    $agora = Get-Date
    $h = $agora.Hour
    $m = $agora.Minute

    # JANELA 1: 08:30 - 10:00 (Despachantes)
    if (($h -eq 8 -and $m -ge 30) -or ($h -eq 9)) {
        Executar-DisparoLote -categoria "DESPACHANTES"
    }
    # JANELA 2: 10:15 - 11:15 (Comissárias & NVOCCs)
    elseif ($h -eq 10 -and $m -ge 15) {
        Executar-DisparoLote -categoria "COMISSARIAS"
    }
    # JANELA 3: 11:30 - 12:30 (Gestores de TI & ERPs)
    elseif (($h -eq 11 -and $m -ge 30) -or ($h -eq 12 -and $m -le 30)) {
        Executar-DisparoLote -categoria "TI_ERPS"
    }
    # JANELA 4: 14:00 - 15:30 (Logística & Cargas)
    elseif (($h -eq 14) -or ($h -eq 15 -and $m -le 30)) {
        Executar-DisparoLote -categoria "LOGISTICA_CARGAS"
    }
    # JANELA 5: 15:45 - 16:45 (Trading Companies)
    elseif (($h -eq 15 -and $m -ge 45) -or ($h -eq 16 -and $m -le 45)) {
        Executar-DisparoLote -categoria "TRADING_COMPANIES"
    }
    # JANELA 6: 17:00 - 18:00 (Executivos & Investidores)
    elseif ($h -eq 17) {
        Executar-DisparoLote -categoria "INVESTIDORES_B2B"
    }
    # JANELA 7: 18:15 - 19:00 (Follow-up)
    elseif ($h -eq 18 -and $m -ge 15) {
        Executar-DisparoLote -categoria "FOLLOW_UP"
    }
    else {
        $horaFormatada = $agora.ToString("HH:mm:ss")
        Write-Host "😴 [$horaFormatada] MÓDULO EM ESPERA (Fora de janela operacional / MODO DORMIR). Checando em 10 min..." -ForegroundColor Yellow
        Start-Sleep -Seconds 600
    }
}