import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# MOTOR DE SIMILARIDADE AVANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ADO

# =========================================================



def detectar_categoria(setor):
    pass



    setor = setor.lower()



    categorias = {



        "saude": [

            "bio",

            "labor",

            "hospital",

            "clinica",

            "farm"

        ],



        "moda": [

            "roupa",

            "fashion",

            "vest",

            "textil"

        ],



        "educacao": [

            "escola",

            "prof",

            "curso",

            "facul"

        ],



        "tecnologia": [

            "software",

            "program",

            "informat",

            "dados"

        ],



        "industrial": [

            "industr",

            "agro",

            "fabrica",

            "produc",

            "logistica"

        ]

    }



    # -----------------------------------------------------

    # BUSCA POR FRAGMENTOS

    # -----------------------------------------------------



    for categoria, palavras in categorias.items():
        pass



        for palavra in palavras:
            pass



            if palavra in setor:
                pass



                return categoria



    return "generico"



# =========================================================

# TESTE

# =========================================================



entrada = input(

    "\nDigite o setor da empresa:\n\n>>> "

)



categoria = detectar_categoria(entrada)



print("\n===================================")

print("CATEGORIA DETECTADA")

print("===================================")



print(f"\nSetor informado: {entrada}")

print(f"Categoria encontrada: {categoria}")






