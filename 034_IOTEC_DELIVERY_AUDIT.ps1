# =========================================================================================
#       USINA IOTEC — MÓDULO EXPRESS & DELIVERY AUDIT (PORTA 8180)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8180
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC EXPRESS & DELIVERY AUDIT ATIVO NA PORTA $port" -ForegroundColor Green
    Write-Host "     Acesse no seu navegador: http://localhost:$port/" -ForegroundColor Yellow
    Write-Host "=================================================================`n" -ForegroundColor Cyan
} catch {
    Write-Host "[ERRO] Não foi possível iniciar na porta $port." -ForegroundColor Red
    exit
}

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $request = $context.Request
    $response = $context.Response

    $html = @"
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC Express & Delivery Audit</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { background-color: #040507; color: #FFFFFF; font-family: 'Plus Jakarta Sans', sans-serif; height: 100vh; display: grid; grid-template-rows: 60px 1fr 40px; padding: 16px; gap: 14px; }
        header { background: rgba(12, 14, 20, 0.85); border: 1px solid rgba(232, 216, 200, 0.3); border-radius: 12px; display: flex; justify-content: space-between; align-items: center; padding: 0 20px; }
        .brand { font-family: 'Cinzel', serif; font-size: 18px; color: #E8D8C8; letter-spacing: 3px; }
        .badge { background: rgba(74, 222, 128, 0.15); border: 1px solid #4ADE80; color: #4ADE80; padding: 4px 12px; border-radius: 20px; font-size: 10px; font-weight: 700; letter-spacing: 1px; }
        .main { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; height: 100%; overflow: hidden; }
        .card { background: rgba(12, 14, 20, 0.85); border: 1px solid rgba(232, 216, 200, 0.3); border-radius: 16px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; }
        .title { font-family: 'Cinzel', serif; color: #E8D8C8; font-size: 16px; margin-bottom: 12px; }
        .input-group { margin-bottom: 12px; }
        label { display: block; font-size: 10.5px; color: #D4B886; margin-bottom: 4px; font-weight: 700; text-transform: uppercase; }
        input, select { width: 100%; padding: 10px; background: rgba(6, 7, 9, 0.9); border: 1px solid rgba(232, 216, 200, 0.3); border-radius: 8px; color: #FFF; font-size: 12px; }
        .btn { width: 100%; padding: 12px; background: rgba(232, 216, 200, 0.1); border: 1px solid #E8D8C8; color: #E8D8C8; font-weight: 700; border-radius: 8px; cursor: pointer; font-size: 11px; text-transform: uppercase; letter-spacing: 1px; transition: all 0.2s; }
        .btn:hover { background: #E8D8C8; color: #040507; }
        .terminal { background: rgba(6, 7, 9, 0.95); border: 1px solid rgba(232, 216, 200, 0.3); border-radius: 12px; padding: 14px; height: 100%; overflow-y: auto; font-family: monospace; font-size: 11px; color: #E8D8C8; display: flex; flex-direction: column; gap: 8px; }
        .msg-success { color: #4ADE80; border-left: 3px solid #4ADE80; padding-left: 8px; }
        .msg-error { color: #F87171; border-left: 3px solid #F87171; padding-left: 8px; }
        footer { display: flex; justify-content: space-between; font-size: 9.5px; color: #9AA0AC; text-transform: uppercase; letter-spacing: 1.5px; }
    </style>
</head>
<body>
    <header>
        <div class="brand">IOTEC EXPRESS & DELIVERY AUDIT</div>
        <div class="badge">● TRAVA DE EXPEDIÇÃO ATIVA</div>
    </header>

    <div class="main">
        <div class="card">
            <div>
                <div class="title">Simulador de Pedido & Pagamento</div>
                
                <div class="input-group">
                    <label>Cliente / Comanda</label>
                    <input type="text" id="cliente" value="Açaí do João - Pedido #104">
                </div>

                <div class="input-group">
                    <label>Valor Total (R$)</label>
                    <input type="number" id="valor" value="35.00">
                </div>

                <div class="input-group">
                    <label>Método de Pagamento</label>
                    <select id="metodo">
                        <option value="PIX_REAL">PIX Autêntico (Confirmado via API Banco)</option>
                        <option value="PIX_FALSO">Comprovante Enviado (Sem Entrada no Banco)</option>
                        <option value="PIX_AGENDADO">PIX Agendado (Não Liquidado)</option>
                        <option value="ESPECIE">Dinheiro em Espécie (Com Troco Registrado)</option>
                    </select>
                </div>

                <button class="btn" onclick="processarPedido()">Simular Validação do Kernel</button>
            </div>

            <div style="background: rgba(6,7,9,0.8); border: 1px solid rgba(232,216,200,0.2); border-radius: 8px; padding: 10px; font-size: 10.5px; color: #9AA0AC;">
                <strong>Regra Ativa:</strong> A impressora de produção da cozinha só libera a comanda se o saldo for confirmado via API bancária ou registrado no caixa com cédula declarada.
            </div>
        </div>

        <div class="card">
            <div class="title">Logs de Auditoria do Kernel (Cozinha & Expedição)</div>
            <div class="terminal" id="terminal">
                <div>[SISTEMA INICIALIZADO] Aguardando requisições de entrega...</div>
            </div>
        </div>
    </div>

    <footer>
        <div>© IOTEC — CNPJ 61.549.037/0001-68</div>
        <div>E-mail: IOTEC.BL@proton.me</div>
        <div>Mesa de Governança: Bruno (Fundador)</div>
    </footer>

    <script>
        function processarPedido() {
            const cliente = document.getElementById('cliente').value;
            const valor = document.getElementById('valor').value;
            const metodo = document.getElementById('metodo').value;
            const term = document.getElementById('terminal');

            const timestamp = new Date().toLocaleTimeString();

            if (metodo === 'PIX_REAL') {
                term.innerHTML += `<div class="msg-success">[${timestamp}] [SUCESSO] PIX de R$ ${valor} confirmado no extrato real! Comanda impressa na cozinha.</div>`;
            } else if (metodo === 'PIX_FALSO') {
                term.innerHTML += `<div class="msg-error">[${timestamp}] [ALERTA DE FRAUDE] Comprovante apresentado, mas saldo não alterado no banco. EXPEDIÇÃO BLOQUEADA.</div>`;
            } else if (metodo === 'PIX_AGENDADO') {
                term.innerHTML += `<div class="msg-error">[${timestamp}] [BLOQUEIO] PIX Agendado detectado. O Kernel exige liquidação imediata para liberar o prato.</div>`;
            } else if (metodo === 'ESPECIE') {
                term.innerHTML += `<div class="msg-success">[${timestamp}] [CAIXA AUDITADO] R$ ${valor} registrado em dinheiro no caixa. Gaveta liberada e comanda enviada.</div>`;
            }
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
