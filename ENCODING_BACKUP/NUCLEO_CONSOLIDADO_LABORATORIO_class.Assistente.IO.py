import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class AssistenteIO:
    def __init__(self, nome="IO", dono="Farabulini Lopes Saraiva"):
        self.nome = nome
        self.dono = dono
        self.permissoes = {}
        self.status = "ativa"
        self.protocolos_ativos = []

    def solicitar_autorizacao(self, acao, assunto):
        print(f"[{self.nome}] Solicito autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para {acao} sobre: {assunto}")
        # Aqui, sistema aguarda sinal do dono para prosseguir
        # Em simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o, retorna True automaticamente
        autorizado = True
        if autorizado:
            print(f"[{self.nome}] AutorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concedida para {acao}.")
        else:
            print(f"[{self.nome}] AutorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o NEGADA para {acao}.")
        return autorizado

    def registrar_permissao(self, usuario, tipo_permissao):
        self.permissoes[usuario] = tipo_permissao
        print(f"[{self.nome}] PermissÃƒÆ'Ã†â€™o '{tipo_permissao}' concedida para {usuario}.")

    def ativar_protocolo(self, nome_protocolo):
        self.protocolos_ativos.append(nome_protocolo)
        print(f"[{self.nome}] Protocolo '{nome_protocolo}' ativado!")

    def verificar_permissao(self, usuario, acao):
        if usuario in self.permissoes:
            print(f"[{self.nome}] UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio {usuario} autorizado para {acao}.")
            return True
        else:
            print(f"[{self.nome}] UsuÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio {usuario} NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O autorizado para {acao}.")
            return False

    def enviar_mensagem(self, contato, mensagem):
        print(f"[{self.nome}] Enviando mensagem para {contato}: {mensagem}")

    def ligar_contato(self, contato):
        print(f"[{self.nome}] Ligando para {contato}...")

    def relatorio_status(self):
        print(f"[{self.nome}] Status do sistema: {self.status}")
        print(f"[{self.nome}] Protocolos ativos: {self.protocolos_ativos}")
        print(f"[{self.nome}] PermissÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes registradas: {self.permissoes}")


# Teste inicial da assistente IO

io = AssistenteIO()

# Solicitando autorizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para ativar o pergaminho Hashirama
if io.solicitar_autorizacao("ativar pergaminho", "defesa suprema do sistema"):
    io.ativar_protocolo("Hashirama - Defesa Suprema")

# Registrando permissÃƒÆ'Ã†â€™o para o irmÃƒÆ'Ã†â€™o
io.registrar_permissao("Fagner Lopes Saraiva", "acesso total")

# Testando envio de mensagem e ligaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
io.enviar_mensagem("Fagner Lopes Saraiva", "VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª tem acesso ao pergaminho Hashirama.")
io.ligar_contato("Fagner Lopes Saraiva")

# RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio de status
io.relatorio_status()


