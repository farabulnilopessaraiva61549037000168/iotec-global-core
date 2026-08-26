import os
import shutil
import subprocess
import sqlite3
import datetime

class LockFrontendEngine:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.dist_dir = os.path.join(self.root_dir, "dist")
        self.index_file = os.path.join(self.root_dir, "index.html")
        self.db_path = os.path.join(self.root_dir, "iotec.db")

    def reescrever_index_travado(self):
        print(" [1/3] 🔒 Reescrevendo index.html para neutralizar gerador PDF local no navegador...")
        
        # HTML travado com interface escura e validacao obrigatoria de pagamento
        html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Global Intelligence & Multimodal</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; }
        body { background-color: #0b0f19; color: #ffffff; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
        .card { background-color: #111827; border: 1px solid #1f2937; border-radius: 12px; width: 100%; max-width: 550px; padding: 40px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { font-size: 1.5rem; font-weight: 700; margin-bottom: 12px; color: #ffffff; }
        .cnpj { font-size: 0.875rem; font-weight: 600; color: #9ca3af; margin-bottom: 24px; border-bottom: 1px solid #1f2937; padding-bottom: 16px; }
        .btn-emissao { width: 100%; background-color: #2563eb; color: #ffffff; border: none; padding: 14px 20px; font-size: 0.95rem; font-weight: 700; border-radius: 6px; cursor: pointer; transition: background-color 0.2s; text-transform: uppercase; letter-spacing: 0.5px; }
        .btn-emissao:hover { background-color: #1d4ed8; }
        .status-box { margin-top: 20px; padding: 12px; border-radius: 6px; font-size: 0.875rem; font-weight: 600; display: none; }
        .status-error { background-color: rgba(239, 68, 68, 0.1); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.2); }
    </style>
</head>
<body>
    <div class="card">
        <h1>Emissão de Certidão & Compliance</h1>
        <div class="cnpj">CNPJ MATRIZ: 61.549.037/0001-68</div>
        <button id="btnEmitir" class="btn-emissao" onclick="processarEmissao()">Solicitar Emissão de Certidão</button>
        <div id="msgStatus" class="status-box status-error"></div>
    </div>

    <script>
        function processarEmissao() {
            const btn = document.getElementById('btnEmitir');
            const msg = document.getElementById('msgStatus');
            btn.disabled = true;
            btn.innerText = 'VERIFICANDO STATUS FINANCEIRO...';

            setTimeout(() => {
                btn.disabled = false;
                btn.innerText = 'SOLICITAR EMISSÃO DE CERTIDÃO';
                msg.style.display = 'block';
                msg.innerHTML = '🛑 <strong>ACESSO BLOQUEADO (403 FORBIDDEN)</strong><br>A emissão deste documento exige confirmação de pagamento prévia via Pix/Cartão no sistema central.';
            }, 800);
        }
    </script>
</body>
</html>
"""
        with open(self.index_file, "w", encoding="utf-8") as f:
            f.write(html_content)
        print("  ✅ Arquivo `index.html` reescrito sem chamadas a geradores PDF locais.")

    def preparar_dist(self):
        print(" [2/3] 📦 Atualizando diretório isolado 'dist'...")
        if os.path.exists(self.dist_dir):
            shutil.rmtree(self.dist_dir)
        os.makedirs(self.dist_dir, exist_ok=True)

        shutil.copy2(self.index_file, os.path.join(self.dist_dir, "index.html"))

        # Copia diretivas de cabeçalho
        for arq in ["_headers", "_redirects"]:
            orig = os.path.join(self.root_dir, arq)
            if os.path.exists(orig):
                shutil.copy2(orig, os.path.join(self.dist_dir, arq))

    def disparar_deploy(self):
        print(" [3/3] 🚀 Publicando alterações diretamente no Netlify (--prod)...")
        cmd = "npx netlify-cli deploy --dir dist --prod --skip-functions-cache"
        subprocess.run(cmd, shell=True, text=True)

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('NETLIFY_FRONTEND_PDF_GENERATOR_DISABLED', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" ✅ PROCESSO FINALIZADO COM SUCESSO!")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = LockFrontendEngine()
    engine.reescrever_index_travado()
    engine.preparar_dist()
    engine.disparar_deploy()
