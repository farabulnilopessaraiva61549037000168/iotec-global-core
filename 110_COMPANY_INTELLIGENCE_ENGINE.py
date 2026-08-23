import json
import os
from datetime import datetime

ARQUIVO_ENTRADA = "IOTEC_REAL_COMPANIES.json"
ARQUIVO_SAIDA = "IOTEC_COMPANY_DATABASE.json"

EXCLUIR = [

    "universidade",
    "departamento",
    "curso",
    "campus",
    "laboratÃƒÂ³rio",
    "laboratorio",
    "bloco",
    "instituto",
    "escola",
    "faculdade",
    "biblioteca",
    "prefeitura",
    "governo",
    "secretaria",
    "hospital universitÃƒÂ¡rio",
    "hospital universitario"

]

SEGMENTOS = {

    "engenharia":"ENGENHARIA",
    "construtora":"CONSTRUÃƒâ€¡ÃƒÆ'O",
    "construÃƒÂ§ÃƒÂ£o":"CONSTRUÃƒâ€¡ÃƒÆ'O",
    "energia":"ENERGIA",
    "industrial":"INDÃƒÅ¡STRIA",
    "metal":"METALURGIA",
    "elÃƒÂ©trica":"ENGENHARIA ELÃƒâ€°TRICA",
    "eletrica":"ENGENHARIA ELÃƒâ€°TRICA",
    "telecom":"TELECOM",
    "tecnologia":"TECNOLOGIA",
    "software":"TECNOLOGIA",
    "consultoria":"CONSULTORIA"

}


def detectar_segmento(nome):

    texto = nome.lower()

    for chave in SEGMENTOS:

        if chave in texto:
            return SEGMENTOS[chave]

    return "NÃƒÆ'O CLASSIFICADO"


def empresa_valida(nome):

    texto = nome.lower()

    for palavra in EXCLUIR:

        if palavra in texto:
            return False

    return True


def calcular_score(nome):

    score = 50

    texto = nome.lower()

    if "engenharia" in texto:
        score += 20

    if "consultoria" in texto:
        score += 15

    if "industrial" in texto:
        score += 10

    if "tecnologia" in texto:
        score += 10

    return min(score,100)


def sugerir_produto(segmento):

    tabela = {

        "ENGENHARIA":"Dashboard Executivo",

        "CONSTRUÃƒâ€¡ÃƒÆ'O":"GestÃƒÂ£o de Obras",

        "ENERGIA":"Monitoramento",

        "INDÃƒÅ¡STRIA":"Analytics Industrial",

        "TECNOLOGIA":"IA Corporativa",

        "CONSULTORIA":"Business Intelligence"

    }

    return tabela.get(segmento,"DiagnÃƒÂ³stico Corporativo")


def main():

    print("="*80)
    print("IOTEC COMPANY INTELLIGENCE ENGINE")
    print("="*80)
    print()

    if not os.path.exists(ARQUIVO_ENTRADA):

        print("Arquivo nÃƒÂ£o encontrado:")
        print(ARQUIVO_ENTRADA)
        return

    with open(

        ARQUIVO_ENTRADA,

        "r",

        encoding="utf-8"

    ) as arquivo:

        empresas = json.load(arquivo)

    resultado = []

    descartadas = 0

    for empresa in empresas:

        nome = empresa.get("company_name","")

        if not empresa_valida(nome):

            descartadas += 1
            continue

        segmento = detectar_segmento(nome)

        score = calcular_score(nome)

        empresa["segmento"] = segmento

        empresa["market_score"] = score

        empresa["produto_iotec"] = sugerir_produto(segmento)

        empresa["status_comercial"] = "NOVO LEAD"

        resultado.append(empresa)

    resultado.sort(

        key=lambda x:x["market_score"],

        reverse=True

    )

    with open(

        ARQUIVO_SAIDA,

        "w",

        encoding="utf-8"

    ) as arquivo:

        json.dump(

            resultado,

            arquivo,

            indent=4,

            ensure_ascii=False

        )

    print("Empresas analisadas :",len(empresas))
    print("Empresas vÃƒÂ¡lidas    :",len(resultado))
    print("Descartadas         :",descartadas)
    print()

    print("="*80)
    print("TOP 10")
    print("="*80)
    print()

    for empresa in resultado[:10]:

        print(empresa["company_name"])
        print("Segmento :",empresa["segmento"])
        print("Score    :",empresa["market_score"])
        print("Produto  :",empresa["produto_iotec"])
        print()

    print("="*80)
    print("ARQUIVO GERADO")
    print("="*80)
    print()

    print(ARQUIVO_SAIDA)
    print()

    print("Data :",datetime.now())
    print("STATUS : COMPANY INTELLIGENCE READY")


if __name__ == "__main__":
    main()

