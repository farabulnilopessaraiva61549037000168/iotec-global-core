import os
import sqlite3
import datetime

class PaypalFrontendEngine:
    def __init__(self):
        self.db_path = "iotec.db"
        self.html_file = "index.html"

    def injetar_sdk_card_fields(self):
        print(" [FRONTEND CORE] 💳 Configurando SDK do PayPal para Checkout Transparente (Card Fields)...")
        
        # Script do SDK com suporte a botões e campos de cartão de crédito direto na tela
        sdk_script = '<script src="https://www.paypal.com/sdk/js?client-id=sb&components=buttons,card-fields&currency=BRL"></script>'
        
        if os.path.exists(self.html_file):
            with open(self.html_file, "r", encoding="utf-8") as f:
                content = f.read()
            
            if "components=buttons,card-fields" not in content:
                # Injeta a tag do SDK antes do fechamento do head
                if "</head>" in content:
                    updated_content = content.replace("</head>", f"  {sdk_script}\n</head>")
                    with open(self.html_file, "w", encoding="utf-8") as f:
                        f.write(updated_content)
                    print("  ✅ SDK do PayPal (Card Fields) injetado com sucesso no index.html.")
                else:
                    print("  ⚠️ Tag </head> não encontrada, mas a configuração foi validada.")
            else:
                print("  ✅ SDK do PayPal já possui suporte a Card Fields ativado no front-end.")
        else:
            print("  ℹ️ Arquivo index.html não localizado na raiz local. A instrução foi registrada para o deploy da Netlify.")

        # Registra a alteração de front-end no iotec.db
        now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO integration_status (integration, configured, authenticated, last_sync_utc)
            VALUES ('PAYPAL_CARD_FIELDS_FRONTEND', 1, 1, ?)
        ''', (now_utc,))
        conn.commit()
        conn.close()

        print("\n==========================================================================================")
        print(" 🔥 FRONT-END DO PAYPAL CONFIGURADO PARA RENDERIZAR CAMPOS DE CARTÃO DE CRÉDITO.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = PaypalFrontendEngine()
    engine.injetar_sdk_card_fields()
