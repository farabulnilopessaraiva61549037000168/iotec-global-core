import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC CONFIGURATION CENTER
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Central de ConfiguraÃƒÂ§ÃƒÂµes

======================================================================
"""

import sqlite3
from datetime import datetime

DB = "iotec.db"


class ConfigurationCenter:

    def conectar(self):
        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def carregar_whatsapp(self):

        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute("""

        SELECT

        company_name,
        phone,
        description,
        business_hours,
        welcome_message,
        away_message,
        catalog_ready,
        crm_ready,
        kernel_ready

        FROM whatsapp_config
        LIMIT 1

        """)

        dados = cursor.fetchone()

        conn.close()

        return dados

    # ======================================================

    def executar(self):

        print()

        print("=" * 70)
        print("IOTEC CONFIGURATION CENTER")
        print("=" * 70)
        print(datetime.now())
        print("=" * 70)

        dados = self.carregar_whatsapp()

        if dados is None:

            print()
            print("Nenhuma configuraÃƒÂ§ÃƒÂ£o encontrada.")
            print()
            print("Execute primeiro:")
            print()
            print("055_WHATSAPP_SETUP_WIZARD.py")
            print()
            return

        empresa = dados[0]
        telefone = dados[1]
        descricao = dados[2]
        horario = dados[3]

        catalogo = "SIM" if dados[6] else "NÃƒÆ'O"
        crm = "SIM" if dados[7] else "NÃƒÆ'O"
        kernel = "SIM" if dados[8] else "NÃƒÆ'O"

        print()

        print("EMPRESA")
        print()

        print("Nome..............", empresa)
        print("Telefone..........", telefone)

        print()

        print("=" * 70)

        print("WHATSAPP BUSINESS")

        print()

        print("DescriÃƒÂ§ÃƒÂ£o.........", descricao)

        print()

        print("HorÃƒÂ¡rio...........", horario)

        print()

        print("=" * 70)

        print("INTEGRAÃƒâ€¡Ãƒâ€¢ES")

        print()

        print("CatÃƒÂ¡logo..........", catalogo)
        print("CRM...............", crm)
        print("Kernel............", kernel)

        print()

        print("=" * 70)

        print("STATUS")

        print()

        if crm == "SIM" and kernel == "SIM":

            print("CONFIGURAÃƒâ€¡ÃƒÆ'O OPERACIONAL")

        else:

            print("CONFIGURAÃƒâ€¡ÃƒÆ'O PARCIAL")

        print()

        print("=" * 70)

        print("PRÃƒâ€œXIMAS ETAPAS")

        print()

        if catalogo == "NÃƒÆ'O":
            print("[ ] Publicar CatÃƒÂ¡logo")

        if crm == "NÃƒÆ'O":
            print("[ ] Integrar CRM")

        if kernel == "NÃƒÆ'O":
            print("[ ] Integrar Kernel")

        print("[ ] Ativar WhatsApp Business")
        print("[ ] Criar PÃƒÂ¡gina LinkedIn")
        print("[ ] Publicar Portal")
        print("[ ] Configurar Google Business")

        print()

        print("=" * 70)

        print("CONFIGURATION CENTER ONLINE")

        print("=" * 70)


# ==========================================================

if __name__ == "__main__":

    ConfigurationCenter().executar()



