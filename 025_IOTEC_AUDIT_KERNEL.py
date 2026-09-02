import sqlite3

try:
    conn = sqlite3.connect(r"C:\IOTEC\iotec_kernel.db")
    c = conn.cursor()

    leads = c.execute("SELECT COUNT(*) FROM iotec_investor_leads").fetchone()[0]
    virtual_room = c.execute("SELECT COUNT(*) FROM iotec_investor_virtual_room").fetchone()[0]

    print("\n=======================================================")
    print("           AUDITORIA DE DADOS - IOTEC KERNEL           ")
    print("=======================================================")
    print(f" Mapeamento de Investidores (Leads) : {leads} registros")
    print(f" Atendimentos na Sala Virtual       : {virtual_room} registros")
    print("=======================================================\n")

    conn.close()
except Exception as e:
    print(f"[ERRO DE AUDITORIA] {e}")
