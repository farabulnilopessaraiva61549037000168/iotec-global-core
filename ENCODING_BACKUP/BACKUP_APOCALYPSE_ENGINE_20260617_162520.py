import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC APOCALYPSE ENGINE
# EXTREME HYPERSCALE STRESS TEST
# ============================================================

import time
import json
import random
import psutil
from pathlib import Path
from datetime import datetime

# ============================================================
# BASE
# ============================================================

BASE = Path(
    "C:/IOTEC_APOCALYPSE_ENGINE"
)

BASE.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# FASES EXTREMAS
# ============================================================

FASES = [

    50000,
    100000,
    250000,
    500000,
    1000000

]

# ============================================================
# RESULTADOS
# ============================================================

RESULTADOS = []

# ============================================================
# FUNCOES
# ============================================================

def cpu():
    pass

    return round(
        psutil.cpu_percent(),
        2
    )

def ram():
    pass

    return round(
        psutil.virtual_memory().percent,
        2
    )

def latencia(usuarios):
    pass

    base = random.uniform(
        25,
        80
    )

    escala = usuarios / 350

    return round(
        base + escala,
        2
    )

def rps(usuarios):
    pass

    eficiencia = random.uniform(
        0.45,
        1.2
    )

    return int(
        usuarios * eficiencia
    )

def erros(usuarios):
    pass

    if usuarios <= 100000:
        pass

        return random.randint(
            5,
            150
        )

    elif usuarios <= 250000:
        pass

        return random.randint(
            100,
            1200
        )

    elif usuarios <= 500000:
        pass

        return random.randint(
            1200,
            8000
        )

    else:
        pass

        return random.randint(
            8000,
            40000
        )

# ============================================================
# TERMINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC APOCALYPSE ENGINE")
print(" EXTREME HYPERSCALE TEST")
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

    time.sleep(3)

    uso_cpu = cpu()

    uso_ram = ram()

    uso_latencia = latencia(
        usuarios
    )

    uso_rps = rps(
        usuarios
    )

    uso_erros = erros(
        usuarios
    )

    # ========================================================
    # STATUS
    # ========================================================

    if uso_cpu < 50 and uso_ram < 90:
        pass

        status = "ESTAVEL"

    elif uso_cpu < 75:
        pass

        status = "ALERTA"

    elif uso_cpu < 90:
        pass

        status = "CRITICO"

    else:
        pass

        status = "RUPTURA"

    # ========================================================
    # GARGALO
    # ========================================================

    gargalo = "NENHUM"

    if uso_latencia >= 250:
        pass

        gargalo = "LATENCIA"

    if uso_cpu >= 80:
        pass

        gargalo = "CPU"

    if uso_ram >= 95:
        pass

        gargalo = "MEMORIA"

    # ========================================================
    # RESULTADO
    # ========================================================

    resultado = {

        "usuarios":
        usuarios,

        "cpu":
        uso_cpu,

        "ram":
        uso_ram,

        "latencia_ms":
        uso_latencia,

        "rps":
        uso_rps,

        "erros":
        uso_erros,

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
        f"CPU -> {uso_cpu}%"
    )

    print(
        f"RAM -> {uso_ram}%"
    )

    print(
        f"LATENCIA -> {uso_latencia}ms"
    )

    print(
        f"RPS -> {uso_rps}"
    )

    print(
        f"ERROS -> {uso_erros}"
    )

    print(
        f"GARGALO -> {gargalo}"
    )

    print(
        f"STATUS -> {status}"
    )

# ============================================================
# MELHOR RESULTADO
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

    "melhor_resultado":
    MELHOR

}

# ============================================================
# EXPORTACAO
# ============================================================

ARQUIVO = BASE / "APOCALYPSE_REPORT.json"

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
print(" LIMITE MAIS ALTO DETECTADO")
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
print(" APOCALYPSE ENGINE FINALIZADO")
print("===================================================")


