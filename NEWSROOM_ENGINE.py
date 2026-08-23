import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
=============================================================

IOTEC NEWSROOM ENGINE

Central de RedaÃ§Ã£o Executiva

=============================================================

Todo mÃ³dulo da plataforma envia eventos para este motor.

O motor decide:

â€¢ PlantÃ£o
â€¢ Reportagem
â€¢ Alerta
â€¢ Comunicado
â€¢ Briefing Executivo

=============================================================
"""

from datetime import datetime


class NewsRoom:


    def __init__(self):

        self.eventos=[]


    def registrar(

        self,

        origem,

        categoria,

        titulo,

        descricao,

        prioridade="MEDIA"

    ):

        evento={

            "data":datetime.now(),

            "origem":origem,

            "categoria":categoria,

            "titulo":titulo,

            "descricao":descricao,

            "prioridade":prioridade

        }

        self.eventos.append(evento)

        return evento


    def publicar(self):

        print()

        print("="*70)

        print("CENTRAL DE REDAÃ‡ÃƒO IOTEC")

        print("="*70)

        print()

        for e in self.eventos:

            print(f"[{e['categoria']}]")

            print()

            print(e["titulo"])

            print()

            print(e["descricao"])

            print()

            print(f"Origem : {e['origem']}")

            print(f"Prioridade : {e['prioridade']}")

            print("-"*70)





if __name__=="__main__":

    newsroom=NewsRoom()


    newsroom.registrar(

        "COMMERCIAL",

        "PLANTÃƒO",

        "Pipeline abaixo da meta",

        "O nÃºcleo comercial identificou que o volume atual de oportunidades permanece abaixo da meta mensal. Recomenda-se ampliar as campanhas comerciais e intensificar a prospecÃ§Ã£o.",

        "ALTA"

    )


    newsroom.registrar(

        "FINANCEIRO",

        "REPORTAGEM",

        "Receita permanece estÃ¡vel",

        "Nenhum novo contrato foi registrado nesta atualizaÃ§Ã£o. O foco deve permanecer no avanÃ§o das negociaÃ§Ãµes em andamento.",

        "MEDIA"

    )


    newsroom.publicar()




