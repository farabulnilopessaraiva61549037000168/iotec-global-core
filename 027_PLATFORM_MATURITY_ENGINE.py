# ==============================================================================
# IOTEC
# 027_PLATFORM_MATURITY_ENGINE.py
# Ãndice de Maturidade da Plataforma
# ==============================================================================

import os
from dataclasses import dataclass

# ==============================================================================

@dataclass
class Capability:

    nome: str

    engine=False
    database=False
    config=False
    api=False
    dashboard=False
    auditor=False
    monitor=False
    testes=False
    docs=False
    eventos=False

    maturidade=0
    nivel=""

# ==============================================================================

class PlatformMaturityEngine:

    def __init__(self,pasta="."):

        self.pasta=pasta

        self.capacidades={}

        self.regras={

            "PAYPAL":[
                "paypal",
                "payment",
                "pagamento"
            ],

            "CRM":[
                "crm",
                "lead",
                "cliente"
            ],

            "EMAIL":[
                "email",
                "gmail",
                "smtp"
            ],

            "WHATSAPP":[
                "whatsapp"
            ],

            "DATABASE":[
                "database",
                "sqlite",
                ".db"
            ],

            "API":[
                "api",
                "flask",
                "fastapi"
            ]

        }

    # -------------------------------------------------------------------------

    def analisar(self):

        arquivos=[]

        for raiz,_,files in os.walk(self.pasta):

            for f in files:

                arquivos.append(f.lower())

        for nome,palavras in self.regras.items():

            cap=Capability(nome)

            relacionados=[]

            for arq in arquivos:

                if any(p in arq for p in palavras):

                    relacionados.append(arq)

            texto="\n".join(relacionados)

            cap.engine="engine" in texto
            cap.database=".db" in texto or "database" in texto
            cap.config="config" in texto or ".json" in texto
            cap.api="api" in texto or "flask" in texto or "fastapi" in texto
            cap.dashboard="dashboard" in texto
            cap.auditor="auditor" in texto or "audit" in texto
            cap.monitor="monitor" in texto
            cap.testes="test" in texto
            cap.docs=".pdf" in texto or ".md" in texto or "manual" in texto
            cap.eventos="event" in texto or "bus" in texto

            score=0

            pesos={

                "engine":20,
                "database":15,
                "config":10,
                "api":10,
                "dashboard":10,
                "auditor":10,
                "monitor":10,
                "testes":5,
                "docs":5,
                "eventos":5

            }

            for item,peso in pesos.items():

                if getattr(cap,item):

                    score+=peso

            cap.maturidade=score

            if score>=90:
                cap.nivel="ENTERPRISE"

            elif score>=70:
                cap.nivel="PRODUÃ‡ÃƒO"

            elif score>=50:
                cap.nivel="FUNCIONAL"

            elif score>=30:
                cap.nivel="DESENVOLVIMENTO"

            else:
                cap.nivel="PROTÃ"TIPO"

            self.capacidades[nome]=cap

    # -------------------------------------------------------------------------

    def imprimir(self):

        print()
        print("="*100)
        print("IOTEC - MATURIDADE DA PLATAFORMA")
        print("="*100)

        total=0

        for cap in self.capacidades.values():

            barra="â-ˆ"*int(cap.maturidade/5)
            barra=barra.ljust(20,"â-'")

            print()

            print(cap.nome)
            print("-"*80)

            print(f"Engine.............. {cap.engine}")
            print(f"Database............ {cap.database}")
            print(f"Config.............. {cap.config}")
            print(f"API................. {cap.api}")
            print(f"Dashboard........... {cap.dashboard}")
            print(f"Auditor............. {cap.auditor}")
            print(f"Monitor............. {cap.monitor}")
            print(f"Testes.............. {cap.testes}")
            print(f"DocumentaÃ§Ã£o........ {cap.docs}")
            print(f"Eventos............. {cap.eventos}")

            print()

            print(f"Maturidade.......... {cap.maturidade}%")
            print(f"NÃ­vel............... {cap.nivel}")

            print(barra)

            total+=cap.maturidade

        geral=round(total/len(self.capacidades),1)

        print()
        print("="*100)
        print(f"MATURIDADE GERAL : {geral}%")

        if geral>=90:
            nivel="ENTERPRISE"

        elif geral>=70:
            nivel="PRODUÃ‡ÃƒO"

        elif geral>=50:
            nivel="FUNCIONAL"

        elif geral>=30:
            nivel="DESENVOLVIMENTO"

        else:
            nivel="PROTÃ"TIPO"

        print(f"NÃVEL DA IOTEC   : {nivel}")
        print("="*100)

# ==============================================================================

if __name__=="__main__":

    engine=PlatformMaturityEngine(".")

    engine.analisar()

    engine.imprimir()

