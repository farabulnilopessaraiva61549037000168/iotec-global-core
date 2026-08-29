import sqlite3
import time
import threading
import datetime

DB_PATH = r'C:\IOTEC\iotec.db'

def configurar_wal():
    # Ativa o modo Write-Ahead Logging para permitir leitura e escrita concorrentes
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    cursor = conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL;")
    cursor.execute("PRAGMA busy_timeout = 30000;")
    conn.commit()
    conn.close()

def auditoria_integridade():
    print("===============================================================================")
    print(" 🛠️  [THREAD 1] AUDITORIA DE INTEGRIDADE & OTIMIZAÇÃO WAL (IOTEC.DB)")
    print("===============================================================================")
    
    inicio = time.time()
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    cursor = conn.cursor()
    
    cursor.execute("PRAGMA integrity_check;")
    status_integridade = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM leads;")
    total_leads = cursor.fetchone()[0]
    
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_mesa_status ON leads (mesa_designada, status);")
    conn.commit()
    conn.close()
    
    tempo_exec = round(time.time() - inicio, 3)
    
    print(f"  • Integridade do Banco : [{status_integridade.upper()}]")
    print(f"  • Total Registrado     : {total_leads:,} empresas".replace(",", "."))
    print(f"  • Tempo de Auditoria   : {tempo_exec}s")
    print("  • Modo de Concorrência : WAL (Write-Ahead Logging) Ativado")
    print("===============================================================================\n")

def motor_disparos_background():
    time.sleep(1.0)
    print("===============================================================================")
    print(" 🚀 [THREAD 2] MOTOR DE DISPAROS AUTÔNOMOS MULTI-THREAD ATIVADO")
    print("===============================================================================")
    
    ciclos = 0
    while True:
        try:
            conn = sqlite3.connect(DB_PATH, timeout=30.0)
            cursor = conn.cursor()
            ciclos += 1
            agora = datetime.datetime.now().strftime("%H:%M:%S")
            
            cursor.execute("""
                SELECT id, razao_social, mesa_designada 
                FROM leads 
                WHERE status LIKE '%PENDENTE%' 
                LIMIT 10
            """)
            lote = cursor.fetchall()
            
            if not lote:
                print(f" [{agora}] [CICLO {ciclos}] Todos os leads processados.")
                conn.close()
                time.sleep(5)
                continue
            
            ids_lote = [item[0] for item in lote]
            cursor.execute(f"""
                UPDATE leads 
                SET status = 'EM_PROCESSAMENTO_AUTONOMO' 
                WHERE id IN ({','.join(['?']*len(ids_lote))})
            """, ids_lote)
            
            conn.commit()
            conn.close()
            
            print(f" [{agora}] [CICLO {ciclos}] Processado lote de {len(lote)} empresas (Mesa Ref: {lote[0][2]}).")
            time.sleep(1.0)
            
        except sqlite3.OperationalError as e:
            print(f" [!] Aguardando liberação do banco: {e}")
            time.sleep(1.5)
        except Exception as e:
            print(f" [!] Erro no motor de background: {e}")
            time.sleep(2.0)

if __name__ == "__main__":
    configurar_wal()
    thread_audit = threading.Thread(target=auditoria_integridade)
    thread_engine = threading.Thread(target=motor_disparos_background)
    
    thread_audit.start()
    thread_engine.start()
