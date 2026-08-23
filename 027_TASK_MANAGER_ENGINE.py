import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC TASK MANAGER ENGINE
FASE 03
ETAPA 004

VersÃƒÂ£o 5.0

======================================================================
"""

from datetime import datetime


class TaskManagerEngine:

    VERSION = "5.0"

    def __init__(self):

        self.tarefas = [

            {
                "id":1,
                "titulo":"Ativar WhatsApp Business",
                "responsavel":"Marketing",
                "prioridade":"CRÃƒÂTICA",
                "status":"PENDENTE",
                "impacto":"ALTO"
            },

            {
                "id":2,
                "titulo":"Publicar Portal Institucional",
                "responsavel":"Marketing",
                "prioridade":"CRÃƒÂTICA",
                "status":"PENDENTE",
                "impacto":"ALTO"
            },

            {
                "id":3,
                "titulo":"Concluir Landing Pages",
                "responsavel":"Marketing",
                "prioridade":"ALTA",
                "status":"PENDENTE",
                "impacto":"ALTO"
            },

            {
                "id":4,
                "titulo":"Cadastrar Produtos",
                "responsavel":"Comercial",
                "prioridade":"ALTA",
                "status":"PENDENTE",
                "impacto":"MÃƒâ€°DIO"
            },

            {
                "id":5,
                "titulo":"Gerar 20 Leads",
                "responsavel":"Comercial",
                "prioridade":"ALTA",
                "status":"PENDENTE",
                "impacto":"ALTO"
            },

            {
                "id":6,
                "titulo":"Enviar 10 Propostas",
                "responsavel":"Comercial",
                "prioridade":"ALTA",
                "status":"PENDENTE",
                "impacto":"ALTO"
            },

            {
                "id":7,
                "titulo":"Fechar Primeiro Contrato",
                "responsavel":"Comercial",
                "prioridade":"MÃƒÂXIMA",
                "status":"PENDENTE",
                "impacto":"MÃƒÂXIMO"
            },

            {
                "id":8,
                "titulo":"Receber Primeiro Pagamento",
                "responsavel":"Financeiro",
                "prioridade":"MÃƒÂXIMA",
                "status":"PENDENTE",
                "impacto":"MÃƒÂXIMO"
            }

        ]

    # --------------------------------------------------------

    def executar(self):

        print()

        print("="*70)
        print("IOTEC TASK MANAGER ENGINE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        print("PAINEL DE TAREFAS")

        print()

        for tarefa in self.tarefas:

            print(f"[{tarefa['id']:02}] {tarefa['titulo']}")
            print(f"     ResponsÃƒÂ¡vel : {tarefa['responsavel']}")
            print(f"     Prioridade  : {tarefa['prioridade']}")
            print(f"     Impacto     : {tarefa['impacto']}")
            print(f"     Status      : {tarefa['status']}")
            print()

        print("="*70)

        total = len(self.tarefas)

        concluidas = len(
            [t for t in self.tarefas if t["status"] == "CONCLUÃƒÂDA"]
        )

        pendentes = total - concluidas

        print("RESUMO")

        print()

        print(f"Tarefas Totais........ {total}")
        print(f"ConcluÃƒÂ­das........... {concluidas}")
        print(f"Pendentes............ {pendentes}")

        print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Executar primeiro")
        print("as tarefas de maior")
        print("prioridade e impacto")
        print("na geraÃƒÂ§ÃƒÂ£o de receita.")

        print()

        print("="*70)

        print("TASK MANAGER ONLINE")
        print("="*70)


if __name__ == "__main__":

    TaskManagerEngine().executar()



