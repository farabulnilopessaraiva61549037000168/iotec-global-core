import threading
import time
import os
from app import app  # Ou o arquivo principal do seu servidor Web

def rodar_engine_continuo():
    time.sleep(5)
    print("🚀 [NUVEM 24/7] Iniciando motor continuo IOTEC no servidor web...")
    try:
        os.system("python CONTINUOUS_OPERATION.py")
    except Exception as e:
        print(f"Erro no motor continuo: {e}")

# Sobe a thread contínua junta com o servidor
threading.Thread(target=rodar_engine_continuo, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
