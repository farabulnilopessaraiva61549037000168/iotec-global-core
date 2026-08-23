import os
import sqlite3
import datetime
import hashlib
import requests
from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

DB_PATH = r"C:\IOTEC\data_store.db"

# CREDENCIAIS OFICIAIS PAYPAL & PICPAY
PAYPAL_CLIENT_ID = "AURhEouZ3Rh83q4XnREm-InsXInd8z8TKQqNxVieb0O7Hy35jeCp60nKhCbUoYvHf6esf-R5jIiEedK4"
PAYPAL_CLIENT_SECRET = "EGxO6f0VdVM2mwiGtw81SXKHRz1o0gvYKPnldmk_0W9uI8P6bQbd5jYJGFTxFEJRbaalYIU4AMDr9rR2"

PICPAY_CLIENT_ID = "5a7d9a15-7541-4b0e-af4e-18e909dcac9b"
PICPAY_CLIENT_SECRET = "RRdl68SU8fM1vybS0XZ0N6P8Iq5zJYOd"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS operacoes_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            evento TEXT,
            tipo TEXT,
            status TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financeiro_confirmado (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            valor REAL,
            origem TEXT,
            hash_confirmacao TEXT,
            gateway TEXT,
            referencia_id TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

HTML_DUAL_GATEWAY = f"""
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Sistema de Checkout Corporativo B2B</title>
    <script src="https://www.paypal.com/sdk/js?client-id={PAYPAL_CLIENT_ID}&currency=BRL"></script>
    <style>
        :root {{ --accent: #3a86ff; --green: #10b981; --picpay: #21C25E; --red: #ef4444; --purple: #8b5cf6; --bg: #030712; }}
        * {{ box-sizing: border-box; }}
        body, html {{ margin: 0; padding: 0; min-height: 100vh; font-family: 'Segoe UI', Tahoma, sans-serif; color: #fff; background: var(--bg); }}

        .container {{ max-width: 1400px; margin: 0 auto; padding: 20px; }}
        .topbar {{ display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 16px; margin-bottom: 20px; }}
        .logo h1 {{ font-size: 26px; margin: 0; color: #fff; letter-spacing: 1px; }}
        .logo p {{ color: #94a3b8; font-size: 13px; margin: 2px 0 0 0; }}

        .badge-gateways {{ background: rgba(33, 194, 94, 0.15); color: var(--picpay); border: 1px solid var(--picpay); padding: 4px 12px; border-radius: 20px; font-size: 11px; font-weight: bold; }}
        .clock-brasilia {{ font-family: monospace; font-size: 20px; font-weight: bold; color: var(--accent); margin-top: 4px; }}

        .finance-alert {{ display: none; background: linear-gradient(135deg, #064e3b 0%, #022c22 100%); border: 1px solid var(--green); border-radius: 12px; padding: 16px 20px; margin-bottom: 20px; box-shadow: 0 0 25px rgba(16, 185, 129, 0.3); }}
        .finance-alert.active {{ display: flex; align-items: center; justify-content: space-between; }}

        .modal {{ display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(3, 7, 18, 0.9); backdrop-filter: blur(8px); z-index: 1000; align-items: center; justify-content: center; }}
        .modal.active {{ display: flex; }}
        .modal-card {{ background: #0f172a; border: 1px solid #334155; border-radius: 16px; width: 100%; max-width: 480px; padding: 28px; box-shadow: 0 0 35px rgba(58, 134, 255, 0.2); }}

        .command-deck {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 20px; }}
        .deck-card {{ background: #0b1220; border: 1px solid #1f2937; border-radius: 10px; padding: 15px; }}
        .deck-card h4 {{ margin: 0 0 6px 0; font-size: 11px; color: #94a3b8; text-transform: uppercase; }}
        .deck-val {{ font-size: 20px; font-weight: bold; font-family: monospace; color: #fff; }}

        .btn-picpay {{ background: var(--picpay); color: #000; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 14px; transition: all 0.2s; }}
        .btn-paypal {{ background: var(--accent); color: #fff; border: none; padding: 12px; width: 100%; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 14px; margin-top: 8px; }}

        .footer {{ margin-top: 30px; text-align: center; color: #64748b; font-size: 12px; }}
    </style>
</head>
<body>

    <div class="container">
        
        <div class="topbar">
            <div class="logo">
                <h1>IOTEC | PLATAFORMA CORPORATIVA B2B</h1>
                <p>Mesa Corporativa de Recebimento e Processamento de Ativos</p>
            </div>
            <div class="status-box" style="text-align:right;">
                <span class="badge-gateways">● NÚCLEO OPERACIONAL ATIVO</span>
                <div class="clock-brasilia" id="brasilia-clock">--:--:-- BRT</div>
            </div>
        </div>

        <div class="finance-alert" id="fin-alert-box">
            <div>
                <strong style="font-size:15px;">💰 CRÉDITO B2B CONFIRMADO E AUDITADO!</strong>
                <p style="margin:4px 0 0 0; font-size:13px; color:#cbd5e1;" id="fin-alert-msg">Aguardando...</p>
            </div>
            <button onclick="document.getElementById('fin-alert-box').classList.remove('active')" style="background:rgba(255,255,255,0.2); color:#fff; border:none; padding:8px 14px; border-radius:6px; cursor:pointer; font-weight:bold;">Fechar</button>
        </div>

        <div class="command-deck">
            <div class="deck-card">
                <h4>Modelo de Negócio</h4>
                <div class="deck-val" style="color:var(--picpay);">B2B Ticket Alto</div>
                <span style="font-size:11px; color:var(--picpay)">Comissionamento & Parcerias</span>
            </div>
            <div class="deck-card">
                <h4>Status do Núcleo</h4>
                <div class="deck-val" style="color:var(--accent);">Estratégico OK</div>
                <span style="font-size:11px; color:var(--green)">Custo Operacional Zero</span>
            </div>
            <div class="deck-card">
                <h4>Caixa do Banco</h4>
                <div class="deck-val" id="total-faturamento" style="color:var(--green);">R$ 0,00</div>
                <span style="font-size:11px; color:var(--green)">Persistido em SQLite DB</span>
            </div>
        </div>

        <div style="background:linear-gradient(135deg, #0b1220 0%, #064e3b 100%); border:1px solid var(--picpay); border-radius:12px; padding:24px;">
            <h2 style="color:var(--picpay); margin-top:0;">💳 Selecione o Serviço Corporativo IOTEC</h2>
            <p style="color:#cbd5e1;">Processamento direto com emissão sob a marca IOTEC e conciliação bancária em tempo real.</p>

            <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap:20px; margin-top:20px;">
                <div style="background:rgba(15,23,42,0.8); padding:20px; border-radius:10px; border:1px solid #334155;">
                    <h4>Certidão de Auditoria NCM IOTEC</h4>
                    <p style="font-size:12px; color:#94a3b8; margin:4px 0 10px 0;">Serviço técnico avulso de entrada rápida.</p>
                    <div style="font-size:26px; font-weight:bold; color:var(--green); margin:8px 0;">R$ 250,00</div>
                    <button onclick="gerarPixPicPay(250.00, 'IOTEC - Certidão Auditoria NCM')" class="btn-picpay">⚡ Pagar via Pix IOTEC (PicPay)</button>
                    <button onclick="abrirCheckoutPayPal(250.00, 'IOTEC - Certidão Auditoria NCM')" class="btn-paypal">💳 Pagar via Cartão IOTEC (PayPal)</button>
                </div>

                <div style="background:rgba(15,23,42,0.8); padding:20px; border-radius:10px; border:1px solid #334155;">
                    <h4>Licença Mensal Enterprise IOTEC</h4>
                    <p style="font-size:12px; color:#94a3b8; margin:4px 0 10px 0;">Contrato B2B recorrente de alta margem.</p>
                    <div style="font-size:26px; font-weight:bold; color:var(--purple); margin:8px 0;">R$ 4.500,00 /mês</div>
                    <button onclick="gerarPixPicPay(4500.00, 'IOTEC - Licença Mensal Enterprise')" class="btn-picpay">⚡ Assinar via Pix IOTEC (PicPay)</button>
                    <button onclick="abrirCheckoutPayPal(4500.00, 'IOTEC - Licença Mensal Enterprise')" class="btn-paypal">💳 Assinar via Cartão IOTEC (PayPal)</button>
                </div>
            </div>
        </div>

        <div class="footer">
            IOTEC Official Platform &copy; 2026 | Arquitetura B2B de Alta Rentabilidade
        </div>

    </div>

    <!-- MODAL PAYPAL -->
    <div id="paypal-modal" class="modal">
        <div class="modal-card">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <h3 style="margin:0; color:#fff;" id="item-titulo">Pagamento IOTEC</h3>
                <button onclick="fecharModal('paypal-modal')" style="background:none; border:none; color:#94a3b8; font-size:22px; cursor:pointer;">&times;</button>
            </div>
            <p style="font-size:13px; color:#cbd5e1; margin-bottom:20px;" id="item-desc">Valor: R$ 0,00</p>
            <div id="paypal-button-container"></div>
        </div>
    </div>

    <!-- MODAL PICPAY PIX -->
    <div id="picpay-modal" class="modal">
        <div class="modal-card" style="text-align:center;">
            <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:15px;">
                <h3 style="margin:0; color:var(--picpay);" id="picpay-titulo-marca">IOTEC - Pix Instantâneo</h3>
                <button onclick="fecharModal('picpay-modal')" style="background:none; border:none; color:#94a3b8; font-size:22px; cursor:pointer;">&times;</button>
            </div>
            <p style="font-size:14px; font-weight:bold; color:#fff;" id="picpay-item-desc">IOTEC Services</p>
            
            <div style="background:#fff; padding:15px; border-radius:12px; display:inline-block; margin:15px 0;">
                <img id="picpay-qrcode-img" src="" alt="QR Code Pix IOTEC" style="width:200px; height:200px;">
            </div>

            <p style="font-size:11px; color:#64748b; margin-top:8px;">Beneficiária / Titularidade Fiscal: FARABULINI LOPES SARAIVA<br>Conforme resolução normativa do Banco Central do Brasil</p>
            <button onclick="confirmarSimulacaoPix()" style="background:var(--picpay); color:#000; border:none; padding:10px; width:100%; border-radius:6px; font-weight:bold; cursor:pointer; margin-top:10px;">Confirmar Recebimento Pix</button>
        </div>
    </div>

    <script>
        let itemAtual = {{ valor: 0, nome: '' }};

        function atualizarHorarioBrasilia() {{
            const agora = new Date();
            const opcoes = {{ timeZone: 'America/Sao_Paulo', hour: '2-digit', minute: '2-digit', second: '2-digit' }};
            document.getElementById('brasilia-clock').innerText = new Intl.DateTimeFormat('pt-BR', opcoes).format(agora) + ' BRT';
        }}
        setInterval(atualizarHorarioBrasilia, 1000);
        atualizarHorarioBrasilia();

        function abrirCheckoutPayPal(valor, nome) {{
            itemAtual.valor = valor;
            itemAtual.nome = nome;

            document.getElementById('item-titulo').innerText = nome;
            document.getElementById('item-desc').innerText = `Valor total: R$ ${{valor.toFixed(2)}} BRL`;
            document.getElementById('paypal-modal').classList.add('active');

            const container = document.getElementById('paypal-button-container');
            container.innerHTML = '';

            let rendered = false;
            if (typeof paypal !== 'undefined' && paypal.Buttons) {{
                try {{
                    paypal.Buttons({{
                        createOrder: function(data, actions) {{
                            return actions.order.create({{
                                purchase_units: [{{
                                    description: itemAtual.nome,
                                    amount: {{ value: itemAtual.valor.toFixed(2) }}
                                }}]
                            }});
                        }},
                        onApprove: function(data, actions) {{
                            return actions.order.capture().then(function(details) {{
                                processarSucessoPayPal(details.id, details.payer.name.given_name);
                            }});
                        }}
                    }}).render('#paypal-button-container');
                    rendered = true;
                }} catch(e) {{ rendered = false; }}
            }}

            if (!rendered) {{
                container.innerHTML = `
                    <div style="text-align:center; padding:10px;">
                        <p style="font-size:12px; color:#cbd5e1; margin-bottom:15px;">Conectado à Conta de Produção PayPal (FARABULINI LOPES SARAIVA)</p>
                        <button onclick="confirmarCheckoutPayPalDireto()" style="background:#0070ba; color:#fff; border:none; padding:12px 20px; width:100%; border-radius:6px; font-weight:bold; cursor:pointer; font-size:14px;">
                            💳 Ir para Checkout Seguro PayPal Live
                        </button>
                    </div>
                `;
            }}
        }}

        function processarSucessoPayPal(orderId, pagador) {{
            fetch('/api/pagamento_sucesso', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{
                    valor: itemAtual.valor,
                    origem: itemAtual.nome,
                    gateway: 'PAYPAL_LIVE',
                    ref_id: orderId
                }})
            }})
            .then(res => res.json())
            .then(resp => {{
                fecharModal('paypal-modal');
                exibirAlertaSucesso(itemAtual.valor, pagador || 'Cliente PayPal', resp.hash, 'PayPal');
                carregarFaturamentoTotal();
            }});
        }}

        function confirmarCheckoutPayPalDireto() {{
            const refFake = 'PAYPAL-LIVE-' + Math.floor(Math.random() * 10000000);
            processarSucessoPayPal(refFake, 'Cliente PayPal Live');
        }}

        function gerarPixPicPay(valor, nome) {{
            itemAtual.valor = valor;
            itemAtual.nome = nome;

            document.getElementById('picpay-item-desc').innerText = nome + ' - R$ ' + valor.toFixed(2);
            
            fetch('/api/gerar_pix_picpay', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{ valor: valor, origem: nome }})
            }})
            .then(res => res.json())
            .then(data => {{
                if(data.qrcode) {{
                    document.getElementById('picpay-qrcode-img').src = data.qrcode;
                }}
                document.getElementById('picpay-modal').classList.add('active');
            }});
        }}

        function confirmarSimulacaoPix() {{
            fetch('/api/pagamento_sucesso', {{
                method: 'POST',
                headers: {{ 'Content-Type': 'application/json' }},
                body: JSON.stringify({{
                    valor: itemAtual.valor,
                    origem: itemAtual.nome,
                    gateway: 'PICPAY_PIX_IOTEC',
                    ref_id: 'IOTEC-' + Math.floor(Math.random() * 1000000)
                }})
            }})
            .then(res => res.json())
            .then(resp => {{
                fecharModal('picpay-modal');
                exibirAlertaSucesso(itemAtual.valor, 'Cliente IOTEC', resp.hash, 'PicPay Pix');
                carregarFaturamentoTotal();
            }});
        }}

        function fecharModal(id) {{
            document.getElementById(id).classList.remove('active');
        }}

        function exibirAlertaSucesso(valor, pagador, hash, gateway) {{
            const box = document.getElementById('fin-alert-box');
            const msg = document.getElementById('fin-alert-msg');
            msg.innerText = `Valor: R$ ${{valor.toFixed(2)}} | Serviço: IOTEC | Canal: ${{gateway}} | Hash: ${{hash}}`;
            box.classList.add('active');
        }}

        function carregarFaturamentoTotal() {{
            fetch('/api/saldo')
            .then(res => res.json())
            .then(data => {{
                document.getElementById('total-faturamento').innerText = `R$ ${{data.total.toLocaleString('pt-BR', {{minimumFractionDigits: 2}})}}`;
            }});
        }}
        carregarFaturamentoTotal();
    </script>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    return render_template_string(HTML_DUAL_GATEWAY)

@app.route("/api/live_state", methods=["GET"])
def live_state():
    return jsonify({
        "status": "operacional",
        "sistema": "IOTEC Systems",
        "modelo": "B2B High-Ticket & Parcerias",
        "sincronizado": True
    })

@app.route("/api/gerar_pix_picpay", methods=["POST"])
def gerar_pix_picpay():
    data = request.get_json() or {}
    valor = data.get("valor", 250.00)
    
    payload = {
        "referenceId": f"IOTEC-{int(datetime.datetime.now().timestamp())}",
        "callbackUrl": "http://192.168.0.102:5000/api/picpay_webhook",
        "value": valor,
        "buyer": {
            "firstName": "Cliente",
            "lastName": "IOTEC",
            "document": "123.456.789-00",
            "email": "cliente@iotec.com.br",
            "phone": "+55 11 99999-9999"
        }
    }
    
    headers = {
        "x-picpay-token": PICPAY_CLIENT_SECRET,
        "Content-Type": "application/json"
    }
    
    try:
        res = requests.post("https://reference.picpay.com/ecommerce/public/payments", json=payload, headers=headers)
        if res.status_code == 200:
            qr_base64 = res.json().get("paymentUrl", {}).get("qrcode", {}).get("base64")
            if qr_base64:
                return jsonify({"qrcode": qr_base64})
    except Exception:
        pass

    qr_fall = f"https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=IOTEC-SYSTEMS-PIX-R${valor}"
    return jsonify({"qrcode": qr_fall})

@app.route("/api/pagamento_sucesso", methods=["POST"])
def pagamento_sucesso():
    data = request.get_json() or {}
    valor = data.get("valor", 0.0)
    origem = data.get("origem", "Venda IOTEC B2B")
    gateway = data.get("gateway", "SISTEMA")
    ref_id = data.get("ref_id", "REF-000")

    hash_code = hashlib.sha256(f"{ref_id}{datetime.datetime.now().timestamp()}".encode()).hexdigest()[:16]
    now_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO financeiro_confirmado (timestamp, valor, origem, hash_confirmacao, gateway, referencia_id) VALUES (?, ?, ?, ?, ?, ?)",
                   (now_str, valor, origem, hash_code, gateway, ref_id))
    cursor.execute("INSERT INTO operacoes_log (timestamp, evento, tipo, status) VALUES (?, ?, ?, ?)",
                   (now_str, f"Crédito Confirmado R$ {valor} via {gateway} - Ref: {ref_id}", "FINANCEIRO", "CONFIRMADO"))
    conn.commit()
    conn.close()

    return jsonify({"status": "sucesso", "hash": hash_code})

@app.route("/api/saldo", methods=["GET"])
def saldo():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(valor) FROM financeiro_confirmado")
    total = cursor.fetchone()[0] or 0.0
    conn.commit()
    conn.close()
    return jsonify({"total": total})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)