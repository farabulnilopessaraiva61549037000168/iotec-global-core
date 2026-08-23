import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def dias_de_autonomia(estoque, consumo_diario):
    pass

    if consumo_diario <= 0:
        return 9999

    return round(estoque / consumo_diario, 1)




