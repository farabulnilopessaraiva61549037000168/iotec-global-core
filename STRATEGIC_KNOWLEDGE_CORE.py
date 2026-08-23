import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC STRATEGIC KNOWLEDGE CORE
VersÃƒÂ£o Enterprise 1.0

Biblioteca EstratÃƒÂ©gica da IOTEC

NÃƒÂ£o contÃƒÂ©m regras fixas.
ContÃƒÂ©m princÃƒÂ­pios de engenharia.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class StrategicKnowledge:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    def criar_tabela(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS strategic_knowledge(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            category TEXT,

            title TEXT,

            description TEXT,

            strategic_value TEXT,

            created_at TEXT

        )

        """)

        conn.commit()
        conn.close()

    def registrar(self):

        conhecimentos = [

        (

        "FILOSOFIA",

        "IOTEC NÃƒÆ'O VENDE SOFTWARE",

        """

A IOTEC vende capacidade operacional.

Software ÃƒÂ© apenas um dos componentes.

O verdadeiro produto ÃƒÂ© conhecimento aplicado,
inteligÃƒÂªncia organizacional,
automaÃƒÂ§ÃƒÂ£o
e apoio ÃƒÂ s decisÃƒÂµes.

        """,

        "ALTO"

        ),

        (

        "MOTORES",

        "MOTORES ESPECIALIZADOS",

        """

Cada empresa pode receber
motores especializados.

Os motores sÃƒÂ£o construÃƒÂ­dos
para resolver necessidades especÃƒÂ­ficas.

Um motor representa
uma capacidade organizacional.

NÃƒÂ£o ÃƒÂ© um animal.

Ãƒâ€° um conjunto de estratÃƒÂ©gias.

A inspiraÃƒÂ§ÃƒÂ£o pode vir
da natureza,
engenharia,
economia,
administraÃƒÂ§ÃƒÂ£o,
logÃƒÂ­stica
ou ciÃƒÂªncia.

        """,

        "CRÃƒÂTICO"

        ),

        (

        "BIOINSPIRAÃƒâ€¡ÃƒÆ'O",

        "INSPIRAÃƒâ€¡ÃƒÆ'O NA NATUREZA",

        """

EstratÃƒÂ©gias observadas na natureza
podem inspirar arquiteturas.

Exemplos:

cooperaÃƒÂ§ÃƒÂ£o

paralelismo

resiliÃƒÂªncia

coordenaÃƒÂ§ÃƒÂ£o

exploraÃƒÂ§ÃƒÂ£o

adaptaÃƒÂ§ÃƒÂ£o

aprendizagem

A IOTEC utiliza estas inspiraÃƒÂ§ÃƒÂµes
como engenharia
e nÃƒÂ£o como produto.

        """,

        "ALTO"

        ),

        (

        "CONSULTORIA",

        "CONHECER ANTES DE VENDER",

        """

Antes de recomendar qualquer soluÃƒÂ§ÃƒÂ£o
o Kernel deverÃƒÂ¡ procurar compreender
a organizaÃƒÂ§ÃƒÂ£o.

Pesquisar informaÃƒÂ§ÃƒÂµes pÃƒÂºblicas.

Preparar um dossiÃƒÂª.

Validar hipÃƒÂ³teses com o cliente.

Somente depois recomendar.

        """,

        "CRÃƒÂTICO"

        ),

        (

        "PRODUTOS",

        "MOTORES COMO COMPONENTES",

        """

O cliente compra resultados.

Os motores sÃƒÂ£o componentes internos.

Eles podem compor:

Centro de InteligÃƒÂªncia

Programa Comercial

Programa Industrial

Programa Agro

Programa Executivo

Programa Financeiro

        """,

        "ALTO"

        ),

        (

        "LICENCIAMENTO",

        "LICENCIAR TECNOLOGIA",

        """

A IOTEC poderÃƒÂ¡:

licenciar motores;

licenciar arquiteturas;

licenciar metodologias;

licenciar agentes;

licenciar modelos operacionais;

licenciar o Kernel;

licenciar mÃƒÂ³dulos;

licenciar conhecimento especializado.

O licenciamento pode ocorrer
por implantaÃƒÂ§ÃƒÂ£o,
assinatura,
franquia tecnolÃƒÂ³gica,
OEM,
white-label
ou contratos corporativos.

        """,

        "CRÃƒÂTICO"

        ),

        (

        "APRENDIZAGEM",

        "O KERNEL APRENDE",

        """

O Kernel deve evoluir.

Aprender com projetos.

Aprender com clientes.

Aprender com erros.

Aprender com resultados.

Aprender continuamente.

        """,

        "ALTO"

        ),

        (

        "MISSÃƒÆ'O",

        "GERAR VALOR",

        """

Toda evoluÃƒÂ§ÃƒÂ£o deverÃƒÂ¡ responder:

Como isto ajuda o cliente?

Como isto aumenta produtividade?

Como isto reduz desperdÃƒÂ­cios?

Como isto melhora decisÃƒÂµes?

Como isto aumenta receita?

        """,

        "CRÃƒÂTICO"

        )

        ]

        conn = self.conectar()
        cursor = conn.cursor()

        for item in conhecimentos:

            cursor.execute("""

            INSERT INTO strategic_knowledge(

                category,
                title,
                description,
                strategic_value,
                created_at

            )

            VALUES(?,?,?,?,?)

            """,(

                item[0],
                item[1],
                item[2],
                item[3],
                str(datetime.now())

            ))

        conn.commit()
        conn.close()

    def mostrar(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        category,
        title,
        strategic_value

        FROM strategic_knowledge

        ORDER BY category

        """)

        dados = cursor.fetchall()

        conn.close()

        print()

        print("="*70)
        print("IOTEC STRATEGIC KNOWLEDGE CORE")
        print("="*70)
        print(datetime.now())
        print("="*70)

        print()

        for d in dados:

            print(d[0])

            print("Conhecimento....",d[1])

            print("ImportÃƒÂ¢ncia.....",d[2])

            print()

        print("="*70)

        print("MISSÃƒÆ'O")

        print()

        print("Preservar")

        print("a inteligÃƒÂªncia")

        print("estratÃƒÂ©gica")

        print("da IOTEC.")

        print()

        print("="*70)

        print("STRATEGIC CORE ONLINE")

        print("="*70)

    def executar(self):

        self.criar_tabela()

        self.registrar()

        self.mostrar()


if __name__ == "__main__":

    StrategicKnowledge().executar()



