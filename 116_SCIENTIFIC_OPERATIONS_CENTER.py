import json
from datetime import datetime

# ==========================================================
# IOTEC SCIENTIFIC OPERATIONS CENTER
# ==========================================================

class Scientist:

    def __init__(self, name, area):

        self.name = name
        self.area = area

        self.status = "ONLINE"

        self.current_mission = ""

        self.queue = []

        self.daily_goal = 5

        self.completed = 0

    def add_task(self, task):

        self.queue.append(task)

    def to_dict(self):

        return {

            "name": self.name,

            "area": self.area,

            "status": self.status,

            "current_mission": self.current_mission,

            "daily_goal": self.daily_goal,

            "completed": self.completed,

            "queue": self.queue

        }


scientists = [

    Scientist("Economic Research Scientist","Economia"),

    Scientist("Market Research Scientist","Mercado"),

    Scientist("Data Economy Scientist","Economia dos Dados"),

    Scientist("Artificial Intelligence Scientist","IA"),

    Scientist("Engineering Scientist","Engenharia"),

    Scientist("Commercial Scientist","Comercial"),

    Scientist("Technology Scientist","Tecnologia"),

    Scientist("Innovation Scientist","InovaÃƒÂ§ÃƒÂ£o")

]

# ==========================================================
# MISSÃƒâ€¢ES
# ==========================================================

scientists[0].add_task("Pesquisar Economia Digital")
scientists[0].add_task("Pesquisar Economia dos Dados")
scientists[0].add_task("Pesquisar Plataformas Digitais")

scientists[1].add_task("Pesquisar concorrÃƒÂªncia")
scientists[1].add_task("Pesquisar posicionamento")
scientists[1].add_task("Pesquisar precificaÃƒÂ§ÃƒÂ£o")

scientists[2].add_task("MonetizaÃƒÂ§ÃƒÂ£o de Dados")
scientists[2].add_task("Mercado Global de Dados")

scientists[3].add_task("Novos modelos de IA")
scientists[3].add_task("Agentes Inteligentes")

scientists[4].add_task("Lean Manufacturing")
scientists[4].add_task("Theory of Constraints")

scientists[5].add_task("Funil Comercial")
scientists[5].add_task("ConversÃƒÂ£o")

scientists[6].add_task("Tecnologias Emergentes")
scientists[6].add_task("ComputaÃƒÂ§ÃƒÂ£o em Nuvem")

scientists[7].add_task("Criar novos produtos")
scientists[7].add_task("Melhorar produtos existentes")


# ==========================================================

def save():

    with open(

        "IOTEC_SCIENTIFIC_OPERATIONS.json",

        "w",

        encoding="utf-8"

    ) as f:

        json.dump(

            [s.to_dict() for s in scientists],

            f,

            indent=4,

            ensure_ascii=False

        )


# ==========================================================

print("="*90)
print("IOTEC SCIENTIFIC OPERATIONS CENTER")
print("="*90)
print()

for s in scientists:

    print("-"*90)

    print("Especialista :",s.name)

    print("ÃƒÂrea........ :",s.area)

    print("Status...... :",s.status)

    print("Meta DiÃƒÂ¡ria. :",s.daily_goal)

    print()

    print("Fila de Pesquisa:")

    for tarefa in s.queue:

        print("  Ã¢â‚¬Â¢",tarefa)

    print()

save()

print("="*90)
print("CHEFE DE GABINETE")
print("="*90)
print()

print("Bom dia, Presidente.")
print()

print("O Corpo CientÃƒÂ­fico")
print("passa agora")
print("a trabalhar")
print("por missÃƒÂµes.")
print()

print("Cada especialista")
print("possui metas")
print("fila de pesquisa")
print("e produÃƒÂ§ÃƒÂ£o diÃƒÂ¡ria.")
print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Especialistas :",len(scientists))
print("Data :",datetime.now())

print()

print("SCIENTIFIC OPERATIONS CENTER OPERACIONAL.")

