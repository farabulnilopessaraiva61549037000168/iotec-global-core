import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
if EMPRESA_AURORA.saldo >= DIVIDA_EMPRESA_COR:
    ativar_fusao()




