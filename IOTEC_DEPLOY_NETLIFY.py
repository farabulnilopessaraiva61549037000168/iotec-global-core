import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import subprocess



# =========================================

# CONFIG

# =========================================



PASTA_SITE = r"C:\Users\Bruno Lopes\Desktop\regulus site"



# =========================================

# VERIFICA SE EXISTE

# =========================================



if not os.path.exists(PASTA_SITE):
    pass

    print("Pasta nÃƒÆ'Ã†â€™o encontrada!")

    exit()



print("Pasta encontrada:", PASTA_SITE)



# =========================================

# EXECUTA DEPLOY

# =========================================



os.chdir(PASTA_SITE)



print("Iniciando deploy...")



comando = [

    "netlify",

    "deploy",

    "--prod",

    "--dir",

    "."

]



subprocess.run(comando)



print("Deploy finalizado.")






