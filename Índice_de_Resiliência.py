import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def calcular_resilience_index(indicadores):
    pass

    if not indicadores:
        return 0

    total = sum(indicadores.values())

    return round(total / len(indicadores), 2)





