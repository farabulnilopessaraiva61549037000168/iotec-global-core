import sqlite3
import os

DB_PATH = "C:\\IOTEC\\iotec_database.db"

def auditar_e_liberar():
    print("==================================================")
    print("   AUDITORIA DE SISTEMA E LIBERAÇÃO DE VENDAS IOTEC   ")
    print("==================================================\n")

    # 1. Auditoria de Banco de Dados
    if os.path.exists(DB_PATH):
        print("[✔] Banco de dados iotec_database.db ENCONTRADO.")
    else:
        print("[!] Banco de dados não localizado. Criando novo ambiente...")

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Tabela de Configurações Globais de Produção
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS config_producao (
            chave TEXT PRIMARY KEY,
            valor TEXT,
            status TEXT
        )
    ''')

    # Configurações de Venda Real
    configs = [
        ("MODO_OPERACAO", "PRODUCAO_REAL", "ATIVO"),
        ("GATEWAY_PAYPAL_STATUS", "AGUARDANDO_KEYS", "PENDENTE"),
        ("GATEWAY_PIX_STATUS", "CHAVE_REQUERIDA", "PENDENTE"),
        ("WHATSAPP_API_STATUS", "DESCONECTADO", "PENDENTE"),
        ("EMAIL_SMTP_STATUS", "DESCONECTADO", "PENDENTE")
    ]

    for chave, valor, status in configs:
        cursor.execute('''
            INSERT OR REPLACE INTO config_producao (chave, valor, status)
            VALUES (?, ?, ?)
        ''', (chave, valor, status))

    conn.commit()

    # 2. Resumo de Leads Prontos para Abordagem
    cursor.execute("SELECT COUNT(*) FROM central_vendas_leads")
    total_leads = cursor.fetchone()[0] if cursor else 0
    print(f"[✔] Total de Leads Minerados no Banco: {total_leads}")

    print("\n--------------------------------------------------")
    print("STATUS DO NÚCLEO: [ MODO PRODUÇÃO ATIVADO ]")
    print("--------------------------------------------------")
    print("Para que as mensagens e cobranças reais saiam no mundo externo,")
    print("você precisa fornecer as credenciais abaixo:\n")
    print("1. Chave PIX (E-mail, CPF/CNPJ ou Aleatória)")
    print("2. Credenciais PayPal (Client ID & Secret)")
    print("3. Dados SMTP do E-mail (Host, Porta, Usuário, Senha)")
    print("4. Token/QR Code da API de WhatsApp")
    print("==================================================")

if __name__ == "__main__":
    auditar_e_liberar()
