import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================

IOTEC EDITOR IN CHIEF

Diretoria de RedaÃ§Ã£o

==============================================================

MissÃ£o

Receber eventos produzidos pelos motores
e decidir o que serÃ¡ publicado
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
            print("Nenhum evento para publicaÃ§Ã£o.")
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
            f"Foram publicados {len(self.publicados)} eventos prioritÃ¡rios."
        )

        print()

        print("Editor-Chefe concluiu a revisÃ£o do plantÃ£o.")



if __name__=="__main__":

    editor=EditorInChief()

    editor.receber({

        "origem":"COMMERCIAL",

        "categoria":"PLANTÃƒO",

        "titulo":"Pipeline abaixo da meta",

        "descricao":"O volume atual de oportunidades permanece abaixo da meta mensal.",

        "prioridade":"ALTA"

    })

    editor.receber({

        "origem":"FINANCEIRO",

        "categoria":"REPORTAGEM",

        "titulo":"Receita permanece estÃ¡vel",

        "descricao":"Ainda nÃ£o foram registrados novos contratos nesta atualizaÃ§Ã£o.",

        "prioridade":"MEDIA"

    })

    editor.receber({

        "origem":"COMMERCIAL",

        "categoria":"PLANTÃƒO",

        "titulo":"Pipeline abaixo da meta",

        "descricao":"Evento duplicado para teste.",

        "prioridade":"ALTA"

    })

    editor.boletim()




