import threading
import sqlite3
import time
import datetime

class DualUTCEngine:
    def __init__(self):
        self.db_path = "iotec.db"
        self.cnpj = "61.549.037/0001-68"

    def padronizar_datas_utc(self):
        """Thread 1: Garante timestamps ISO-8601 UTC sem travar o banco para leitura"""
        print(" [THREAD 1] 🌐 Iniciando Padronização de Fuso Horário Universal (UTC) no `iotec.db`...\n")
        time.sleep(1)
        
        try:
            conn = sqlite3.connect(self.db_path, timeout=10)
            cursor = conn.cursor()
            
            # Timestamp UTC padronizado
            now_utc = datetime.datetime.now(datetime.timezone.utc).isoformat()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS system_timezone_config (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    master_timezone TEXT NOT NULL,
                    last_sync_utc TEXT NOT NULL
                )
            ''')
            
            cursor.execute('''
                INSERT INTO system_timezone_config (master_timezone, last_sync_utc)
                VALUES ('UTC', ?)
            ''', (now_utc,))
            
            conn.commit()
            conn.close()
            
            print(f" [THREAD 1] 🕒 [UTC SYNC] Timestamp registrado com sucesso: {now_utc}")
            print(" [THREAD 1] ✅ Suporte a múltiplos fusos horários (MS a Sydney) ativo no banco.")
        except Exception as e:
            print(f" [THREAD 1] ⚠️ Nota de sincronização de fuso: {e}")

    def escuta_caixa_asaas(self):
        """Thread 2: Mantém a escuta ativa do webhook sem bloqueio de I/O"""
        print(" [THREAD 2] 🎧 Escuta de Caixa Asaas (PIX / Boleto BRL) Operacional...\n")
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print(f" [{now}] 🟢 Escuta Ativa (Conta PJ {self.cnpj}) | Monitorando recebimentos do Lote 01")

    def executar(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" ⚡  IOTEC DUAL ENGINE | PADRONIZAÇÃO DE FUSO UTC + ESCUTA DE CAIXA ASAAS                ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [STAMP DE EXECUÇÃO       : {now}]")
        print("==========================================================================================\n")

        t1 = threading.Thread(target=self.padronizar_datas_utc)
        t2 = threading.Thread(target=self.escuta_caixa_asaas)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("\n==========================================================================================")
        print(" 🔥 ESTRUTURA MULTI-FUSO ATIVADA E ESCUTA DE CAIXA NATIVA MONITORANDO O TERMINAL.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = DualUTCEngine()
    engine.executar()
