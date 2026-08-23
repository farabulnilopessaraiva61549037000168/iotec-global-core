"""
======================================================================
IOTEC
022_PRODUCT_SHOWCASE.py

VITRINE COMERCIAL

Apresenta os produtos exatamente como um consultor comercial
os enxergaria.

======================================================================
"""

import sqlite3

class ProductShowcase:

    def __init__(self):

        self.db = sqlite3.connect("iotec_kernel.db")
        self.cursor = self.db.cursor()

    # =========================================================

    def mostrar_catalogo(self):

        self.cursor.execute("""

        SELECT

            codigo,
            nome,
            categoria,
            descricao,
            problema,
            publico,
            preco,
            prazo,
            status,
            responsavel

        FROM produtos

        ORDER BY nome

        """)

        produtos = self.cursor.fetchall()

        print()
        print("="*80)
        print("                IOTEC - CATÃƒÂLOGO COMERCIAL")
        print("="*80)

        if not produtos:

            print()
            print("Nenhum produto disponÃƒÂ­vel.")
            return

        for p in produtos:

            print()
            print("="*80)

            print("CÃƒÂ³digo.............", p[0])

            print("Produto............", p[1])

            print("Categoria..........", p[2])

            print()

            print("O que fazemos")

            print("-"*80)

            print(p[3])

            print()

            print("Problema resolvido")

            print("-"*80)

            print(p[4])

            print()

            print("PÃƒÂºblico")

            print("-"*80)

            print(p[5])

            print()

            print("Investimento inicial")

            print("-"*80)

            print(f"R$ {p[6]:,.2f}")

            print()

            print("Prazo")

            print("-"*80)

            print(p[7])

            print()

            print("ResponsÃƒÂ¡vel")

            print("-"*80)

            print(p[9])

            print()

            print("Status")

            print("-"*80)

            print(p[8])

            print()

            print("ServiÃƒÂ§os adicionais")

            print("-"*80)

            print("Ã¢Å"â€ PersonalizaÃƒÂ§ÃƒÂ£o")
            print("Ã¢Å"â€ Suporte")
            print("Ã¢Å"â€ AtualizaÃƒÂ§ÃƒÂµes")
            print("Ã¢Å"â€ DocumentaÃƒÂ§ÃƒÂ£o")
            print("Ã¢Å"â€ Treinamento (quando contratado)")
            print()

            print("Fluxo Comercial")

            print("-"*80)

            print("""
Cliente
   Ã¢â€â€š
   Ã¢â€"Â¼
Contato
   Ã¢â€â€š
   Ã¢â€"Â¼
DiagnÃƒÂ³stico
   Ã¢â€â€š
   Ã¢â€"Â¼
Proposta
   Ã¢â€â€š
   Ã¢â€"Â¼
Contrato
   Ã¢â€â€š
   Ã¢â€"Â¼
ProduÃƒÂ§ÃƒÂ£o
   Ã¢â€â€š
   Ã¢â€"Â¼
Entrega
   Ã¢â€â€š
   Ã¢â€"Â¼
PÃƒÂ³s-venda
""")

        print("="*80)

    # =========================================================

    def painel(self):

        self.cursor.execute(
            "SELECT COUNT(*) FROM produtos"
        )

        total = self.cursor.fetchone()[0]

        self.cursor.execute(
            "SELECT COUNT(*) FROM produtos WHERE status='PRONTO'"
        )

        prontos = self.cursor.fetchone()[0]

        print()
        print("="*80)
        print("PAINEL COMERCIAL")
        print("="*80)

        print()

        print(f"Produtos cadastrados........ {total}")
        print(f"Prontos para venda.......... {prontos}")
        print(f"Pendentes................... {total-prontos}")

        print()

        if prontos > 0:

            print("STATUS DO COMERCIAL")

            print()

            print("A plataforma possui produtos")
            print("que podem ser apresentados")
            print("a clientes.")

        else:

            print("Nenhum produto pronto.")

        print()

        print("="*80)

    # =========================================================

    def fechar(self):

        self.db.close()


if __name__ == "__main__":

    sistema = ProductShowcase()

    sistema.painel()

    sistema.mostrar_catalogo()

    sistema.fechar()


