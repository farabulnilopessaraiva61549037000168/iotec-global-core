"""
======================================================================
IOTEC

027_CONVERGENCE_ENGINE.py

CONVERGENCE ENGINE

VERSÃƒÆ'O 1.0

======================================================================
"""

import os
from pathlib import Path
from collections import defaultdict

PASTA = r"C:\IOTEC"

# ===============================================================

PALAVRAS = {

    "COMERCIAL":"COMERCIAL",

    "CLIENTE":"COMERCIAL",

    "VENDA":"COMERCIAL",

    "CRM":"CRM",

    "CONTRATO":"JURÃƒÂDICO",

    "JURIDICO":"JURÃƒÂDICO",

    "FINANCEIRO":"FINANCEIRO",

    "RECEITA":"FINANCEIRO",

    "KERNEL":"KERNEL",

    "MISSION":"MISSÃƒâ€¢ES",

    "MISSAO":"MISSÃƒâ€¢ES",

    "MISSÃƒÆ'O":"MISSÃƒâ€¢ES",

    "PRODUTO":"PRODUTOS",

    "CATALOGO":"PRODUTOS",

    "CATÃƒÂLOGO":"PRODUTOS",

    "LOGISTICA":"LOGÃƒÂSTICA",

    "LOGÃƒÂSTICA":"LOGÃƒÂSTICA",

    "DASHBOARD":"DASHBOARD",

    "AUDITORIA":"AUDITORIA",

    "INTELIGENCIA":"INTELIGÃƒÅ NCIA",

    "INTELIGÃƒÅ NCIA":"INTELIGÃƒÅ NCIA",

    "AGENTE":"AGENTES"

}

# ===============================================================

class ConvergenceEngine:

    def __init__(self):

        self.modulos=[]

        self.setores=defaultdict(list)

    # ===========================================================

    def executar(self):

        print("="*70)
        print("IOTEC CONVERGENCE ENGINE")
        print("="*70)
        print()

        self.varrer()

        self.resumo()

    # ===========================================================

    def varrer(self):

        contador=0

        for raiz,_,arquivos in os.walk(PASTA):

            for arquivo in arquivos:

                if not arquivo.endswith(".py"):
                    continue

                contador+=1

                caminho=os.path.join(raiz,arquivo)

                self.analisar(caminho)

        print("Arquivos analisados:",contador)
        print()

    # ===========================================================

    def analisar(self,caminho):

        try:

            texto=Path(caminho).read_text(
                encoding="utf-8",
                errors="ignore"
            ).upper()

        except:

            return

        categorias=[]

        for palavra,categoria in PALAVRAS.items():

            if palavra in texto:

                categorias.append(categoria)

        if not categorias:

            categorias.append("GERAL")

        categorias=list(set(categorias))

        self.modulos.append({

            "arquivo":os.path.basename(caminho),

            "categorias":categorias,

            "linhas":len(texto.splitlines())

        })

        for c in categorias:

            self.setores[c].append(

                os.path.basename(caminho)

            )

    # ===========================================================

    def resumo(self):

        print("="*70)
        print("CENTRAIS DA IOTEC")
        print("="*70)
        print()

        for setor in sorted(self.setores):

            print(f"{setor:<20}{len(self.setores[setor])}")

        print()

        print("="*70)
        print("MÃƒâ€œDULOS MAIS IMPORTANTES")
        print("="*70)
        print()

        for setor in sorted(self.setores):

            print()

            print(setor)

            print("-"*50)

            for arquivo in self.setores[setor][:10]:

                print("Ã¢â‚¬Â¢",arquivo)

        print()

        print("="*70)

        print("ANÃƒÂLISE")

        print("="*70)

        print()

        print("O Kernel identificou que a plataforma")

        print("jÃƒÂ¡ possui nÃƒÂºcleos especializados.")

        print()

        print("PrÃƒÂ³xima missÃƒÂ£o:")

        print()

        print("Descobrir quais mÃƒÂ³dulos")

        print("estÃƒÂ£o completos.")

        print()

        print("Descobrir quais")

        print("podem virar produtos.")

        print()

        print("="*70)

# ===============================================================

if __name__=="__main__":

    sistema=ConvergenceEngine()

    sistema.executar()


