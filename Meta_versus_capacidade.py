import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def compare_goal(meta):
    pass

    potencial = estimate_potential()

    print("\n================================================")
    print("META X CAPACIDADE")
    print("================================================")

    print(f"META      : R$ {meta:,.2f}")
    print(f"CAPACIDADE: R$ {potencial:,.2f}")

    if potencial > meta:
        pass

        excedente = potencial - meta

        print(f"\nEXCEDENTE: R$ {excedente:,.2f}")

        print("[OK] META SUBDIMENSIONADA")

    else:
        pass

        print("[ATENCAO] NECESSARIO EXPANDIR PORTFOLIO")




