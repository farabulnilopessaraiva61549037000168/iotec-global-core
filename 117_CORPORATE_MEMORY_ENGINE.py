import json
import os
from datetime import datetime

OUTPUT_FILE = "IOTEC_CORPORATE_MEMORY.json"

# ==========================================================
# MEMÃƒâ€œRIA CORPORATIVA
# ==========================================================

knowledge = [

    {
        "id":1,
        "area":"Economia",
        "title":"Economia Digital",
        "author":"Economic Research Scientist",
        "summary":"Pesquisa sobre economia digital.",
        "tags":["economia","digital"],
        "status":"CATALOGADO"
    },

    {
        "id":2,
        "area":"Mercado",
        "title":"Posicionamento Competitivo",
        "author":"Market Research Scientist",
        "summary":"EstratÃƒÂ©gias de posicionamento.",
        "tags":["mercado","concorrÃƒÂªncia"],
        "status":"CATALOGADO"
    },

    {
        "id":3,
        "area":"IA",
        "title":"Agentes Inteligentes",
        "author":"Artificial Intelligence Scientist",
        "summary":"Arquiteturas modernas de agentes.",
        "tags":["ia","llm","agentes"],
        "status":"CATALOGADO"
    },

    {
        "id":4,
        "area":"Engenharia",
        "title":"Theory of Constraints",
        "author":"Engineering Scientist",
        "summary":"EliminaÃƒÂ§ÃƒÂ£o de gargalos.",
        "tags":["engenharia","pcp"],
        "status":"CATALOGADO"
    },

    {
        "id":5,
        "area":"Tecnologia",
        "title":"Cloud Computing",
        "author":"Technology Scientist",
        "summary":"Infraestrutura em nuvem.",
        "tags":["cloud","infraestrutura"],
        "status":"CATALOGADO"
    }

]

# ==========================================================

def salvar():

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as arquivo:

        json.dump(
            knowledge,
            arquivo,
            indent=4,
            ensure_ascii=False
        )

# ==========================================================

def mostrar():

    print("="*90)
    print("IOTEC CORPORATE MEMORY ENGINE")
    print("="*90)
    print()

    print("MEMÃƒâ€œRIA CORPORATIVA")
    print("-"*90)

    areas = {}

    for item in knowledge:

        area = item["area"]
        areas[area] = areas.get(area,0)+1

    for area,total in sorted(areas.items()):

        print(f"{area:<25} {total}")

    print()

    print("="*90)
    print("ÃƒÅ¡LTIMOS REGISTROS")
    print("="*90)
    print()

    for item in knowledge:

        print(item["title"])
        print("ÃƒÂrea......:",item["area"])
        print("Autor.....:",item["author"])
        print("Status....:",item["status"])
        print()

    print("="*90)
    print("MISSÃƒÆ'O")
    print("="*90)
    print()

    print("Nenhum conhecimento")
    print("produzido pela IOTEC")
    print("poderÃƒÂ¡ ser perdido.")
    print()

    print("Toda descoberta")
    print("ÃƒÂ© registrada")
    print("classificada")
    print("e incorporada")
    print("ÃƒÂ  memÃƒÂ³ria")
    print("corporativa.")
    print()

    print("="*90)
    print("CHEFE DE GABINETE")
    print("="*90)
    print()

    print("Bom dia, Presidente.")
    print()

    print("Toda pesquisa")
    print("passa agora")
    print("a integrar")
    print("o patrimÃƒÂ´nio")
    print("intelectual")
    print("da IOTEC.")
    print()

    print("O conhecimento")
    print("fica disponÃƒÂ­vel")
    print("para todos")
    print("os motores")
    print("da plataforma.")
    print()

    print("="*90)
    print("STATUS")
    print("="*90)
    print()

    print("Registros...........",len(knowledge))
    print("Data................",datetime.now())
    print()

    print("CORPORATE MEMORY OPERACIONAL.")

# ==========================================================

def main():

    salvar()

    mostrar()

# ==========================================================

if __name__ == "__main__":

    main()

