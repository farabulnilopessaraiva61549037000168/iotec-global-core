import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def validar_dossie(d):
    pass



    regras = [

        d["paginas"] >= 20,

        d["graficos"] >= 6,

        d["tabelas"] >= 8,

        d["excel"],

        d["pdf"],

        d["metodologia"],

        d["referencias"]

    ]



    return all(regras)





