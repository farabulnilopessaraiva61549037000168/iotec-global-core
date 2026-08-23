Clear-Host

Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC NEWSROOM ENGINE"
Write-Host "==============================================="
Write-Host ""

$arquivo = "C:\IOTEC\NEWSROOM_ENGINE.py"

$codigo = @'
"""
=============================================================

IOTEC NEWSROOM ENGINE

Central de Redação Executiva

=============================================================

Todo módulo da plataforma envia eventos para este motor.

O motor decide:

• Plantão
• Reportagem
• Alerta
• Comunicado
• Briefing Executivo

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

        print("CENTRAL DE REDAÇÃO IOTEC")

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

        "PLANTÃO",

        "Pipeline abaixo da meta",

        "O núcleo comercial identificou que o volume atual de oportunidades permanece abaixo da meta mensal. Recomenda-se ampliar as campanhas comerciais e intensificar a prospecção.",

        "ALTA"

    )


    newsroom.registrar(

        "FINANCEIRO",

        "REPORTAGEM",

        "Receita permanece estável",

        "Nenhum novo contrato foi registrado nesta atualização. O foco deve permanecer no avanço das negociações em andamento.",

        "MEDIA"

    )


    newsroom.publicar()
'@

Set-Content `
    -Path $arquivo `
    -Value $codigo `
    -Encoding UTF8

Write-Host ""
Write-Host "Arquivo criado:"
Write-Host ""
Write-Host $arquivo
Write-Host ""
Write-Host "Execute:"
Write-Host ""
Write-Host "python NEWSROOM_ENGINE.py"
Write-Host ""