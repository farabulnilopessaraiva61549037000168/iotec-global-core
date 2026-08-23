import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================

IOTEC EVENT BUS

Barramento Central de Eventos

======================================================

Todos os mÃ³dulos conversam por aqui.

======================================================
"""

from datetime import datetime


class EventBus:


    def __init__(self):

        self.events=[]


    def publish(

        self,

        origem,

        categoria,

        titulo,

        descricao,

        prioridade="MEDIA"

    ):

        evento={

            "id":len(self.events)+1,

            "timestamp":datetime.now(),

            "origem":origem,

            "categoria":categoria,

            "titulo":titulo,

            "descricao":descricao,

            "prioridade":prioridade

        }

        self.events.append(evento)

        return evento


    def total(self):

        return len(self.events)


    def latest(self,n=5):

        return self.events[-n:]


    def critical(self):

        return [

            e

            for e in self.events

            if e["prioridade"]=="CRITICA"

        ]


    def show(self):

        print()

        print("="*70)

        print("EVENT BUS")

        print("="*70)

        print()

        print(f"Eventos registrados : {len(self.events)}")

        print()

        for e in self.events:

            print(

                f"[{e['categoria']}] "

                f"{e['titulo']}"

            )

        print()



if __name__=="__main__":

    bus=EventBus()


    bus.publish(

        "COMMERCIAL",

        "PLANTÃƒO",

        "Pipeline abaixo da meta",

        "Pipeline permanece abaixo da meta.",

        "ALTA"

    )


    bus.publish(

        "FINANCEIRO",

        "REPORTAGEM",

        "Receita estÃ¡vel",

        "Nenhum contrato novo.",

        "MEDIA"

    )


    bus.publish(

        "OPERATIONS",

        "STATUS",

        "Servidores Operacionais",

        "Todos os serviÃ§os ativos.",

        "BAIXA"

    )


    bus.show()





