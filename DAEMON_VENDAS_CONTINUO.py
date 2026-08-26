import time
import subprocess
import datetime

def rodar_loop_vendas():
    print("============================================================")
    print(" 🔄 IOTEC DAEMON CONTINUO — CAPTURA & OFERTA EM PRODUÇÃO    ")
    print("============================================================")
    
    while True:
        horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f"\n[{horario}] ⚙️ Executando ciclo de captura e ofertas...")
        
        try:
            # 1. Busca novos alvos reais
            subprocess.run(["python", "C:\\IOTEC\\CAPTADOR_INTERNACIONAL.py"], check=True)
            
            # 2. Processa os envios de ofertas Shield
            subprocess.run(["python", "C:\\IOTEC\\PROCESSAR_OFERTAS_REAIS.py"], check=True)
            
            print(" [✔] Ciclo finalizado. Próxima varredura em 15 minutos.")
        except Exception as e:
            print(f" [!] Erro no ciclo: {e}")
            
        time.sleep(900) # Loop a cada 15 minutos

if __name__ == "__main__":
    rodar_loop_vendas()
