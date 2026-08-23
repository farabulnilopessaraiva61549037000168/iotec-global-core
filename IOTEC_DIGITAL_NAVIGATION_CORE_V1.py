import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ===============================================================
# IOTEC DIGITAL NAVIGATION CORE V1.0
#
# GPS TÃƒÂ©cnico da Arquitetura IoTec
#
# FunÃƒÂ§ÃƒÂ£o:
# Mapear mÃƒÂ³dulos, identificar travas internas,
# priorizar correÃƒÂ§ÃƒÂµes e orientar evoluÃƒÂ§ÃƒÂ£o.
#
# ===============================================================


from datetime import datetime


class IndicadorTecnico:

    def __init__(
        self,
        area,
        modulo,
        status,
        problema,
        impacto,
        solucao,
        responsavel,
        porta
    ):
        self.area = area
        self.modulo = modulo
        self.status = status
        self.problema = problema
        self.impacto = impacto
        self.solucao = solucao
        self.responsavel = responsavel
        self.porta = porta



class IOTECNavigationCore:


    def __init__(self):

        self.nome = "IOTEC DIGITAL NAVIGATION CORE V1.0"

        self.indicadores = [

            IndicadorTecnico(
                "Infraestrutura",
                "Netlify",
                "VERDE",
                "Hospedagem frontend localizada",
                "Baixo impacto",
                "Manter monitoramento",
                "Agente Infraestrutura",
                "PresenÃƒÂ§a web"
            ),


            IndicadorTecnico(
                "Infraestrutura",
                "Render",
                "AMARELO",
                "Backend precisa validaÃƒÂ§ÃƒÂ£o de conexÃƒÂ£o",
                "Pode impedir processamento",
                "Testar API e comunicaÃƒÂ§ÃƒÂ£o",
                "Agente IntegraÃƒÂ§ÃƒÂ£o",
                "ExecuÃƒÂ§ÃƒÂ£o do nÃƒÂºcleo"
            ),


            IndicadorTecnico(
                "FormulÃƒÂ¡rio",
                "Entrada de cliente",
                "VERMELHO",
                "FormulÃƒÂ¡rio sem confirmaÃƒÂ§ÃƒÂ£o de fluxo",
                "Cliente nÃƒÂ£o consegue iniciar operaÃƒÂ§ÃƒÂ£o",
                "Conectar formulÃƒÂ¡rio ao backend",
                "Agente FormulÃƒÂ¡rio",
                "Entrada comercial"
            ),


            IndicadorTecnico(
                "Pagamento",
                "PayPal/PicPay",
                "VERMELHO",
                "Necessita validaÃƒÂ§ÃƒÂ£o do botÃƒÂ£o e retorno",
                "Bloqueia venda",
                "Criar checkout funcional",
                "Agente Financeiro",
                "Recebimento financeiro"
            ),


            IndicadorTecnico(
                "Produto",
                "Motor AnalÃƒÂ­tico",
                "VERDE",
                "Motores Python existentes",
                "Capacidade de anÃƒÂ¡lise disponÃƒÂ­vel",
                "Integrar ao fluxo comercial",
                "Agente Produto",
                "Entrega tÃƒÂ©cnica"
            ),


            IndicadorTecnico(
                "ComunicaÃƒÂ§ÃƒÂ£o",
                "WhatsApp Business",
                "AMARELO",
                "Existe mas precisa integraÃƒÂ§ÃƒÂ£o",
                "Perde contato automÃƒÂ¡tico",
                "Criar canal operacional",
                "Agente ComunicaÃƒÂ§ÃƒÂ£o",
                "Relacionamento cliente"
            )

        ]



    def calcular_saude(self):

        pontos = 0

        for item in self.indicadores:

            if item.status == "VERDE":
                pontos += 100

            elif item.status == "AMARELO":
                pontos += 50

            else:
                pontos += 0


        return round(
            pontos / len(self.indicadores),
            2
        )



    def mostrar_mapa(self):

        print("\n")
        print("="*75)
        print(" IOTEC DIGITAL NAVIGATION CORE V1.0 ")
        print("="*75)


        print("\nDATA:")
        print(datetime.now())


        print("\nSAÃƒÅ¡DE DA ARQUITETURA:")
        print(
            str(self.calcular_saude()) + "%"
        )


        print("\nMAPA DE INDICADORES\n")


        for i, item in enumerate(self.indicadores,1):

            print("-"*65)

            print(
                f"{i}. {item.area} - {item.modulo}"
            )

            print(
                "STATUS:",
                item.status
            )

            print(
                "PROBLEMA:",
                item.problema
            )

            print(
                "IMPACTO:",
                item.impacto
            )

            print(
                "SOLUÃƒâ€¡ÃƒÆ'O:",
                item.solucao
            )

            print(
                "RESPONSÃƒÂVEL:",
                item.responsavel
            )

            print(
                "PORTA DESTRAVADA:",
                item.porta
            )



    def mostrar_prioridades(self):

        print("\n")
        print("="*75)
        print(" PRIORIDADES DE AÃƒâ€¡ÃƒÆ'O ")
        print("="*75)


        for item in self.indicadores:

            if item.status == "VERMELHO":

                print("\nURGENTE:")
                print(item.modulo)
                print("AÃƒÂ§ÃƒÂ£o:", item.solucao)
                print("ResponsÃƒÂ¡vel:", item.responsavel)



# ===============================================================
# EXECUÃƒâ€¡ÃƒÆ'O
# ===============================================================


if __name__ == "__main__":


    nucleo = IOTECNavigationCore()


    nucleo.mostrar_mapa()


    nucleo.mostrar_prioridades()



