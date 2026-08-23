"""
======================================================================
IOTEC
031_COMMERCIAL_AUTOPILOT.py

COMMERCIAL AUTOPILOT

Decide automaticamente a prÃƒÂ³xima aÃƒÂ§ÃƒÂ£o comercial.

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec_kernel.db"


class CommercialAutopilot:

    def __init__(self):

        self.db = sqlite3.connect(DB, timeout=30)
        self.cursor = self.db.cursor()

    # ======================================================

    def listar_clientes(self):

        self.cursor.execute("""

        SELECT

            codigo,
            empresa,
            status

        FROM clientes

        ORDER BY id

        """)

        return self.cursor.fetchall()

    # ======================================================

    def sugerir(self,status):

        status=status.upper()

        if status=="NOVO":

            return (

                "Entrar em contato",

                "ALTA",

                "Telefone, WhatsApp ou E-mail"

            )

        elif status=="CONTATO":

            return (

                "Agendar reuniÃƒÂ£o",

                "ALTA",

                "AtÃƒÂ© 24 horas"

            )

        elif status=="REUNIÃƒÆ'O":

            return (

                "Preparar proposta",

                "ALTA",

                "Enviar orÃƒÂ§amento"

            )

        elif status=="PROPOSTA":

            return (

                "Fazer Follow-up",

                "MÃƒâ€°DIA",

                "Confirmar recebimento"

            )

        elif status=="NEGOCIAÃƒâ€¡ÃƒÆ'O":

            return (

                "Negociar condiÃƒÂ§ÃƒÂµes",

                "ALTA",

                "Buscar fechamento"

            )

        elif status=="CONTRATO":

            return (

                "Enviar para ProduÃƒÂ§ÃƒÂ£o",

                "ALTA",

                "Liberar equipe"

            )

        elif status=="PRODUÃƒâ€¡ÃƒÆ'O":

            return (

                "Acompanhar execuÃƒÂ§ÃƒÂ£o",

                "NORMAL",

                "Monitorar equipe"

            )

        elif status=="ENTREGUE":

            return (

                "PÃƒÂ³s-venda",

                "NORMAL",

                "Solicitar avaliaÃƒÂ§ÃƒÂ£o"

            )

        return (

            "Sem aÃƒÂ§ÃƒÂ£o",

            "BAIXA",

            "-"

        )

    # ======================================================

    def executar(self):

        print("="*70)
        print("IOTEC COMMERCIAL AUTOPILOT")
        print("="*70)

        print()

        print("Data :",datetime.now().strftime("%d/%m/%Y"))

        print("Hora :",datetime.now().strftime("%H:%M:%S"))

        print()

        clientes=self.listar_clientes()

        if len(clientes)==0:

            print("Nenhum cliente cadastrado.")

            return

        print("="*70)

        print("CLIENTES")

        print("="*70)

        for codigo,empresa,status in clientes:

            acao,

            prioridade,

            prazo=self.sugerir(status)

            print()

            print("Cliente......",codigo)

            print("Empresa......",empresa)

            print("Status.......",status)

            print()

            print("PrÃƒÂ³xima aÃƒÂ§ÃƒÂ£o")

            print("-------------------------------")

            print(acao)

            print()

            print("Prioridade... ",prioridade)

            print("Prazo........ ",prazo)

            print()

            print("-"*60)

        print()

        print("="*70)

        print("MISSÃƒÆ'O DO KERNEL")

        print("="*70)

        print()

        print("Todo cliente deve avanÃƒÂ§ar")

        print("automaticamente para a")

        print("prÃƒÂ³xima etapa comercial.")

        print()

        print("="*70)

    # ======================================================

    def fechar(self):

        self.db.close()


# ===========================================================

if __name__=="__main__":

    sistema=CommercialAutopilot()

    sistema.executar()

    sistema.fechar()


