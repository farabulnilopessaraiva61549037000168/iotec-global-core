# =========================================================================================
#       USINA IOTEC — REDE DE VENDAS & CATÁLOGOS SEGMENTADOS (PORTA 8190)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8190
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC SALES NETWORK — REDE MULTICATÁLOGO ATIVA (PORTA $port)" -ForegroundColor Green
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
    <title>IOTEC — Central de Vendas & Catálogos</title>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800&family=Plus+Jakarta+Sans:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body { background:#040507; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; height:100vh; display:grid; grid-template-rows:60px 1fr 40px; padding:16px; gap:12px; }
        header { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.3); border-radius:12px; display:flex; justify-content:space-between; align-items:center; padding:0 20px; }
        .brand { font-family:'Cinzel',serif; font-size:18px; color:#E8D8C8; letter-spacing:3px; }
        .badge { background:rgba(74,222,128,0.15); border:1px solid #4ADE80; color:#4ADE80; padding:4px 10px; border-radius:20px; font-size:10px; font-weight:700; }
        .main { display:grid; grid-template-columns:1.1fr 0.9fr; gap:12px; height:100%; overflow:hidden; }
        .card { background:rgba(12,14,20,0.85); border:1px solid rgba(232,216,200,0.3); border-radius:14px; padding:18px; display:flex; flex-direction:column; justify-content:space-between; }
        .title { font-family:'Cinzel',serif; color:#E8D8C8; font-size:15px; margin-bottom:8px; }
        .catalog-grid { display:grid; grid-template-columns:1fr 1fr; gap:10px; margin-top:10px; }
        .cat-item { background:rgba(232,216,200,0.04); border:1px solid rgba(232,216,200,0.3); border-radius:10px; padding:12px; cursor:pointer; transition:all 0.2s; }
        .cat-item:hover { border-color:#FFF; background:rgba(232,216,200,0.1); }
        .cat-title { font-size:11px; font-weight:700; color:#E8D8C8; }
        .cat-desc { font-size:9.5px; color:#9AA0AC; margin-top:4px; }
        .terminal { background:rgba(6,7,9,0.95); border:1px solid rgba(232,216,200,0.3); border-radius:10px; padding:12px; height:100%; overflow-y:auto; font-size:11px; color:#E8D8C8; display:flex; flex-direction:column; gap:8px; }
        footer { display:flex; justify-content:space-between; font-size:9px; color:#9AA0AC; text-transform:uppercase; letter-spacing:1px; }
    </style>
</head>
<body>
    <header>
        <div class="brand">IOTEC SALES NETWORK — PAINEL DO VENDEDOR</div>
        <div class="badge">● SISTEMA DE PARTICIPAÇÃO MÚTUA ATIVO</div>
    </header>

    <div class="main">
        <div class="card">
            <div>
                <div class="title">Selecione o Catálogo do Especialista</div>
                <p style="font-size:11px; color:#9AA0AC;">Cada catálogo adapta a trava técnica para o nicho de mercado correto.</p>

                <div class="catalog-grid">
                    <div class="cat-item" onclick="selecionar('Gastronomia & Delivery', 'R$ 99,00/mês', 'Trava Anti-PIX Falso na Cozinha')">
                        <div class="cat-title">01. Delivery & Gastronomia</div>
                        <div class="cat-desc">Açaíterias, Pizzarias, Marmitas.</div>
                    </div>

                    <div class="cat-item" onclick="selecionar('Serviços & Estética', 'R$ 89,00/mês', 'Trava de Agendamento com Sinal')">
                        <div class="cat-title">02. Serviços & Estética</div>
                        <div class="cat-desc">Salões, Pet Shops, Clínicas.</div>
                    </div>

                    <div class="cat-item" onclick="selecionar('Conveniência & Posto', 'R$ 149,00/mês', 'Fechamento Cego de Gaveta e Troco')">
                        <div class="cat-title">03. Conveniência & Balcão</div>
                        <div class="cat-desc">Mercadinhos, Lojas de Conveniência.</div>
                    </div>

                    <div class="cat-item" onclick="selecionar('Cotas Orbitais B2B', 'Sob Consulta', 'Contrato SAFE + Participação no Fluxo')">
                        <div class="cat-title">04. Capital & Cotas B2B</div>
                        <div class="cat-desc">Investidores do Café com Economia.</div>
                    </div>
                </div>
            </div>

            <div style="background:rgba(6,7,9,0.8); border:1px solid rgba(232,216,200,0.2); border-radius:8px; padding:10px; font-size:10px; color:#E8D8C8;">
                <strong>Regra de Participação:</strong> Indicações cruzadas entre vendedores geram comissionamento mútua de 5% sobre a mensalidade do cliente retido.
            </div>
        </div>

        <div class="card">
            <div class="title">Extrato de Vendas e Indicações Mútuas</div>
            <div class="terminal" id="term">
                <div>[SISTEMA PRONTO] Escolha um catálogo para simular o fechamento de um contrato...</div>
            </div>
        </div>
    </div>

    <footer>
        <div>© IOTEC — CNPJ 61.549.037/0001-68</div>
        <div>E-mail: IOTEC.BL@proton.me</div>
        <div>Mesa de Governança: Bruno (Fundador)</div>
    </footer>

    <script>
        function selecionar(nome, valor, trava) {
            const t = document.getElementById('term');
            const time = new Date().toLocaleTimeString();
            t.innerHTML += `<div style="border-left:3px solid #4ADE80; padding-left:8px;">
                <strong>[${time}] [CATÁLOGO SELECIONADO]</strong><br>
                Produto: <strong>${nome}</strong><br>
                Valor: ${valor} | Regra: ${trava}<br>
                <span style="color:#4ADE80;">Contrato liberado para emissão imediata e vinculo à rede.</span>
            </div>`;
            t.scrollTop = t.scrollHeight;
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
