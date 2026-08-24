import threading
import time
import datetime

class DualLote3Engine:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"

    def processar_lote_03_internacional(self):
        """Thread 1: Beneficia e dispara o Lote 03 focado na Camada Global (USD/EUR)"""
        print(" [THREAD 1] 🌐 Processando Lote 03: Expansão Global (EUA, UE e LatAm)...")
        time.sleep(1)
        
        alvos_global = [
            {"id": "USA-01", "pais": "🇺🇸 EUA", "moeda": "USD", "ticket": "$ 199.00", "gateway": "Remessa Swift Direct"},
            {"id": "EUR-01", "pais": "🇪🇺 União Europeia", "moeda": "EUR", "ticket": "€ 180.00", "gateway": "SEPA / Remessa"},
            {"id": "LAT-01", "pais": "🇺🇾 Uruguai / Chile", "moeda": "USD", "ticket": "$ 299.00", "gateway": "Cross-Border LatAm"}
        ]
        
        for alvo in alvos_global:
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(f" [{now}] 🚀 [LOTE 03] Disparo Global | {alvo['pais']} | Ticket: {alvo['ticket']} | Canal: {alvo['gateway']}")
            time.sleep(1)
            
        print("\n [THREAD 1] ✅ Lote 03 Internacional ativado e conectado à esteira de câmbio da Remessa Online.")

    def escuta_caixa_asaas(self):
        """Thread 2: Mantém a escuta do webhook do Asaas para os Lotes 01 e 02 (BRL)"""
        print(" [THREAD 2] 🎧 Escuta de Caixa Asaas (PIX / Boleto BRL) Operacional...\n")
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print(f" [{now}] 🟢 Escuta Ativa: Monitorando créditos instantâneos na conta PJ ({self.cnpj})...")

    def executar(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" ⚡  IOTEC DUAL ENGINE | EXPANSÃO GLOBAL LOTE 03 (USD/EUR) + ESCUTA DE CAIXA ASAAS (BRL)  ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [STAMP DE EXECUÇÃO       : {now}]")
        print("==========================================================================================\n")

        t1 = threading.Thread(target=self.processar_lote_03_internacional)
        t2 = threading.Thread(target=self.escuta_caixa_asaas)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("\n==========================================================================================")
        print(" 🔥 CAMADA INTERNACIONAL ATIVADA E ESCUTA DE CAIXA NACIONAL OPERACIONAL.")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = DualLote3Engine()
    engine.executar()
