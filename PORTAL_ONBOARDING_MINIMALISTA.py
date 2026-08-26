import http.server
import socketserver

PORT = 8080

HTML_PAGE = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC — Onboarding do Sistema</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
        body { background-color: #09090B; color: #FAFAFA; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .container { width: 100%; max-width: 480px; background: #121215; border: 1px solid #27272A; border-radius: 16px; padding: 40px; box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7); }
        .header { margin-bottom: 32px; }
        .tag { font-size: 11px; font-weight: 600; text-transform: uppercase; letter-spacing: 1.5px; color: #2563EB; margin-bottom: 8px; display: block; }
        h2 { font-size: 24px; font-weight: 600; letter-spacing: -0.5px; margin-bottom: 8px; }
        p { font-size: 14px; color: #A1A1AA; line-height: 1.5; }
        .form-group { margin-bottom: 24px; }
        label { display: block; font-size: 12px; font-weight: 500; color: #A1A1AA; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px; }
        textarea { width: 100%; background: #18181B; border: 1px solid #27272A; border-radius: 8px; padding: 14px; color: #FAFAFA; font-size: 14px; resize: none; height: 120px; outline: none; transition: border-color 0.2s; }
        textarea:focus { border-color: #2563EB; }
        button { width: 100%; background: #FAFAFA; color: #09090B; border: none; padding: 14px; border-radius: 8px; font-size: 14px; font-weight: 600; cursor: pointer; transition: opacity 0.2s; }
        button:hover { opacity: 0.9; }
        .footer-note { text-align: center; margin-top: 24px; font-size: 12px; color: #52525B; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <span class="tag">Pagamento Confirmado</span>
            <h2>Especificação do Sistema</h2>
            <p>Descreva os principais gargalos ou funções prioritárias da sua empresa. O Agente Arquiteto compilará seu software em segundos.</p>
        </div>
        <form>
            <div class="form-group">
                <label>Relato de Requisitos / Dores Operacionais</label>
                <textarea placeholder="Ex: Preciso automatizar o controle do fluxo de caixa e enviar notificações pelo WhatsApp..."></textarea>
            </div>
            <button type="button" onclick="alert('Requisição enviada! O Agente Arquiteto iniciou a compilação do seu software.')">Iniciar Fabricação Autônoma</button>
        </form>
        <div class="footer-note">IOTEC Engine v2.4 — Criptografia de Ponta a Ponta</div>
    </div>
</body>
</html>
"""

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML_PAGE.encode('utf-8'))

print(f"[✔] Portal Onboarding IOTEC rodando em: http://localhost:{PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
