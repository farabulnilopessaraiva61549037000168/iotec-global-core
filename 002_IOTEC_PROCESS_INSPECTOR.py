# ==============================================================================
# IOTEC PROCESS INSPECTOR
# Descobre QUAL SCRIPT estÃ¡ rodando
# ==============================================================================

import psutil
import time
import json
import os
from datetime import datetime

LOG_DIR = r"C:\IOTEC\LOGS"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "PROCESS_INSPECTOR.json")

vistos = set()


def salvar(evento):

    with open(LOG_FILE, "a", encoding="utf-8") as arq:
        arq.write(json.dumps(evento, ensure_ascii=False))
        arq.write("\n")


print("=" * 80)
print("IOTEC PROCESS INSPECTOR")
print("=" * 80)

while True:

    for proc in psutil.process_iter():

        try:

            pid = proc.pid

            if pid in vistos:
                continue

            nome = proc.name()

            if "python" not in nome.lower():
                continue

            cmd = proc.cmdline()

            script = ""

            if len(cmd) >= 2:
                script = cmd[1]

            evento = {

                "timestamp": datetime.now().isoformat(),

                "pid": pid,

                "processo": nome,

                "script": script,

                "cpu": proc.cpu_percent(),

                "memoria_mb": round(proc.memory_info().rss / 1024 / 1024, 2),

                "status": proc.status(),

                "usuario": proc.username(),

                "diretorio": proc.cwd() if proc.cwd else ""

            }

            vistos.add(pid)

            salvar(evento)

            print("\n" + "=" * 80)

            for k, v in evento.items():

                print(f"{k:15}: {v}")

        except Exception:
            pass

    time.sleep(2)

