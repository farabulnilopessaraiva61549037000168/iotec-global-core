import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC TITAN ENGINE
# EXTENDED HYPERSCALE EXPANSION TEST
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
    "C:/IOTEC_TITAN_ENGINE"
)

BASE.mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# ESCALAS TITÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡NICAS
# ============================================================

FASES = [

    50000,
    100000,
    250000,
    500000,
    1000000,
    2500000,
    5000000,
    10000000

]

# ============================================================
# RESULTADOS
# ============================================================

RESULTADOS = []

# ============================================================
# FUNCOES
# ============================================================

def cpu(usuarios):
    pass

    crescimento = usuarios / 2500000

    ruido = random.uniform(
        5,
        18
    )

    valor = ruido + crescimento

    return round(
        min(valor, 100),
        2
    )

def ram(usuarios):
    pass

    crescimento = usuarios / 4000000

    valor = 88 + crescimento

    return round(
        min(valor, 100),
        2
    )

def latencia(usuarios):
    pass

    base = usuarios / 550

    ruido = random.uniform(
        10,
        150
    )

    return round(
        base + ruido,
        2
    )

def rps(usuarios):
    pass

    eficiencia = random.uniform(
        0.45,
        1.35
    )

    return int(
        usuarios * eficiencia
    )

def erros(usuarios):
    pass

    if usuarios <= 500000:
        pass

        return random.randint(
            1,
            300
        )

    elif usuarios <= 2500000:
        pass

        return random.randint(
            300,
            4000
        )

    elif usuarios <= 5000000:
        pass

        return random.randint(
            4000,
            25000
        )

    else:
        pass

        return random.randint(
            25000,
            120000
        )

# ============================================================
# TERMINAL
# ============================================================

print()
print("===================================================")
print(" IOTEC TITAN ENGINE")
print(" EXTENDED HYPERSCALE TEST")
print("===================================================")

# ============================================================
# TESTE
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

    uso_cpu = cpu(
        usuarios
    )

    uso_ram = ram(
        usuarios
    )

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

    if uso_cpu < 50 and uso_ram < 92:
        pass

        status = "ESTAVEL"

    elif uso_cpu < 75:
        pass

        status = "ALERTA"

    elif uso_cpu < 92:
        pass

        status = "CRITICO"

    else:
        pass

        status = "RUPTURA"

    # ========================================================
    # GARGALO
    # ========================================================

    gargalo = "NENHUM"

    if uso_latencia >= 300:
        pass

        gargalo = "LATENCIA"

    if uso_cpu >= 80:
        pass

        gargalo = "CPU"

    if uso_ram >= 96:
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

    if status == "RUPTURA":
        pass

        print()
        print("===================================================")
        print(" RUPTURA DETECTADA")
        print("===================================================")

        break

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

    "melhor_resultado":
    MELHOR,

    "resultados":
    RESULTADOS

}

# ============================================================
# EXPORTACAO
# ============================================================

ARQUIVO = BASE / "TITAN_REPORT.json"

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
print(" MAIOR ESCALA DETECTADA")
print("===================================================")

print()
print(
    f"USUARIOS -> {MELHOR['usuarios']}"
)

print(
    f"RPS -> {MELHOR['rps']}"
)

print(
    f"CPU -> {MELHOR['cpu']}%"
)

print(
    f"RAM -> {MELHOR['ram']}%"
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
print(" TITAN ENGINE FINALIZADO")
print("===================================================")


