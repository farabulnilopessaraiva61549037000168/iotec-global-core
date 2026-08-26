import sqlite3

DB_PATH = "C:\\IOTEC\\iotec.db"

def registrar_remessa_online():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Cria tabela de gateways caso nao exista
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS gateways_pagamento (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_gateway TEXT UNIQUE,
            status_gateway TEXT DEFAULT 'ATIVO',
            tipo_operacao TEXT,
            api_key_publica TEXT,
            webhook_url TEXT
        )
    ''')

    # Injeta ou atualiza os gateways ativos
    gateways = [
        ('ASAAS', 'ATIVO', 'NACIONAL_PIX_BOLETO', 'asaas_live_key_991823', 'https://iotec-shield.render.com/webhook/asaas'),
        ('PICPAY', 'ATIVO', 'NACIONAL_PIX_CARD', 'picpay_live_token_77123', 'https://iotec-shield.render.com/webhook/picpay'),
        ('REMESSA_ONLINE', 'ATIVO', 'INTERNACIONAL_CROSSBORDER', 'remessa_cnpj_live_88301', 'https://iotec-shield.render.com/webhook/remessa')
    ]

    for nome, status, tipo, key, webhook in gateways:
        cursor.execute('''
            INSERT INTO gateways_pagamento (nome_gateway, status_gateway, tipo_operacao, api_key_publica, webhook_url)
            VALUES (?, ?, ?, ?, ?)
            ON CONFLICT(nome_gateway) DO UPDATE SET
                status_gateway=excluded.status_gateway,
                tipo_operacao=excluded.tipo_operacao,
                webhook_url=excluded.webhook_url
        ''', (nome, status, tipo, key, webhook))

    conn.commit()
    conn.close()

    print("============================================================")
    print(" 💳 GATEWAY REMESSA ONLINE REGISTRADO COM SUCESSO!")
    print("============================================================")
    print(" ├─ Modalidade: Internacional / Cross-Border (USD / EUR / BRL)")
    print(" ├─ Status no iotec.db: ATIVO & HABILITADO")
    print(" └─ Webhook de Retorno: https://iotec-shield.render.com/webhook/remessa")
    print("============================================================\n")

if __name__ == "__main__":
    registrar_remessa_online()
