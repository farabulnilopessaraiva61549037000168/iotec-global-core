# ==============================================================================
# IOTEC
# 024_CONNECTOR_ENGINE.py
# Gerenciador Central de Conectores
# ==============================================================================

import os
import importlib.util
from datetime import datetime


# ==============================================================================
# CONECTOR
# ==============================================================================

class Connector:

    def __init__(

        self,

        codigo,

        nome,

        biblioteca=None,

        arquivo=None

    ):

        self.codigo = codigo

        self.nome = nome

        self.biblioteca = biblioteca

        self.arquivo = arquivo

        self.instalado = False

        self.online = False

        self.ultima_verificacao = "-"

        self.erro = ""


# ==============================================================================
# ENGINE
# ==============================================================================

class ConnectorEngine:

    def __init__(self):

        self.conectores = []

    # --------------------------------------------------------------------------

    def registrar(

        self,

        codigo,

        nome,

        biblioteca=None,

        arquivo=None

    ):

        self.conectores.append(

            Connector(

                codigo,

                nome,

                biblioteca,

                arquivo

            )

        )

    # --------------------------------------------------------------------------

    def verificar(self):

        for c in self.conectores:

            c.ultima_verificacao = datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            )

            try:

                if c.biblioteca:

                    spec = importlib.util.find_spec(c.biblioteca)

                    c.instalado = spec is not None

                else:

                    c.instalado = True

                if c.arquivo:

                    c.online = os.path.exists(c.arquivo)

                else:

                    c.online = c.instalado

            except Exception as erro:

                c.erro = str(erro)

                c.online = False

    # --------------------------------------------------------------------------

    def painel(self):

        print()

        print("=" * 90)

        print("IOTEC - CENTRAL DE CONECTORES")

        print("=" * 90)

        print()

        for c in self.conectores:

            status = "ONLINE"

            if not c.online:

                status = "OFFLINE"

            print(f"""

CÃ³digo.............: {c.codigo}

Nome...............: {c.nome}

Biblioteca.........: {c.biblioteca}

Arquivo............: {c.arquivo}

Instalado..........: {c.instalado}

Status.............: {status}

Ãšltima VerificaÃ§Ã£o.: {c.ultima_verificacao}

Erro...............: {c.erro}

---------------------------------------------------------------------

""")

# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    engine = ConnectorEngine()

    engine.registrar(

        codigo="PAYPAL",

        nome="PayPal SDK",

        biblioteca="paypalrestsdk"

    )

    engine.registrar(

        codigo="PANDAS",

        nome="Pandas",

        biblioteca="pandas"

    )

    engine.registrar(

        codigo="SQLITE",

        nome="SQLite",

        biblioteca="sqlite3"

    )

    engine.registrar(

        codigo="CRM",

        nome="Banco CRM",

        arquivo="iotec.db"

    )

    engine.registrar(

        codigo="CONFIG",

        nome="ConfiguraÃ§Ã£o Geral",

        arquivo="config.json"

    )

    engine.verificar()

    engine.painel()

