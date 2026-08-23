import json
from datetime import datetime

# ==========================================================
# IOTEC STRATEGIC KNOWLEDGE CENTER
# ==========================================================

class KnowledgeCenter:

    def __init__(self):

        self.libraries = [

            {
                "name": "Scientific Library",
                "mission": "Pesquisar literatura cientÃƒÂ­fica.",
                "status": "ONLINE"
            },

            {
                "name": "Market Intelligence Library",
                "mission": "Pesquisar mercados e concorrÃƒÂªncia.",
                "status": "ONLINE"
            },

            {
                "name": "Economics Observatory",
                "mission": "Acompanhar indicadores econÃƒÂ´micos.",
                "status": "ONLINE"
            },

            {
                "name": "Technology Observatory",
                "mission": "Monitorar tecnologias emergentes.",
                "status": "ONLINE"
            },

            {
                "name": "Geoeconomic Observatory",
                "mission": "Observar movimentos geoeconÃƒÂ´micos.",
                "status": "ONLINE"
            },

            {
                "name": "Future Scenario Laboratory",
                "mission": "Construir cenÃƒÂ¡rios prospectivos.",
                "status": "ONLINE"
            },

            {
                "name": "Product Innovation Laboratory",
                "mission": "Criar novos produtos digitais.",
                "status": "ONLINE"
            }

        ]

    def save(self):

        with open(
            "IOTEC_STRATEGIC_KNOWLEDGE_CENTER.json",
            "w",
            encoding="utf-8"
        ) as arquivo:

            json.dump(
                self.libraries,
                arquivo,
                indent=4,
                ensure_ascii=False
            )

    def show(self):

        print("=" * 90)
        print("IOTEC STRATEGIC KNOWLEDGE CENTER")
        print("=" * 90)
        print()

        print("BIBLIOTECAS")
        print("-" * 90)

        for biblioteca in self.libraries:

            print()

            print("Nome.....:", biblioteca["name"])
            print("MissÃƒÂ£o...:", biblioteca["mission"])
            print("Status...:", biblioteca["status"])

        print()

        print("=" * 90)
        print("MISSÃƒÆ'O")
        print("=" * 90)

        print()

        print("Transformar conhecimento")
        print("cientÃƒÂ­fico")
        print("em capacidades.")

        print()

        print("Transformar capacidades")
        print("em produtos.")

        print()

        print("Transformar produtos")
        print("em receita.")

        print()

        print("=" * 90)
        print("CHEFE DE GABINETE")
        print("=" * 90)

        print()

        print("Bom dia, Presidente.")
        print()

        print("O Centro EstratÃƒÂ©gico")
        print("estÃƒÂ¡ estudando")
        print("continuamente")

        print("Ã¢â‚¬Â¢ literatura cientÃƒÂ­fica")
        print("Ã¢â‚¬Â¢ economia")
        print("Ã¢â‚¬Â¢ tecnologia")
        print("Ã¢â‚¬Â¢ mercados")
        print("Ã¢â‚¬Â¢ inovaÃƒÂ§ÃƒÂ£o")
        print("Ã¢â‚¬Â¢ cenÃƒÂ¡rios")
        print("Ã¢â‚¬Â¢ novos produtos")

        print()

        print("Toda descoberta")
        print("passarÃƒÂ¡ a alimentar")
        print("o Kernel.")

        print()

        print("=" * 90)
        print("STATUS")
        print("=" * 90)

        print()

        print("Bibliotecas........", len(self.libraries))
        print("Data................", datetime.now())

        print()

        print("STRATEGIC KNOWLEDGE CENTER OPERACIONAL.")


def main():

    centro = KnowledgeCenter()

    centro.save()

    centro.show()


if __name__ == "__main__":
    main()

