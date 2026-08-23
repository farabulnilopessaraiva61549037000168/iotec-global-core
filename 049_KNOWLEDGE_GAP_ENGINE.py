import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC KNOWLEDGE GAP ENGINE
FASE 07
ETAPA 006

VersÃƒÂ£o 8.0

Auditoria das Lacunas de Conhecimento

======================================================================
"""

from datetime import datetime


class KnowledgeGapEngine:

    VERSION = "8.0"

    def __init__(self):

        self.meta = 95

        self.campos = [

            ("RazÃƒÂ£o Social",5,False),
            ("Nome Fantasia",3,False),
            ("CNPJ / Registro",5,False),
            ("Status",2,False),
            ("PaÃƒÂ­s",2,True),
            ("Estado",2,False),
            ("Cidade",2,False),
            ("Website Oficial",5,False),
            ("LinkedIn Oficial",5,False),
            ("Telefone Comercial",5,False),
            ("E-mail Comercial",5,False),
            ("Segmento",5,True),
            ("Subsegmento",3,False),
            ("Produtos",10,False),
            ("ServiÃƒÂ§os",10,False),
            ("Mercados",8,False),
            ("Tecnologias",8,False),
            ("Executivos",5,False),
            ("Parceiros",5,False),
            ("Potencial Comercial",5,False),
            ("Prioridade",3,False),
            ("Origem dos Dados",3,False),
            ("ÃƒÅ¡ltima AtualizaÃƒÂ§ÃƒÂ£o",4,False)

        ]

    # ======================================================

    def executar(self):

        print()

        print("="*70)
        print("IOTEC KNOWLEDGE GAP ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        total = 0
        atual = 0

        faltantes = []

        for campo, peso, status in self.campos:

            total += peso

            if status:

                atual += peso

            else:

                faltantes.append((campo, peso))

        percentual = (atual / total) * 100

        print()

        print("CAPITAL INTELECTUAL")

        print()

        print(f"Atual.................... {percentual:.1f}%")
        print(f"Meta..................... {self.meta}%")
        print(f"EvoluÃƒÂ§ÃƒÂ£o NecessÃƒÂ¡ria...... {self.meta-percentual:.1f}%")

        print()

        print("="*70)

        print("LACUNAS IDENTIFICADAS")

        print()

        faltantes = sorted(faltantes, key=lambda x: x[1], reverse=True)

        for campo, peso in faltantes:

            print(f"[ ] {campo:<30} +{peso} pontos")

        print()

        print("="*70)

        print("PRIORIDADES")

        print()

        top = faltantes[:5]

        for i, (campo, peso) in enumerate(top,1):

            print(f"{i}. {campo} ({peso} pontos)")

        print()

        ganho = sum(peso for _, peso in top)

        novo = ((atual + ganho)/total)*100

        print("="*70)

        print("SIMULAÃƒâ€¡ÃƒÆ'O")

        print()

        print(f"Conhecimento Atual....... {percentual:.1f}%")
        print(f"ApÃƒÂ³s Prioridades......... {novo:.1f}%")
        print(f"Ganho Previsto........... +{novo-percentual:.1f}%")

        print()

        print("="*70)

        print("RECOMENDAÃƒâ€¡ÃƒÆ'O DO KERNEL")

        print()

        if percentual < 20:

            print("NÃƒÆ'O iniciar abordagem comercial.")
            print("Priorizar enriquecimento dos dados.")

        elif percentual < 50:

            print("Realizar apenas contatos exploratÃƒÂ³rios.")

        elif percentual < 80:

            print("Preparar estratÃƒÂ©gia personalizada.")

        else:

            print("Perfil pronto para proposta executiva.")

        print()

        print("="*70)

        print("FILOSOFIA")

        print()

        print("Toda lacuna preenchida")

        print("aumenta a inteligÃƒÂªncia")

        print("da IOTEC.")

        print()

        print("Conhecer melhor")

        print("ÃƒÂ© vender melhor.")

        print()

        print("="*70)

        print("KNOWLEDGE GAP ENGINE ONLINE")

        print("="*70)


# ==========================================================

if __name__ == "__main__":

    KnowledgeGapEngine().executar()



