import sqlite3

DB_PATH = "C:\\IOTEC\\iotec_database.db"

def salvar_credenciais(pix="", paypal_client="", paypal_secret="", smtp_host="", smtp_user="", smtp_pass=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    credenciais = [
        ("CHAVE_PIX", pix),
        ("PAYPAL_CLIENT_ID", paypal_client),
        ("PAYPAL_SECRET", paypal_secret),
        ("SMTP_HOST", smtp_host),
        ("SMTP_USER", smtp_user),
        ("SMTP_PASS", smtp_pass)
    ]
    
    for chave, valor in credenciais:
        if valor:
            cursor.execute("INSERT OR REPLACE INTO config_producao (chave, valor, status) VALUES (?, ?, 'CONFIGURADO')", (chave, valor))
            print(f"[✔] {chave} atualizada com sucesso.")
            
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Insira seus dados reais entre as aspas para gravar no sistema:
    salvar_credenciais(
        pix="SUA_CHAVE_PIX_AQUI",
        paypal_client="SEU_CLIENT_ID_PAYPAL",
        paypal_secret="SEU_SECRET_PAYPAL",
        smtp_host="smtp.seuemail.com.br",
        smtp_user="contato@seuemail.com.br",
        smtp_pass="SUA_SENHA_EMAIL"
    )
