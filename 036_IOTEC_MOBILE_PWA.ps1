# =========================================================================================
#       USINA IOTEC — APLICATIVO MOBILE EXTERNO PWA (PORTA 8200)
#       CNPJ: 61.549.037/0001-68 | Mesa de Governança: Bruno
# =========================================================================================

$port = 8200
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:$port/")

try {
    $listener.Start()
    Write-Host "`n=================================================================" -ForegroundColor Cyan
    Write-Host "     IOTEC MOBILE PWA — INTERFACE DO COMERCIANTE ATIVA (PORTA $port)" -ForegroundColor Green
    Write-Host "     Acesse no seu celular ou navegador: http://localhost:$port/" -ForegroundColor Yellow
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>IOTEC — App do Comerciante</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        * { margin:0; padding:0; box-sizing:border-box; -webkit-tap-highlight-color: transparent; }
        body { background:#040507; color:#FFF; font-family:'Plus Jakarta Sans',sans-serif; display:flex; justify-content:center; align-items:center; min-height:100vh; padding:10px; }
        
        /* MOLDURA SIMULANDO SMARTPHONE */
        .phone-frame { width:100%; max-width:380px; height:740px; background:#0B0E14; border:2px solid rgba(232,216,200,0.3); border-radius:36px; padding:16px; display:flex; flex-direction:column; justify-content:space-between; box-shadow:0 20px 50px rgba(0,0,0,0.9); position:relative; overflow:hidden; }
        
        .notch { width:120px; height:18px; background:#040507; border-radius:0 0 12px 12px; position:absolute; top:0; left:50%; transform:translateX(-50%); z-index:10; }
        
        .app-header { display:flex; justify-content:space-between; align-items:center; margin-top:14px; padding-bottom:12px; border-bottom:1px solid rgba(232,216,200,0.2); }
        .biz-title { font-size:14px; font-weight:800; color:#E8D8C8; letter-spacing:0.5px; }
        .status-dot { font-size:9px; color:#4ADE80; font-weight:700; background:rgba(74,222,128,0.12); padding:3px 8px; border-radius:12px; border:1px solid #4ADE80; }

        .segment-selector { display:flex; gap:6px; margin-top:10px; overflow-x:auto; padding-bottom:4px; }
        .chip { background:rgba(232,216,200,0.06); border:1px solid rgba(232,216,200,0.2); color:#E8D8C8; padding:6px 10px; border-radius:16px; font-size:10px; font-weight:600; white-space:nowrap; cursor:pointer; }
        .chip.active { background:#E8D8C8; color:#040507; font-weight:800; }

        .card-body { background:rgba(6,7,9,0.85); border:1px solid rgba(232,216,200,0.25); border-radius:18px; padding:14px; margin-top:10px; }
        .field-label { font-size:10px; color:#D4B886; font-weight:700; text-transform:uppercase; margin-bottom:4px; }
        .input-mobile { width:100%; padding:10px; background:rgba(4,5,7,0.9); border:1px solid rgba(232,216,200,0.2); border-radius:10px; color:#FFF; font-size:13px; margin-bottom:10px; font-weight:600; }

        .btn-action { width:100%; padding:12px; background:rgba(232,216,200,0.12); border:1px solid #E8D8C8; color:#E8D8C8; font-weight:800; border-radius:12px; font-size:11px; text-transform:uppercase; letter-spacing:1px; cursor:pointer; }
        .btn-action:active { transform:scale(0.98); background:#E8D8C8; color:#040507; }

        .live-feed { background:rgba(4,5,7,0.95); border:1px solid rgba(232,216,200,0.2); border-radius:14px; padding:10px; height:180px; overflow-y:auto; font-size:10.5px; display:flex; flex-direction:column; gap:6px; margin-top:10px; }
        .alert-ok { border-left:3px solid #4ADE80; padding-left:6px; color:#E8D8C8; }
        .alert-warn { border-left:3px solid #F87171; padding-left:6px; color:#F87171; }

        .pwa-footer { text-align:center; font-size:9px; color:#9AA0AC; border-top:1px solid rgba(232,216,200,0.15); padding-top:8px; }
    </style>
</head>
<body>

    <div class="phone-frame">
        <div class="notch"></div>

        <div>
            <div class="app-header">
                <div>
                    <div class="biz-title" id="bizName">Bronze da Lu — Estética</div>
                    <div style="font-size:9px; color:#9AA0AC;">ID da Loja: #8842-IOTEC</div>
                </div>
                <div class="status-dot">● KERNEL ATIVO</div>
            </div>

            <!-- SELETOR DE PERFIL PARA O CLIENTE SELECIONAR SEU SECTOR -->
            <div class="segment-selector">
                <div class="chip active" id="c1" onclick="mudarPerfil('Bronze da Lu — Estética', 'Bronzeamento & Agendamento', 'c1')"> Bronzeamento</div>
                <div class="chip" id="c2" onclick="mudarPerfil('Floricultura Bella Rosa', 'Venda de Buquês & Encomendas', 'c2')"> Floricultura</div>
                <div class="chip" id="c3" onclick="mudarPerfil('Marmitaria Dona Ana', 'Marmitas & Pedidos', 'c3')"> Marmitaria</div>
                <div class="chip" id="c4" onclick="mudarPerfil('Açaí do Bairro', 'Copos & Delivery Express', 'c4')"> Açaíterias</div>
            </div>

            <div class="card-body">
                <div class="field-label" id="lblDesc">Cliente / Serviço</div>
                <input type="text" class="input-mobile" id="inDesc" value="Sinal do Agendamento — Bronze Completo">

                <div class="field-label">Valor do Cobrado (R$)</div>
                <input type="number" class="input-mobile" id="inVal" value="50.00">

                <button class="btn-action" onclick="gerarCobranca()">Gerar Trava de Cobrança</button>
            </div>

            <div class="live-feed" id="feed">
                <div style="color:#9AA0AC; font-size:10px;">[SISTEMA APOSTOS] Nenhuma cobrança pendente.</div>
            </div>
        </div>

        <div class="pwa-footer">
            IOTEC WebPWA Mobile — CNPJ 61.549.037/0001-68<br>
            Licença Ativa: R$ 89,00/mês | Suporte: IOTEC.BL@proton.me
        </div>
    </div>

    <script>
        function mudarPerfil(nome, desc, idChip) {
            document.getElementById('bizName').innerText = nome;
            document.getElementById('inDesc').value = desc;
            
            document.querySelectorAll('.chip').forEach(c => c.classList.remove('active'));
            document.getElementById(idChip).classList.add('active');

            const feed = document.getElementById('feed');
            feed.innerHTML += `<div style="color:#D4B886;">[MODO ALTERADO] Perfil ajustado para <strong>${nome}</strong>.</div>`;
            feed.scrollTop = feed.scrollHeight;
        }

        function gerarCobranca() {
            const desc = document.getElementById('inDesc').value;
            const val = document.getElementById('inVal').value;
            const feed = document.getElementById('feed');
            const time = new Date().toLocaleTimeString();

            feed.innerHTML += `<div class="alert-ok">
                <strong>[${time}] COBRANÇA CRIADA</strong><br>
                ${desc} — R$ ${val}<br>
                <span style="color:#4ADE80;">Aguardando liquidação na API bancária... (Comprovantes em imagem serão ignorados).</span>
            </div>`;
            
            setTimeout(() => {
                feed.innerHTML += `<div class="alert-ok" style="border-color:#4ADE80; background:rgba(74,222,128,0.08); padding:4px; border-radius:6px;">
                    <strong>[${time}] PAGAMENTO CONFIRMADO!</strong><br>
                    Dinheiro em conta. Horário / Pedido Liberado na Cozinha.
                </div>`;
                feed.scrollTop = feed.scrollHeight;
            }, 3000);

            feed.scrollTop = feed.scrollHeight;
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

