import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

def gerar_dossie(d):
    pasta = "C:\\IOTEC\\RELATORIOS"
    os.makedirs(pasta, exist_ok=True)

    with open(os.path.join(pasta, "relatorio.txt"), "w") as f:
        f.write("RelatÃƒÆ'Ã‚Â³rio gerado com sucesso.")



