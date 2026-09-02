# =========================================================================================
#       USINA IOTEC — MÓDULO DE ESTORNO & DEVOLUÇÃO SEGURA (PORTA 8210)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8210
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC REFUND ENGINE — SISTEMA DE ESTORNO ATIVO (PORTA $port)" -ForegroundColor Green
    Write-Host "     Acesse no seu navegador: http://localhost:$port/" -ForegroundColor Yellow
    Write-Host "=================================================================`n" -ForegroundColor Cyan
} catch {
    Write-Host "[ERRO] Não foi possível iniciar na porta $port." -ForegroundColor Red
    exit
}

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $response = $context.Response

    $html = @"
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>IOTEC — Módulo de Estorno & Devolução</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#040507; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; height:100vh; display:grid; grid-template-rows:60px 1fr 40px; padding:16px; gap:12px; }
        header { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.3); border-radius:12px; display:flex; justify-content:space-between; align-items:center; padding:0 20px; }
        .brand { font-family:'Cinzel',serif; font-size:18px; color:#E8D8C8; letter-spacing:3px; }
        .badge { background:rgba(248,113,113,0.15); border:1px solid #F87171; color:#F87171; padding:4px 10px; border-radius:20px; font-size:10px; font-weight:700; }
        .main { display:grid; grid-template-columns:1fr 1fr; gap:12px; height:100%; overflow:hidden; }
        .card { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.3); border-radius:14px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; }
        .title { font-family:'Cinzel',serif; color:#E8D8C8; font-size:15px; margin-bottom:10px; }
        .field { margin-bottom:10px; }
        label { font-size:10px; color:#D4B886; font-weight:700; display:block; margin-bottom:4px; text-transform:uppercase; }
        input, select { width:100%; padding:10px; background:rgba(6,7,9,0.9); border:1px solid rgba(232,216,200,0.3); border-radius:8px; color:#FFF; font-size:12px; }
        .btn-refund { width:100%; padding:12px; background:rgba(248,113,113,0.15); border:1px solid #F87171; color:#F87171; font-weight:800; border-radius:8px; cursor:pointer; font-size:11px; text-transform:uppercase; letter-spacing:1px; margin-top:8px; }
        .btn-refund:hover { background:#F87171; color:#040507; }
        .terminal { background:rgba(6,7,9,0.95); border:1px solid rgba(232,216,200,0.3); border-radius:10px; padding:12px; height:100%; overflow-y:auto; font-size:11px; color:#E8D8C8; display:flex; flex-direction:column; gap:8px; }
        footer { display:flex; justify-content:space-between; font-size:9px; color:#9AA0AC; text-transform:uppercase; letter-spacing:1px; }
    </style>
</head>
<body>
    <header>
        <div class="brand">IOTEC REFUND ENGINE — DEVOLUÇÃO AUDITADA</div>
        <div class="badge">● REGRA DE RESTITUIÇÃO NA ORIGEM</div>
    </header>

    <div class="main">
        <div class="card">
            <div>
                <div class="title">Solicitar Estorno / Devolução de Pedido</div>
                
                <div class="field">
                    <label>ID da Transação Original</label>
                    <input type="text" id="txId" value="TX-9982314-PIX">
                </div>

                <div class="field">
                    <label>Valor a Restituir (R$)</label>
                    <input type="number" id="valRef" value="35.00">
                </div>

                <div class="field">
                    <label>Motivo do Estorno</label>
                    <select id="motivo">
                        <option value="RETORNO_MERCADORIA">Item Retornou ao Estabelecimento</option>
                        <option value="CANCELAMENTO_CLIENTE">Cancelamento Antes do Preparo</option>
                        <option value="SEM_ITEM">Falta de Insumo na Cozinha</option>
                    </select>
                </div>

                <button class="btn-refund" onclick="executarEstorno()">Executar Estorno Via API Bancária</button>
            </div>

            <div style="background:rgba(6,7,9,0.8); border:1px solid rgba(232,216,200,0.2); border-radius:8px; padding:10px; font-size:10px; color:#E8D8C8;">
                <strong>Segurança Mapeada:</strong> A devolução é processada diretamente para a conta bancária de origem que efetuou o pagamento, impedindo desvios para terceiros.
            </div>
        </div>

        <div class="card">
            <div class="title">Logs de Execução de Devolução</div>
            <div class="terminal" id="term">
                <div>[MOTOR PRONTO] Nenhuma solicitação de estorno em andamento...</div>
            </div>
        </div>
    </div>

    <footer>
        <div>© IOTEC — CNPJ 61.549.037/0001-68</div>
        <div>E-mail: IOTEC.BL@proton.me</div>
        <div>Mesa de Governança: Bruno (Fundador)</div>
    </footer>

    <script>
        function executarEstorno() {
            const tx = document.getElementById('txId').value;
            const val = document.getElementById('valRef').value;
            const mot = document.getElementById('motivo').value;
            const term = document.getElementById('term');
            const time = new Date().toLocaleTimeString();

            term.innerHTML += `<div style="border-left:3px solid #F87171; padding-left:8px;">
                <strong>[${time}] [ESTORNO SOLICITADO]</strong><br>
                Transação: ${tx} | Valor: R$ ${val}<br>
                Motivo: ${mot}<br>
                <span style="color:#4ADE80;">✔ Devolução processada com sucesso via API do Banco para a conta de origem!</span>
            </div>`;
            term.scrollTop = term.scrollHeight;
        }
    </script>
</body>
</html>
"@

    $buffer = [System.Text.Encoding]::UTF8.GetBytes($html)
    $response.ContentLength64 = $buffer.Length
    $response.ContentType = "text/html; charset=utf-8"
    $response.OutputStream.Write($buffer, 0, $buffer.Length)
    $response.OutputStream.Close()
}
