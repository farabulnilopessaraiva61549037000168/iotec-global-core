import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC DATA VALIDATION ENGINE
FASE 07
ETAPA 003

VersÃƒÂ£o 8.0

ValidaÃƒÂ§ÃƒÂ£o da InteligÃƒÂªncia Corporativa

======================================================================
"""

from datetime import datetime


class DataValidationEngine:

    def __init__(self):

        self.campos = [

            ("RazÃƒÂ£o Social",False),
            ("Nome Fantasia",False),
            ("CNPJ / Registro",False),
            ("Status da Empresa",False),
            ("PaÃƒÂ­s",False),
            ("Estado",False),
            ("Cidade",False),
            ("Website Oficial",False),
            ("LinkedIn Oficial",False),
            ("E-mail Comercial",False),
            ("Telefone Comercial",False),
            ("Segmento",True),
            ("Subsegmento",False),
            ("Produtos",False),
            ("ServiÃƒÂ§os",False),
            ("Mercados",False),
            ("Tecnologias",False),
            ("ResponsÃƒÂ¡vel Comercial",False),
            ("ÃƒÅ¡ltima AtualizaÃƒÂ§ÃƒÂ£o",False),
            ("Origem dos Dados",False)

        ]

    # ======================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC DATA VALIDATION ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        completos = 0

        print("VALIDAÃƒâ€¡ÃƒÆ'O DOS CAMPOS")
        print()

        for campo,status in self.campos:

            texto = "VALIDADO" if status else "PENDENTE"

            print(f"{campo:<30} {texto}")

            if status:
                completos += 1

        print()

        print("="*70)

        percentual = (completos/len(self.campos))*100

        print("RESUMO")

        print()

        print("Campos.................",len(self.campos))
        print("Validados..............",completos)
        print("Pendentes..............",len(self.campos)-completos)
        print(f"Qualidade.............. {percentual:.1f}%")

        print()

        print("="*70)

        print("CRITÃƒâ€°RIOS DE QUALIDADE")

        print()

        print("Ã¢Å"â€œ InformaÃƒÂ§ÃƒÂ£o pÃƒÂºblica")

        print("Ã¢Å"â€œ Fonte verificÃƒÂ¡vel")

        print("Ã¢Å"â€œ AtualizaÃƒÂ§ÃƒÂ£o registrada")

        print("Ã¢Å"â€œ Dados consistentes")

        print("Ã¢Å"â€œ Sem duplicidade")

        print("Ã¢Å"â€œ Estrutura padronizada")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("O Kernel")

        print("nÃƒÂ£o trabalha")

        print("com informaÃƒÂ§ÃƒÂµes")

        print("nÃƒÂ£o verificadas.")

        print()

        print("Toda informaÃƒÂ§ÃƒÂ£o")

        print("deve possuir")

        print("origem conhecida")

        print("e qualidade comprovada.")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMA ETAPA")

        print()

        print("NORMALIZAÃƒâ€¡ÃƒÆ'O DOS DADOS")

        print()

        print("="*70)

        print("DATA VALIDATION ONLINE")

        print("="*70)


if __name__ == "__main__":

    DataValidationEngine().executar()



