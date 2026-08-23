import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CORPORATE PROFILE ENGINE
FASE 07
ETAPA 004

VersÃƒÂ£o 8.0

Gerenciamento da Qualidade
dos Perfis Corporativos

======================================================================
"""

from datetime import datetime


class CorporateProfileEngine:

    def __init__(self):

        self.campos = [

            ("RazÃƒÂ£o Social",False),
            ("Nome Fantasia",False),
            ("CNPJ / Registro",False),
            ("Status",False),
            ("PaÃƒÂ­s",True),
            ("Estado",False),
            ("Cidade",False),
            ("Website Oficial",False),
            ("LinkedIn",False),
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

    # ========================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC CORPORATE PROFILE ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        completos = 0

        print()

        print("MATURIDADE DO PERFIL")

        print()

        for campo,status in self.campos:

            if status:

                print(f"[Ã¢Å"â€œ] {campo}")

                completos += 1

            else:

                print(f"[ ] {campo}")

        print()

        percentual = completos/len(self.campos)*100

        print("="*70)

        print("QUALIDADE DO PERFIL")

        print()

        print(f"{percentual:.1f}%")

        print()

        if percentual < 25:

            nivel = "BÃƒÂSICO"

        elif percentual < 50:

            nivel = "EM CONSTRUÃƒâ€¡ÃƒÆ'O"

        elif percentual < 75:

            nivel = "INTERMEDIÃƒÂRIO"

        elif percentual < 90:

            nivel = "AVANÃƒâ€¡ADO"

        else:

            nivel = "PREMIUM"

        print("CLASSIFICAÃƒâ€¡ÃƒÆ'O")

        print()

        print(nivel)

        print()

        print("="*70)

        print("PRÃƒâ€œXIMOS CAMPOS PRIORITÃƒÂRIOS")

        print()

        for campo,status in self.campos:

            if not status:

                print("Ã¢â‚¬Â¢",campo)

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Cada informaÃƒÂ§ÃƒÂ£o")

        print("adicionada")

        print("aumenta a capacidade")

        print("de compreensÃƒÂ£o")

        print("da organizaÃƒÂ§ÃƒÂ£o.")

        print()

        print("="*70)

        print("CORPORATE PROFILE ONLINE")

        print("="*70)


if __name__ == "__main__":

    CorporateProfileEngine().executar()



