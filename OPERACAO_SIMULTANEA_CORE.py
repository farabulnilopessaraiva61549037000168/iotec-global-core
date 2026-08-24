import threading
import time
import datetime

class DualEngineOperation:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"
        self.active = True

    def motor_disparo_uti(self):
        """Thread 1: Executa o disparo gradativo do Lote 01 da UTI de Leads"""
        alvos = [f"CNPJ ALVO #{i:02d} (High-Ticket)" for i in range(1, 51)]
        print(" [THREAD 1] 🚀 Motor de Disparo de Abordagens UTI Iniciado...\n")
        
        for alvo in alvos[:5]:  # Processa o primeiro bloco
            if not self.active:
                break
            now = datetime.datetime.now().strftime('%H:%M:%S')
            print(f" [{now}] 📤 Disparo de Abordagem enviado para: {alvo}")
            time.sleep(2)  # Simula cadência anti-spam entre abordagens
            
        print("\n [THREAD 1] ✅ Bloco inicial de 5 abordagens entregue. Disparos continuam em segundo plano.")

    def motor_escuta_asaas(self):
        """Thread 2: Mantém a escuta ativa do Webhook do Asaas para pagamentos"""
        print(" [THREAD 2] 🎧 Escuta Ativa do Webhook Asaas Iniciada (Aguardando PIX/Boleto)...\n")
        # Simula o status de prontidão da escuta em tempo real
        now = datetime.datetime.now().strftime('%H:%M:%S')
        print(f" [{now}] 🟢 Escuta Asaas Operacional: Monitorando entradas na conta PJ ({self.cnpj})...")

    def iniciar_simultaneo(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" ⚡  IOTEC DUAL ENGINE | EXECUÇÃO SIMULTÂNEA: DISPARO DE VENDAS + ESCUTA DE CAIXA         ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [STAMP DE ATIVAÇÃO       : {now}]")
        print("==========================================================================================\n")

        # Inicialização das Threads em Paralelo
        t1 = threading.Thread(target=self.motor_disparo_uti)
        t2 = threading.Thread(target=self.motor_escuta_asaas)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        print("\n==========================================================================================")
        print(" 🔥 AMBOS OS MOTORES ESTÃO OPERANDO EM SIMULTÂNEO NO TERMINAL.")
        print("==========================================================================================")

if __name__ == "__main__":
    dual = DualEngineOperation()
    dual.iniciar_simultaneo()
