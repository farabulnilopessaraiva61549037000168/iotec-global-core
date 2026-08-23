import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json

from pathlib import Path

from datetime import datetime



ROOT = Path(r"C:\IOTEC")



WAR_ROOM = ROOT / "IOTEC_WAR_ROOM_DATABASE.json"

REVENUE = ROOT / "IOTEC_REAL_REVENUE.json"



print("")

print("===================================")

print("IOTEC FUNNEL AUDITOR")

print("===================================")



print("")

print("DATA:")

print(datetime.now())



clientes = 0

oportunidades = 0

operacoes = 0

receita = 0



# ===================================

# WAR ROOM

# ===================================



try:
    pass



    with open(

        WAR_ROOM,

        "r",

        encoding="utf-8-sig"

    ) as f:



        db = json.load(f)



    clientes = len(

        db.get(

            "clientes",

            []

        )

    )



    oportunidades = len(

        db.get(

            "oportunidades",

            []

        )

    )



    operacoes = len(

        db.get(

            "operacoes",

            []

        )

    )



except Exception as erro:
    pass



    print("")

    print("ERRO WAR ROOM:")

    print(erro)



# ===================================

# RECEITA

# ===================================



try:
    pass



    with open(

        REVENUE,

        "r",

        encoding="utf-8-sig"

    ) as f:



        banco = json.load(f)



    eventos = banco.get(

        "eventos",

        []

    )



    receita = sum(

        x.get("valor", 0)

        for x in eventos

    )



except Exception as erro:
    pass



    print("")

    print("ERRO RECEITA:")

    print(erro)



# ===================================

# AUDITORIA

# ===================================



print("")

print("===================================")

print("FUNIL COMERCIAL")

print("===================================")



print("")

print("CLIENTES:")

print(clientes)



print("")

print("OPORTUNIDADES:")

print(oportunidades)



print("")

print("OPERACOES:")

print(operacoes)



print("")

print("RECEITA:")

print(f"R$ {receita:,.2f}")



print("")

print("===================================")

print("DIAGNOSTICO")

print("===================================")



if clientes == 0:
    pass



    print("")

    print("[ALTA]")

    print("SEM CLIENTES REGISTRADOS")



if oportunidades == 0:
    pass



    print("")

    print("[ALTA]")

    print("SEM OPORTUNIDADES")



if operacoes == 0:
    pass



    print("")

    print("[ALTA]")

    print("SEM OPERACOES")



if receita == 0:
    pass



    print("")

    print("[ALTA]")

    print("SEM RECEITA")



if clientes > 0:
    pass



    print("")

    print("[OK]")

    print("CLIENTES DETECTADOS")



if oportunidades > 0:
    pass



    print("")

    print("[OK]")

    print("OPORTUNIDADES DETECTADAS")



if operacoes > 0:
    pass



    print("")

    print("[OK]")

    print("OPERACOES DETECTADAS")



if receita > 0:
    pass



    print("")

    print("[OK]")

    print("RECEITA DETECTADA")



print("")

print("===================================")

print("MISSAO FASE 2")

print("===================================")



print("LOCALIZAR O CAMINHO:")

print("")

print("CLIENTE")

print("->")

print("FORMULARIO")

print("->")

print("PROPOSTA")

print("->")

print("FATURA")

print("->")

print("PAGAMENTO")

print("->")

print("RECEITA")



print("")

print("AUDITORIA FINALIZADA")






