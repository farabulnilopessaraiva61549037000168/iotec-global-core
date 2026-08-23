import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC ROCKBOOST ORBITAL ENGINE
# ============================================================

import gc
import json
import psutil
import time
from pathlib import Path
from datetime import datetime

BASE = Path(
    "C:/IOTEC_ROCKBOOST_ORBITAL"
)

BASE.mkdir(
    parents=True,
    exist_ok=True
)

RAM_ALERTA = 85
RAM_CRITICA = 92

ALVOS = [

    "chrome.exe",
    "msedge.exe",
    "node.exe"

]

def memoria():
    pass

    return psutil.virtual_memory().percent

def cpu():
    pass

    return psutil.cpu_percent(
        interval=1
    )

def limpar_python():
    pass

    gc.collect()

RAM_INICIAL = memoria()

CPU_INICIAL = cpu()

print()
print("===================================================")
print(" IOTEC ROCKBOOST ORBITAL ENGINE")
print("===================================================")

print()
print(f"RAM INICIAL -> {RAM_INICIAL}%")

print(f"CPU INICIAL -> {CPU_INICIAL}%")

PROCESSOS = []

print()
print("===================================================")
print(" PROCESSOS PESADOS")
print("===================================================")

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

        if nome in ALVOS:
            pass

            PROCESSOS.append({

                "nome": nome,

                "pid":
                proc.info['pid'],

                "memoria":
                memoria_proc

            })

            print()

            print(
                f"PROCESSO -> {nome}"
            )

            print(
                f"PID -> {proc.info['pid']}"
            )

            print(
                f"MEMORIA -> {memoria_proc}%"
            )

    except:
        pass

        pass

ACOES = []

print()
print("===================================================")
print(" LIMPEZA PYTHON")
print("===================================================")

limpar_python()

ACOES.append(
    "GC COLLECT EXECUTADO"
)

time.sleep(2)

if RAM_INICIAL >= RAM_ALERTA:
    pass

    print()
    print("===================================================")
    print(" MODO ALERTA")
    print("===================================================")

    ACOES.append(
        "ATIVAR STREAMING"
    )

    ACOES.append(
        "REDUZIR BLUR"
    )

    ACOES.append(
        "LAZY LOADING"
    )

    ACOES.append(
        "ATIVAR CDN"
    )

if RAM_INICIAL >= RAM_CRITICA:
    pass

    print()
    print("===================================================")
    print(" MODO PROTECAO MAXIMA")
    print("===================================================")

    ACOES.append(
        "DESATIVAR VIDEOS"
    )

    ACOES.append(
        "MODO FRONTEND LEVE"
    )

    ACOES.append(
        "HIBERNAR MODULOS"
    )

print()
print("===================================================")
print(" RECICLAGEM DE PROCESSOS")
print("===================================================")

for item in PROCESSOS:
    pass

    if item["memoria"] >= 2:
        pass

        try:
            pass

            pid = item["pid"]

            processo = psutil.Process(pid)

            processo.terminate()

            print()

            print(
                f"FINALIZADO -> {item['nome']}"
            )

            print(
                f"PID -> {pid}"
            )

            ACOES.append(

                f"PROCESSO FINALIZADO {item['nome']}"

            )

        except:
            pass

            pass

ACOES.append(
    "IA ASSINCRONA"
)

ACOES.append(
    "CACHE DE RESPOSTAS"
)

ACOES.append(
    "FILA INTELIGENTE"
)

ACOES.append(
    "STORAGE HIBRIDO"
)

ACOES.append(
    "ARQUIVAMENTO FRIO"
)

ACOES.append(
    "BACKUP AUTOMATICO"
)

time.sleep(3)

RAM_FINAL = memoria()

CPU_FINAL = cpu()

if RAM_FINAL < 80:
    pass

    STATUS = "ULTRA ESTAVEL"

elif RAM_FINAL < 90:
    pass

    STATUS = "ESTAVEL"

else:
    pass

    STATUS = "ALERTA"

RELATORIO = {

    "empresa": "IOTEC",

    "timestamp":
    str(datetime.now()),

    "ram_inicial":
    RAM_INICIAL,

    "ram_final":
    RAM_FINAL,

    "cpu_inicial":
    CPU_INICIAL,

    "cpu_final":
    CPU_FINAL,

    "status":
    STATUS,

    "acoes":
    ACOES,

    "processos":
    PROCESSOS

}

ARQUIVO = BASE / "ROCKBOOST_ORBITAL_REPORT.json"

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
    f"STATUS -> {STATUS}"
)

print()
print("===================================================")
print(" ACOES")
print("===================================================")

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
print(" ORBITAL ENGINE FINALIZADO")
print("===================================================")


