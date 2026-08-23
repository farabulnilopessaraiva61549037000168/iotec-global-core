import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def main():
    pass

    print("\nMISSAO KATSUYU")

    for etapa in MISSAO_KATSUYU:
        pass

        print(f"[OK] {etapa}")

    indicadores = {

        "AGUA": 80,
        "ALIMENTOS": 75,
        "SAUDE": 65,
        "ENERGIA": 90,
        "COMUNICACAO": 85

    }

    indice = calcular_resilience_index(
        indicadores
    )

    print("\n================================================")
    print("RESILIENCE INDEX")
    print("================================================")

    print(indice)

    avaliar_estoques()

    protocolo("SECA")

if __name__ == "__main__":
    main()




