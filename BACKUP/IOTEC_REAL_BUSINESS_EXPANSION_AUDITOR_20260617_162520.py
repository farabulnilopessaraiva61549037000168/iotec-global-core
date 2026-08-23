import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# IOTEC_REAL_BUSINESS_EXPANSION_AUDITOR.py

import json
from pathlib import Path
from collections import Counter

ROOT = Path(r"C:\IOTEC")

ARQUIVO = ROOT / "REAL_BUSINESS_RESERVOIR.json"

CAMPOS = [
    "empresa",
    "cliente",
    "email",
    "telefone",
    "whatsapp",
    "cnpj",
    "cidade",
    "estado",
    "site",
    "segmento"
]

resultado = {
    "entidades": [],
    "faltantes": Counter(),
    "estatisticas": {}
}

with open(
    ARQUIVO,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    dados = json.load(f)

registros = []

registros.extend(
    dados.get("reais", [])
)

registros.extend(
    dados.get("provaveis_reais", [])
)

for registro in registros:
    pass

    entidade = {
        "arquivo": registro.get(
            "arquivo",
            "desconhecido"
        ),
        "campos_encontrados": [],
        "campos_faltantes": []
    }

    texto = json.dumps(
        registro,
        ensure_ascii=False
    ).lower()

    for campo in CAMPOS:
        pass

        if f'"{campo}"' in texto:
            pass

            entidade[
                "campos_encontrados"
            ].append(campo)

        else:
            pass

            entidade[
                "campos_faltantes"
            ].append(campo)

            resultado[
                "faltantes"
            ][campo] += 1

    resultado[
        "entidades"
    ].append(entidade)

resultado[
    "estatisticas"
] = {

    "total_entidades":
        len(
            resultado["entidades"]
        ),

    "top_faltantes":
        dict(
            resultado[
                "faltantes"
            ].most_common(20)
        )
}

saida = ROOT / "REAL_BUSINESS_EXPANSION_REPORT.json"

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nREAL BUSINESS EXPANSION AUDIT\n")

print(
    "ENTIDADES:",
    resultado["estatisticas"][
        "total_entidades"
    ]
)

print("\nTOP CAMPOS FALTANTES:\n")

for campo, qtd in resultado[
    "faltantes"
].most_common():

    print(
        f"{campo}: {qtd}"
    )

print(
    "\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO:"
)

print(saida)


