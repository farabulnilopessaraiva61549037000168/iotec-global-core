Clear-Host

Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC EVENT BUS"
Write-Host "==============================================="
Write-Host ""

$arquivo="C:\IOTEC\EVENT_BUS.py"

$codigo=@'
"""
======================================================

IOTEC EVENT BUS

Barramento Central de Eventos

======================================================

Todos os módulos conversam por aqui.

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

        "PLANTÃO",

        "Pipeline abaixo da meta",

        "Pipeline permanece abaixo da meta.",

        "ALTA"

    )


    bus.publish(

        "FINANCEIRO",

        "REPORTAGEM",

        "Receita estável",

        "Nenhum contrato novo.",

        "MEDIA"

    )


    bus.publish(

        "OPERATIONS",

        "STATUS",

        "Servidores Operacionais",

        "Todos os serviços ativos.",

        "BAIXA"

    )


    bus.show()

'@

Set-Content `
-Path $arquivo `
-Value $codigo `
-Encoding UTF8

Write-Host ""

Write-Host "EVENT BUS CRIADO"

Write-Host ""

Write-Host $arquivo

Write-Host ""

Write-Host "Execute:"

Write-Host ""

Write-Host "python EVENT_BUS.py"