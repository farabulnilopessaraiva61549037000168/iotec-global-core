Clear-Host

Write-Host ""
Write-Host "==============================================="
Write-Host " IOTEC EDITOR IN CHIEF"
Write-Host " STAGE 001"
Write-Host "==============================================="
Write-Host ""

$arquivo = "C:\IOTEC\EDITOR_IN_CHIEF.py"

$codigo = @'
"""
==============================================================

IOTEC EDITOR IN CHIEF

Diretoria de Redação

==============================================================

Missão

Receber eventos produzidos pelos motores
e decidir o que será publicado
na Torre de Comando.

==============================================================
"""

from datetime import datetime


class EditorInChief:

    def __init__(self):

        self.eventos=[]

        self.publicados=[]


    def receber(self,evento):

        self.eventos.append(evento)


    def ordenar(self):

        ordem={

            "CRITICA":1,

            "ALTA":2,

            "MEDIA":3,

            "BAIXA":4

        }

        self.eventos.sort(

            key=lambda e:ordem.get(
                e.get("prioridade","MEDIA"),99
            )

        )


    def selecionar(self):

        self.ordenar()

        escolhidos=[]

        vistos=set()

        for evento in self.eventos:

            chave=(
                evento.get("categoria",""),
                evento.get("titulo","")
            )

            if chave in vistos:
                continue

            vistos.add(chave)

            escolhidos.append(evento)

        self.publicados=escolhidos


    def boletim(self):

        self.selecionar()

        print()

        print("="*70)
        print("BOLETIM EXECUTIVO IOTEC")
        print(datetime.now())
        print("="*70)

        if len(self.publicados)==0:

            print()
            print("Nenhum evento para publicação.")
            return

        numero=1

        for e in self.publicados:

            print()

            print(f"{numero}. {e['titulo']}")

            print()

            print(e["descricao"])

            print()

            print(f"Origem..... {e['origem']}")

            print(f"Categoria.. {e['categoria']}")

            print(f"Prioridade. {e['prioridade']}")

            print("-"*70)

            numero+=1

        print()

        print("Resumo Editorial")

        print()

        print(
            f"Foram analisados {len(self.eventos)} eventos."
        )

        print(
            f"Foram publicados {len(self.publicados)} eventos prioritários."
        )

        print()

        print("Editor-Chefe concluiu a revisão do plantão.")



if __name__=="__main__":

    editor=EditorInChief()

    editor.receber({

        "origem":"COMMERCIAL",

        "categoria":"PLANTÃO",

        "titulo":"Pipeline abaixo da meta",

        "descricao":"O volume atual de oportunidades permanece abaixo da meta mensal.",

        "prioridade":"ALTA"

    })

    editor.receber({

        "origem":"FINANCEIRO",

        "categoria":"REPORTAGEM",

        "titulo":"Receita permanece estável",

        "descricao":"Ainda não foram registrados novos contratos nesta atualização.",

        "prioridade":"MEDIA"

    })

    editor.receber({

        "origem":"COMMERCIAL",

        "categoria":"PLANTÃO",

        "titulo":"Pipeline abaixo da meta",

        "descricao":"Evento duplicado para teste.",

        "prioridade":"ALTA"

    })

    editor.boletim()
'@

Set-Content `
    -Path $arquivo `
    -Value $codigo `
    -Encoding UTF8

Write-Host ""
Write-Host "==============================================="
Write-Host "EDITOR IN CHIEF CRIADO"
Write-Host "==============================================="
Write-Host ""
Write-Host $arquivo
Write-Host ""
Write-Host "Execute:"
Write-Host ""
Write-Host "python EDITOR_IN_CHIEF.py"
Write-Host ""