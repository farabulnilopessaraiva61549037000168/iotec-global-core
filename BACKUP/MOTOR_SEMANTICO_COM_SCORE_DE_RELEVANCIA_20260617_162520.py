import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================

# IOTEC AI v6

# MOTOR SEMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡NTICO COM SCORE DE RELEVÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡NCIA

# =========================================================

# OBJETIVO:

# Corrigir falsos positivos semÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢nticos

# usando pontuaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o contextual inteligente.

# =========================================================



import time

from collections import defaultdict



# =========================================================

# BASE SEMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡NTICA

# =========================================================



BASE_SEMANTICA = {



    "energia": [

        "petroleo",

        "gas",

        "petroquimica",

        "combustivel",

        "energia",

        "refinaria",

        "oleo",

        "etanol"

    ],



    "industrial": [

        "industria",

        "industrial",

        "mineracao",

        "mineraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o",

        "fabrica",

        "producao",

        "manufatura",

        "metalurgia",

        "quimica"

    ],



    "tecnologia": [

        "dados",

        "software",

        "sistema",

        "api",

        "cloud",

        "programacao",

        "informatica",

        "inteligencia",

        "automacao"

    ],



    "financeiro": [

        "financeiro",

        "fiscal",

        "pagamento",

        "faturamento",

        "caixa",

        "credito",

        "custos"

    ],



    "logistica": [

        "logistica",

        "entrega",

        "transporte",

        "frota",

        "pedido",

        "distribuicao"

    ],



    "saude": [

        "hospital",

        "clinica",

        "laboratorio",

        "farmaceutica",

        "medicina",

        "bioquimica"

    ],



    "educacao": [

        "escola",

        "professor",

        "aluno",

        "curso",

        "universidade",

        "faculdade"

    ]

}



# =========================================================

# RECOMENDAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

# =========================================================



RECOMENDACOES = {



    "industrial": [

        "Controle operacional",

        "Monitoramento industrial",

        "AutomaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o produtiva"

    ],



    "tecnologia": [

        "Dashboard analÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­tico",

        "Infraestrutura cloud",

        "API inteligente",

        "AutomaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de processos"

    ],



    "financeiro": [

        "Fluxo de caixa",

        "Controle financeiro",

        "RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rios fiscais"

    ],



    "logistica": [

        "Rastreamento logÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­stico",

        "Controle de entregas",

        "GestÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de pedidos"

    ],



    "energia": [

        "Painel energÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©tico",

        "Monitoramento de ativos",

        "Auditoria operacional"

    ],



    "saude": [

        "ProntuÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio digital",

        "Painel clÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­nico",

        "Controle laboratorial"

    ],



    "educacao": [

        "Painel acadÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âªmico",

        "Controle de alunos",

        "DiÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡rio eletrÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â´nico"

    ]

}



# =========================================================

# IA PRINCIPAL

# =========================================================



class MotorSemantico:
    pass



    def __init__(self):
        pass



        self.memoria = {}



    # =====================================================

    # EFEITO IA

    # =====================================================



    def pensar(self, texto):
        pass



        print(f"\n[IA] {texto}")



        time.sleep(1)



    # =====================================================

    # TOKENIZAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

    # =====================================================



    def tokenizar(self, texto):
        pass



        texto = texto.lower()



        texto = texto.replace(",", " ")

        texto = texto.replace(".", " ")

        texto = texto.replace("-", " ")



        return texto.split()



    # =====================================================

    # MOTOR SEMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡NTICO COM SCORE

    # =====================================================



    def detectar_categorias(self, texto):
        pass



        tokens = self.tokenizar(texto)



        scores = defaultdict(int)



        # -------------------------------------------------

        # COMPARAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O INTELIGENTE

        # -------------------------------------------------



        for token in tokens:
            pass



            for categoria, palavras in BASE_SEMANTICA.items():
                pass



                for palavra in palavras:
                    pass



                    # -------------------------------------

                    # MATCH EXATO

                    # -------------------------------------



                    if token == palavra:
                        pass



                        scores[categoria] += 3



                    # -------------------------------------

                    # MATCH PARCIAL

                    # -------------------------------------



                    elif (

                        token in palavra or

                        palavra in token

                    ):



                        # evita matches muito pequenos

                        if len(token) >= 5:
                            pass



                            scores[categoria] += 1



        # -------------------------------------------------

        # FILTRAR RESULTADOS RELEVANTES

        # -------------------------------------------------



        categorias_detectadas = []



        for categoria, score in scores.items():
            pass



            if score >= 2:
                pass



                categorias_detectadas.append(

                    (categoria, score)

                )



        # -------------------------------------------------

        # ORDENAR POR SCORE

        # -------------------------------------------------



        categorias_detectadas.sort(

            key=lambda x: x[1],

            reverse=True

        )



        return categorias_detectadas



    # =====================================================

    # GERAR RECOMENDAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

    # =====================================================



    def gerar_recomendacoes(self, categorias):
        pass



        recomendacoes = []



        for categoria, score in categorias:
            pass



            if categoria in RECOMENDACOES:
                pass



                recomendacoes.extend(

                    RECOMENDACOES[categoria]

                )



        return list(set(recomendacoes))



    # =====================================================

    # INVESTIGAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

    # =====================================================



    def investigar(self):
        pass



        print("\n====================================================")

        print("        IOTEC AI - MOTOR SEMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡NTICO v6")

        print("====================================================")



        descricao = input(

            "\n[IA] Descreva sua empresa e seus problemas:\n\n>>> "

        )



        self.memoria["descricao"] = descricao



        self.pensar("Processando linguagem natural...")

        self.pensar("Executando anÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡lise semÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ntica...")

        self.pensar("Calculando relevÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ncia contextual...")



        categorias = self.detectar_categorias(descricao)



        self.memoria["categorias"] = categorias



        recomendacoes = self.gerar_recomendacoes(categorias)



        self.memoria["recomendacoes"] = recomendacoes



        # -------------------------------------------------

        # EXIBIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

        # -------------------------------------------------



        print("\n====================================================")

        print("           CATEGORIAS DETECTADAS")

        print("====================================================")



        if categorias:
            pass



            for categoria, score in categorias:
                pass



                print(f"\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¦ {categoria.upper()}")

                print(f"Score semÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¢ntico: {score}")



        else:
            pass



            print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  Nenhuma categoria relevante detectada.")



        print("\n====================================================")

        print("      FUNCIONALIDADES RECOMENDADAS")

        print("====================================================")



        if recomendacoes:
            pass



            for item in recomendacoes:
                pass



                print(f"\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â°ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¸ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¹ {item}")



        else:
            pass



            print("\nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã¢â‚¬Â¦Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã¢â‚¬Å¡  Nenhuma recomendaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o disponÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­vel.")



        objetivo = input(

            "\n[IA] Qual ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â© o principal objetivo do sistema?\n\n>>> "

        )



        self.memoria["objetivo"] = objetivo



        self.relatorio_final()



    # =====================================================

    # RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO FINAL

    # =====================================================



    def relatorio_final(self):
        pass



        self.pensar("Gerando diagnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³stico operacional...")

        self.pensar("Calculando arquitetura inteligente...")

        self.pensar("Encaminhando ao nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo produtivo...")



        print("\n====================================================")

        print("              RELATÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"RIO FINAL")

        print("====================================================")



        print(f"\nDESCRIÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O:\n{self.memoria['descricao']}")



        print("\nCATEGORIAS:")



        for categoria, score in self.memoria["categorias"]:
            pass



            print(f" - {categoria} (score: {score})")



        print("\nRECOMENDAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES:")



        for item in self.memoria["recomendacoes"]:
            pass



            print(f" - {item}")



        print(f"\nOBJETIVO:\n{self.memoria['objetivo']}")



        print("\n====================================================")



        print("[IA] DiagnÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³stico concluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­do.")

        print("[IA] Escopo tÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnico preparado.")

        print("[IA] Ordem operacional liberada.")

        print("[IA] Sistema interno iniciarÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ produÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o.")



# =========================================================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# =========================================================



if __name__ == "__main__":
    pass



    sistema = MotorSemantico()



    sistema.investigar()




