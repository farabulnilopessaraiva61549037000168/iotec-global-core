#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
IOTEC MONEY ENGINE
VersÃ£o: 1.0
=========================================================

Autor: IOTEC + ChatGPT

Objetivo:
Descobrir capacidades comerciais existentes na base
de cÃ³digo e gerar um relatÃ³rio executivo.

=========================================================
"""

from pathlib import Path
import json
import datetime

from scanner import CodeScanner
from capability_engine import CapabilityEngine
from money_score import MoneyScore


ROOT = Path(r"C:\IOTEC")


def salvar_json(relatorio, arquivo):

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(
            relatorio,
            f,
            indent=4,
            ensure_ascii=False
        )


def main():

    print("=" * 60)
    print("IOTEC MONEY ENGINE")
    print("=" * 60)

    scanner = CodeScanner(ROOT)

    arquivos = scanner.scan()

    print(f"\nArquivos encontrados: {len(arquivos)}")

    engine = CapabilityEngine()

    ativos = []

    for arquivo in arquivos:

        try:

            resultado = engine.analisar(arquivo)

            ativos.append(resultado)

            print(f"OK  {arquivo.name}")

        except Exception as erro:

            print(f"ERRO {arquivo.name}")
            print(erro)

    score = MoneyScore()

    ranking = score.processar(ativos)

    relatorio = {
        "data": str(datetime.datetime.now()),
        "arquivos": len(arquivos),
        "ativos": ativos,
        "ranking": ranking
    }

    salvar_json(relatorio, "MONEY_REPORT.json")

    print("\nRelatÃ³rio salvo em MONEY_REPORT.json")

    print("\nTOP OPORTUNIDADES\n")

    for item in ranking[:10]:

        print("-" * 40)
        print(item["produto"])
        print(f"Score : {item['score']}")
        print(f"EvidÃªncias : {item['evidencias']}")
        print("-" * 40)


if __name__ == "__main__":
    main()

