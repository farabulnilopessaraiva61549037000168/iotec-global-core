# ==============================================================================
# IOTEC RCDE
# 002 - CAPABILITY ENGINE
#
# Descobre capacidades ocultas dentro das funÃ§Ãµes.
# ==============================================================================

from pathlib import Path
import ast
import json

ROOT = Path.home() / "Documents" / "OMEGA_BASE"

SAIDA = ROOT / "RCDE_CAPABILITIES.json"

# ------------------------------------------------------------------------------
# DicionÃ¡rio inicial de capacidades
# (Depois ficarÃ¡ enorme)
# ------------------------------------------------------------------------------

CAPABILIDADES = {

    "pdf": "Gerar Documentos",

    "reportlab": "Gerar Documentos",

    "ocr": "Leitura Inteligente",

    "pytesseract": "OCR",

    "sqlite": "Banco de Dados",

    "postgres": "Banco de Dados",

    "mysql": "Banco de Dados",

    "crm": "GestÃ£o Comercial",

    "cliente": "Relacionamento",

    "empresa": "Cadastro Empresarial",

    "lead": "ProspecÃ§Ã£o",

    "api": "IntegraÃ§Ã£o",

    "requests": "IntegraÃ§Ã£o Externa",

    "httpx": "IntegraÃ§Ã£o Externa",

    "fastapi": "API",

    "flask": "API",

    "dashboard": "VisualizaÃ§Ã£o",

    "streamlit": "Dashboard",

    "dash": "Dashboard",

    "plotly": "VisualizaÃ§Ã£o",

    "analytics": "Analytics",

    "predict": "PrediÃ§Ã£o",

    "forecast": "PrediÃ§Ã£o",

    "eventbus": "Arquitetura Orientada a Eventos",

    "queue": "Filas",

    "scheduler": "AutomaÃ§Ã£o",

    "thread": "Paralelismo",

    "async": "ExecuÃ§Ã£o AssÃ­ncrona",

    "openai": "LLM",

    "embedding": "Embeddings",

    "rag": "Busca SemÃ¢ntica",

    "vector": "Vetores",

    "mapa": "Geoprocessamento",

    "geopandas": "Geoprocessamento",

    "folium": "Mapas",

    "cnpj": "InteligÃªncia Empresarial",

    "licitacao": "LicitaÃ§Ãµes",

    "contrato": "Contratos",

    "auditoria": "Auditoria",

    "sensor": "IoT",

    "esp32": "IoT",

    "arduino": "IoT"
}

# ------------------------------------------------------------------------------

resultado = []

# ------------------------------------------------------------------------------

class CapabilityVisitor(ast.NodeVisitor):

    def __init__(self):

        self.chamadas = []

        self.imports = []

        self.nomes = []

    def visit_Call(self,node):

        try:

            if isinstance(node.func,ast.Name):

                self.chamadas.append(node.func.id.lower())

            elif isinstance(node.func,ast.Attribute):

                self.chamadas.append(node.func.attr.lower())

        except:

            pass

        self.generic_visit(node)

    def visit_Name(self,node):

        self.nomes.append(node.id.lower())

    def visit_Import(self,node):

        for alias in node.names:

            self.imports.append(alias.name.lower())

    def visit_ImportFrom(self,node):

        if node.module:

            self.imports.append(node.module.lower())


# ------------------------------------------------------------------------------

for arquivo in ROOT.rglob("*.py"):

    try:

        codigo = arquivo.read_text(
            encoding="utf8",
            errors="ignore"
        )

        arvore = ast.parse(codigo)

    except:

        continue

    visitante = CapabilityVisitor()

    visitante.visit(arvore)

    palavras = set(
        visitante.imports +
        visitante.chamadas +
        visitante.nomes
    )

    capacidades = set()

    for palavra in palavras:

        for chave in CAPABILIDADES:

            if chave in palavra:

                capacidades.add(CAPABILIDADES[chave])

    resultado.append({

        "arquivo": str(arquivo),

        "capacidades": sorted(capacidades),

        "total": len(capacidades)

    })

# ------------------------------------------------------------------------------

with open(
    SAIDA,
    "w",
    encoding="utf8"
) as f:

    json.dump(
        resultado,
        f,
        indent=4,
        ensure_ascii=False
    )

# ------------------------------------------------------------------------------

print("="*80)

print("RCDE CAPABILITY ENGINE")

print("="*80)

print()

for item in sorted(
        resultado,
        key=lambda x:x["total"],
        reverse=True
):

    if item["total"] == 0:

        continue

    print()

    print(item["arquivo"])

    print("-"*80)

    for cap in item["capacidades"]:

        print("  â€¢",cap)

print()

print("="*80)

print("Arquivo salvo:")

print(SAIDA)

