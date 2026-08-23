import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC ACROPOLE CITY ENGINE

# FUTURISTIC EDUCATIONAL CIVILIZATION

# VERSION 2.0

# ============================================================



import json

import random

from datetime import datetime



# ============================================================

# IDENTIDADE

# ============================================================



EMPRESA = {



    "nome": "IOTEC ACROPOLE GLOBAL",

    "tipo": "Civilizacao Educacional",

    "cnpj": "61.549.037/0001-68",

    "email": "iotec.bl@proton.me",

    "status": "ONLINE",

    "fundacao": str(datetime.utcnow())



}



# ============================================================

# PLANOS

# ============================================================



PLANOS = {



    "BASIC": {



        "mensal_brl": 3500,

        "mensal_usd": 900,



        "acesso": [



            "Bibliotecas",

            "Agoras",

            "Centro Cultural",

            "Ambientes de Estudo"



        ]



    },



    "PRO": {



        "mensal_brl": 12000,

        "mensal_usd": 3200,



        "acesso": [



            "IA Educacional",

            "Laboratorios",

            "Urbanismo Inteligente",

            "Mentorias",

            "Centro Tecnologico"



        ]



    },



    "PREMIUM": {



        "mensal_brl": 48000,

        "mensal_usd": 12000,



        "acesso": [



            "Residencia Academica",

            "Agoras Privadas",

            "Observatorios",

            "Networking Global",

            "Centro Filosofico",

            "Campus Monumental"



        ]



    }



}



# ============================================================

# ACRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"POLES

# ============================================================



ACROPOLES = [



    {



        "nome": "ACROPOLE ATHENA",

        "pais": "Brasil",

        "cidade": "Fortaleza",



        "estilo": "Neo-Minimalismo Grego",



        "residentes": 182,



        "bibliotecas": 4,

        "agoras": 7,

        "torres": 2,



        "status": "OPERACIONAL"



    },



    {



        "nome": "ACROPOLE HELIOS",

        "pais": "Estados Unidos",

        "cidade": "Miami",



        "estilo": "Futurismo Mediterraneo",



        "residentes": 96,



        "bibliotecas": 6,

        "agoras": 11,

        "torres": 4,



        "status": "EXPANSAO"



    },



    {



        "nome": "ACROPOLE ORION",

        "pais": "JapÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o",

        "cidade": "Tokyo",



        "estilo": "Minimalismo Tecnologico",



        "residentes": 61,



        "bibliotecas": 8,

        "agoras": 9,

        "torres": 5,



        "status": "PROJECAO"



    }



]



# ============================================================

# ALUNOS

# ============================================================



ALUNOS = []



# ============================================================

# MATRICULAR

# ============================================================



def matricular(



    nome,

    pais,

    plano,

    acropole



):



    aluno = {



        "id": f"AL-{random.randint(100000,999999)}",



        "nome": nome,

        "pais": pais,

        "plano": plano,

        "acropole": acropole,



        "nivel": random.choice([



            "Fundamental",

            "AvanÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ado",

            "Civilizacional"



        ]),



        "timestamp": str(datetime.utcnow())



    }



    ALUNOS.append(aluno)



# ============================================================

# RECEITA

# ============================================================



def calcular_receita():
    pass



    receita_brl = 0

    receita_usd = 0



    for aluno in ALUNOS:
        pass



        plano = aluno["plano"]



        if aluno["pais"] == "Brasil":
            pass



            receita_brl += PLANOS[plano]["mensal_brl"]



        else:
            pass



            receita_usd += PLANOS[plano]["mensal_usd"]



    return receita_brl, receita_usd



# ============================================================

# DASHBOARD

# ============================================================



def dashboard():
    pass



    receita_brl, receita_usd = calcular_receita()



    print()

    print("===================================================")

    print(" IOTEC ACROPOLE CITY ENGINE")

    print(" FUTURISTIC EDUCATIONAL CIVILIZATION")

    print("===================================================")



    print()

    print(f"EMPRESA: {EMPRESA['nome']}")

    print(f"CNPJ: {EMPRESA['cnpj']}")

    print(f"STATUS: {EMPRESA['status']}")



    print()

    print("===================================================")

    print(" ACRÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"POLES")

    print("===================================================")



    for acropole in ACROPOLES:
        pass



        print()

        print(f"NOME: {acropole['nome']}")

        print(f"PAIS: {acropole['pais']}")

        print(f"CIDADE: {acropole['cidade']}")

        print(f"ESTILO: {acropole['estilo']}")



        print(

            f"RESIDENTES: "

            f"{acropole['residentes']}"

        )



        print(

            f"AGORAS: "

            f"{acropole['agoras']}"

        )



        print(

            f"BIBLIOTECAS: "

            f"{acropole['bibliotecas']}"

        )



        print(

            f"TORRES: "

            f"{acropole['torres']}"

        )



        print(

            f"STATUS: "

            f"{acropole['status']}"

        )



    print()

    print("===================================================")

    print(" MATRICULADOS")

    print("===================================================")



    print()

    print(f"TOTAL: {len(ALUNOS)}")



    for aluno in ALUNOS:
        pass



        print()



        print(f"ID: {aluno['id']}")

        print(f"NOME: {aluno['nome']}")

        print(f"PAIS: {aluno['pais']}")

        print(f"PLANO: {aluno['plano']}")

        print(f"ACROPOLE: {aluno['acropole']}")

        print(f"NIVEL: {aluno['nivel']}")



    print()

    print("===================================================")

    print(" RECEITA GLOBAL")

    print("===================================================")



    print()

    print(f"BRASIL: R$ {receita_brl:,.2f}")



    print(

        f"GLOBAL: US$ {receita_usd:,.2f}"

    )



# ============================================================

# EXPORTACAO

# ============================================================



def exportar():
    pass



    relatorio = {



        "empresa": EMPRESA,

        "planos": PLANOS,

        "acropoles": ACROPOLES,

        "alunos": ALUNOS



    }



    with open(



        "IOTEC_ACROPOLE_CITY.json",

        "w",

        encoding="utf-8"



    ) as arquivo:



        json.dump(



            relatorio,

            arquivo,

            indent=4,

            ensure_ascii=False



        )



    print()

    print("===================================================")

    print(" EXPORTACAO")

    print("===================================================")



    print()

    print(

        "ARQUIVO -> "

        "IOTEC_ACROPOLE_CITY.json"

    )



# ============================================================

# SIMULACAO

# ============================================================



matricular(



    "Lucas Andrade",

    "Brasil",

    "BASIC",

    "ACROPOLE ATHENA"



)



matricular(



    "Emma Richardson",

    "Estados Unidos",

    "PREMIUM",

    "ACROPOLE HELIOS"



)



matricular(



    "Akira Sato",

    "JapÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o",

    "PRO",

    "ACROPOLE ORION"



)



matricular(



    "Sophie Laurent",

    "Europa",

    "PREMIUM",

    "ACROPOLE HELIOS"



)



# ============================================================

# EXECUCAO

# ============================================================



dashboard()



exportar()



print()

print("===================================================")

print(" NUCLEO FINALIZADO")

print("===================================================")






