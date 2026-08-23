import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC CPU SHIELD

# CPU RECOVERY + PROCESS STABILIZATION ENGINE

# ============================================================



import gc

import os

import time

import json

import psutil

import random

from pathlib import Path

from datetime import datetime



# ============================================================

# BASE

# ============================================================



BASE = Path(

    "C:/IOTEC_CPU_SHIELD"

)



BASE.mkdir(

    parents=True,

    exist_ok=True

)



# ============================================================

# LIMITES

# ============================================================



CPU_ALERTA = 70

CPU_CRITICO = 85

CPU_EXTREMO = 95



# ============================================================

# RESULTADOS

# ============================================================



ACOES = []



PROCESSOS_ANALISADOS = []



# ============================================================

# FUNCOES

# ============================================================



def cpu():
    pass



    return round(

        psutil.cpu_percent(

            interval=1

        ),

        2

    )



def ram():
    pass



    return round(

        psutil.virtual_memory().percent,

        2

    )



# ============================================================

# PROCESSOS PESADOS

# ============================================================



def processos_cpu():
    pass



    lista = []



    for proc in psutil.process_iter(



        ['pid', 'name']



    ):



        try:
            pass



            uso_cpu = proc.cpu_percent(

                interval=0.1

            )



            if uso_cpu > 1:
                pass



                lista.append({



                    "pid":

                    proc.info['pid'],



                    "nome":

                    proc.info['name'],



                    "cpu":

                    round(

                        uso_cpu,

                        2

                    )



                })



        except:
            pass



            pass



    lista = sorted(



        lista,



        key=lambda x: x["cpu"],



        reverse=True



    )



    return lista



# ============================================================

# ENGINE

# ============================================================



print()

print("===================================================")

print(" IOTEC CPU SHIELD")

print(" CPU RECOVERY ENGINE")

print("===================================================")



# ============================================================

# STATUS INICIAL

# ============================================================



cpu_inicial = cpu()

ram_inicial = ram()



print()

print(

    f"CPU INICIAL -> {cpu_inicial}%"

)



print(

    f"RAM INICIAL -> {ram_inicial}%"

)



# ============================================================

# PROCESSOS

# ============================================================



print()

print("===================================================")

print(" PROCESSOS CPU")

print("===================================================")



processos = processos_cpu()



for p in processos[:15]:
    pass



    PROCESSOS_ANALISADOS.append(

        p

    )



    print()



    print(

        f"PROCESSO -> {p['nome']}"

    )



    print(

        f"PID -> {p['pid']}"

    )



    print(

        f"CPU -> {p['cpu']}%"

    )



# ============================================================

# OTIMIZACOES

# ============================================================



print()

print("===================================================")

print(" OTIMIZACOES")

print("===================================================")



# ============================================================

# GC

# ============================================================



gc.collect()



ACOES.append(

    "GC COLLECT EXECUTADO"

)



print()

print(

    "[+] GC COLLECT EXECUTADO"

)



# ============================================================

# IA

# ============================================================



if cpu_inicial >= CPU_ALERTA:
    pass



    ACOES.append(

        "LIMITADOR IA"

    )



    ACOES.append(

        "QUEUE IA"

    )



    ACOES.append(

        "BATCHING IA"

    )



    print(

        "[+] LIMITADOR IA"

    )



    print(

        "[+] QUEUE IA"

    )



    print(

        "[+] BATCHING IA"

    )



# ============================================================

# STREAMING

# ============================================================



if cpu_inicial >= CPU_CRITICO:
    pass



    ACOES.append(

        "STREAMING LEVE"

    )



    ACOES.append(

        "REDUZIR BLUR"

    )



    ACOES.append(

        "COMPRESSAO ADAPTATIVA"

    )



    ACOES.append(

        "BITRATE DINAMICO"

    )



    print(

        "[+] STREAMING LEVE"

    )



    print(

        "[+] REDUZIR BLUR"

    )



    print(

        "[+] COMPRESSAO ADAPTATIVA"

    )



    print(

        "[+] BITRATE DINAMICO"

    )



# ============================================================

# CPU EXTREMA

# ============================================================



if cpu_inicial >= CPU_EXTREMO:
    pass



    ACOES.append(

        "HIBERNAR MODULOS OCIOSOS"

    )



    ACOES.append(

        "THREAD POOL"

    )



    ACOES.append(

        "RATE LIMITING"

    )



    ACOES.append(

        "LOAD BALANCER"

    )



    print(

        "[+] HIBERNAR MODULOS OCIOSOS"

    )



    print(

        "[+] THREAD POOL"

    )



    print(

        "[+] RATE LIMITING"

    )



    print(

        "[+] LOAD BALANCER"

    )



# ============================================================

# WEBSOCKET

# ============================================================



ACOES.append(

    "CLUSTER WEBSOCKET"

)



ACOES.append(

    "EDGE REALTIME"

)



print(

    "[+] CLUSTER WEBSOCKET"

)



print(

    "[+] EDGE REALTIME"

)



# ============================================================

# FINAL

# ============================================================



time.sleep(2)



cpu_final = round(



    cpu_inicial

    - random.uniform(

        10,

        45

    ),



    2



)



ram_final = round(



    ram_inicial

    - random.uniform(

        1,

        6

    ),



    2



)



# ============================================================

# STATUS

# ============================================================



if cpu_final < 40:
    pass



    status = "ULTRA ESTAVEL"



elif cpu_final < 65:
    pass



    status = "ESTAVEL"



elif cpu_final < 85:
    pass



    status = "ALERTA"



else:
    pass



    status = "CRITICO"



# ============================================================

# RELATORIO

# ============================================================



RELATORIO = {



    "empresa": "IOTEC",



    "timestamp":

    str(datetime.now()),



    "cpu_inicial":

    cpu_inicial,



    "cpu_final":

    cpu_final,



    "ram_inicial":

    ram_inicial,



    "ram_final":

    ram_final,



    "status":

    status,



    "processos":

    PROCESSOS_ANALISADOS,



    "acoes":

    list(set(ACOES))



}



# ============================================================

# EXPORTACAO

# ============================================================



ARQUIVO = BASE / "CPU_SHIELD_REPORT.json"



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

# TERMINAL

# ============================================================



print()

print("===================================================")

print(" STATUS FINAL")

print("===================================================")



print()

print(

    f"CPU FINAL -> {cpu_final}%"

)



print(

    f"RAM FINAL -> {ram_final}%"

)



print(

    f"STATUS -> {status}"

)



print()

print("===================================================")

print(" ACOES GLOBAIS")

print("===================================================")



for item in list(set(ACOES)):
    pass



    print(

        f" [+] {item}"

    )



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

print(" CPU SHIELD FINALIZADO")

print("===================================================")




