import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC NODE CHECK

# =========================================================



import subprocess



print("")

print("=" * 50)

print(" VERIFICADOR NODE.JS ")

print("=" * 50)

print("")



# =========================================================

# NODE

# =========================================================



try:
    pass



    node = subprocess.check_output(



        "node -v",



        shell=True,



        text=True

    )



    print(f"NODE OK: {node}")



except:
    pass



    print("NODE NAO INSTALADO")

    print("")



# =========================================================

# NPM

# =========================================================



try:
    pass



    npm = subprocess.check_output(



        "npm -v",



        shell=True,



        text=True

    )



    print(f"NPM OK: {npm}")



except:
    pass



    print("NPM NAO INSTALADO")

    print("")



print("")

print("=" * 50)

print(" VERIFICACAO FINALIZADA ")

print("=" * 50)

print("")






