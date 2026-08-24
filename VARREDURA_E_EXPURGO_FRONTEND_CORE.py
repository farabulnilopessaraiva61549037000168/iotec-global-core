import os
import glob
import sqlite3
import datetime

class ExpurgarScriptsVulneraveisEngine:
    def __init__(self):
        self.db_path = "iotec.db"

    def expurgar(self):
        print(" [EXPURGO CORE] 🧹 Varrendo e eliminando scripts de geração local de PDF/TXT...")

        # HTML com bloqueio absoluto e sem funções legadas
        html_seguro = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Global Intelligence & Multi-Currency</title>
    <style>
        body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #0b0f19; color: #e2e8f0; text-align: center; padding: 50px 20px; }
        .card { background: #111827; border: 1px solid #1e293b; padding: 30px; border-radius: 8px; max-width: 480px; margin: 0 auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }
        .alert-error { background-color: #451a1a; border: 1px solid #7f1d1d; color: #fca5a5; padding: 15px; border-radius: 6px; margin-top: 20px; font-size: 14px; text-align: left; }
        .btn-pay { background-color: #2563eb; color: #fff; border: none; padding: 14px; width: 100%; border-radius: 4px; font-weight: bold; cursor: pointer; font-size: 15px; }
        .btn-disabled { background-color: #374151; color: #9ca3af; cursor: not-allowed; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Emissão de Certidão & Compliance</h2>
        <p><strong>CNPJ MATRIZ:</strong> 61.549.037/0001-68</p>
        <hr style="border-color: #1e293b; margin: 20px 0;">

        <button id="btn-emitir" class="btn-pay" onclick="tentarEmissaoServer('DUIMP')">
            SOLICITAR EMISSÃO DE CERTIDÃO
        </button>

        <div id="painel-bloqueio" class="alert-error" style="display:none;">
            🛑 <strong>EMISSÃO BLOQUEADA (403 FORBIDDEN)</strong><br>
            A chave PIX/PayPal não registrou a liquidação do valor na conta PJ. É proibido emitir documentos sem confirmação do gateway.
        </div>
    </div>

    <script>
        async function tentarEmissaoServer(doc) {
            const painel = document.getElementById('painel-bloqueio');
            painel.style.display = 'none';

            try {
                // Tenta consultar a API server-side
                let res = await fetch('/api/download-certidao?documento=' + doc);
                if (res.status === 200) {
                    let blob = await res.blob();
                    let url = window.URL.createObjectURL(blob);
                    let a = document.createElement('a');
                    a.href = url;
                    a.download = "Certidao_" + doc + ".pdf";
                    a.click();
                } else {
                    // Se não estiver PAGO (403), exibe o bloqueio
                    painel.style.display = 'block';
                }
            } catch (e) {
                // Se não houver servidor, BLOQUEIA IMEDIATAMENTE
                painel.style.display = 'block';
            }
        }
    </script>
</body>
</html>
"""
        # Sobrescreve index.html
        with open("index.html", "w", encoding="utf-8") as f:
            f.write(html_seguro)

        # Procura e limpa outros arquivos HTML/JS soltos que possam conter o gerador antigo
        for filepath in glob.glob("*.html"):
            if filepath != "index.html":
                os.remove(filepath)
                print(f"  🗑️ Arquivo legado removido: {filepath}")

        # Atualiza o registro no iotec.db
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('FRONTEND_EXPURGO_COMPLETO', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("  ✅ Limpeza concluída. Apenas a checagem Server-Side permaneceu.")

if __name__ == "__main__":
    engine = ExpurgarScriptsVulneraveisEngine()
    engine.expurgar()
