import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 RELEASE MANAGER
# ============================================================

from datetime import datetime

RELEASES = [

    ("1.0","ARQUITETURA INICIAL"),

    ("2.0","RESILIENCIA"),

    ("3.0","GOVERNANCA"),

    ("4.0","CONHECIMENTO"),

    ("5.0","PLATAFORMA")

]

print("\n================================================")
print("X27 RELEASE MANAGER")
print("================================================")

print(f"DATA : {datetime.now()}")

for versao, descricao in RELEASES:
    pass

    print("\n------------------------------------------------")

    print("VERSAO :", versao)

    print("DESCRICAO :", descricao)

print("\n================================================")
print("ROADMAP REGISTRADO")
print("================================================")


