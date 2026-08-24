import sqlite3
import datetime

class NetlifyServerLockEngine:
    def __init__(self):
        self.html_file = "index.html"
        self.db_path = "iotec.db"

    def aplicar_trava_real_netlify(self):
        print(" [NETLIFY LOCK] 🔒 Removendo geração local de PDF/TXT e vinculando à API local...")

        # HTML e JS limpos: O botão NÃO gera mais o documento localmente.
        # Ele obrigatoriamente faz uma requisição HTTP para checar o status de pagamento.
        html_code = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Compliance & Licenciamento Global</title>
    <style>
        body { font-family: Arial, sans-serif; background-color: #0b0f19; color: #e2e8f0; text-align: center; padding: 40px; }
        .box { background: #111827; border: 1px solid #1e293b; padding: 30px; border-radius: 8px; max-width: 450px; margin: 0 auto; }
        .btn { background-color: #2563eb; color: white; padding: 12px 20px; border: none; border-radius: 4px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 15px; }
        .btn:disabled { background-color: #374151; color: #9ca3af; cursor: not-allowed; }
        .alert { color: #f87171; font-size: 13px; margin-top: 15px; display: none; }
    </style>
</head>
<body>
    <div class="box">
        <h2>Solicitação de Certidão Oficial</h2>
        <p>CNPJ MATRIZ: 61.549.037/0001-68</p>
        
        <button id="btn-download" class="btn" onclick="solicitarDownloadServer('IBAMA_CARGAS')">
            CONFIRMAR PAGAMENTO E BAIXAR CERTIDÃO
        </button>

        <div id="erro-trava" class="alert">
            🛑 <strong>ACESSO NEGADO (403):</strong> Pagamento não confirmado via Webhook. Realize o PIX ou transação no PayPal para liberar o documento.
        </div>
    </div>

    <script>
        async function solicitarDownloadServer(documento) {
            const btn = document.getElementById('btn-download');
            const alertBox = document.getElementById('erro-trava');
            alertBox.style.display = 'none';

            try {
                // Chama a API do backend real em vez de gerar arquivo no navegador
                // Substitua a URL abaixo pelo seu endpoint público (ex: Ngrok / Render / Seu IP público)
                const response = await fetch('/api/download-certidao?documento=' + documento);

                if (response.status === 403) {
                    // BLOQUEIO ATIVO: O servidor recusou o download
                    alertBox.style.display = 'block';
                    alert('🛑 ERRO 403: O pagamento não foi confirmado pelo Asaas/PayPal. O documento não pode ser emitido de graça.');
                } else if (response.ok) {
                    // SUCESSO: Servidor liberou o arquivo
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const a = document.createElement('a');
                    a.href = url;
                    a.download = "Certidao_IOTEC_" + documento + ".pdf";
                    a.click();
                } else {
                    alert('Erro ao processar validação no servidor.');
                }
            } catch (error) {
                // Se a API backend não estiver acessível, bloqueia por padrão
                alertBox.style.display = 'block';
                alert('🛑 ERRO DE SERVIDOR: Impossível validar pagamento. Emissão bloqueada por segurança.');
            }
        }
    </script>
</body>
</html>
"""
        with open(self.html_file, "w", encoding="utf-8") as f:
            f.write(html_code)

        # Atualiza status no iotec.db
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_FRONTEND_LOCK_HARDENED', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("  ✅ Código estático fraudulento removido do index.html.")
        print("  ✅ O botão no Netlify agora EXIGE resposta positiva (HTTP 200) da API para liberar qualquer arquivo.")

if __name__ == "__main__":
    engine = NetlifyServerLockEngine()
    engine.aplicar_trava_real_netlify()
