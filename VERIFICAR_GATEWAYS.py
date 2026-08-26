import sqlite3

DB_PATH = "C:\\IOTEC\\iotec.db"

def listar_gateways():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("\n============================================================")
    print(" 💳 MATRIZ DE GATEWAYS OPERACIONAIS — IOTEC.DB")
    print("============================================================")

    cursor.execute("SELECT nome_gateway, status_gateway, tipo_operacao, webhook_url FROM gateways_pagamento")
    gateways = cursor.fetchall()

    for nome, status, tipo, webhook in gateways:
        print(f" 🟢 [{status}] {nome:<15} | Tipo: {tipo}")
        print(f"    └─ Webhook: {webhook}\n")

    print("============================================================\n")
    conn.close()

if __name__ == "__main__":
    listar_gateways()
