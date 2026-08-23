import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC NUCLEUS INVESTIGATION ENGINE

# MAPEAMENTO COMPLETO DOS NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEOS

# ============================================================



import json

from pathlib import Path



# ============================================================

# BASE

# ============================================================



BASE = Path("C:/IOTEC_NUCLEUS_INVESTIGATION")



BASE.mkdir(

    parents=True,

    exist_ok=True

)



# ============================================================

# NUCLEOS IDENTIFICADOS

# ============================================================



NUCLEOS = [



    {

        "nome": "IOTEC CORE",

        "categoria": "NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo Central",

        "status": "ATIVO",

        "receita_mensal_usd": 0

    },



    {

        "nome": "IOTEC GLOBAL REALTY",

        "categoria": "ImobiliÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio",

        "status": "ATIVO",

        "receita_mensal_usd": 49000

    },



    {

        "nome": "ACROPOLE GLOBAL",

        "categoria": "EducaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o Premium",

        "status": "ATIVO",

        "receita_mensal_usd": 150000

    },



    {

        "nome": "ACROPOLE PRIME",

        "categoria": "Portal Institucional",

        "status": "ATIVO",

        "receita_mensal_usd": 12000

    },



    {

        "nome": "ACROPOLE OMEGA",

        "categoria": "Sistema Educacional",

        "status": "ATIVO",

        "receita_mensal_usd": 35000

    },



    {

        "nome": "ACROPOLE COSMOS",

        "categoria": "ExperiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia CinemÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica",

        "status": "ATIVO",

        "receita_mensal_usd": 18000

    },



    {

        "nome": "EXECUTIVE DASHBOARD",

        "categoria": "Analytics",

        "status": "ATIVO",

        "receita_mensal_usd": 22000

    },



    {

        "nome": "REALTIME EXECUTIVE",

        "categoria": "Monitoramento",

        "status": "ATIVO",

        "receita_mensal_usd": 9000

    },



    {

        "nome": "IOTEC AI",

        "categoria": "InteligÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªncia Artificial",

        "status": "PROJEÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O",

        "receita_mensal_usd": 80000

    },



    {

        "nome": "IOTEC LICENSING",

        "categoria": "Licenciamento",

        "status": "PROJEÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O",

        "receita_mensal_usd": 120000

    }



]



# ============================================================

# CALCULOS

# ============================================================



TOTAL_EMPRESAS = len(NUCLEOS)



RECEITA_TOTAL = sum(

    item["receita_mensal_usd"]

    for item in NUCLEOS

)



RECEITA_ANUAL = RECEITA_TOTAL * 12



# ============================================================

# RELATORIO

# ============================================================



RELATORIO = {



    "empresa_principal": "IOTEC",



    "total_de_nucleos":

    TOTAL_EMPRESAS,



    "receita_mensal_usd":

    RECEITA_TOTAL,



    "receita_anual_usd":

    RECEITA_ANUAL,



    "nucleos":

    NUCLEOS



}



# ============================================================

# EXPORTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



ARQUIVO = BASE / "IOTEC_NUCLEUS_REPORT.json"



with open(

    ARQUIVO,

    "w",

    encoding="utf-8"

) as f:



    json.dump(

        RELATORIO,

        f,

        indent=4,

        ensure_ascii=False

    )



# ============================================================

# TERMINAL

# ============================================================



print()

print("===================================================")

print(" IOTEC NUCLEUS INVESTIGATION ENGINE")

print("===================================================")



print()

print("EMPRESA CENTRAL:")

print("IOTEC")



print()

print("===================================================")

print(" NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEOS IDENTIFICADOS")

print("===================================================")



for nucleo in NUCLEOS:
    pass



    print()

    print(f"NOME: {nucleo['nome']}")

    print(f"CATEGORIA: {nucleo['categoria']}")

    print(f"STATUS: {nucleo['status']}")



    print(

        "RECEITA USD: "

        f"US$ {nucleo['receita_mensal_usd']:,.2f}"

    )



print()

print("===================================================")

print(" MAPA FINANCEIRO")

print("===================================================")



print()

print(f"TOTAL DE NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡CLEOS: {TOTAL_EMPRESAS}")



print()

print(

    "RECEITA MENSAL GLOBAL:"

)



print(

    f"US$ {RECEITA_TOTAL:,.2f}"

)



print()

print(

    "RECEITA ANUAL GLOBAL:"

)



print(

    f"US$ {RECEITA_ANUAL:,.2f}"

)



print()

print("===================================================")

print(" EXPORTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O")

print("===================================================")



print()

print(

    f"ARQUIVO -> {ARQUIVO}"

)



print()

print("===================================================")

print(" INVESTIGAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O FINALIZADA")

print("===================================================")







