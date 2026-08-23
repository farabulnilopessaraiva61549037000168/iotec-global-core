import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def avaliar_estoques():
    pass

    agua = dias_de_autonomia(
        estoque=1000000,
        consumo_diario=50000
    )

    alimentos = dias_de_autonomia(
        estoque=250000,
        consumo_diario=10000
    )

    print("\n================================================")
    print("SEGURANCA DE ESTOQUES")
    print("================================================")

    print(f"AGUA       : {agua} dias")
    print(f"ALIMENTOS  : {alimentos} dias")




