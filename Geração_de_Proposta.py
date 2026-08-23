import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def generate_proposal(
    cliente,
    problema,
    pessoas_afetadas,
    prejuizo_estimado,
    criticidade
):

    score = calculate_impact_score(
        pessoas_afetadas,
        prejuizo_estimado,
        criticidade
    )

    categoria = classify_project(score)

    valor = calculate_value(score)

    entrada = valor * 0.30
    entrega = valor * 0.70

    print("\n================================================")
    print("PROPOSTA X27")
    print("================================================")

    print(f"CLIENTE : {cliente}")
    print(f"PROBLEMA : {problema}")

    print("\nANALISE")

    print(f"PESSOAS AFETADAS : {pessoas_afetadas}")
    print(f"PREJUIZO : R$ {prejuizo_estimado:,.2f}")

    print(f"SCORE : {score}")
    print(f"CATEGORIA : {categoria}")

    print("\nVALOR")

    print(f"VALOR PROJETO : R$ {valor:,.2f}")

    print(f"ENTRADA 30% : R$ {entrada:,.2f}")
    print(f"ENTREGA 70% : R$ {entrega:,.2f}")

    print("\nSTATUS")

    print("PROPOSTA GERADA")




