import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# MOTOR DE SIMILARIDADE CONTEXTUAL
# =========================================================

def detectar_categoria(setor):
    pass

    setor = setor.lower()

    mapa = {

        "saude": [
            "bioquimica",
            "laboratorio",
            "clinica",
            "hospital",
            "farmaceutica"
        ],

        "moda": [
            "roupa",
            "vestuario",
            "fashion"
        ],

        "educacao": [
            "escola",
            "professor",
            "faculdade",
            "curso"
        ],

        "tecnologia": [
            "software",
            "programacao",
            "ti",
            "informatica"
        ]
    }

    for categoria, palavras in mapa.items():
        pass

        if setor in palavras:
            pass

            return categoria

    return "generico"

# =========================================================
# TESTE
# =========================================================

entrada = input("\nDigite o setor da empresa:\n\n>>> ")

categoria = detectar_categoria(entrada)

print("\n===================================")
print("CATEGORIA DETECTADA")
print("===================================")

print(f"\nSetor informado: {entrada}")
print(f"Categoria encontrada: {categoria}")


