import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class CodigoConformidade:
    def __init__(self):
        self.compromisso_aceito = False

    def exibir_codigo(self):
        codigo_texto = """
        CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDIGO DE CONFORMIDADE SOCIAL E ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°TICA DO SISTEMA MESTRE

        1. O sistema opera apenas dentro dos limites legais e ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©ticos.
        2. Atua exclusivamente em mineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o digital, comÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rcio autorizado e anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise legÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tima.
        3. Proibido uso para fraudes, invasÃƒÆ'Ã†â€™o de privacidade ou lesÃƒÆ'Ã†â€™o a terceiros.
        4. ResponsÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡veis monitoram uso e cessam qualquer operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o ilegal.
        5. TransparÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia e cooperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com auditorias legais garantidas.

        Digite 'SIM' para aceitar e continuar:
        """
        print(codigo_texto)

    def solicitar_aceite(self):
        resposta = input("Aceita o cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo de conformidade? (SIM/NAO): ").strip().upper()
        if resposta == "SIM":
            self.compromisso_aceito = True
            print("Compromisso aceito. Sistema operando dentro da conformidade social e ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica.")
        else:
            print("Compromisso nÃƒÆ'Ã†â€™o aceito. Encerrando sistema para evitar uso indevido.")
            exit()

# Uso no sistema
if __name__ == "__main__":
    codigo = CodigoConformidade()
    codigo.exibir_codigo()
    codigo.solicitar_aceite()

    if codigo.compromisso_aceito:
        # Continue com a ativaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo mestre e outras operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes
        print("Continuando ativaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o do sistema...")
    else:
        # Sistema desativa e encerra
        pass


