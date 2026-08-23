import sqlite3

db_path = "iotec_financial.db"

def inspecionar_projeto():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print("="*65)
    print("        IOTEC - PAINEL DE INSPEÇÃO E STATUS OPERACIONAL")
    print("="*65)
    
    # 1. Total na Auditoria
    cursor.execute("SELECT COUNT(*), SUM(amount) FROM audit_receipts WHERE status = 'VERIFIED_AND_SETTLED'")
    total_audita, valor_audita = cursor.fetchone()
    valor_audita = valor_audita or 0.0
    
    print(f"[*] TRANSAÇÕES LIQUIDADAS E AUDITADAS : {total_audita}")
    print(f"[*] CAIXA REAL CONSOLIDADO           : R$ {valor_audita:.2f}")
    
    # 2. Pendentes
    try:
        cursor.execute("SELECT COUNT(*) FROM real_transactions WHERE status = 'PENDING'")
        pendentes = cursor.fetchone()[0]
    except:
        pendentes = 0
        
    print(f"[*] FATURAS AGUARDANDO PAGAMENTO     : {pendentes}")
    print("="*65)
    
    if valor_audita > 0:
        print("\nSTATUS: ENGINE PRONTA E OPERACIONAL FOR PRODUCTION!")
    else:
        print("\nSTATUS: AGUARDANDO PRIMEIRA LIQUIDAÇÃO COMERCIAL.")
    print("="*65 + "\n")

    conn.close()

if __name__ == "__main__":
    inspecionar_projeto()
