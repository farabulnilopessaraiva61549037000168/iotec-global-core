import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# X27 LEARNING ENGINE
# ============================================================

import json
from datetime import datetime

# ============================================================
# OPERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ANALISADA
# ============================================================

OPERACAO = {

    "id": "X27-5202",

    "evento": "ROMPIMENTO_BARRAGEM",

    "municipio": "IBICUITINGA",

    "data": str(datetime.now())

}

# ============================================================
# LIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES APRENDIDAS
# ============================================================

LICOES = {

    "funcionou": [

        "Hospital parceiro respondeu rapidamente",

        "Rede satelital manteve comunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",

        "Abrigos foram ativados"

    ],

    "falhou": [

        "Atraso no transporte de medicamentos",

        "Internet terrestre indisponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel"

    ],

    "melhorias": [

        "Criar estoque regional de medicamentos",

        "Ampliar redundÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia de internet",

        "Expandir rede mesh"

    ]

}

# ============================================================
# GERAR RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ============================================================

def gerar_relatorio():
    pass

    relatorio = {

        "operacao": OPERACAO,

        "licoes": LICOES

    }

    with open(
        "X27_LEARNING_REPORT.json",
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            relatorio,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

    return relatorio

# ============================================================
# EXIBIR
# ============================================================

def exibir(relatorio):
    pass

    print("\n================================================")
    print("X27 LEARNING ENGINE")
    print("================================================")

    print(f"OPERAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O : {OPERACAO['id']}")

    print(f"EVENTO   : {OPERACAO['evento']}")

    print(f"MUNICIPIO: {OPERACAO['municipio']}")

    print("\n================================================")
    print("FUNCIONOU")
    print("================================================")

    for item in relatorio["licoes"]["funcionou"]:
        pass

        print(f"[OK] {item}")

    print("\n================================================")
    print("FALHAS")
    print("================================================")

    for item in relatorio["licoes"]["falhou"]:
        pass

        print(f"[FALHA] {item}")

    print("\n================================================")
    print("MELHORIAS")
    print("================================================")

    for item in relatorio["licoes"]["melhorias"]:
        pass

        print(f"[AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] {item}")

    print("\n================================================")
    print("MEMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIA OPERACIONAL ATUALIZADA")
    print("================================================")

# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":
    pass

    relatorio = gerar_relatorio()

    exibir(relatorio)

    print(
        "\n[OK] Arquivo salvo: "
        "X27_LEARNING_REPORT.json"
    )




