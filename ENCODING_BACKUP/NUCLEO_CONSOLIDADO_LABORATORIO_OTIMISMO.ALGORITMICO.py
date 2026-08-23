import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
if sistema.tempo_ocioso():
    sistema.ativar("PROTO-OTIMISMO-ALGORITMICO")



