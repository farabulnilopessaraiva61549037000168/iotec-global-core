import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================

IOTEC WHATSAPP SETUP WIZARD
FASE 08
REVENUE ACTIVATION

VersÃƒÂ£o 9.0

Assistente de ConfiguraÃƒÂ§ÃƒÂ£o
WhatsApp Business

======================================================================
"""

import sqlite3

DB = "iotec.db"


class WhatsAppSetupWizard:

    def conectar(self):

        return sqlite3.connect(DB, timeout=30)

    # ======================================================

    def criar_tabela(self):

        conn = self.conectar()

        cursor = conn.cursor()

        cursor.execute("""

        CREATE TABLE IF NOT EXISTS whatsapp_config (

            id INTEGER PRIMARY KEY,

            company_name TEXT,

            phone TEXT,

            description TEXT,

            business_hours TEXT,

            welcome_message TEXT,

            away_message TEXT,

            catalog_ready INTEGER,

            crm_ready INTEGER,

            kernel_ready INTEGER

        )

        """)

        conn.commit()

        conn.close()

    # ======================================================

    def executar(self):

        self.criar_tabela()

        print()

        print("="*70)
        print("IOTEC WHATSAPP SETUP WIZARD")
        print("="*70)

        empresa=input("Nome da empresa: ")

        telefone=input("Telefone: ")

        descricao=input("DescriÃƒÂ§ÃƒÂ£o: ")

        horario=input("HorÃƒÂ¡rio de atendimento: ")

        boas=input("Mensagem de boas-vindas: ")

        ausencia=input("Mensagem de ausÃƒÂªncia: ")

        conn=self.conectar()

        cursor=conn.cursor()

        cursor.execute("""

        DELETE FROM whatsapp_config

        """)

        cursor.execute("""

        INSERT INTO whatsapp_config(

        company_name,

        phone,

        description,

        business_hours,

        welcome_message,

        away_message,

        catalog_ready,

        crm_ready,

        kernel_ready

        )

        VALUES(?,?,?,?,?,?,?,?,?)

        """,(empresa,

             telefone,

             descricao,

             horario,

             boas,

             ausencia,

             0,

             0,

             0))

        conn.commit()

        conn.close()

        print()

        print("="*70)

        print("CONFIGURAÃƒâ€¡ÃƒÆ'O SALVA")

        print("="*70)

        print()

        print("Empresa........",empresa)

        print("Telefone.......",telefone)

        print()

        print("Status......... CONFIGURADO")

        print()

        print("="*70)

        print("PRÃƒâ€œXIMAS ETAPAS")

        print()

        print("[ ] Instalar WhatsApp Business")

        print("[ ] Criar Perfil")

        print("[ ] Publicar CatÃƒÂ¡logo")

        print("[ ] Integrar CRM")

        print("[ ] Integrar Kernel")

        print()

        print("="*70)

        print("WHATSAPP SETUP FINALIZADO")

        print("="*70)


if __name__=="__main__":

    WhatsAppSetupWizard().executar()



