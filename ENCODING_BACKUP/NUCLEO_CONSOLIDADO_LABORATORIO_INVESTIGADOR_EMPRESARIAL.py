import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC AI - INVESTIGADOR EMPRESARIAL
# NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Inteligente de Levantamento de Requisitos
# =========================================================

class InvestigadorEmpresarial:
    pass

    def __init__(self):
        pass

        self.dados_cliente = {}

    # =====================================================
    # INICIAR ATENDIMENTO
    # =====================================================

    def iniciar_atendimento(self):
        pass

        print("\n[IA] OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡! Bem-vindo ao sistema inteligente da IOTEC.")
        print("[IA] Vou analisar sua necessidade para montar a melhor soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.\n")

        self.perguntar_setor()
        self.perguntar_problemas()
        self.perguntar_usuarios()
        self.perguntar_recursos()
        self.perguntar_objetivo()

        self.gerar_diagnostico()

    # =====================================================
    # PERGUNTAR SETOR
    # =====================================================

    def perguntar_setor(self):
        pass

        print("======================================")
        print("SETOR DA EMPRESA")
        print("======================================")

        setor = input(
            "\n[IA] Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o setor da sua empresa?\n"
            "1 - EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o\n"
            "2 - ComÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rcio\n"
            "3 - SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde\n"
            "4 - JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico\n"
            "5 - Tecnologia\n"
            "6 - Outro\n\n"
            "Digite: "
        )

        setores = {
            "1": "EducaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
            "2": "ComÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rcio",
            "3": "SaÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºde",
            "4": "JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico",
            "5": "Tecnologia",
            "6": "Outro"
        }

        self.dados_cliente["setor"] = setores.get(setor, "NÃƒÆ'Ã†â€™o informado")

    # =====================================================
    # PERGUNTAR PROBLEMAS
    # =====================================================

    def perguntar_problemas(self):
        pass

        print("\n======================================")
        print("PROBLEMAS ENFRENTADOS")
        print("======================================")

        problemas = input(
            "\n[IA] Quais problemas sua empresa enfrenta atualmente?\n\n"
            "Exemplos:\n"
            "- Falta de organizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o\n"
            "- Processos manuais\n"
            "- Controle financeiro\n"
            "- LentidÃƒÆ'Ã†â€™o operacional\n"
            "- Falta de automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o\n\n"
            "Resposta: "
        )

        self.dados_cliente["problemas"] = problemas

    # =====================================================
    # PERGUNTAR USUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIOS
    # =====================================================

    def perguntar_usuarios(self):
        pass

        print("\n======================================")
        print("USUÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIOS")
        print("======================================")

        usuarios = input(
            "\n[IA] Quantas pessoas utilizarÃƒÆ'Ã†â€™o o sistema?\n\n"
            "Resposta: "
        )

        self.dados_cliente["usuarios"] = usuarios

    # =====================================================
    # PERGUNTAR RECURSOS
    # =====================================================

    def perguntar_recursos(self):
        pass

        print("\n======================================")
        print("FUNCIONALIDADES")
        print("======================================")

        recursos = input(
            "\n[IA] Quais funcionalidades deseja?\n\n"
            "Exemplos:\n"
            "- Painel administrativo\n"
            "- Controle financeiro\n"
            "- Aplicativo\n"
            "- Dashboard\n"
            "- AutomaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o\n"
            "- API\n"
            "- WhatsApp\n\n"
            "Resposta: "
        )

        self.dados_cliente["recursos"] = recursos

    # =====================================================
    # PERGUNTAR OBJETIVO
    # =====================================================

    def perguntar_objetivo(self):
        pass

        print("\n======================================")
        print("OBJETIVO PRINCIPAL")
        print("======================================")

        objetivo = input(
            "\n[IA] Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o principal objetivo do sistema?\n\n"
            "Exemplos:\n"
            "- Automatizar processos\n"
            "- Melhorar gestÃƒÆ'Ã†â€™o\n"
            "- Reduzir custos\n"
            "- Organizar operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes\n"
            "- Melhorar produtividade\n\n"
            "Resposta: "
        )

        self.dados_cliente["objetivo"] = objetivo

    # =====================================================
    # GERAR DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO
    # =====================================================

    def gerar_diagnostico(self):
        pass

        print("\n======================================")
        print("DIAGNÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œSTICO INTELIGENTE")
        print("======================================")

        print("\n[IA] Analisando informaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes do cliente...\n")

        for chave, valor in self.dados_cliente.items():
            pass

            print(f"{chave.upper()} -> {valor}")

        print("\n======================================")

        print("[IA] DiagnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³stico inicial concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")
        print("[IA] Preparando escopo tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico...")
        print("[IA] Encaminhando solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ao nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo operacional...")
        print("[IA] Sistema interno iniciarÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")

# =========================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# =========================================================

ia = InvestigadorEmpresarial()

ia.iniciar_atendimento()


