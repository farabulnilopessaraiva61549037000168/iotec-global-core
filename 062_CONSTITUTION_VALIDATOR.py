# ==========================================================
# 062_CONSTITUTION_VALIDATOR.py
# IOTEC CONSTITUTION VALIDATOR
# ==========================================================

import json
import os

ROOT = r"C:\IOTEC"
ARQUIVO = "IOTEC_CONSTITUTION.json"

print("="*70)
print("IOTEC CONSTITUTION VALIDATOR")
print("="*70)
print()

if not os.path.exists(ARQUIVO):

    print("ERRO")
    print()
    print("ConstituiÃƒÂ§ÃƒÂ£o nÃƒÂ£o encontrada.")
    exit()

with open(ARQUIVO,"r",encoding="utf8") as f:

    CONST = json.load(f)

arquitetura = CONST["architecture"]

print("CONSTITUIÃƒâ€¡ÃƒÆ'O CARREGADA")
print()

total = 0
ok = 0

print("="*70)
print("VALIDAÃƒâ€¡ÃƒÆ'O")
print("="*70)
print()

for cargo,arquivo in arquitetura.items():

    total += 1

    encontrado = False
    caminho = ""

    for pasta,dirs,files in os.walk(ROOT):

        if arquivo in files:

            encontrado = True
            caminho = os.path.join(pasta,arquivo)
            break

    if encontrado:

        ok += 1

        print("[OK] ",cargo)
        print("Arquivo :",arquivo)
        print("Local   :",caminho)

    else:

        print("[ERRO]",cargo)
        print("Arquivo :",arquivo)
        print("Status  : NÃƒÆ'O ENCONTRADO")

    print("-"*60)

print()

print("="*70)
print("INDICADORES")
print("="*70)
print()

print("Itens Oficiais :",total)
print("Encontrados    :",ok)
print("Ausentes       :",total-ok)

print()

if ok == total:

    print("STATUS GERAL : APROVADO")

elif ok >= total*0.8:

    print("STATUS GERAL : PARCIAL")

else:

    print("STATUS GERAL : CRÃƒÂTICO")

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A ConstituiÃƒÂ§ÃƒÂ£o foi")
print("validada contra")
print("a arquitetura real.")


