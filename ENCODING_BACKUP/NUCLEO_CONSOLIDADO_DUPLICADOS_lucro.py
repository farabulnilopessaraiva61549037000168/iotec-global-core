import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
lucro_liquido = 12000.00
repasse_pessoal = lucro_liquido * 0.4  # R$ 4800,00
reinvestimento = lucro_liquido * 0.5   # R$ 6000,00
tributos = lucro_liquido * 0.1         # R$ 1200,00



