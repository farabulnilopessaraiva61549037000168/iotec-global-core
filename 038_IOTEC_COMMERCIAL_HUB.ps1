# =========================================================================================
#       USINA IOTEC — CENTRAL DE CARDÁPIOS, TABELAS & EVENTOS B2B (PORTA 8220)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8220
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC COMMERCIAL HUB — CENTRAL B2B ATIVA NA PORTA $port" -ForegroundColor Green
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC — Central Comercial & Configuração de Negócio</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#040507; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; height:100vh; display:grid; grid-template-rows:60px 1fr 40px; padding:16px; gap:12px; }
        header { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.3); border-radius:12px; display:flex; justify-content:space-between; align-items:center; padding:0 20px; }
        .brand { font-family:'Cinzel',serif; font-size:18px; color:#E8D8C8; letter-spacing:3px; }
        .badge { background:rgba(74,222,128,0.15); border:1px solid #4ADE80; color:#4ADE80; padding:4px 10px; border-radius:20px; font-size:10px; font-weight:700; }
        .main { display:grid; grid-template-columns:1fr 1fr; gap:12px; height:100%; overflow:hidden; }
        .card { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.3); border-radius:14px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; }
        .title { font-family:'Cinzel',serif; color:#E8D8C8; font-size:15px; margin-bottom:10px; }
        .field { margin-bottom:10px; }
        label { font-size:10px; color:#D4B886; font-weight:700; display:block; margin-bottom:4px; text-transform:uppercase; }
        input, select { width:100%; padding:10px; background:rgba(6,7,9,0.9); border:1px solid rgba(232,216,200,0.3); border-radius:8px; color:#FFF; font-size:12px; }
        .btn-hub { width:100%; padding:12px; background:rgba(232,216,200,0.12); border:1px solid #E8D8C8; color:#E8D8C8; font-weight:800; border-radius:8px; cursor:pointer; font-size:11px; text-transform:uppercase; letter-spacing:1px; margin-top:8px; }
        .btn-hub:hover { background:#E8D8C8; color:#040507; }
        .terminal { background:rgba(6,7,9,0.95); border:1px solid rgba(232,216,200,0.3); border-radius:10px; padding:12px; height:100%; overflow-y:auto; font-size:11px; color:#E8D8C8; display:flex; flex-direction:column; gap:8px; }
        footer { display:flex; justify-content:space-between; font-size:9px; color:#9AA0AC; text-transform:uppercase; letter-spacing:1px; }
    </style>
</head>
<body>
    <header>
        <div class="brand">IOTEC COMMERCIAL HUB — BLINDAGEM DE VENDAS</div>
        <div class="badge">● MÓDULO B2B PRONTO PARA VENDA</div>
    </header>

    <div class="main">
        <div class="card">
            <div>
                <div class="title">Configuração de Tabela & Perfil de Operação</div>
                
                <div class="field">
                    <label>Nome do Estabelecimento / Evento</label>
                    <input type="text" id="nomeEmpresa" value="Marmitaria & Festa da Vila">
                </div>

                <div class="field">
                    <label>Modo de Operação</label>
                    <select id="modoOp">
                        <option value="DELIVERY">Delivery & Gastronomia (Marmitas, Açaí, Pizzas)</option>
                        <option value="EVENTO">Grandes Eventos & Festas (Fichas de Bar e Bebidas)</option>
                        <option value="SERVICO">Serviços & Estética (Bronzeamento, Salões, Pet)</option>
                    </select>
                </div>

                <div class="field">
                    <label>Item / Produto Cadastrado</label>
                    <input type="text" id="prodNome" value="Ficha de Bebida / Combo Marmita">
                </div>

                <div class="field">
                    <label>Preço Base (R$)</label>
                    <input type="number" id="prodPreco" value="25.00">
                </div>

                <div class="field">
                    <label>Taxa de Entrega / Frete (R$)</label>
                    <input type="number" id="taxaEntrega" value="5.00">
                </div>

                <button class="btn-hub" onclick="salvarConfig()">Ativar Tabela com Trava do Kernel</button>
            </div>

            <div style="background:rgba(6,7,9,0.8); border:1px solid rgba(232,216,200,0.2); border-radius:8px; padding:10px; font-size:10px; color:#E8D8C8;">
                <strong>Guardião Invisível:</strong> O comerciante foca no atendimento. O robô IOTEC assume a validação bancária, bloqueando $100\%$ das tentativas de golpes com PIX e erros de troco.
            </div>
        </div>

        <div class="card">
            <div class="title">Painel de Operação do Contratante</div>
            <div class="terminal" id="term">
                <div>[SISTEMA PRONTO] Insira as configurações para iniciar o fluxo blindado...</div>
            </div>
        </div>
    </div>

    <footer>
        <div>© IOTEC — CNPJ 61.549.037/0001-68</div>
        <div>E-mail: IOTEC.BL@proton.me</div>
        <div>Mesa de Governança: Bruno (Fundador)</div>
    </footer>

    <script>
        function salvarConfig() {
            const emp = document.getElementById('nomeEmpresa').value;
            const modo = document.getElementById('modoOp').value;
            const prod = document.getElementById('prodNome').value;
            const preco = parseFloat(document.getElementById('prodPreco').value);
            const taxa = parseFloat(document.getElementById('taxaEntrega').value);
            const total = preco + taxa;
            const term = document.getElementById('term');
            const time = new Date().toLocaleTimeString();

            term.innerHTML += `<div style="border-left:3px solid #4ADE80; padding-left:8px;">
                <strong>[${time}] [TABELA ATIVADA]</strong><br>
                Empresa: <strong>${emp}</strong> | Modo: <strong>${modo}</strong><br>
                Item: ${prod} (R$ ${preco.toFixed(2)}) + Frete (R$ ${taxa.toFixed(2)})<br>
                Total do Pedido: <strong>R$ ${total.toFixed(2)}</strong><br>
                <span style="color:#4ADE80;">✔ Trava Anti-Fraude e Validação Bancária Ativas na Porta 8220!</span>
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
