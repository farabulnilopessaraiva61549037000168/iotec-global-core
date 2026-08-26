import sqlite3

DB_PATH = "C:\\IOTEC\\iotec.db"

def registrar_paypal():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO gateways_pagamento (nome_gateway, status_gateway, tipo_operacao, api_key_publica, webhook_url)
        VALUES ('PAYPAL', 'ATIVO', 'GLOBAL_EXPRESS_CHECKOUT', 'paypal_live_client_id_001', 'https://iotec-shield.render.com/webhook/paypal')
        ON CONFLICT(nome_gateway) DO UPDATE SET
            status_gateway=excluded.status_gateway,
            tipo_operacao=excluded.tipo_operacao,
            webhook_url=excluded.webhook_url
    ''')

    conn.commit()

    print("============================================================")
    print(" 💳 GATEWAY PAYPAL REGISTRADO E RECONHECIDO NO IOTEC.DB!")
    print("============================================================")
    print(" ├─ Modalidade: Global Express Checkout (USD / EUR / GBP / BRL)")
    print(" ├─ Status no iotec.db: ATIVO & HABILITADO")
    print(" └─ Webhook de Retorno: https://iotec-shield.render.com/webhook/paypal")
    print("============================================================\n")

    conn.close()

if __name__ == "__main__":
    registrar_paypal()
