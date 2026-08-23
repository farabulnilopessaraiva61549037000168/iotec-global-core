import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
if mercado_global.atividade_negativa():
    sistema.ativar("PROTO-RESILIENCIA-FINANCEIRA")



