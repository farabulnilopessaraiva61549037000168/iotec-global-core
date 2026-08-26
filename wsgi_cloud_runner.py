import threading
import time
from wsgi_cloud import app  # Importa sua app Flask existente

def rodar_agente_arquiteto():
    try:
        import IOTEC_AGENTE_FABRICANTE_REAL
        IOTEC_AGENTE_FABRICANTE_REAL.pulsar_engine_fabricante()
    except Exception as e:
        print(f"[-] Erro na thread do Agente Arquiteto: {e}")

# Inicia a thread do Agente Arquiteto em segundo plano na nuvem
t = threading.Thread(target=rodar_agente_arquiteto, daemon=True)
t.start()

if __name__ == "__main__":
    app.run()
