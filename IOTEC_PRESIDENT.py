import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================

IOTEC PRESIDENT

Centro Executivo Digital

==============================================================

O Presidente Digital reÃºne informaÃ§Ãµes dos departamentos
e produz um Ãºnico briefing executivo.

==============================================================
"""

from datetime import datetime


class President:


    def __init__(self):

        self.nome="Farabulini"

        self.departamentos=[]


    def receber(

        self,

        nome,

        status,

        resumo,

        prioridade="MEDIA"

    ):

        self.departamentos.append({

            "nome":nome,

            "status":status,

            "resumo":resumo,

            "prioridade":prioridade

        })


    def abertura(self):

        print()

        print("="*70)

        print("PRESIDÃŠNCIA EXECUTIVA IOTEC")

        print(datetime.now())

        print("="*70)

        print()

        print(f"Boa noite, {self.nome}.")

        print()

        print(

            "Todos os departamentos concluÃ­ram "

            "o Ãºltimo ciclo de monitoramento."

        )

        print()


    def situacao(self):

        print("="*70)

        print("SITUAÃ‡ÃƒO DOS DEPARTAMENTOS")

        print("="*70)

        print()

        for d in self.departamentos:

            print(f"[{d['status']}] {d['nome']}")

        print()


    def briefing(self):

        print("="*70)

        print("BRIEFING EXECUTIVO")

        print("="*70)

        print()

        for d in self.departamentos:

            print(f"{d['nome']}")

            print()

            print(d["resumo"])

            print()

            print("-"*70)

            print()


    def prioridades(self):

        print("="*70)

        print("PRIORIDADES DO DIA")

        print("="*70)

        print()

        criticos=[

            d for d in self.departamentos

            if d["prioridade"] in ("CRITICA","ALTA")

        ]

        if len(criticos)==0:

            print("Nenhuma prioridade crÃ­tica.")

        else:

            for d in criticos:

                print(f"â€¢ {d['nome']}")

        print()


    def encerramento(self):

        print("="*70)

        print("MENSAGEM DO NÃšCLEO EXECUTIVO")

        print("="*70)

        print()

        print(

            "Farabulini, a plataforma permanece "

            "em monitoramento contÃ­nuo."

        )

        print()

        print(

            "Os departamentos continuarÃ£o "

            "analisando oportunidades,"

        )

        print(

            "riscos, contratos, campanhas "

            "e desempenho da empresa."

        )

        print()

        print("PrÃ³ximo briefing: 10 minutos.")

        print()

        print("="*70)



if __name__=="__main__":


    presidente=President()


    presidente.receber(

        "Diretoria Comercial",

        "ATENÃ‡ÃƒO",

        "O pipeline permanece abaixo da meta mensal. "
        "Recomenda-se ampliar campanhas e prospecÃ§Ã£o.",

        "ALTA"

    )


    presidente.receber(

        "Diretoria Financeira",

        "ESTÃVEL",

        "Nenhum contrato foi registrado "
        "desde o Ãºltimo plantÃ£o.",

        "MEDIA"

    )


    presidente.receber(

        "Centro de OperaÃ§Ãµes",

        "ESTÃVEL",

        "Infraestrutura funcionando normalmente.",

        "BAIXA"

    )


    presidente.abertura()

    presidente.situacao()

    presidente.briefing()

    presidente.prioridades()

    presidente.encerramento()





