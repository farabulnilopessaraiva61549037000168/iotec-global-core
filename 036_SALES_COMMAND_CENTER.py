"""
======================================================================
IOTEC SALES COMMAND CENTER
VersÃƒÂ£o 1.0
======================================================================

Centro de Comando Comercial

ResponsÃƒÂ¡vel por coordenar toda a operaÃƒÂ§ÃƒÂ£o
de vendas da IOTEC.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"


class SalesCommandCenter:

    def __init__(self):

        self.conn = sqlite3.connect(DB, timeout=30)
        self.cursor = self.conn.cursor()

        self.criar_tabelas()

    # ======================================================

    def criar_tabelas(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS sales_dashboard(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            atualizado TEXT,

            produtos INTEGER,

            clientes INTEGER,

            leads INTEGER,

            propostas INTEGER,

            contratos INTEGER,

            receita REAL

        )

        """)

        self.conn.commit()

    # ======================================================

    def contar(self, tabela):

        try:

            self.cursor.execute(

                f"SELECT COUNT(*) FROM {tabela}"

            )

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ======================================================

    def receita(self):

        try:

            self.cursor.execute("""

            SELECT
            IFNULL(SUM(valor),0)

            FROM contratos

            WHERE status='PAGO'

            """)

            return self.cursor.fetchone()[0]

        except:

            return 0

    # ======================================================

    def atualizar_dashboard(self):

        produtos = self.contar("produtos")
        clientes = self.contar("clientes")
        propostas = self.contar("propostas")
        contratos = self.contar("contratos")

        leads = 0

        try:

            self.cursor.execute("""

            SELECT COUNT(*)

            FROM clientes

            WHERE status='NOVO'

            """)

            leads = self.cursor.fetchone()[0]

        except:

            pass

        receita = self.receita()

        self.cursor.execute("""

        INSERT INTO sales_dashboard(

            atualizado,

            produtos,

            clientes,

            leads,

            propostas,

            contratos,

            receita

        )

        VALUES(?,?,?,?,?,?,?)

        """,(

            datetime.now().strftime("%d/%m/%Y %H:%M:%S"),

            produtos,

            clientes,

            leads,

            propostas,

            contratos,

            receita

        ))

        self.conn.commit()

        return (

            produtos,

            clientes,

            leads,

            propostas,

            contratos,

            receita

        )

    # ======================================================

    def painel(self):

        (

            produtos,

            clientes,

            leads,

            propostas,

            contratos,

            receita

        ) = self.atualizar_dashboard()

        print("="*70)
        print("IOTEC SALES COMMAND CENTER")
        print("="*70)
        print()

        print("Data :",datetime.now().strftime("%d/%m/%Y"))
        print("Hora :",datetime.now().strftime("%H:%M:%S"))

        print()

        print("="*70)
        print("META GLOBAL")
        print("="*70)
        print()

        print("GERAR RECEITA")

        print()

        print("="*70)
        print("INDICADORES")
        print("="*70)

        print()

        print(f"Produtos................ {produtos}")

        print(f"Clientes............... {clientes}")

        print(f"Leads.................. {leads}")

        print(f"Propostas.............. {propostas}")

        print(f"Contratos.............. {contratos}")

        print(f"Receita................ R$ {receita:,.2f}")

        print()

        print("="*70)
        print("AGENTES")
        print("="*70)

        print()

        agentes = [

            ("HUNTER","Encontrar Empresas"),

            ("PESQUISADOR","Pesquisar Clientes"),

            ("CONSULTOR","Escolher Produto"),

            ("NEGOCIADOR","Fechar Contrato"),

            ("PRODUÃƒâ€¡ÃƒÆ'O","Produzir Pedido"),

            ("PÃƒâ€œS-VENDA","Acompanhar Cliente")

        ]

        for nome,missao in agentes:

            print(f"{nome:<18} ONLINE")

            print("MissÃƒÂ£o:",missao)

            print()

        print("="*70)
        print("CHECKLIST COMERCIAL")
        print("="*70)

        print()

        itens = [

            "CatÃƒÂ¡logo",

            "CRM",

            "Pipeline",

            "Produtos",

            "Clientes",

            "ProduÃƒÂ§ÃƒÂ£o",

            "Qualidade",

            "Entrega"

        ]

        for item in itens:

            print("[OK]",item)

        print()

        print("[ ] Loja Virtual")

        print("[ ] PIX")

        print("[ ] Gateway de Pagamento")

        print("[ ] Compra AutomÃƒÂ¡tica")

        print()

        print("="*70)
        print("MISSÃƒÆ'O DO KERNEL")
        print("="*70)

        print()

        print("Todo agente deve executar")

        print("uma missÃƒÂ£o que aproxime")

        print("a IOTEC do prÃƒÂ³ximo contrato.")

        print()

        print("="*70)

    # ======================================================

    def fechar(self):

        self.conn.close()


# ==========================================================

if __name__ == "__main__":

    sistema = SalesCommandCenter()

    sistema.painel()

    sistema.fechar()


