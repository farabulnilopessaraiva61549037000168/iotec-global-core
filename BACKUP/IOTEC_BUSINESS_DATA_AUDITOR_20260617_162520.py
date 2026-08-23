import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
from pathlib import Path
from collections import Counter
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

PALAVRAS_NEGOCIO = {

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

resultado = {
    "data": str(datetime.now()),
    "arquivos_lidos": 0,
    "arquivos_comerciais": 0,
    "campos_encontrados": Counter(),
    "arquivos_relevantes": [],
    "top_reservatorios": []
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

        resultado["arquivos_lidos"] += 1

        encontrados = set()

        def analisar(obj):
            pass

            if isinstance(obj, dict):
                pass

                for chave, valor in obj.items():
                    pass

                    chave_lower = str(chave).lower()

                    if chave_lower in PALAVRAS_NEGOCIO:
                        pass

                        encontrados.add(chave_lower)

                    analisar(valor)

            elif isinstance(obj, list):
                pass

                for item in obj:
                    pass

                    analisar(item)

        analisar(dados)

        if encontrados:
            pass

            tamanho = arq.stat().st_size

            resultado["arquivos_comerciais"] += 1

            for campo in encontrados:
                pass

                resultado["campos_encontrados"][campo] += 1

            resultado["arquivos_relevantes"].append({

                "arquivo": str(arq),

                "bytes": tamanho,

                "campos": sorted(list(encontrados))

            })

    except:
        pass

resultado["arquivos_relevantes"] = sorted(
    resultado["arquivos_relevantes"],
    key=lambda x: x["bytes"],
    reverse=True
)

resultado["top_reservatorios"] = \
resultado["arquivos_relevantes"][:100]

resultado["campos_encontrados"] = dict(
    resultado["campos_encontrados"].most_common()
)

saida = ROOT / "IOTEC_BUSINESS_DATA_REPORT.json"

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

print("\nBUSINESS AUDIT FINALIZADO\n")

print(
    f"Arquivos lidos: "
    f"{resultado['arquivos_lidos']}"
)

print(
    f"Arquivos comerciais: "
    f"{resultado['arquivos_comerciais']}"
)

print("\nTOP CAMPOS DE NEGÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œCIO:\n")

for campo, qtd in resultado[
    "campos_encontrados"
].items():

    print(f"{campo}: {qtd}")

print(
    f"\nRelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio: {saida}"
)


