# ==============================================================================
# IOTEC PROCESS WATCHER
# Monitor de Processos Reais
# ==============================================================================

import psutil
import json
import os
import time
from datetime import datetime

LOG_DIR = r"C:\IOTEC\LOGS"

os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "PROCESS_MONITOR.json")

FILTROS = [
    "IOTEC",
    "OMEGA",
    "python"
]


def registrar(evento):

    with open(LOG_FILE, "a", encoding="utf-8") as arq:

        arq.write(json.dumps(evento, ensure_ascii=False))

        arq.write("\n")


print("=" * 70)
print("IOTEC PROCESS WATCHER")
print("=" * 70)

vistos = set()

while True:

    for proc in psutil.process_iter(
        ['pid',
         'name',
         'exe',
         'username',
         'memory_info',
         'cpu_percent']):

        try:

            nome = str(proc.info['name'])

            if not any(f.lower() in nome.lower() for f in FILTROS):
                continue

            pid = proc.info['pid']

            if pid in vistos:
                continue

            vistos.add(pid)

            evento = {

                "timestamp": datetime.now().isoformat(),

                "tipo": "PROCESSO_INICIADO",

                "pid": pid,

                "nome": nome,

                "executavel": proc.info['exe'],

                "usuario": proc.info['username'],

                "memoria_mb":
                    round(proc.info['memory_info'].rss / 1024 / 1024, 2)

            }

            registrar(evento)

            print(evento)

        except Exception:
            pass

    time.sleep(2)

