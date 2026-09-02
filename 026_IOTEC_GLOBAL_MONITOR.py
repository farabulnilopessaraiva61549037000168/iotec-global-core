from datetime import datetime
import zoneinfo
import sqlite3

def auditar_kernel():
    try:
        conn = sqlite3.connect(r"C:\IOTEC\iotec_kernel.db")
        c = conn.cursor()
        leads = c.execute("SELECT COUNT(*) FROM iotec_investor_leads").fetchone()[0]
        v_room = c.execute("SELECT COUNT(*) FROM iotec_investor_virtual_room").fetchone()[0]
        conn.close()
        return leads, v_room
    except Exception as e:
        return 0, 0

def exibir_usina_global():
    leads, v_room = auditar_kernel()

    paises = [
        ("Brasil (BRT - Fortaleza)", "America/Fortaleza", "Fechamento / Custódia"),
        ("EUA (EDT - Delaware/NY)", "America/New_York", "Mercado Américas"),
        ("Reino Unido (BST - Londres)", "Europe/London", "Hub Financeiro Europa"),
        ("Alemanha (CEST - Berlim)", "Europe/Berlin", "Operação Central UE"),
        ("Emirados Árabes (GST - Dubai)", "Asia/Dubai", "Captação Oriente Médio"),
        ("Japão (JST - Tóquio)", "Asia/Tokyo", "Abertura Mercado Asiático"),
        ("Austrália (AEST - Sydney)", "Australia/Sydney", "Pico Transacional Oceania"),
        ("Cingapura (SGT - Cingapura)", "Asia/Singapore", "Hub Tecnológico Ásia")
    ]

    print("\n=================================================================================")
    print("                     USINA GLOBAL IOTEC - MONITOR EXPANDIDO (24/7)               ")
    print("=================================================================================")
    print(f" AUDITORIA KERNEL | Leads Mapeados: {leads} | Sala Virtual: {v_room}")
    print("---------------------------------------------------------------------------------")
    
    for nome, fuso, status in paises:
        hora_local = datetime.now(zoneinfo.ZoneInfo(fuso)).strftime("%Y-%m-%d %H:%M:%S")
        print(f" {nome:<30} : {hora_local} | [{status}]")

    print("=================================================================================\n")

if __name__ == "__main__":
    exibir_usina_global()


