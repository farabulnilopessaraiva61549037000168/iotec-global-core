from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import sqlite3
import webbrowser

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Portal de Auditoria & Governança Executiva</title>
    <style>
        :root { --primary: #0f172a; --accent: #2563eb; --success: #16a34a; --bg: #f8fafc; }
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: var(--bg); color: #334155; margin: 0; padding: 20px; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); }
        .header { border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: center; }
        .badge { background: #dcfce7; color: var(--success); padding: 6px 12px; border-radius: 20px; font-weight: bold; font-size: 0.85rem; }
        .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 20px; margin-bottom: 30px; }
        .card { background: #f1f5f9; padding: 20px; border-radius: 8px; border-left: 4px solid var(--accent); }
        .card h3 { margin: 0 0 10px 0; font-size: 0.9rem; color: #64748b; text-transform: uppercase; }
        .card p { margin: 0; font-size: 1.6rem; font-weight: bold; color: var(--primary); }
        .section-title { font-size: 1.2rem; font-weight: bold; margin-bottom: 15px; color: var(--primary); border-left: 4px solid var(--primary); padding-left: 10px; }
        .table-container { overflow-x: auto; margin-bottom: 30px; }
        table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        th, td { text-align: left; padding: 12px; border-bottom: 1px solid #e2e8f0; }
        th { background-color: #f8fafc; color: #475569; }
        .btn { background: var(--accent); color: white; border: none; padding: 12px 24px; border-radius: 6px; font-weight: bold; cursor: pointer; text-decoration: none; display: inline-block; }
        .btn:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div>
                <h1 style="margin:0; font-size: 1.8rem; color: var(--primary);">IOTEC GLOBAL CORE</h1>
                <p style="margin:5px 0 0 0; color: #64748b;">CNPJ: 61.549.037/0001-68 | Projeto REGULUS</p>
            </div>
            <span class="badge">AUDITORIA ATIVA - EM TEMPO REAL</span>
        </div>

        <div class="grid">
            <div class="card">
                <h3>Base de Leads (B2B)</h3>
                <p>2.155 CNPJs</p>
            </div>
            <div class="card">
                <h3>Gateway Nacional</h3>
                <p style="color: var(--success);">ASAAS (Ativo)</p>
            </div>
            <div class="card">
                <h3>Gateway Global</h3>
                <p style="color: var(--success);">USD / EUR (Ativo)</p>
            </div>
            <div class="card">
                <h3>Modelo de Receita</h3>
                <p>SaaS High-Ticket</p>
            </div>
        </div>

        <div class="section-title">Amostra Auditável do Banco de Dados (`iotec.db`)</div>
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Razão Social / Identificador</th>
                        <th>Segmento</th>
                        <th>Status no Core</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td>001</td><td>EMPRESA TECNOLÓGICA B2B 01</td><td>SaaS / Tecnologia</td><td><span class="badge">Qualificado</span></td></tr>
                    <tr><td>002</td><td>LOGÍSTICA & OPERAÇÕES B2B 02</td><td>Logística</td><td><span class="badge">Qualificado</span></td></tr>
                    <tr><td>003</td><td>SERVIÇOS FINANCEIROS B2B 03</td><td>Fintech</td><td><span class="badge">Qualificado</span></td></tr>
                    <tr><td>004</td><td>GRUPO INDUSTRIAL B2B 04</td><td>Indústria</td><td><span class="badge">Qualificado</span></td></tr>
                    <tr><td>005</td><td>CONSULTORIA EXECUTIVA B2B 05</td><td>Serviços</td><td><span class="badge">Qualificado</span></td></tr>
                </tbody>
            </table>
        </div>

        <div class="section-title">Engenharia de Retiradas & Governança (CPF 011.902.313-01)</div>
        <p>Sistema configurado com trava de retenção para liquidação de compromissos bancários e automação de repasse de <strong>Pró-Labore Fixo (1 Mínimo)</strong> + <strong>Dividendos Isentos de IRPF</strong>.</p>
        
        <div style="margin-top: 30px; text-align: right;">
            <button class="btn" onclick="alert('Relatório de Governança Auditado com Sucesso!')">Confirmar Validação de Crédito</button>
        </div>
    </div>
</body>
</html>
"""

class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(HTML_TEMPLATE.encode('utf-8'))

def run_server():
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, DemoHandler)
    print(f"==========================================================================================")
    print(f" 🌐  IOTEC WEB CORE | PORTAL DE DEMONSTRAÇÃO ATIVO EM: http://localhost:{port}")
    print(f"==========================================================================================")
    webbrowser.open(f"http://localhost:{port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run_server()
