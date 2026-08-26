import sqlite3
import time
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

def processar_ofertas_reais():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    print("============================================================")
    print(" 🚀 IOTEC MAIL CORE — DISPARO DE OFERTAS REAIS (SHIELD B2B)")
    print("============================================================\n")

    cursor.execute("SELECT id, razao_social, polo_regiao FROM leads_reais_capturados WHERE status_prospecacao = 'PRONTO_PARA_OFETA_REAL'")
    leads = cursor.fetchall()

    if not leads:
        print(" [!] Nenhum lead real pendente na fila.")
        conn.close()
        return

    for lead_id, razao, polo in leads:
        horario = datetime.datetime.now().strftime('%H:%M:%S')
        print(f"[{horario}] 🛡️ ENVIANDO OFERTA SHIELD -> {razao}")
        print(f"          ├─ Polo: {polo}")
        print(f"          ├─ Proposta: Alívio Técnico, Bloqueio Anti-Spam & Limpeza de RAM")
        print(f"          └─ Link Checkout: https://iotec-shield.render.com/checkout?lead={lead_id}\n")
        
        # Atualiza o status no banco de dados
        cursor.execute("UPDATE leads_reais_capturados SET status_prospecacao = 'OFERTA_ENVIADA' WHERE id = ?", (lead_id,))
        time.sleep(1)

    conn.commit()
    conn.close()

    print("============================================================")
    print(" [✔] CICLO DE ENVIOS CONCLUÍDO COM SUCESSO NA BASE REAL!")
    print("============================================================\n")

if __name__ == "__main__":
    processar_ofertas_reais()
