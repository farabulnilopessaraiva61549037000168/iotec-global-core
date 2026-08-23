#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
=========================================================
IOTEC MONEY ENGINE
Capability Engine
=========================================================
"""

import ast
from pathlib import Path


class CapabilityEngine:

    def __init__(self):

        self.keywords = {
            "api": [
                "fastapi",
                "flask",
                "django",
                "requests",
                "httpx"
            ],

            "database": [
                "sqlite3",
                "sqlalchemy",
                "pymysql",
                "psycopg2",
                "mysql",
                "postgres"
            ],

            "ai": [
                "openai",
                "google.generativeai",
                "transformers",
                "torch",
                "tensorflow",
                "langchain"
            ],

            "pdf": [
                "fpdf",
                "reportlab",
                "fitz",
                "pymupdf"
            ],

            "excel": [
                "openpyxl",
                "xlsxwriter",
                "pandas"
            ],

            "vision": [
                "cv2",
                "PIL",
                "easyocr"
            ]
        }

    def analisar(self, arquivo):

        arquivo = Path(arquivo)

        resultado = {
            "arquivo": str(arquivo),
            "classes": [],
            "funcoes": [],
            "imports": [],
            "capacidades": []
        }

        try:

            codigo = arquivo.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            arvore = ast.parse(codigo)

        except Exception:

            return resultado

        for node in ast.walk(arvore):

            if isinstance(node, ast.ClassDef):

                resultado["classes"].append(node.name)

            elif isinstance(node, ast.FunctionDef):

                resultado["funcoes"].append(node.name)

            elif isinstance(node, ast.Import):

                for modulo in node.names:

                    resultado["imports"].append(modulo.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:

                    resultado["imports"].append(node.module)

        capacidades = set()

        imports = " ".join(resultado["imports"]).lower()

        for categoria, lista in self.keywords.items():

            for palavra in lista:

                if palavra.lower() in imports:

                    capacidades.add(categoria)

        resultado["capacidades"] = sorted(capacidades)

        return resultado

