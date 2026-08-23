import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

PALAVRAS = {

    "empresa",
    "cliente",
    "clientes",
    "telefone",
    "celular",
    "whatsapp",
    "email",
    "contato",
    "cidade",
    "estado",
    "endereco",
    "site",
    "segmento",
    "cnpj",
    "fornecedor",
    "parceiro",
    "parceiros",
    "lead",
    "leads",
    "oportunidade",
    "oportunidades",
    "escola",
    "escolas",
    "universidade",
    "universidades",
    "faculdade",
    "faculdades"
}

MASTER = {
    "gerado_em": str(datetime.now()),
    "origens": [],
    "registros": []
}

jsons = list(ROOT.rglob("*.json"))

for arq in jsons:
    pass

    try:
        pass

        with open(
            arq,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            dados = json.load(f)

        encontrou = False

        def verificar(obj):
            pass

            global encontrou

            if isinstance(obj, dict):
                pass

                for k, v in obj.items():
                    pass

                    if str(k).lower() in PALAVRAS:
                        pass

                        return True

                    if verificar(v):
                        pass

                        return True

            elif isinstance(obj, list):
                pass

                for item in obj:
                    pass

                    if verificar(item):
                        pass

                        return True

            return False

        encontrou = verificar(dados)

        if encontrou:
            pass

            MASTER["origens"].append(
                str(arq)
            )

            MASTER["registros"].append({
                "arquivo": arq.name,
                "caminho": str(arq),
                "dados": dados
            })

    except:
        pass

saida = ROOT / "BUSINESS_MASTER_RESERVOIR.json"

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        MASTER,
        f,
        indent=2,
        ensure_ascii=False
    )

print("\nBUSINESS MASTER CRIADO\n")

print(
    f"ORIGENS: {len(MASTER['origens'])}"
)

print(
    f"REGISTROS: {len(MASTER['registros'])}"
)

print(
    f"\nARQUIVO: {saida}"
)




