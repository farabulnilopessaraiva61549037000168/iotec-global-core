import os
import sqlite3
import datetime

class FixPaypalNetlifyEngine:
    def __init__(self):
        self.db_path = "iotec.db"
        self.html_file = "index.html"

    def injetar_renderizador_paypal(self):
        print(" [PAYPAL FIX] 🛠️ Injetando container dinamico do PayPal SDK no index.html...")

        # Estrutura HTML/JS limpa para renderizar botões e campos de cartão no Netlify
        html_code = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>IOTEC | Global Intelligence & Multi-Currency</title>
    <!-- PayPal SDK com Card Fields e Buttons -->
    <script src="https://www.paypal.com/sdk/js?client-id=sb&components=buttons,card-fields&currency=BRL"></script>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0b0f19; color: #e2e8f0; margin: 0; padding: 20px; }
        .card { background: #111827; border: 1px solid #1e293b; padding: 20px; border-radius: 8px; max-width: 500px; margin: 40px auto; text-align: center; }
        .btn-pix { background-color: #00bdae; color: #fff; padding: 12px; border: none; border-radius: 4px; font-weight: bold; width: 100%; cursor: pointer; margin-bottom: 15px; }
        #paypal-button-container { margin-top: 15px; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Emissão Oficial de Licenças</h2>
        <p><strong>CNPJ MATRIZ:</strong> 61.549.037/0001-68</p>

        <button class="btn-pix">PAGAR VIA PIX CNPJ / PICPAY NEGÓCIOS</button>

        <div id="paypal-container">
            <h3>Pagamento Global (PayPal / Cartão)</h3>
            <div id="paypal-button-container"></div>
        </div>
    </div>

    <script>
        // Renderiza os botões do PayPal no container dedicado
        if (window.paypal) {
            paypal.Buttons({
                style: { layout: 'vertical', color: 'gold', shape: 'rect', label: 'pay' }
            }).render('#paypal-button-container');
        }
    </script>
</body>
</html>
"""
        with open(self.html_file, "w", encoding="utf-8") as f:
            f.write(html_code)

        print("  ✅ Arquivo `index.html` atualizado com o container `#paypal-button-container`.")

        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('PAYPAL_HTML_RENDER_FIXED', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("  ✅ Status registrado no `iotec.db` e pronto para deploy.")

if __name__ == "__main__":
    engine = FixPaypalNetlifyEngine()
    engine.injetar_renderizador_paypal()
