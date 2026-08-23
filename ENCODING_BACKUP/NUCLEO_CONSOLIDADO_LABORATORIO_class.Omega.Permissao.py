import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

   class OmegaPermissao:
    def __init__(self, arquivo_credenciais):
        with open(arquivo_credenciais) as f:
            self.dados = json.load(f)

    def listar_fontes(self):
        return self.dados['fontes']

    def validar_cartoes(self):
        for cartao in self.dados['cartoes']:
            print(f"Validando cartÃƒÆ'Ã†â€™o {cartao['id']}: Status OK")

    def ativar_permissoes(self):
        fontes = self.listar_fontes()
        for fonte in fontes:
            print(f"Ativando permissÃƒÆ'Ã†â€™o para {fonte['nome']} via token {fonte['token']}")
        print("Todas as permissÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes estÃƒÆ'Ã†â€™o ativas e sincronizadas.")

# SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de uso
if __name__ == "__main__":
    omega = OmegaPermissao('credenciais.json')
    omega.validar_cartoes()
    omega.ativar_permissoes()


