import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# DESCOBERTA DE CAPACIDADES
# ============================================================

    def search_components(self):

        self.log("Analisando missÃƒÂ£o...")

        mission = (
            str(self.context.get("mission","")) + " " +
            str(self.context.get("objective",""))
        ).lower()

        categories = {

            "LANDING":[
                "landing",
                "index",
                "home",
                "netlify",
                "portal"
            ],

            "FORM":[
                "form",
                "lead",
                "cadastro"
            ],

            "PAYMENT":[
                "payment",
                "paypal",
                "pagamento",
                "checkout",
                "picpay"
            ],

            "DATABASE":[
                "database",
                "db",
                "sqlite",
                "banco"
            ],

            "EMAIL":[
                "email",
                "mail"
            ],

            "WHATSAPP":[
                "whatsapp"
            ],

            "API":[
                "api",
                "gateway"
            ]

        }

        self.context["components"]={}

        for category,words in categories.items():

            found=[]

            for module,path in self.modules.items():

                name=module.lower()

                for word in words:

                    if word in name:

                        found.append(path)

                        break

            self.context["components"][category]=found

        self.log("Capacidades identificadas.")

# ============================================================

    def choose_official_components(self):

        self.log("Escolhendo componentes oficiais...")

        self.context["official"]={}

        for category,files in self.context["components"].items():

            if len(files)==0:

                self.context["official"][category]=None

                continue

            files=sorted(files,key=len)

            official=files[0]

            self.context["official"][category]=official

            self.log(

                f"{category} -> {Path(official).name}"

            )

# ============================================================

    def executive_report(self):

        print()

        print("="*70)

        print("RELATÃƒâ€œRIO EXECUTIVO")

        print("="*70)

        print()

        print("MISSÃƒÆ'O")

        print(self.context["mission"])

        print()

        print("COMPONENTES OFICIAIS")

        print()

        for category,path in self.context["official"].items():

            print(category)

            if path:

                print("OK")

                print(Path(path).name)

            else:

                print("NÃƒÆ'O ENCONTRADO")

            print()

# ============================================================

    def mission_ready(self):

        required=[

            "LANDING",

            "FORM",

            "PAYMENT",

            "DATABASE"

        ]

        missing=[]

        for item in required:

            if self.context["official"].get(item) is None:

                missing.append(item)

        print()

        print("="*70)

        print("ANÃƒÂLISE DA MISSÃƒÆ'O")

        print("="*70)

        print()

        if len(missing)==0:

            print("STATUS")

            print("MISSÃƒÆ'O PODE SER EXECUTADA")

            print()

            print("Fluxo mÃƒÂ­nimo localizado.")

        else:

            print("STATUS")

            print("MISSÃƒÆ'O INCOMPLETA")

            print()

            print("Faltando")

            for x in missing:

                print("-",x)

# ============================================================

    def run(self):

        self.discover_modules()

        self.build_context()

        self.search_components()

        self.choose_official_components()

        self.executive_report()

        self.mission_ready()

# ============================================================

if __name__=="__main__":

    print()

    print("="*70)

    print("IOTEC SPEC INTERPRETER")

    print("="*70)

    print()

    engine=SpecInterpreter()

    engine.run()



