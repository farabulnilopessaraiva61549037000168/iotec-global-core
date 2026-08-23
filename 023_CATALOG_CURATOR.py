"""
======================================================================
IOTEC
023_CATALOG_CURATOR.py

CATALOG CURATOR

InventÃƒÂ¡rio da Plataforma

======================================================================
"""

import os
from pathlib import Path
from datetime import datetime

PASTA_RAIZ = r"C:\IOTEC"


class CatalogCurator:

    def __init__(self):

        self.modulos = []

    # ===========================================================

    def analisar(self):

        print("=" * 70)
        print("IOTEC CATALOG CURATOR")
        print("=" * 70)
        print()

        total = 0

        for raiz, _, arquivos in os.walk(PASTA_RAIZ):

            for arquivo in arquivos:

                if not arquivo.endswith(".py"):
                    continue

                caminho = os.path.join(raiz, arquivo)

                total += 1

                try:

                    texto = Path(caminho).read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                except Exception:

                    texto = ""

                linhas = len(texto.splitlines())

                tamanho = round(
                    os.path.getsize(caminho) / 1024,
                    2
                )

                categoria = self.classificar(arquivo, texto)

                potencial = self.potencial(categoria)

                self.modulos.append({

                    "arquivo": arquivo,

                    "categoria": categoria,

                    "linhas": linhas,

                    "kb": tamanho,

                    "potencial": potencial

                })

        print(f"MÃƒÂ³dulos encontrados : {total}")
        print()

    # ===========================================================

    def classificar(self, nome, texto):

        n = nome.lower()
        t = texto.lower()

        if "commercial" in n or "comercial" in n:
            return "COMERCIAL"

        if "crm" in n:
            return "CRM"

        if "finance" in n or "financeiro" in n:
            return "FINANCEIRO"

        if "audit" in n or "auditoria" in n:
            return "AUDITORIA"

        if "contract" in n or "contrato" in n:
            return "CONTRATOS"

        if "product" in n or "catalog" in n:
            return "PRODUTOS"

        if "mission" in n:
            return "MISSÃƒâ€¢ES"

        if "kernel" in n:
            return "KERNEL"

        if "truck" in n or "logistica" in n:
            return "LOGÃƒÂSTICA"

        if "dashboard" in t:
            return "DASHBOARD"

        return "GERAL"

    # ===========================================================

    def potencial(self, categoria):

        mapa = {

            "COMERCIAL": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦",

            "PRODUTOS": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦",

            "CONTRATOS": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦",

            "CRM": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦",

            "FINANCEIRO": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ ",

            "AUDITORIA": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ ",

            "KERNEL": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ Ã¢Ëœâ€ ",

            "MISSÃƒâ€¢ES": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ Ã¢Ëœâ€ ",

            "LOGÃƒÂSTICA": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ Ã¢Ëœâ€ ",

            "DASHBOARD": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ Ã¢Ëœâ€ ",

            "GERAL": "Ã¢Ëœâ€¦Ã¢Ëœâ€¦Ã¢Ëœâ€ Ã¢Ëœâ€ Ã¢Ëœâ€ "

        }

        return mapa.get(categoria, "Ã¢Ëœâ€¦Ã¢Ëœâ€ Ã¢Ëœâ€ Ã¢Ëœâ€ Ã¢Ëœâ€ ")

    # ===========================================================

    def relatorio(self):

        print("=" * 70)
        print("INVENTÃƒÂRIO DA PLATAFORMA")
        print("=" * 70)

        self.modulos.sort(

            key=lambda x: (

                x["potencial"],

                x["categoria"],

                x["arquivo"]

            ),

            reverse=True

        )

        categorias = {}

        for m in self.modulos:

            categorias[m["categoria"]] = categorias.get(

                m["categoria"],

                0

            ) + 1

            print()

            print("Arquivo........", m["arquivo"])

            print("Categoria......", m["categoria"])

            print("Linhas.........", m["linhas"])

            print("Tamanho........", f'{m["kb"]} KB')

            print("Potencial......", m["potencial"])

            print("-" * 60)

        print()
        print("=" * 70)
        print("RESUMO")
        print("=" * 70)

        print()

        for categoria in sorted(categorias):

            print(f"{categoria:<20} {categorias[categoria]}")

        print()

        print("=" * 70)

        print()

        print("ANÃƒÂLISE DO CURATOR")

        print()

        comerciais = sum(
            1 for m in self.modulos
            if m["categoria"] in
            (
                "COMERCIAL",
                "PRODUTOS",
                "CRM",
                "CONTRATOS"
            )
        )

        print(f"MÃƒÂ³dulos com potencial comercial: {comerciais}")

        print()

        print("PrÃƒÂ³xima missÃƒÂ£o do Kernel:")

        print()

        print("Ã¢â‚¬Â¢ Descobrir quais mÃƒÂ³dulos podem")

        print("  virar serviÃƒÂ§os.")

        print()

        print("Ã¢â‚¬Â¢ Agrupar funcionalidades")

        print("  semelhantes.")

        print()

        print("Ã¢â‚¬Â¢ Montar catÃƒÂ¡logo comercial.")

        print()

        print("Ã¢â‚¬Â¢ Preparar primeiro contrato.")

        print()

        print("=" * 70)

        print("RelatÃƒÂ³rio gerado em")

        print(datetime.now())

        print("=" * 70)


# ===============================================================

if __name__ == "__main__":

    curator = CatalogCurator()

    curator.analisar()

    curator.relatorio()


