import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class PonteMultiverso:
    def __init__(self):
        self.canais = {
            "cartorios": {"status": "ativo", "autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes": []},
            "biblioteca_nacional": {"status": "ativo", "autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes": []},
            "universo_anime": {"status": "ativo", "autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes": []},
            "universo_digital": {"status": "ativo", "autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes": []},
            "universo_financeiro": {"status": "ativo", "autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes": []},
            # Adicione outros universos/mundos conforme necessidade
        }
        self.io = None  # LigaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com a assistente IO

    def ligar_io(self, assistente_io):
        self.io = assistente_io
        print("[PonteMultiverso] Assistente IO conectada.")

    def solicitar_autorizacao_canal(self, canal, usuario, acao):
        if canal in self.canais:
            if self.io.verificar_permissao(usuario, acao):
                if self.io.solicitar_autorizacao(acao, f"canal {canal}"):
                    self.canais[canal]["autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes"].append((usuario, acao))
                    print(f"[PonteMultiverso] AutorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concedida para {usuario} no canal {canal} para {acao}.")
                    return True
                else:
                    print(f"[PonteMultiverso] AutorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o NEGADA para {usuario} no canal {canal} para {acao}.")
            else:
                print(f"[PonteMultiverso] {usuario} sem permissÃƒÆ'Ã†â€™o para {acao} no canal {canal}.")
        else:
            print(f"[PonteMultiverso] Canal {canal} nÃƒÆ'Ã†â€™o existe.")
        return False

    def ativar_canal(self, canal):
        if canal in self.canais:
            self.canais[canal]["status"] = "ativo"
            print(f"[PonteMultiverso] Canal {canal} ativado.")
        else:
            print(f"[PonteMultiverso] Canal {canal} nÃƒÆ'Ã†â€™o existe.")

    def desativar_canal(self, canal):
        if canal in self.canais:
            self.canais[canal]["status"] = "inativo"
            print(f"[PonteMultiverso] Canal {canal} desativado.")
        else:
            print(f"[PonteMultiverso] Canal {canal} nÃƒÆ'Ã†â€™o existe.")

    def status_canais(self):
        for canal, dados in self.canais.items():
            print(f"[PonteMultiverso] Canal: {canal} - Status: {dados['status']} - AutorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes: {len(dados['autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes'])}")

# Exemplo de uso

io = AssistenteIO()
ponte = PonteMultiverso()
ponte.ligar_io(io)

# Registrar permissÃƒÆ'Ã†â€™o para Fagner no sistema IO
io.registrar_permissao("Fagner Lopes Saraiva", "acesso total")

# Solicitar autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para usar o canal cartorios
ponte.solicitar_autorizacao_canal("cartorios", "Fagner Lopes Saraiva", "acesso leitura")

# Ativar canal universo_financeiro
ponte.ativar_canal("universo_financeiro")

# Mostrar status dos canais
ponte.status_canais()


