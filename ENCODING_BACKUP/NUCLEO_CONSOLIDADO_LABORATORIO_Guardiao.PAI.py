import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# watcher_stalking.py

import time
from guardiao_pai import GuardiaoPAI

def iniciar_vigilancia():
    jaguar = GuardiaoPAI(tempo_espera_horas=24)  # Define o tempo crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico de ausÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
    print("[STALKING] VigilÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia iniciada. Aguardando sinais do idealizador.")

    while True:
        jaguar.monitorar_ausencia()
        time.sleep(3600)  # Verifica a cada hora (ajustÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel para minutos em teste)

# Para teste imediato, troque para time.sleep(10)



