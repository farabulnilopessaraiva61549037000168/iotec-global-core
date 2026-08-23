import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===============================================================
# IOTEC DIGITAL SALES FLOW AUDITOR V1.0
#
# Auditor de fluxo comercial digital
#
# Objetivo:
# Descobrir se existe um caminho completo:
#
# Cliente -> Site -> FormulÃƒÂ¡rio -> NÃƒÂºcleo ->
# Pedido -> Pagamento -> Entrega
#
# NÃƒÂ£o gera dados fictÃƒÂ­cios.
# Analisa a estrutura encontrada.
#
# ===============================================================

from pathlib import Path
from datetime import datetime


class SalesFlowAuditor:


    def __init__(self, pasta):

        self.pasta = Path(pasta)

        self.resultado = {

            "web": [],
            "backend": [],
            "formularios": [],
            "pagamento": [],
            "produto": [],
            "entrega": [],
            "email": []

        }

        self.bloqueios = []



    def procurar_arquivos(self):


        for arquivo in self.pasta.rglob("*"):


            if arquivo.is_file():


                nome = arquivo.name.lower()


                caminho = str(arquivo)


                # WEB

                if any(x in nome for x in
                       ["index", "home", "netlify", "site", "html"]):

                    self.resultado["web"].append(caminho)



                # BACKEND

                if arquivo.suffix == ".py":

                    self.resultado["backend"].append(caminho)



                # FORMULARIOS

                if any(x in nome for x in
                       ["form", "cadastro", "register", "lead"]):

                    self.resultado["formularios"].append(caminho)



                # PAGAMENTO

                if any(x in nome for x in
                       ["paypal", "picpay", "payment",
                        "pagamento", "checkout"]):

                    self.resultado["pagamento"].append(caminho)



                # PRODUTO

                if any(x in nome for x in
                       ["produto", "product",
                        "service", "catalog"]):

                    self.resultado["produto"].append(caminho)



                # ENTREGA

                if any(x in nome for x in
                       ["delivery", "entrega",
                        "report", "pdf"]):

                    self.resultado["entrega"].append(caminho)



                # EMAIL

                if any(x in nome for x in
                       ["email", "mail"]):

                    self.resultado["email"].append(caminho)




    def avaliar_fluxo(self):


        testes = {


            "web":
            "Entrada do cliente",


            "formularios":
            "RecepÃƒÂ§ÃƒÂ£o do pedido",


            "backend":
            "Processamento do nÃƒÂºcleo",


            "pagamento":
            "Recebimento financeiro",


            "produto":
            "DefiniÃƒÂ§ÃƒÂ£o da entrega",


            "entrega":
            "FinalizaÃƒÂ§ÃƒÂ£o do serviÃƒÂ§o",


            "email":
            "ComunicaÃƒÂ§ÃƒÂ£o com cliente"

        }



        for chave, descricao in testes.items():


            if len(self.resultado[chave]) == 0:


                self.bloqueios.append(

                    {
                    "etapa": descricao,
                    "problema":
                    f"Nenhum componente encontrado: {chave}",
                    "aÃƒÂ§ÃƒÂ£o":
                    "Localizar ou criar integraÃƒÂ§ÃƒÂ£o"
                    }

                )




    def gerar_relatorio(self):


        print("\n")
        print("="*75)
        print(" IOTEC DIGITAL SALES FLOW AUDITOR V1.0 ")
        print("="*75)


        print("\nDATA:")
        print(datetime.now())


        print("\nMAPA DO FLUXO\n")


        for etapa, arquivos in self.resultado.items():


            print("-"*60)

            print(etapa.upper())

            print(
                "Encontrados:",
                len(arquivos)
            )


            for arquivo in arquivos[:5]:

                print(
                    arquivo
                )


        print("\n")
        print("="*75)

        print(" BLOQUEIOS IDENTIFICADOS ")

        print("="*75)


        if self.bloqueios:


            for item in self.bloqueios:


                print("\nETAPA:")
                print(item["etapa"])

                print("PROBLEMA:")
                print(item["problema"])

                print("AÃƒâ€¡ÃƒÆ'O:")
                print(item["aÃƒÂ§ÃƒÂ£o"])


        else:

            print(
                "Nenhum bloqueio estrutural encontrado."
            )




    def salvar_relatorio(self):


        arquivo = Path(
            "IOTEC_RELATORIO_BLOQUEIOS_VENDAS.txt"
        )


        with open(
            arquivo,
            "w",
            encoding="utf-8"
        ) as f:


            f.write(
                "IOTEC DIGITAL SALES FLOW AUDITOR\n"
            )

            f.write(
                str(datetime.now())
            )


            f.write("\n\nBLOQUEIOS:\n")


            for item in self.bloqueios:


                f.write("\n")

                f.write(
                    item["etapa"]
                )

                f.write("\n")

                f.write(
                    item["problema"]
                )

                f.write("\n")

                f.write(
                    item["aÃƒÂ§ÃƒÂ£o"]
                )


        print("\nRelatÃƒÂ³rio salvo:")
        print(arquivo)



# ===============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ===============================================================


if __name__ == "__main__":


    auditor = SalesFlowAuditor(
        r"C:\IOTEC"
    )


    auditor.procurar_arquivos()

    auditor.avaliar_fluxo()

    auditor.gerar_relatorio()

    auditor.salvar_relatorio()



