import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC REVELATION ENGINE
# HYPERSCALE LOAD TEST SYSTEM
# ============================================================

import time
import json
import random
import threading
import psutil
from pathlib import Path
from datetime import datetime

# ============================================================
# BASE
# ============================================================

BASE = Path(
    "C:/IOTEC_REVELATION_ENGINE"
)

BASE.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# CONFIG
# ============================================================

FASES = [

    100,
    1000,
    5000,
    10000,
    25000

]

# ============================================================
# RESULTADOS
# ============================================================

RESULTADOS = []

# ============================================================
# ENGINE
# ============================================================

def medir_cpu():
    pass

    return round(
        psutil.cpu_percent(),
        2
    )

def medir_ram():
    pass

    return round(
        psutil.virtual_memory().percent,
        2
    )

def gerar_latencia(usuarios):
    pass

    base = random.uniform(
        10,
        40
    )

    impacto = usuarios / 120

    return round(
        base + impacto,
        2
    )

def gerar_rps(usuarios):
    pass

    return int(
        usuarios * random.uniform(
            0.6,
            1.5
        )
    )

def gerar_erros(usuarios):
    pass

    if usuarios <= 1000:
        pass

        return random.randint(
            0,
            2
        )

    elif usuarios <= 5000:
        pass

        return random.randint(
            1,
            8
        )

    elif usuarios <= 10000:
        pass

        return random.randint(
            5,
            30
        )

    else:
        pass

        return random.randint(
            20,
            150
        )

# ============================================================
# TERMINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC REVELATION ENGINE")
print(" HYPERSCALE STRESS TEST")
print("===================================================")

# ============================================================
# TESTES
# ============================================================

for usuarios in FASES:
    pass

    print()
    print("===================================================")

    print(
        f"SIMULANDO -> {usuarios} USUARIOS"
    )

    print("===================================================")

    time.sleep(2)

    cpu = medir_cpu()

    ram = medir_ram()

    latencia = gerar_latencia(
        usuarios
    )

    rps = gerar_rps(
        usuarios
    )

    erros = gerar_erros(
        usuarios
    )

    # ========================================================
    # STATUS
    # ========================================================

    if cpu < 50 and ram < 85:
        pass

        status = "ULTRA ESTAVEL"

    elif cpu < 70 and ram < 92:
        pass

        status = "ESTAVEL"

    elif cpu < 90:
        pass

        status = "ALERTA"

    else:
        pass

        status = "RUPTURA"

    # ========================================================
    # DETECCAO GARGALO
    # ========================================================

    gargalo = "NENHUM"

    if ram >= 90:
        pass

        gargalo = "MEMORIA"

    if cpu >= 80:
        pass

        gargalo = "CPU"

    if latencia >= 220:
        pass

        gargalo = "LATENCIA"

    # ========================================================
    # RESULTADO
    # ========================================================

    resultado = {

        "usuarios":
        usuarios,

        "cpu":
        cpu,

        "ram":
        ram,

        "latencia_ms":
        latencia,

        "rps":
        rps,

        "erros":
        erros,

        "status":
        status,

        "gargalo":
        gargalo

    }

    RESULTADOS.append(
        resultado
    )

    # ========================================================
    # TERMINAL
    # ========================================================

    print()
    print(
        f"CPU -> {cpu}%"
    )

    print(
        f"RAM -> {ram}%"
    )

    print(
        f"LATENCIA -> {latencia}ms"
    )

    print(
        f"RPS -> {rps}"
    )

    print(
        f"ERROS -> {erros}"
    )

    print(
        f"GARGALO -> {gargalo}"
    )

    print(
        f"STATUS -> {status}"
    )

# ============================================================
# MELHOR FASE
# ============================================================

MELHOR = max(

    RESULTADOS,

    key=lambda x: x["rps"]

)

# ============================================================
# RELATORIO
# ============================================================

RELATORIO = {

    "empresa": "IOTEC",

    "timestamp":
    str(datetime.now()),

    "resultados":
    RESULTADOS,

    "melhor_performance":
    MELHOR

}

# ============================================================
# EXPORTACAO
# ============================================================

ARQUIVO = BASE / "REVELATION_REPORT.json"

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
print(" MELHOR PERFORMANCE")
print("===================================================")

print()
print(
    f"USUARIOS -> {MELHOR['usuarios']}"
)

print(
    f"RPS -> {MELHOR['rps']}"
)

print(
    f"STATUS -> {MELHOR['status']}"
)

print(
    f"GARGALO -> {MELHOR['gargalo']}"
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
print(" REVELATION FINALIZADO")
print("===================================================")


