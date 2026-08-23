import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_PAYMENT_BRIDGE_ENGINE.py



import json

from pathlib import Path

from datetime import datetime



ROOT = Path(r"C:\IOTEC")



ARQ_PAGAMENTOS = (

    ROOT /

    "NUCLEO_CONSOLIDADO" /

    "FINANCEIRO" /

    "pagamentos.json"

)



ARQ_RECEITA = (

    ROOT /

    "IOTEC_REAL_REVENUE.json"

)



print("\nIOTEC PAYMENT BRIDGE ENGINE\n")



if not ARQ_PAGAMENTOS.exists():
    pass



    print(

        "PAGAMENTOS.JSON NAO ENCONTRADO"

    )



    raise SystemExit



with open(

    ARQ_PAGAMENTOS,

    "r",

    encoding="utf-8"

) as f:



    pagamentos = json.load(f)



if ARQ_RECEITA.exists():
    pass



    with open(

        ARQ_RECEITA,

        "r",

        encoding="utf-8"

    ) as f:



        receita = json.load(f)



else:
    pass



    receita = {

        "eventos": []

    }



eventos_existentes = {



    (

        e.get("data"),

        e.get("descricao"),

        e.get("valor")

    )



    for e in receita["eventos"]

}



novos = 0



for pagamento in pagamentos:
    pass



    if (

        pagamento.get(

            "status",

            ""

        ).lower()

        !=

        "confirmado"

    ):

        continue



    evento = {



        "data":

            pagamento.get(

                "data",

                str(datetime.now())

            ),



        "descricao":

            pagamento.get(

                "descricao",

                "PAGAMENTO"

            ),



        "valor":

            float(

                pagamento.get(

                    "valor",

                    0

                )

            )

    }



    chave = (

        evento["data"],

        evento["descricao"],

        evento["valor"]

    )



    if chave in eventos_existentes:
        pass

        continue



    receita["eventos"].append(

        evento

    )



    eventos_existentes.add(

        chave

    )



    novos += 1



with open(

    ARQ_RECEITA,

    "w",

    encoding="utf-8"

) as f:



    json.dump(

        receita,

        f,

        indent=4,

        ensure_ascii=False

    )



total = sum(

    e["valor"]

    for e in receita["eventos"]

)



print(

    "PAGAMENTOS PROCESSADOS:",

    len(pagamentos)

)



print(

    "NOVOS EVENTOS:",

    novos

)



print(

    "RECEITA TOTAL:",

    f"R$ {total:,.2f}"

)



print(

    "\nARQUIVO:"

)



print(

    ARQ_RECEITA

)




