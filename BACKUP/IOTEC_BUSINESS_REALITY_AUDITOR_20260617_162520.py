import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import re
from pathlib import Path
from collections import Counter

ARQUIVO = Path(r"C:\IOTEC\BUSINESS_MASTER_RESERVOIR.json")

EMAIL_RE = re.compile(
    r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
)

resultado = {
    "total": 0,
    "real": 0,
    "provavel_real": 0,
    "desconhecido": 0,
    "simulado": 0,
    "campos": Counter(),
    "registros": []
}

SIMULADOS = {
    "teste",
    "test",
    "empresa teste",
    "cliente teste",
    "exemplo",
    "sample",
    "dummy"
}

with open(
    ARQUIVO,
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    master = json.load(f)

for item in master.get("registros", []):
    pass

    resultado["total"] += 1

    dados = item.get("dados", {})

    score = 0

    encontrou_empresa = False
    encontrou_email = False
    encontrou_cnpj = False
    encontrou_whatsapp = False
    encontrou_site = False

    texto = json.dumps(
        dados,
        ensure_ascii=False
    ).lower()

    for palavra in SIMULADOS:
        pass

        if palavra in texto:
            pass

            resultado["simulado"] += 1

            resultado["registros"].append({
                "arquivo": item["arquivo"],
                "status": "SIMULADO"
            })

            score = -999
            break

    if score == -999:
        continue

    def analisar(obj):
        pass

        nonlocal_vars = {
            "empresa": False,
            "email": False,
            "cnpj": False,
            "whatsapp": False,
            "site": False
        }

        def percorrer(x):
            pass

            if isinstance(x, dict):
                pass

                for k, v in x.items():
                    pass

                    chave = str(k).lower()

                    if chave == "empresa":
                        nonlocal_vars["empresa"] = True

                    if chave == "email":
                        pass

                        if EMAIL_RE.match(
                            str(v).strip()
                        ):
                            nonlocal_vars["email"] = True

                    if chave == "cnpj":
                        nonlocal_vars["cnpj"] = True

                    if chave == "whatsapp":
                        nonlocal_vars["whatsapp"] = True

                    if chave == "site":
                        nonlocal_vars["site"] = True

                    percorrer(v)

            elif isinstance(x, list):
                pass

                for y in x:
                    percorrer(y)

        percorrer(obj)

        return nonlocal_vars

    flags = analisar(dados)

    if flags["empresa"]:
        score += 2

    if flags["email"]:
        score += 2

    if flags["cnpj"]:
        score += 3

    if flags["whatsapp"]:
        score += 1

    if flags["site"]:
        score += 1

    if score >= 6:
        pass

        status = "REAL"
        resultado["real"] += 1

    elif score >= 3:
        pass

        status = "PROVAVEL_REAL"
        resultado["provavel_real"] += 1

    else:
        pass

        status = "DESCONHECIDO"
        resultado["desconhecido"] += 1

    resultado["registros"].append({

        "arquivo": item["arquivo"],
        "status": status,
        "score": score

    })

saida = Path(
    r"C:\IOTEC\BUSINESS_REALITY_REPORT.json"
)

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

print("\nREALITY AUDIT\n")

print(
    f"TOTAL: {resultado['total']}"
)

print(
    f"REAL: {resultado['real']}"
)

print(
    f"PROVAVEL_REAL: {resultado['provavel_real']}"
)

print(
    f"DESCONHECIDO: {resultado['desconhecido']}"
)

print(
    f"SIMULADO: {resultado['simulado']}"
)

print(
    f"\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO: {saida}"
)


