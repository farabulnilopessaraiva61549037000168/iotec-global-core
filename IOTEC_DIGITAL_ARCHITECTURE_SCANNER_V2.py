import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
from datetime import datetime


class ArchitectureScanner:


    def __init__(self, pasta):

        self.pasta = Path(pasta)

        self.resultado = {
            "python": [],
            "html": [],
            "javascript": [],
            "json": [],
            "env": [],
            "pagamento": [],
            "formularios": []
        }


    def analisar(self):

        for arquivo in self.pasta.rglob("*"):

            if arquivo.is_file():

                nome = arquivo.name.lower()

                caminho = str(arquivo)


                if nome.endswith(".py"):
                    self.resultado["python"].append(caminho)


                elif nome.endswith(".html"):
                    self.resultado["html"].append(caminho)


                elif nome.endswith(".js"):
                    self.resultado["javascript"].append(caminho)


                elif nome.endswith(".json"):
                    self.resultado["json"].append(caminho)


                elif nome.endswith(".env"):
                    self.resultado["env"].append(caminho)


                if any(
                    palavra in nome
                    for palavra in [
                        "pay",
                        "paypal",
                        "picpay",
                        "pagamento",
                        "checkout"
                    ]
                ):
                    self.resultado["pagamento"].append(caminho)


                if "form" in nome:
                    self.resultado["formularios"].append(caminho)



    def relatorio(self):

        print("\n")
        print("="*70)
        print(" IOTEC DIGITAL ARCHITECTURE SCANNER V2 ")
        print("="*70)

        print("\nDATA:")
        print(datetime.now())


        for categoria, arquivos in self.resultado.items():

            print("\n")
            print(categoria.upper())
            print("-"*50)

            if arquivos:

                for item in arquivos[:20]:
                    print(item)

                if len(arquivos) > 20:
                    print(
                        "...",
                        len(arquivos),
                        "arquivos encontrados"
                    )

            else:

                print("Nenhum encontrado")


        print("\n")
        print("DIAGNÃƒâ€œSTICO")

        print(
            "Python encontrados:",
            len(self.resultado["python"])
        )

        print(
            "Interfaces HTML:",
            len(self.resultado["html"])
        )

        print(
            "FormulÃƒÂ¡rios candidatos:",
            len(self.resultado["formularios"])
        )

        print(
            "Arquivos pagamento:",
            len(self.resultado["pagamento"])
        )



if __name__ == "__main__":


    scanner = ArchitectureScanner(
        r"C:\IOTEC"
    )


    scanner.analisar()

    scanner.relatorio()



