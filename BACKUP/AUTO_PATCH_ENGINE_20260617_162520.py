import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import re

ROOT = r"C:\IOTEC"

print("")
print("==================================================")
print("IOTEC AUTO PATCH ENGINE")
print("==================================================")
print("")

correcoes = 0

# ==================================================
# PATCH SALES_BRAIN
# ==================================================

arquivo = os.path.join(ROOT, "SALES_BRAIN.py")

if os.path.exists(arquivo):
    pass

    texto = open(
        arquivo,
        "r",
        encoding="utf-8"
    ).read()

    if (
        "WHERE status <> 'CLIENTE_ATIVO'"
        not in texto
    ):

        novo = re.sub(

            r"FROM\s+commercial_opportunities\s+ORDER\s+BY\s+estimated_value\s+DESC",

            """FROM commercial_opportunities

WHERE status <> 'CLIENTE_ATIVO'

ORDER BY estimated_value DESC""",

            texto,

            flags=re.IGNORECASE | re.MULTILINE

        )

        if novo != texto:
            pass

            open(
                arquivo,
                "w",
                encoding="utf-8"
            ).write(novo)

            print(
                "[PATCH] SALES_BRAIN.py"
            )

            correcoes += 1

# ==================================================
# PATCH ACTION EXECUTOR
# ==================================================

arquivo = os.path.join(
    ROOT,
    "COMMERCIAL_ACTION_EXECUTOR.py"
)

if os.path.exists(arquivo):
    pass

    texto = open(
        arquivo,
        "r",
        encoding="utf-8"
    ).read()

    if (
        'novo_status = "PAGAMENTO_PENDENTE"'
        in texto
    ):

        texto = texto.replace(

            'novo_status = "PAGAMENTO_PENDENTE"',

            'novo_status = "CLIENTE_ATIVO"'

        )

        open(
            arquivo,
            "w",
            encoding="utf-8"
        ).write(texto)

        print(
            "[PATCH] COMMERCIAL_ACTION_EXECUTOR.py"
        )

        correcoes += 1

# ==================================================
# RELATORIO
# ==================================================

print("")
print("==================================================")
print("RESUMO")
print("==================================================")
print("")

print(
    f"CORRECOES APLICADAS: "
    f"{correcoes}"
)

if correcoes == 0:
    pass

    print(
        "NUCLEO JA ESTA CONSISTENTE"
    )

else:
    pass

    print(
        "PATCHES APLICADOS COM SUCESSO"
    )

print("")
print("==================================================")


