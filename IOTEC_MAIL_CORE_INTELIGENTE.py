import sqlite3
import time
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"
INTERVALO_ENTRE_EMAILS = 0.5  # Disparo ultra-rápido
PAUSA_SEM_LEADS = 10         # Pausa reduzida quando a base esvaziar

def rodar_motor_continuo():
    print("============================================================")
    print("   MOTOR IOTEC MAIL CORE - MODO TURBO (24/7) INICIADO       ")
    print("============================================================")
    
    total_enviados_sessao = 0

    while True:
        try:
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            
            cursor.execute("""
                SELECT id, razao_social, email 
                FROM central_vendas_leads 
                WHERE status_venda IN ('PRONTO_PARA_ABORDAGEM', 'MINERADO') 
                LIMIT 200
            """)
            leads = cursor.fetchall()

            if not leads:
                print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] Aguardando novos leads no iotec.db...")
                conn.close()
                time.sleep(PAUSA_SEM_LEADS)
                continue

            for lead in leads:
                lead_id, razao, email = lead
                email_destino = email if email else "comercial@empresa.com.br"
                horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
                print(f"[{horario}] DISPARANDO -> {razao} | Destino: {email_destino}")

                cursor.execute("UPDATE central_vendas_leads SET status_venda = 'EMAIL_ENVIADO' WHERE id = ?", (lead_id,))
                conn.commit()
                total_enviados_sessao += 1
                time.sleep(INTERVALO_ENTRE_EMAILS)

            conn.close()
            print(f"[*] Lote finalizado. Total acumulado nesta sessao: {total_enviados_sessao}")

        except Exception as e:
            print(f"[-] Erro na operacao contínua: {e}")
            time.sleep(5)

if __name__ == "__main__":
    rodar_motor_continuo()
