import json
import os
from datetime import datetime

ARQUIVO_ENTRADA = "IOTEC_COMPANY_DATABASE.json"
ARQUIVO_SAIDA = "IOTEC_COMPANY_MASTER.json"


def gerar_slug(nome):

    texto = nome.lower()

    remover = [
        ",", ".", ";", ":", "/", "\", "(", ")", "[", "]",
        "{", "}", "'", '"'
    ]

    for c in remover:
        texto = texto.replace(c, "")

    texto = texto.replace(" ", "-")

    return texto


def gerar_site(nome):

    slug = gerar_slug(nome)

    primeiro = slug.split("-")[0]

    return f"https://www.{primeiro}.com.br"


def enriquecer(empresa):

    nome = empresa.get("company_name", "")

    empresa["website"] = ""

    empresa["email"] = ""

    empresa["phone"] = ""

    empresa["whatsapp"] = ""

    empresa["linkedin"] = ""

    empresa["instagram"] = ""

    empresa["facebook"] = ""

    empresa["youtube"] = ""

    empresa["commercial_channel"] = []

    empresa["needs_validation"] = True

    empresa["slug"] = gerar_slug(nome)

    empresa["possible_website"] = gerar_site(nome)

    empresa["last_update"] = datetime.now().isoformat()

    empresa["status"] = "DISCOVERED"

    return empresa


def main():

    print("=" * 80)
    print("IOTEC COMPANY ENRICHMENT ENGINE")
    print("=" * 80)
    print()

    if not os.path.exists(ARQUIVO_ENTRADA):

        print("Arquivo inexistente:")
        print(ARQUIVO_ENTRADA)
        return

    with open(
        ARQUIVO_ENTRADA,
        "r",
        encoding="utf-8"
    ) as f:

        empresas = json.load(f)

    resultado = []

    for empresa in empresas:

        resultado.append(
            enriquecer(empresa)
        )

    with open(
        ARQUIVO_SAIDA,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            resultado,
            f,
            indent=4,
            ensure_ascii=False
        )

    print("Empresas enriquecidas :", len(resultado))
    print()

    print("=" * 80)
    print("EXEMPLOS")
    print("=" * 80)
    print()

    for empresa in resultado[:5]:

        print("Empresa :", empresa["company_name"])
        print("Segmento:", empresa["segmento"])
        print("Website :", empresa["possible_website"])
        print("Status  :", empresa["status"])
        print()

    print("=" * 80)
    print("ARQUIVO GERADO")
    print("=" * 80)
    print()

    print(ARQUIVO_SAIDA)

    print()

    print("STATUS")
    print("COMPANY ENRICHMENT READY")


if __name__ == "__main__":
    main()

