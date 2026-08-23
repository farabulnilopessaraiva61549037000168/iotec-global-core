import os
import json
import sqlite3
import webbrowser
from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime, timezone, timedelta

DB_PATH = r"C:\IOTEC\audit_ledger.db"
PORT = 8080

def obter_hora_brasilia():
    tz_br = timezone(timedelta(hours=-3))
    return datetime.now(tz_br).strftime("%d/%m/%Y %H:%M:%S")

def obter_dados_dashboard():
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS transacoes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                ordem_id TEXT,
                ambiente TEXT,
                valor REAL,
                status TEXT,
                cliente TEXT
            )
        ''')
        conn.commit()
        conn.close()

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM transacoes WHERE status = 'CONCLUIDO'")
    vendas_concluidas = cursor.fetchone()[0] or 0

    cursor.execute("SELECT SUM(valor) FROM transacoes WHERE status = 'CONCLUIDO'")
    receita_total = cursor.fetchone()[0] or 0.0

    cursor.execute("SELECT COUNT(*) FROM transacoes WHERE status = 'AGUARDANDO_PAGAMENTO'")
    prospecçoes_ativas = cursor.fetchone()[0] or 0

    cursor.execute("SELECT timestamp, ordem_id, ambiente, valor, status, cliente FROM transacoes ORDER BY id DESC LIMIT 10")
    registros = cursor.fetchall()
    conn.close()

    ultimas_transacoes = []
    for reg in registros:
        ultimas_transacoes.append({
            "hora": reg[0],
            "ordem_id": reg[1],
            "ambiente": reg[2],
            "valor": f"R$ {reg[3]:,.2f}",
            "status": reg[4],
            "cliente": reg[5]
        })

    return {
        "hora": obter_hora_brasilia(),
        "vendas": vendas_concluidas,
        "receita": f"R$ {receita_total:,.2f}",
        "prospecçoes": prospecçoes_ativas,
        "transacoes": ultimas_transacoes
    }

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC / X27 - Central de Operações Comerciais</title>
    <style>
        :root {
            --bg-color: #0d1117;
            --panel-bg: #161b22;
            --border-color: #30363d;
            --accent-color: #238636;
            --text-color: #c9d1d9;
            --highlight: #58a6ff;
            --warning: #d29922;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            margin: 0;
            padding: 20px;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 15px;
            margin-bottom: 25px;
        }
        .header h1 {
            margin: 0;
            font-size: 24px;
            color: #fff;
        }
        .status-badge {
            background-color: var(--accent-color);
            color: #fff;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: bold;
        }
        .metrics-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }
        .card {
            background-color: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
        }
        .card h3 {
            margin: 0 0 10px 0;
            font-size: 14px;
            color: #8b949e;
            text-transform: uppercase;
        }
        .card .value {
            font-size: 28px;
            font-weight: bold;
            color: #fff;
        }
        .section-title {
            font-size: 18px;
            color: #fff;
            margin-bottom: 15px;
            border-left: 4px solid var(--highlight);
            padding-left: 10px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            background-color: var(--panel-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            overflow: hidden;
            margin-bottom: 30px;
        }
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid var(--border-color);
        }
        th {
            background-color: #21262d;
            color: #8b949e;
            font-size: 12px;
            text-transform: uppercase;
        }
        tr:last-child td { border-bottom: none; }
        .modules-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .btn-action {
            background-color: #238636;
            color: #fff;
            border: none;
            padding: 8px 16px;
            border-radius: 6px;
            cursor: pointer;
            font-weight: bold;
            text-decoration: none;
            display: inline-block;
            margin-top: 10px;
        }
        .btn-action:hover { background-color: #2ea043; }
    </style>
</head>
<body>

    <div class="header">
        <div>
            <h1>Central de Operações Comerciais IOTEC / X27</h1>
            <small style="color: #8b949e;">Última sincronização: <span id="hora-sincronizacao">--:--:--</span> (Horário de Brasília)</small>
        </div>
        <span class="status-badge">🟢 SISTEMA ONLINE - AUDITORIA ATIVA</span>
    </div>

    <div class="metrics-grid">
        <div class="card">
            <h3>Receita Confirmada (Conta)</h3>
            <div class="value" id="metrica-receita">R$ 0,00</div>
        </div>
        <div class="card">
            <h3>Contratos Liquidados</h3>
            <div class="value" id="metrica-vendas">0</div>
        </div>
        <div class="card">
            <h3>Propostas em Aberto</h3>
            <div class="value" id="metrica-prospecçoes">0</div>
        </div>
    </div>

    <div class="section-title">📊 Observabilidade & Transações em Tempo Real (Zero Simulação)</div>
    <table>
        <thead>
            <tr>
                <th>Data / Hora</th>
                <th>ID da Ordem</th>
                <th>Ambiente</th>
                <th>Valor</th>
                <th>Status</th>
                <th>Cliente / Payer</th>
            </tr>
        </thead>
        <tbody id="tabela-transacoes">
            <tr><td colspan="6" style="text-align:center;">Aguardando primeiras movimentações do audit_ledger.db...</td></tr>
        </tbody>
    </table>

    <div class="section-title">🚀 Catálogo de Módulos & Disparadores de Vendas</div>
    <div class="modules-grid">
        <div class="card">
            <h3 style="color: var(--highlight);">Licença Atendimento Base</h3>
            <p style="font-size: 20px; font-weight: bold; color: #fff; margin: 5px 0;">R$ 29,90</p>
            <p style="font-size: 13px;">Módulo de integração imediata via PIX / Checkout Nacional com auditoria local.</p>
            <button class="btn-action" onclick="alert('Disparando script de geração 099P_SANDBOX_PAYMENT_2990.py via PowerShell...')">Disparar Link de Cobrança</button>
        </div>
        <div class="card">
            <h3 style="color: var(--highlight);">Contrato Corporativo B2B</h3>
            <p style="font-size: 20px; font-weight: bold; color: #fff; margin: 5px 0;">Ticket Personalizado</p>
            <p style="font-size: 13px;">Proposta comercial automatizada com suporte a PayPal International / Multi-moedas.</p>
            <button class="btn-action" style="background-color: #388bfd;" onclick="alert('Módulo de Proposta Internacional em Standby')">Gerar Proposta B2B</button>
        </div>
    </div>

    <script>
        async function atualizarDashboard() {
            try {
                const response = await fetch('/api/dados');
                const data = await response.json();

                document.getElementById('hora-sincronizacao').innerText = data.hora;
                document.getElementById('metrica-receita').innerText = data.receita;
                document.getElementById('metrica-vendas').innerText = data.vendas;
                document.getElementById('metrica-prospecçoes').innerText = data.prospecçoes;

                const tbody = document.getElementById('tabela-transacoes');
                if (data.transacoes.length === 0) {
                    tbody.innerHTML = '<tr><td colspan="6" style="text-align:center;">Nenhuma transação registrada no banco ainda.</td></tr>';
                } else {
                    tbody.innerHTML = data.transacoes.map(t => 
                        <tr>
                            <td></td>
                            <td><code></code></td>
                            <td><span style="color: "></span></td>
                            <td><strong></strong></td>
                            <td><span style="color: "></span></td>
                            <td></td>
                        </tr>
                    ).join('');
                }
            } catch (err) {
                console.error("Erro ao atualizar o dashboard:", err);
            }
        }

        // Atualização automática a cada 3 segundos (Polling em Tempo Real)
        setInterval(atualizarDashboard, 3000);
        atualizarDashboard();
    </script>
</body>
</html>
"""

class CustomHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(HTML_TEMPLATE.encode('utf-8'))
        elif self.path == '/api/dados':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            dados = obter_dados_dashboard()
            self.wfile.write(json.dumps(dados).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()

def iniciar_servidor():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, CustomHandler)
    url = f"http://localhost:{PORT}"
    
    print("=" * 65)
    print("     CENTRAL DE OPERAÇÕES COMERCIAIS IOTEC/X27 - SERVIDOR WEB     ")
    print("=" * 65)
    print(f" [!] PAINEL DISPONÍVEL EM : {url}")
    print(f" [!] STATUS               : AGUARDANDO REQUISIÇÕES EM TEMPO REAL")
    print("=" * 65)
    
    webbrowser.open(url)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[!] Servidor encerrado pelo usuário.")

if __name__ == "__main__":
    iniciar_servidor()
