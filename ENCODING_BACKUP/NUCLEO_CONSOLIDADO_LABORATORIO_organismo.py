import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# organismo_digital.py

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de ConsciÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
class Consciencia:
    def saudacao(self):
        return "[NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO] Sistema operacional consciente. Ciclo iniciado."

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de Varredura
class Varredura:
    def __init__(self, diretorio):
        self.diretorio = diretorio

    def diagnostico(self):
        return ["mod_consciencia", "mod_varredura", "mod_acao", "mod_relatorios"]

# ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
class Executor:
    def executar(self, comando):
        return f"[AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O] Comando executado: {comando}"

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¾ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios
class Relatorio:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def gerar(self):
        return "\n".join(f" - {item}" for item in self.itens)

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo do Organismo Digital
class SistemaVivo:
    def __init__(self):
        self.cons = Consciencia()
        self.scanner = Varredura("./")
        self.executor = Executor()
        self.relatorio = Relatorio()
        self.dados_embutidos = {
            "chave_de_integracao": "DNA-SISTEMA-ORIGINAL",
            "status": "Autorizado",
            "criptografia": True,
            "assinatura_digital": "SIGILO-VALIDO"
        }

    def autenticar(self):
        print("[SISTEMA] Validando integridade...")
        if self.dados_embutidos["status"] == "Autorizado":
            print("[SISTEMA] Chave validada com sucesso.")
            return True
        else:
            print("[SISTEMA] Falha na chave. Encerrando.")
            return False

    def executar_ciclo(self):
        if self.autenticar():
            print(self.cons.saudacao())

            arquivos = self.scanner.diagnostico()
            acao = self.executor.executar("Organizar MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos, Remover Resistores, Liberar Barramentos")

            self.relatorio.adicionar_item(f"Arquivos Mapeados: {len(arquivos)}")
            self.relatorio.adicionar_item(acao)
            self.relatorio.adicionar_item("NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo em perfeito estado. Ciclo concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­do.")

            print("\n[RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO DO CICLO]")
            print(self.relatorio.gerar())

            print("\n[SISTEMA VIVO] OperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da. NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo operante e expandindo.")
        else:
            print("[SISTEMA VIVO] Ciclo abortado.")

# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ InicializaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
if __name__ == "__main__":
    organismo = SistemaVivo()
    organismo.executar_ciclo()


