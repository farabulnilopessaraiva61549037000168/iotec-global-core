import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===============================================================
# IOTEC DIGITAL SALES PIPELINE TRACE ENGINE V2.0
#
# Mapeador de fluxo interno IoTec
#
# Objetivo:
# Encontrar ligaÃƒÂ§ÃƒÂµes entre:
#
# PÃƒÂ¡gina -> Script -> API -> NÃƒÂºcleo -> Pagamento -> Entrega
#
# ===============================================================


from pathlib import Path
from datetime import datetime
import re


class PipelineTracer:


    def __init__(self, pasta):

        self.pasta = Path(pasta)

        self.arquivos = []

        self.mapa = []

        self.padroes = [

            "form",
            "api",
            "fetch",
            "axios",
            "paypal",
            "picpay",
            "payment",
            "checkout",
            "email",
            "mail",
            "order",
            "pedido",
            "produto",
            "product",
            "delivery",
            "entrega",
            "report"

        ]



    def localizar_arquivos(self):

        for arquivo in self.pasta.rglob("*"):

            if arquivo.is_file():

                if arquivo.suffix.lower() in [

                    ".py",
                    ".html",
                    ".js",
                    ".json"

                ]:

                    self.arquivos.append(arquivo)



    def analisar_arquivo(self, arquivo):

        try:

            texto = arquivo.read_text(
                encoding="utf-8",
                errors="ignore"
            )


        except:

            return



        encontrados = []


        for padrao in self.padroes:


            if re.search(
                padrao,
                texto,
                re.IGNORECASE
            ):

                encontrados.append(padrao)



        referencias = []


        for outro in self.arquivos:


            if outro == arquivo:
                continue


            nome = outro.stem.lower()


            if nome in texto.lower():

                referencias.append(
                    str(outro)
                )



        if encontrados or referencias:


            self.mapa.append({

                "arquivo": str(arquivo),

                "funcoes": encontrados,

                "chamadas": referencias[:10]

            })




    def executar_rastreamento(self):


        for arquivo in self.arquivos:

            self.analisar_arquivo(
                arquivo
            )




    def relatorio(self):


        print("\n")
        print("="*80)
        print(" IOTEC DIGITAL SALES PIPELINE TRACE ENGINE V2.0 ")
        print("="*80)


        print("\nDATA:")
        print(datetime.now())


        print("\nARQUIVOS ANALISADOS:")
        print(
            len(self.arquivos)
        )


        print("\nCONEXÃƒâ€¢ES ENCONTRADAS:")
        print(
            len(self.mapa)
        )


        print("\nMAPA DE FLUXO\n")



        for item in self.mapa[:100]:


            print("-"*70)

            print(
                "ARQUIVO:"
            )

            print(
                item["arquivo"]
            )


            print(
                "FUNÃƒâ€¡Ãƒâ€¢ES:"
            )

            print(
                item["funcoes"]
            )


            if item["chamadas"]:

                print(
                    "POSSÃƒÂVEIS CHAMADAS:"
                )


                for chamada in item["chamadas"]:

                    print(
                        " ->",
                        chamada
                    )



    def salvar(self):


        saida = Path(
            "IOTEC_MAPA_FLUXO_V2.txt"
        )


        with open(
            saida,
            "w",
            encoding="utf-8"
        ) as arquivo:


            arquivo.write(
                "IOTEC DIGITAL SALES PIPELINE MAP\n"
            )

            arquivo.write(
                str(datetime.now())
            )


            for item in self.mapa:


                arquivo.write("\n\n")

                arquivo.write(
                    item["arquivo"]
                )

                arquivo.write("\n")

                arquivo.write(
                    str(item["funcoes"])
                )

                arquivo.write("\n")

                arquivo.write(
                    str(item["chamadas"])
                )



        print("\nMapa salvo:")
        print(saida)




# ===============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ===============================================================


if __name__ == "__main__":


    tracer = PipelineTracer(
        r"C:\IOTEC"
    )


    tracer.localizar_arquivos()

    tracer.executar_rastreamento()

    tracer.relatorio()

    tracer.salvar()



