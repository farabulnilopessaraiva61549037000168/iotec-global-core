import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
imposto = 0.25
def calcular_receita_liquida(receita_bruta):
    liquida = receita_bruta * (1 - imposto)
    return liquida



