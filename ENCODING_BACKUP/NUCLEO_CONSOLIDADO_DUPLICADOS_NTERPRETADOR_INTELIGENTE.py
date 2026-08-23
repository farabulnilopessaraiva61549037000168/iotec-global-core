import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC AI - INTERPRETADOR INTELIGENTE
# IA Conversacional Operacional
# =========================================================

class IOTEC_AI:
    pass

    def __init__(self):
        pass

        self.dados = {}

    # =====================================================
    # INICIAR ATENDIMENTO
    # =====================================================

    def iniciar(self):
        pass

        print("\n======================================")
        print("IOTEC AI - ORQUESTRADOR EMPRESARIAL")
        print("======================================")

        mensagem = input(
            "\n[IA] OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡! Descreva o que sua empresa precisa:\n\n>>> "
        )

        self.interpretar_pedido(mensagem)

        self.investigar_problema()

        self.gerar_diagnostico()

    # =====================================================
    # INTERPRETAR PEDIDO
    # =====================================================

    def interpretar_pedido(self, mensagem):
        pass

        texto = mensagem.lower()

        self.dados["pedido_inicial"] = mensagem

        # -------------------------------------------------
        # DETECTAR SETOR
        # -------------------------------------------------

        if (
            "escola" in texto or
            "aluno" in texto or
            "professor" in texto or
            "educaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o" in texto
        ):

            setor = "EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"

        elif (
            "loja" in texto or
            "mercado" in texto or
            "comÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rcio" in texto
        ):

            setor = "ComÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rcio"

        elif (
            "hospital" in texto or
            "clÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nica" in texto or
            "saÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde" in texto
        ):

            setor = "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde"

        elif (
            "advogado" in texto or
            "jurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico" in texto
        ):

            setor = "JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico"

        elif (
            "tecnologia" in texto or
            "software" in texto
        ):

            setor = "Tecnologia"

        else:
            pass

            setor = "NÃƒÆ'Ã†â€™o identificado"

        self.dados["setor"] = setor

        # -------------------------------------------------
        # DETECTAR NECESSIDADE
        # -------------------------------------------------

        if "sistema" in texto:
            pass

            necessidade = "Sistema Empresarial"

        elif "auditoria" in texto:
            pass

            necessidade = "Auditoria"

        elif "dashboard" in texto:
            pass

            necessidade = "Business Intelligence"

        else:
            pass

            necessidade = "ServiÃƒÆ'Ã†â€™o Personalizado"

        self.dados["necessidade"] = necessidade

        print("\n[IA] Pedido interpretado com sucesso.")
        print(f"[IA] Setor identificado: {setor}")
        print(f"[IA] Necessidade detectada: {necessidade}")

    # =====================================================
    # INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INTELIGENTE
    # =====================================================

    def investigar_problema(self):
        pass

        print("\n======================================")
        print("INVESTIGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O EMPRESARIAL")
        print("======================================")

        # -------------------------------------------------
        # CASO NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O IDENTIFIQUE O SETOR
        # -------------------------------------------------

        if self.dados["setor"] == "NÃƒÆ'Ã†â€™o identificado":
            pass

            setor = input(
                "\n[IA] NÃƒÆ'Ã†â€™o consegui identificar o setor da empresa.\n"
                "[IA] Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rea sua empresa atua?\n\n>>> "
            )

            self.dados["setor"] = setor

        # -------------------------------------------------
        # PROBLEMAS
        # -------------------------------------------------

        problemas = input(
            "\n[IA] Quais problemas sua empresa enfrenta atualmente?\n\n>>> "
        )

        self.dados["problemas"] = problemas

        # -------------------------------------------------
        # USUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIOS
        # -------------------------------------------------

        usuarios = input(
            "\n[IA] Quantas pessoas utilizarÃƒÆ'Ã†â€™o o sistema?\n\n>>> "
        )

        self.dados["usuarios"] = usuarios

        # -------------------------------------------------
        # FUNCIONALIDADES
        # -------------------------------------------------

        funcionalidades = input(
            "\n[IA] Quais funcionalidades deseja?\n\n>>> "
        )

        self.dados["funcionalidades"] = funcionalidades

        # -------------------------------------------------
        # OBJETIVO
        # -------------------------------------------------

        objetivo = input(
            "\n[IA] Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o principal objetivo do sistema?\n\n>>> "
        )

        self.dados["objetivo"] = objetivo

    # =====================================================
    # GERAR DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO
    # =====================================================

    def gerar_diagnostico(self):
        pass

        print("\n======================================")
        print("DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO INTELIGENTE")
        print("======================================")

        for chave, valor in self.dados.items():
            pass

            print(f"\n{chave.upper()}:")
            print(valor)

        print("\n======================================")

        print("[IA] AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.")
        print("[IA] Preparando escopo tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico.")
        print("[IA] Encaminhando solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ao nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo operacional.")
        print("[IA] O sistema interno iniciarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ a produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")

# =========================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

ia = IOTEC_AI()

ia.iniciar()


