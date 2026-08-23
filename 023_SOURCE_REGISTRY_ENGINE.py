# ==============================================================================
# IOTEC
# 023_SOURCE_REGISTRY_ENGINE.py
# Cadastro Oficial de Fontes Operacionais
# ==============================================================================

from dataclasses import dataclass
from typing import Dict
from datetime import datetime


# ==============================================================================
# FONTE
# ==============================================================================

@dataclass
class Source:

    codigo: str

    nome: str

    categoria: str

    ativa: bool

    autenticada: bool

    descricao: str

    ultima_sincronizacao: str = "-"


# ==============================================================================
# REGISTRY
# ==============================================================================

class SourceRegistry:

    def __init__(self):

        self.fontes: Dict[str, Source] = {}

    # --------------------------------------------------------------------------

    def registrar(

        self,

        codigo,

        nome,

        categoria,

        ativa=False,

        autenticada=False,

        descricao=""

    ):

        self.fontes[codigo] = Source(

            codigo=codigo,

            nome=nome,

            categoria=categoria,

            ativa=ativa,

            autenticada=autenticada,

            descricao=descricao

        )

    # --------------------------------------------------------------------------

    def sincronizar(self, codigo):

        if codigo in self.fontes:

            self.fontes[codigo].ultima_sincronizacao = (

                datetime.now().strftime("%d/%m/%Y %H:%M:%S")

            )

    # --------------------------------------------------------------------------

    def listar(self):

        print()

        print("=" * 90)

        print("IOTEC - REGISTRO OFICIAL DE FONTES")

        print("=" * 90)

        for f in self.fontes.values():

            print(f"""

CÃ³digo.............: {f.codigo}

Nome...............: {f.nome}

Categoria..........: {f.categoria}

Ativa..............: {f.ativa}

Autenticada........: {f.autenticada}

Ãšltima SincronizaÃ§Ã£o: {f.ultima_sincronizacao}

DescriÃ§Ã£o..........: {f.descricao}

---------------------------------------------------------------------

""")

    # --------------------------------------------------------------------------

    def existe(self, codigo):

        return codigo in self.fontes


# ==============================================================================
# TESTE
# ==============================================================================

if __name__ == "__main__":

    registry = SourceRegistry()

    registry.registrar(

        codigo="PAYPAL",

        nome="PayPal",

        categoria="Pagamento",

        descricao="Gateway oficial de pagamentos"

    )

    registry.registrar(

        codigo="CRM",

        nome="CRM IOTEC",

        categoria="Clientes",

        descricao="Cadastro de clientes"

    )

    registry.registrar(

        codigo="GOOGLE_MAPS",

        nome="Google Maps",

        categoria="Pesquisa",

        descricao="Pesquisa de empresas"

    )

    registry.registrar(

        codigo="GMAIL",

        nome="Gmail",

        categoria="ComunicaÃ§Ã£o",

        descricao="Envio e recebimento de e-mails"

    )

    registry.listar()

