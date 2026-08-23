import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def executive_view():
    pass

    potencial = estimate_potential()

    print("\n================================================")
    print("X27 CAPABILITY FORECAST")
    print("================================================")

    print(f"CAPACIDADES : {len(CAPABILITIES)}")

    print("\nPORTFOLIO")

    for nome, dados in CAPABILITIES.items():
        pass

        print(
            f"{nome:<30} "
            f"{dados['mercado']:<20} "
            f"R$ {dados['valor_medio']:,.2f}"
        )

    print("\n================================================")
    print("POTENCIAL ESTIMADO")
    print("================================================")

    print(f"R$ {potencial:,.2f}")




