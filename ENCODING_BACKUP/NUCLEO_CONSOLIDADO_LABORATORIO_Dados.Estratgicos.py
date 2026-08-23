import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# Jaguar Digital ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de Dados EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicos

class Torre:
    def __init__(self, nome, cnae_principal, cnaes_secundarios):
        self.nome = nome
        self.cnae_principal = cnae_principal
        self.cnaes_secundarios = cnaes_secundarios

class JaguarDigital:
    def __init__(self):
        self.nucleo = "Jaguar Digital ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de Dados EstratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicos"
        self.torres = []

    def adicionar_torre(self, torre: Torre):
        self.torres.append(torre)

    def manifesto_operacional(self):
        return {
            "estrutura": "matriz orgÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢nica de 15 setores",
            "validacao": "sincronizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com Receita Federal, SEFAZ e sistemas federados",
            "protocolo": "cada CNAE ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© funcional e interdependente",
            "nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo": self.nucleo
        }

sistema = JaguarDigital()
# Inserir torres abaixo, com CNAEs estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gicos

sistema.manifesto_operacional()


