import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def validar_servico(servico):
    permitidos = ["auditoria", "dados", "automacao"]
    return servico in permitidos



