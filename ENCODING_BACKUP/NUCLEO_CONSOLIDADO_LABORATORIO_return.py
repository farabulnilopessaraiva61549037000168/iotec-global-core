import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def criar_aldeia(nome, especialidade):
    return {
        "nome": nome,
        "especialidade": especialidade,
        "chakra": 100,
        "status": "ativa",
        "invocavel": True
    }



