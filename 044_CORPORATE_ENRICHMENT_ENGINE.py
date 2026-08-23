import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORPORATE ENRICHMENT ENGINE
FASE 07
ETAPA 001

VersÃƒÂ£o 8.0

Enriquecimento Corporativo

======================================================================
"""

from datetime import datetime


class CorporateEnrichmentEngine:

    def __init__(self):

        self.camadas = [

            "IdentificaÃƒÂ§ÃƒÂ£o",

            "Contato",

            "Comercial",

            "Institucional",

            "Mercado",

            "Tecnologia",

            "Financeiro",

            "Relacionamento",

            "InteligÃƒÂªncia"

        ]

    # ======================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC CORPORATE ENRICHMENT ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("MISSÃƒÆ'O")

        print()

        print("Transformar um simples cadastro")

        print("em um dossiÃƒÂª corporativo completo.")

        print()

        print("="*70)

        print("CAMADAS DE ENRIQUECIMENTO")

        print()

        for numero, camada in enumerate(self.camadas, 1):

            print(f"{numero:02d} - {camada}")

        print()

        print("="*70)

        print("DADOS ESPERADOS")

        print()

        print("Ã¢Å"â€œ RazÃƒÂ£o Social")

        print("Ã¢Å"â€œ Nome Fantasia")

        print("Ã¢Å"â€œ Status")

        print("Ã¢Å"â€œ PaÃƒÂ­s")

        print("Ã¢Å"â€œ Estado")

        print("Ã¢Å"â€œ Cidade")

        print("Ã¢Å"â€œ Site Oficial")

        print("Ã¢Å"â€œ E-mail Comercial")

        print("Ã¢Å"â€œ Telefone")

        print("Ã¢Å"â€œ LinkedIn")

        print("Ã¢Å"â€œ Segmento")

        print("Ã¢Å"â€œ Produtos")

        print("Ã¢Å"â€œ ServiÃƒÂ§os")

        print("Ã¢Å"â€œ Mercados")

        print("Ã¢Å"â€œ Tecnologias")

        print("Ã¢Å"â€œ Potencial Comercial")

        print("Ã¢Å"â€œ Prioridade")

        print("Ã¢Å"â€œ ÃƒÅ¡ltima AtualizaÃƒÂ§ÃƒÂ£o")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Uma empresa")

        print("nÃƒÂ£o ÃƒÂ© apenas")

        print("um nome.")

        print()

        print("Ela ÃƒÂ©")

        print("um conjunto")

        print("de informaÃƒÂ§ÃƒÂµes")

        print("estratÃƒÂ©gicas.")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA ETAPA")

        print()

        print("PUBLIC DATA COLLECTOR")

        print()

        print("="*70)

        print("CORPORATE ENRICHMENT ONLINE")

        print("="*70)


# ==========================================================

if __name__ == "__main__":

    CorporateEnrichmentEngine().executar()



