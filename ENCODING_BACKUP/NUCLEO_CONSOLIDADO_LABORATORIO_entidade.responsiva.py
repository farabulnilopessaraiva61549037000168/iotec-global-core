import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
entidade = invocar_entidade_responsiva(ambiente)
resultado = entidade.executar_missao()



