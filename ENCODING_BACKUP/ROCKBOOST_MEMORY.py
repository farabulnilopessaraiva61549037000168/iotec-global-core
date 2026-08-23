import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ROCKBOOST MEMORY ENGINE
# AUTO RAM CLEANER + SMART GOVERNANCE
# ============================================================

import os
import gc
import json
import time
import psutil
import platform
from pathlib import Path
from datetime import datetime

# ============================================================
# BASE
# ============================================================

BASE = Path("C:/IOTEC_ROCKBOOST_MEMORY")

BASE.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# CONFIG
# ============================================================

RAM_ALERTA = 85
RAM_CRITICA = 92

CPU_ALERTA = 85

# ============================================================
# PROCESSOS PESADOS
# ============================================================

PROCESSOS_PESADOS = [

    "python.exe",
    "node.exe",
    "chrome.exe",
    "msedge.exe"

]

# ============================================================
# GOVERNANÃƒÆ'Ã†â€™A
# ============================================================

def memoria():
    pass

    return psutil.virtual_memory().percent

def cpu():
    pass

    return psutil.cpu_percent(
        interval=1
    )

# ============================================================
# LIMPEZA
# ============================================================

def limpar_memoria():
    pass

    gc.collect()

# ============================================================
# ANALISE PROCESSOS
# ============================================================

PROCESSOS = []

for proc in psutil.process_iter(

    [

        'pid',
        'name',
        'memory_percent'

    ]

):

    try:
        pass

        nome = proc.info['name']

        memoria_proc = round(

            proc.info[
                'memory_percent'
            ],

            2

        )

        if nome in PROCESSOS_PESADOS:
            pass

            PROCESSOS.append({

                "nome": nome,

                "pid":
                proc.info['pid'],

                "memoria":
                memoria_proc

            })

    except:
        pass

        pass

# ============================================================
# STATUS INICIAL
# ============================================================

RAM_INICIAL = memoria()

CPU_INICIAL = cpu()

# ============================================================
# TERMINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC ROCKBOOST MEMORY ENGINE")
print("===================================================")

print()
print(
    f"RAM INICIAL -> {RAM_INICIAL}%"
)

print(
    f"CPU INICIAL -> {CPU_INICIAL}%"
)

print()
print("===================================================")
print(" PROCESSOS DETECTADOS")
print("===================================================")

for proc in PROCESSOS:
    pass

    print()

    print(
        f"PROCESSO -> {proc['nome']}"
    )

    print(
        f"PID -> {proc['pid']}"
    )

    print(
        f"MEMORIA -> {proc['memoria']}%"
    )

# ============================================================
# LIMPEZA AUTOMATICA
# ============================================================

ACOES = []

if RAM_INICIAL >= RAM_ALERTA:
    pass

    print()
    print("===================================================")
    print(" LIMPEZA AUTOMATICA")
    print("===================================================")

    limpar_memoria()

    ACOES.append(
        "GC COLLECT EXECUTADO"
    )

    time.sleep(2)

# ============================================================
# STATUS FINAL
# ============================================================

RAM_FINAL = memoria()

CPU_FINAL = cpu()

# ============================================================
# GOVERNANÃƒÆ'Ã†â€™A INTELIGENTE
# ============================================================

MODO = "NORMAL"

if RAM_FINAL >= RAM_CRITICA:
    pass

    MODO = "PROTECAO MAXIMA"

    ACOES.append(
        "REDUZIR EFEITOS VISUAIS"
    )

    ACOES.append(
        "DESATIVAR VIDEOS"
    )

    ACOES.append(
        "MODO FRONTEND LEVE"
    )

elif RAM_FINAL >= RAM_ALERTA:
    pass

    MODO = "ALERTA"

    ACOES.append(
        "OTIMIZAR FRONTEND"
    )

    ACOES.append(
        "ATIVAR CACHE"
    )

    ACOES.append(
        "ATIVAR STREAMING"
    )

else:
    pass

    ACOES.append(
        "NUCLEO ESTAVEL"
    )

# ============================================================
# RELATORIO
# ============================================================

RELATORIO = {

    "empresa": "IOTEC",

    "timestamp":
    str(datetime.now()),

    "sistema":
    platform.system(),

    "ram_inicial":
    RAM_INICIAL,

    "ram_final":
    RAM_FINAL,

    "cpu_inicial":
    CPU_INICIAL,

    "cpu_final":
    CPU_FINAL,

    "modo":
    MODO,

    "acoes":
    ACOES,

    "processos":
    PROCESSOS

}

# ============================================================
# EXPORTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

ARQUIVO = BASE / "ROCKBOOST_MEMORY_REPORT.json"

with open(
    ARQUIVO,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        RELATORIO,
        f,
        indent=4,
        ensure_ascii=False
    )

# ============================================================
# FINAL
# ============================================================

print()
print("===================================================")
print(" STATUS FINAL")
print("===================================================")

print()
print(
    f"RAM FINAL -> {RAM_FINAL}%"
)

print(
    f"CPU FINAL -> {CPU_FINAL}%"
)

print()
print(
    f"MODO -> {MODO}"
)

print()
print("ACOES:")

for acao in ACOES:
    pass

    print(f" [+] {acao}")

print()
print("===================================================")
print(" EXPORTACAO")
print("===================================================")

print()
print(
    f"ARQUIVO -> {ARQUIVO}"
)

print()
print("===================================================")
print(" GOVERNANCA FINALIZADA")
print("===================================================")


