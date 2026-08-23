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



COMPONENTES = {



    "WAR_ROOM":

        ROOT / "IOTEC_WAR_ROOM_DATABASE.json",



    "REVENUE":

        ROOT / "IOTEC_REAL_REVENUE.json",



    "COCKPIT":

        ROOT / "IOTEC_EXECUTIVE_COCKPIT.json",



    "GOAL":

        ROOT / "IOTEC_GOAL_DEVIATION_REPORT.json",



    "PAYMENT_BRIDGE":

        ROOT / "IOTEC_PAYMENT_BRIDGE_ENGINE.py",



    "PAYPAL":

        ROOT / "paypal_server.py",



    "CORE":

        ROOT / "IOTEC_CORE_LOGIC.py"

}



REPORTAGENS = []



def reportar(

    prioridade,

    titulo,

    descricao

):



    REPORTAGENS.append({



        "data":

            str(datetime.now()),



        "prioridade":

            prioridade,



        "titulo":

            titulo,



        "descricao":

            descricao

    })



print("")

print("===================================")

print("IOTEC SENTINEL ENGINE")

print("===================================")



print("")

print("VERIFICANDO COMPONENTES...")

print("")



ativos = 0



for nome, arquivo in COMPONENTES.items():
    pass



    if arquivo.exists():
        pass



        ativos += 1



        print(

            nome,

            "-> ONLINE"

        )



        reportar(

            "BAIXA",

            f"{nome} ONLINE",

            "Componente operacional."

        )



    else:
        pass



        print(

            nome,

            "-> OFFLINE"

        )



        reportar(

            "CRITICA",

            f"{nome} OFFLINE",

            "Componente nao encontrado."

        )



print("")

print("ANALISANDO RECEITA...")

print("")



try:
    pass



    with open(

        ROOT / "IOTEC_REAL_REVENUE.json",

        "r",

        encoding="utf-8-sig"

    ) as f:



        receita = json.load(f)



    total = sum(



        x["valor"]



        for x in receita["eventos"]

    )



    reportar(

        "ALTA",

        "RECEITA DETECTADA",

        f"Receita acumulada: R$ {total:,.2f}"

    )



except:
    pass



    reportar(

        "MEDIA",

        "SEM RECEITA",

        "Nao foi possivel calcular receita."

    )



print("")

print("ANALISANDO OPORTUNIDADES...")

print("")



try:
    pass



    with open(

        ROOT / "IOTEC_WAR_ROOM_DATABASE.json",

        "r",

        encoding="utf-8-sig"

    ) as f:



        banco = json.load(f)



    oportunidades = len(

        banco["oportunidades"]

    )



    operacoes = len(

        banco["operacoes"]

    )



    reportar(

        "MEDIA",

        "STATUS COMERCIAL",

        f"{oportunidades} oportunidades e {operacoes} operacoes."

    )



except Exception as erro:
    pass



    reportar(

        "ALTA",

        "WAR ROOM INACESSIVEL",

        str(erro)

    )



print("")

print("===================================")

print("CENTRAL DE REPORTAGEM")

print("===================================")



ordem = {



    "CRITICA": 1,

    "ALTA": 2,

    "MEDIA": 3,

    "BAIXA": 4

}



REPORTAGENS.sort(



    key=lambda x:

        ordem.get(

            x["prioridade"],

            99

        )

)



for r in REPORTAGENS:
    pass



    print("")

    print(

        "[",

        r["prioridade"],

        "]",

        r["titulo"]

    )



    print(

        r["descricao"]

    )



print("")

print("===================================")

print("SINAL DE VIDA")

print("===================================")



print(

    "DATA:",

    datetime.now()

)



print(

    "COMPONENTES:",

    ativos,

    "/",

    len(COMPONENTES)

)



print("")

print(

    "NUCLEO OPERACIONAL"

)




