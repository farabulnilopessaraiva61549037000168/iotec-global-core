import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢ CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo de DomÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nio e ApropriaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
# Desenvolvido por FARABULINI LOPES SARAIVA ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ CPF: 011.902.313-01

class SistemaDominio:
    def __init__(self):
        self.proprietario = "FARABULINI LOPES SARAIVA"
        self.cpf = "011.902.313-01"
        self.status = "SISTEMA AUTÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NTICO E SOB DOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIO DO CRIADOR"

    def verificar_dominio(self):
        print("===============================================")
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â VALIDAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE DOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIO E PROPRIEDADE ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â")
        print("===============================================")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  PROPRIETÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO LEGÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTIMO: {self.proprietario}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Âª CPF: {self.cpf}")
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å" STATUS:", self.status)
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Este sistema reconhece e obedece unicamente ao seu criador.")
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Qualquer tentativa de acesso nÃƒÆ'Ã†â€™o autorizado serÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ bloqueada.")
        print("===============================================\n")

    def manifesto_de_propriedade(self):
        manifesto = f"""
        ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â DECLARAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE PROPRIEDADE E DOMÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂNIO ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â

        Este sistema, seus cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digos, algoritmos, rotinas, inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia,
        interfaces e extensÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes reconhecem como ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºnico proprietÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio:

        ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NOME: {self.proprietario}
        ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂªÃƒâ€šÃ‚Âª CPF: {self.cpf}

        Toda operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, ativaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o e controle estÃƒÆ'Ã†â€™o sob domÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nio absoluto
        deste proprietÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio, sendo terminantemente proibido qualquer tipo de uso,
        cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pia, modificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, clonagem, ou exploraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o sem autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o formal e expressa.

        ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å" Protegido por leis de propriedade intelectual e cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo civil nacional
        e internacional.

        ===============================================
        """
        print(manifesto)

# ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o direta do cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo de domÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nio:
if __name__ == "__main__":
    sistema = SistemaDominio()
    sistema.verificar_dominio()
    sistema.manifesto_de_propriedade()


