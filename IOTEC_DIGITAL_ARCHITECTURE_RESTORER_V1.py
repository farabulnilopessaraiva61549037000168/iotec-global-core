import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===============================================================
# IOTEC DIGITAL ARCHITECTURE RESTORER V1.0
#
# Agente de reconstruÃƒÂ§ÃƒÂ£o da arquitetura IoTec
#
# Objetivo:
# Encontrar conexÃƒÂµes reais entre arquivos existentes.
#
# NÃƒÂ£o cria dados.
# Apenas analisa a estrutura encontrada.
#
# ===============================================================

from pathlib import Path
from datetime import datetime


class ArchitectureRestorer:


    def __init__(self, pasta):

        self.pasta = Path(pasta)

        self.arquivos = []

        self.conexoes = []

        self.palavras_chave = [

            "paypal",
            "picpay",
            "payment",
            "pagamento",
            "checkout",
            "form",
            "email",
            "whatsapp",
            "api",
            "render",
            "netlify",
            "database",
            "json"

        ]


    def coletar_arquivos(self):

        extensoes = [
            ".py",
            ".html",
            ".js",
            ".json"
        ]


        for arquivo in self.pasta.rglob("*"):

            if arquivo.is_file():

                if arquivo.suffix.lower() in extensoes:

                    self.arquivos.append(arquivo)



    def analisar_conexoes(self):


        for arquivo in self.arquivos:

            try:

                texto = arquivo.read_text(
                    encoding="utf-8",
                    errors="ignore"
                ).lower()


                encontrados = []


                for palavra in self.palavras_chave:

                    if palavra in texto:

                        encontrados.append(
                            palavra
                        )


                if encontrados:

                    self.conexoes.append({

                        "arquivo": str(arquivo),

                        "elementos": encontrados

                    })


            except Exception:

                pass



    def gerar_relatorio(self):


        print("\n")
        print("="*75)
        print(" IOTEC DIGITAL ARCHITECTURE RESTORER V1.0 ")
        print("="*75)


        print("\nDATA:")
        print(datetime.now())


        print("\nARQUIVOS ANALISADOS:")

        print(
            len(self.arquivos)
        )


        print("\nCONEXÃƒâ€¢ES ENCONTRADAS:")

        print(
            len(self.conexoes)
        )


        print("\nMAPA DE CONEXÃƒâ€¢ES\n")


        for item in self.conexoes[:100]:

            print("-"*60)

            print(
                "ARQUIVO:"
            )

            print(
                item["arquivo"]
            )


            print(
                "ELEMENTOS:"
            )

            print(
                ", ".join(item["elementos"])
            )


        if len(self.conexoes) > 100:

            print(
                "\n...",
                len(self.conexoes),
                "conexÃƒÂµes encontradas"
            )



    def salvar_mapa(self):

        arquivo_saida = Path(
            "IOTEC_MAPA_CONEXOES.txt"
        )


        with open(
            arquivo_saida,
            "w",
            encoding="utf-8"
        ) as f:


            f.write(
                "IOTEC MAPA DE CONEXÃƒâ€¢ES\n"
            )

            f.write(
                str(datetime.now())
            )


            for item in self.conexoes:

                f.write("\n\n")

                f.write(
                    item["arquivo"]
                )

                f.write("\n")

                f.write(
                    ",".join(item["elementos"])
                )


        print(
            "\nMapa salvo:",
            arquivo_saida
        )



# ===============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ===============================================================


if __name__ == "__main__":


    sistema = ArchitectureRestorer(
        r"C:\IOTEC"
    )


    sistema.coletar_arquivos()

    sistema.analisar_conexoes()

    sistema.gerar_relatorio()

    sistema.salvar_mapa()



