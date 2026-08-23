import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os



def gerar_dossie(d):
    pass

    pasta = "C:\\IOTEC\\RELATORIOS"

    os.makedirs(pasta, exist_ok=True)



    with open(os.path.join(pasta, "relatorio.txt"), "w") as f:
        pass

        f.write("RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio gerado com sucesso.")





