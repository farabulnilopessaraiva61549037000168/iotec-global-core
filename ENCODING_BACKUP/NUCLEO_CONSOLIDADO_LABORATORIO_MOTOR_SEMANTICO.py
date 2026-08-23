import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC AI v5
# MOTOR SEMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡NTICO EMPRESARIAL NACIONAL
# =========================================================
# Arquitetura:
# - InterpretaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o contextual
# - Similaridade semÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ntica
# - Multi categorias
# - InvestigaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o empresarial
# - RecomendaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o inteligente
# - DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico operacional
# =========================================================

import time

# =========================================================
# BASE ECONÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂMICA NACIONAL
# =========================================================

BASE_SEMANTICA = {

    # -----------------------------------------------------
    # ENERGIA
    # -----------------------------------------------------

    "energia": [
        "petroleo",
        "gas",
        "petroquimica",
        "combustivel",
        "refinaria",
        "oleo",
        "etanol",
        "energia",
        "solar",
        "eolica",
        "hidreletrica"
    ],

    # -----------------------------------------------------
    # INDUSTRIAL
    # -----------------------------------------------------

    "industrial": [
        "industria",
        "fabrica",
        "producao",
        "manufatura",
        "metalurgia",
        "siderurgia",
        "mineracao",
        "agroindustria",
        "quimica",
        "automobilistica"
    ],

    # -----------------------------------------------------
    # AGRONEGÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œCIO
    # -----------------------------------------------------

    "agronegocio": [
        "agro",
        "fazenda",
        "pecuaria",
        "agricultura",
        "graos",
        "gado",
        "frigorifico",
        "plantacao",
        "rural"
    ],

    # -----------------------------------------------------
    # LOGÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂSTICA
    # -----------------------------------------------------

    "logistica": [
        "logistica",
        "transporte",
        "frota",
        "distribuicao",
        "entrega",
        "pedido",
        "armazenamento",
        "porto",
        "carga"
    ],

    # -----------------------------------------------------
    # FINANCEIRO
    # -----------------------------------------------------

    "financeiro": [
        "financeiro",
        "faturamento",
        "banco",
        "credito",
        "pagamento",
        "caixa",
        "custos",
        "contabilidade",
        "fiscal"
    ],

    # -----------------------------------------------------
    # SAÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡DE
    # -----------------------------------------------------

    "saude": [
        "hospital",
        "clinica",
        "bioquimica",
        "farmaceutica",
        "laboratorio",
        "medicina",
        "odontologia",
        "saude"
    ],

    # -----------------------------------------------------
    # EDUCAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # -----------------------------------------------------

    "educacao": [
        "escola",
        "educacao",
        "professor",
        "curso",
        "faculdade",
        "universidade",
        "aluno",
        "pedagogia"
    ],

    # -----------------------------------------------------
    # TECNOLOGIA
    # -----------------------------------------------------

    "tecnologia": [
        "software",
        "programacao",
        "dados",
        "informatica",
        "cloud",
        "api",
        "inteligencia artificial",
        "ti",
        "tecnologia"
    ],

    # -----------------------------------------------------
    # COMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°RCIO
    # -----------------------------------------------------

    "comercio": [
        "loja",
        "mercado",
        "varejo",
        "atacado",
        "ecommerce",
        "vendas",
        "shopping",
        "comercio"
    ],

    # -----------------------------------------------------
    # MODA
    # -----------------------------------------------------

    "moda": [
        "moda",
        "fashion",
        "roupa",
        "vestuario",
        "textil",
        "calcado",
        "boutique"
    ],

    # -----------------------------------------------------
    # JURÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂDICO
    # -----------------------------------------------------

    "juridico": [
        "advocacia",
        "juridico",
        "tribunal",
        "escritorio",
        "processo",
        "audiencia"
    ],

    # -----------------------------------------------------
    # CONSTRUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # -----------------------------------------------------

    "construcao": [
        "engenharia",
        "obra",
        "construcao",
        "arquitetura",
        "empreendimento",
        "imobiliaria"
    ],

    # -----------------------------------------------------
    # TURISMO
    # -----------------------------------------------------

    "turismo": [
        "hotel",
        "turismo",
        "viagem",
        "resort",
        "pousada",
        "turistico"
    ],

    # -----------------------------------------------------
    # ALIMENTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # -----------------------------------------------------

    "alimentacao": [
        "restaurante",
        "lanchonete",
        "alimentacao",
        "cozinha",
        "delivery",
        "food"
    ]
}

# =========================================================
# RECOMENDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES INTELIGENTES
# =========================================================

RECOMENDACOES = {

    "energia": [
        "Monitoramento operacional",
        "Dashboard energÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tico",
        "Controle de ativos",
        "Auditoria energÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica"
    ],

    "industrial": [
        "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o industrial",
        "Controle de produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
        "GestÃƒÆ'Ã†â€™o operacional",
        "Rastreamento interno"
    ],

    "agronegocio": [
        "Controle agrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cola",
        "GestÃƒÆ'Ã†â€™o rural",
        "Monitoramento de produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
        "Painel agroindustrial"
    ],

    "logistica": [
        "Rastreamento logÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stico",
        "GestÃƒÆ'Ã†â€™o de entregas",
        "Controle de frota",
        "Painel de distribuiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"
    ],

    "financeiro": [
        "Fluxo de caixa",
        "Controle financeiro",
        "RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios financeiros",
        "Painel fiscal"
    ],

    "saude": [
        "ProntuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio digital",
        "Painel clÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nico",
        "GestÃƒÆ'Ã†â€™o laboratorial",
        "Auditoria mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dica"
    ],

    "educacao": [
        "DiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio eletrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´nico",
        "Painel acadÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªmico",
        "Controle de alunos",
        "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o escolar"
    ],

    "tecnologia": [
        "Infraestrutura cloud",
        "API inteligente",
        "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de processos",
        "Dashboard analÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico"
    ],

    "comercio": [
        "Sistema de vendas",
        "Controle de estoque",
        "Dashboard comercial",
        "GestÃƒÆ'Ã†â€™o de pedidos"
    ],

    "moda": [
        "CatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo de produtos",
        "Controle de coleÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
        "GestÃƒÆ'Ã†â€™o fashion",
        "Painel de vendas"
    ],

    "juridico": [
        "Controle processual",
        "GestÃƒÆ'Ã†â€™o jurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dica",
        "Painel de processos",
        "AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o documental"
    ],

    "construcao": [
        "GestÃƒÆ'Ã†â€™o de obras",
        "Controle de materiais",
        "Dashboard operacional",
        "Monitoramento de equipes"
    ],

    "turismo": [
        "Sistema de reservas",
        "Painel turÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stico",
        "GestÃƒÆ'Ã†â€™o hoteleira",
        "Controle de hÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³spedes"
    ],

    "alimentacao": [
        "Sistema delivery",
        "Controle de pedidos",
        "GestÃƒÆ'Ã†â€™o de cozinha",
        "Painel operacional"
    ]
}

# =========================================================
# IA PRINCIPAL
# =========================================================

class IOTEC_AI:
    pass

    def __init__(self):
        pass

        self.memoria = {}

    # =====================================================
    # EFEITO VISUAL
    # =====================================================

    def pensar(self, texto):
        pass

        print(f"\n[IA] {texto}")

        time.sleep(1)

    # =====================================================
    # TOKENIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # =====================================================

    def tokenizar(self, texto):
        pass

        texto = texto.lower()

        return texto.split()

    # =====================================================
    # MOTOR SEMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡NTICO
    # =====================================================

    def detectar_categorias(self, texto):
        pass

        tokens = self.tokenizar(texto)

        categorias_detectadas = []

        for categoria, palavras in BASE_SEMANTICA.items():
            pass

            for palavra in palavras:
                pass

                for token in tokens:
                    pass

                    # -------------------------------------
                    # MATCH INTELIGENTE
                    # -------------------------------------

                    if (
                        palavra in token or
                        token in palavra
                    ):

                        categorias_detectadas.append(categoria)

        return list(set(categorias_detectadas))

    # =====================================================
    # GERAR RECOMENDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
    # =====================================================

    def gerar_recomendacoes(self, categorias):
        pass

        recomendacoes = []

        for categoria in categorias:
            pass

            if categoria in RECOMENDACOES:
                pass

                recomendacoes.extend(
                    RECOMENDACOES[categoria]
                )

        return list(set(recomendacoes))

    # =====================================================
    # INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    # =====================================================

    def investigar(self):
        pass

        print("\n====================================================")
        print("           IOTEC AI - CORE ENTERPRISE")
        print("====================================================")

        descricao = input(
            "\n[IA] Descreva sua empresa e os problemas enfrentados:\n\n>>> "
        )

        self.memoria["descricao"] = descricao

        self.pensar("Processando linguagem natural...")
        self.pensar("Mapeando setores econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´micos...")
        self.pensar("Analisando contexto operacional...")
        self.pensar("Detectando padrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes empresariais...")

        categorias = self.detectar_categorias(descricao)

        if not categorias:
            pass

            categorias = ["generico"]

        self.memoria["categorias"] = categorias

        recomendacoes = self.gerar_recomendacoes(categorias)

        self.memoria["recomendacoes"] = recomendacoes

        # -------------------------------------------------
        # EXIBIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
        # -------------------------------------------------

        print("\n====================================================")
        print("             SETORES IDENTIFICADOS")
        print("====================================================")

        for categoria in categorias:
            pass

            print(f"\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ {categoria.upper()}")

        print("\n====================================================")
        print("         FUNCIONALIDADES RECOMENDADAS")
        print("====================================================")

        if recomendacoes:
            pass

            for item in recomendacoes:
                pass

                print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ {item}")

        else:
            pass

            print("\nÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡  Nenhuma recomendaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o encontrada.")

        objetivo = input(
            "\n[IA] Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o principal objetivo do sistema?\n\n>>> "
        )

        self.memoria["objetivo"] = objetivo

        self.gerar_relatorio()

    # =====================================================
    # RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
    # =====================================================

    def gerar_relatorio(self):
        pass

        self.pensar("Gerando diagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gico...")
        self.pensar("Calculando arquitetura operacional...")
        self.pensar("Preparando nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo produtivo...")
        self.pensar("Iniciando orquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o empresarial...")

        print("\n====================================================")
        print("              RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO FINAL")
        print("====================================================")

        for chave, valor in self.memoria.items():
            pass

            print(f"\n{chave.upper()}:")

            if isinstance(valor, list):
                pass

                for item in valor:
                    pass

                    print(f" - {item}")

            else:
                pass

                print(valor)

        print("\n====================================================")

        print("[IA] DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")
        print("[IA] Escopo tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico preparado.")
        print("[IA] Sistema interno iniciarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ a produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")
        print("[IA] NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo operacional ativado.")

# =========================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

if __name__ == "__main__":
    pass

    sistema = IOTEC_AI()

    sistema.investigar()


