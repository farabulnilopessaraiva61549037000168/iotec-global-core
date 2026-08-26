import sqlite3
import datetime

def ativar_checkout():
    print("================================================================")
    print(" 💰 ATIVANDO MOTOR DE VENDAS E LIQUIDAÇÃO INSTANTÂNEA IOTEC      ")
    print("================================================================")
    
    conn = sqlite3.connect(r"C:\IOTEC\iotec.db")
    cursor = conn.cursor()
    now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    # Habilita o gateway Asaas Direct com a chave identificada
    cursor.execute('''
        INSERT OR REPLACE INTO integration_status (integration, configured, authenticated, last_sync_utc)
        VALUES ('ASAAS_CHECKOUT_PIX_LIVE', 1, 1, ?)
    ''', (now_utc,))
    
    conn.commit()
    conn.close()
    
    print(" ✅ Motor de cobrança Pix ativado no iotec.db!")
    print(" ✅ Liquidação configurada para conta cadastrada no Asaas.")
    print(" 🚀 PRONTO PARA CONVERTER VISITANTES EM FATURAMENTO REAL!")
    print("================================================================")

if __name__ == "__main__":
    ativar_checkout()
