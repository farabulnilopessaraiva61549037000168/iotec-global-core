import json
from datetime import datetime


# ==========================================================
# IOTEC SCIENTIFIC WORKFORCE CENTER
# ==========================================================

class DigitalScientist:

    def __init__(self,
                 name,
                 specialty,
                 mission,
                 department):

        self.name = name
        self.specialty = specialty
        self.mission = mission
        self.department = department

        self.status = "ONLINE"

        self.daily_reports = 0
        self.new_ideas = 0
        self.new_products = 0
        self.improvements = 0

    def to_dict(self):

        return {

            "name": self.name,
            "specialty": self.specialty,
            "department": self.department,
            "mission": self.mission,
            "status": self.status,
            "daily_reports": self.daily_reports,
            "new_ideas": self.new_ideas,
            "new_products": self.new_products,
            "improvements": self.improvements

        }


scientists = [

    DigitalScientist(
        "Economic Research Scientist",
        "Economia",
        "Estudar economia mundial e tendÃƒÂªncias.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Market Research Scientist",
        "Mercado",
        "Estudar concorrÃƒÂªncia e posicionamento.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Data Economy Scientist",
        "Economia dos Dados",
        "Pesquisar monetizaÃƒÂ§ÃƒÂ£o de dados.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Artificial Intelligence Scientist",
        "InteligÃƒÂªncia Artificial",
        "Pesquisar novos modelos de IA.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Engineering Scientist",
        "Engenharia",
        "Pesquisar melhorias estruturais.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Technology Observatory Scientist",
        "Tecnologia",
        "Monitorar tecnologias emergentes.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Geoeconomic Scientist",
        "Geoeconomia",
        "Observar movimentos econÃƒÂ´micos globais.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Commercial Scientist",
        "Comercial",
        "Pesquisar tÃƒÂ©cnicas modernas de vendas.",
        "Scientific Council"
    ),

    DigitalScientist(
        "Innovation Scientist",
        "InovaÃƒÂ§ÃƒÂ£o",
        "Criar novos produtos digitais.",
        "Scientific Council"
    )

]


def save():

    with open(
        "IOTEC_SCIENTIFIC_WORKFORCE.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(

            [s.to_dict() for s in scientists],

            f,

            indent=4,

            ensure_ascii=False

        )


def show():

    print("=" * 90)
    print("IOTEC SCIENTIFIC WORKFORCE CENTER")
    print("=" * 90)
    print()

    print("CORPO CIENTÃƒÂFICO DIGITAL")
    print("-" * 90)

    for s in scientists:

        print()
        print("Especialista :", s.name)
        print("ÃƒÂrea........ :", s.specialty)
        print("Departamento :", s.department)
        print("MissÃƒÂ£o...... :", s.mission)
        print("Status.......:", s.status)

    print()
    print("=" * 90)
    print("MISSÃƒÆ'O")
    print("=" * 90)
    print()

    print("Pesquisar continuamente")
    print("novos conhecimentos")
    print("cientÃƒÂ­ficos, econÃƒÂ´micos")
    print("tecnolÃƒÂ³gicos e comerciais.")
    print()

    print("Transformar")
    print("pesquisa")
    print("em")
    print("vantagem competitiva.")
    print()

    print("=" * 90)
    print("CHEFE DE GABINETE")
    print("=" * 90)
    print()

    print("Bom dia, Presidente.")
    print()

    print("O Corpo CientÃƒÂ­fico")
    print("Digital encontra-se")
    print("operacional.")
    print()

    print("Cada pesquisador")
    print("atua exclusivamente")
    print("na sua especialidade,")
    print("alimentando o Kernel")
    print("com conhecimento")
    print("baseado em evidÃƒÂªncias.")
    print()

    print("=" * 90)
    print("STATUS")
    print("=" * 90)
    print()

    print("Especialistas :", len(scientists))
    print("Data..........", datetime.now())
    print()

    print("SCIENTIFIC WORKFORCE OPERACIONAL.")


def main():

    save()

    show()


if __name__ == "__main__":

    main()

