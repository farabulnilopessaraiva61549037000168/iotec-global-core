#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
IOTEC MONEY ENGINE
Money Score
=========================================================
"""

class MoneyScore:

    def __init__(self):
        self.pesos = {
            "api": 20,
            "database": 20,
            "ai": 30,
            "pdf": 10,
            "excel": 10,
            "vision": 10
        }

    def processar(self, ativos):

        ranking = []

        for ativo in ativos:

            score = 0

            for capacidade in ativo.get("capacidades", []):

                score += self.pesos.get(capacidade, 5)

            ranking.append({
                "arquivo": ativo.get("arquivo"),
                "produto": self._nome_produto(ativo),
                "score": score,
                "evidencias": len(ativo.get("capacidades", [])),
                "capacidades": ativo.get("capacidades", [])
            })

        ranking.sort(
            key=lambda x: x["score"],
            reverse=True
        )

        return ranking

    def _nome_produto(self, ativo):

        caps = set(ativo.get("capacidades", []))

        if {"api", "database"} <= caps:
            return "Sistema Web"

        if {"ai", "api"} <= caps:
            return "ServiÃ§o de IA"

        if "vision" in caps:
            return "VisÃ£o Computacional"

        if "pdf" in caps:
            return "Gerador de RelatÃ³rios"

        if "excel" in caps:
            return "Processador de Planilhas"

        return "Componente Python"

