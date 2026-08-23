import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# IOTEC_BILLING_INTELLIGENCE_ENGINE.py

# ============================================================

# ENGINE DE FATURAMENTO INTELIGENTE

# ============================================================

# OBJETIVO:

# ------------------------------------------------------------

# Este nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo controla:

#

# - geraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de invoice

# - envio por email

# - envio por WhatsApp

# - monitoramento de pagamentos

# - leitura automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica de emails

# - reconhecimento PayPal

# - atualizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o automÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡tica do workflow

# - liberaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o operacional

#

# ============================================================



import sqlite3

import uuid

import time

import imaplib

import email



from datetime import datetime

from email.mime.text import MIMEText

import smtplib



# ============================================================

# CONFIGURAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¢ES

# ============================================================



DATABASE = "iotec_operational.db"



EMAIL_ACCOUNT = "iotec.bl@proton.me"



EMAIL_PASSWORD = "SUA_SENHA"



IMAP_SERVER = "imap.protonmail.com"



SMTP_SERVER = "smtp.protonmail.com"



SMTP_PORT = 587



# ============================================================

# ENGINE

# ============================================================



class IOTECBillingEngine:
    pass



    def __init__(self):
        pass



        self.conn = sqlite3.connect(DATABASE)



        self.cursor = self.conn.cursor()



        self.create_tables()



    # ========================================================

    # IA VISUAL

    # ========================================================



    def think(self, text):
        pass



        print(f"\n[BILLING AI] {text}")



        time.sleep(1)



    # ========================================================

    # TABELAS

    # ========================================================



    def create_tables(self):
        pass



        self.cursor.execute("""



        CREATE TABLE IF NOT EXISTS invoices (



            id INTEGER PRIMARY KEY AUTOINCREMENT,



            invoice_id TEXT,



            project_id TEXT,



            client_email TEXT,



            amount REAL,



            status TEXT,



            created_at TEXT

        )



        """)



        self.conn.commit()



    # ========================================================

    # GERAR FATURA

    # ========================================================



    def generate_invoice(



        self,

        project_id,

        client_email,

        amount



    ):



        invoice_id = f"INV-{str(uuid.uuid4())[:8].upper()}"



        created_at = str(datetime.now())



        self.cursor.execute("""



        INSERT INTO invoices (



            invoice_id,

            project_id,

            client_email,

            amount,

            status,

            created_at



        )



        VALUES (?, ?, ?, ?, ?, ?)



        """, (



            invoice_id,

            project_id,

            client_email,

            amount,

            "PENDING",

            created_at

        ))



        self.conn.commit()



        self.think(

            f"Fatura criada: {invoice_id}"

        )



        return invoice_id



    # ========================================================

    # ENVIAR EMAIL

    # ========================================================



    def send_invoice_email(



        self,

        client_email,

        invoice_id,

        amount



    ):



        self.think(

            "Enviando invoice por email..."

        )



        subject = f"IOTEC INVOICE {invoice_id}"



        body = f"""



OlÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡.



Sua invoice foi gerada com sucesso.



INVOICE:

{invoice_id}



VALOR:

R$ {amount:,.2f}



ApÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³s confirmaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o financeira,

o workflow operacional serÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ liberado.



IOTEC GLOBAL PLATFORM



"""



        msg = MIMEText(body)



        msg["Subject"] = subject



        msg["From"] = EMAIL_ACCOUNT



        msg["To"] = client_email



        try:
            pass



            server = smtplib.SMTP(

                SMTP_SERVER,

                SMTP_PORT

            )



            server.starttls()



            server.login(

                EMAIL_ACCOUNT,

                EMAIL_PASSWORD

            )



            server.sendmail(

                EMAIL_ACCOUNT,

                client_email,

                msg.as_string()

            )



            server.quit()



            self.think(

                "Invoice enviada com sucesso."

            )



        except Exception as e:
            pass



            print("\nERRO EMAIL:")

            print(e)



    # ========================================================

    # WHATSAPP

    # ========================================================



    def whatsapp_invoice(



        self,

        phone,

        invoice_id,

        amount



    ):



        self.think(

            "Preparando envio WhatsApp..."

        )



        message = f"""



IOTEC GLOBAL PLATFORM



INVOICE:

{invoice_id}



VALOR:

R$ {amount:,.2f}



ApÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³s confirmaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o financeira,

o projeto serÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ liberado.



"""



        print("\n================ WHATSAPP ================")



        print(f"\nDESTINO: {phone}")



        print("\nMENSAGEM:")



        print(message)



        print("\nSTATUS:")

        print("PRONTO PARA API WHATSAPP")



    # ========================================================

    # MONITORAMENTO EMAIL

    # ========================================================



    def monitor_payments(self):
        pass



        self.think(

            "Monitorando caixa de email..."

        )



        try:
            pass



            mail = imaplib.IMAP4_SSL(

                IMAP_SERVER

            )



            mail.login(

                EMAIL_ACCOUNT,

                EMAIL_PASSWORD

            )



            mail.select("inbox")



            status, messages = mail.search(

                None,

                "ALL"

            )



            email_ids = messages[0].split()



            latest_email = email_ids[-1]



            status, msg_data = mail.fetch(

                latest_email,

                "(RFC822)"

            )



            raw_email = msg_data[0][1]



            msg = email.message_from_bytes(

                raw_email

            )



            subject = msg["subject"]



            sender = msg["from"]



            print("\n================ EMAIL DETECTADO ================")



            print(f"\nFROM: {sender}")



            print(f"\nSUBJECT: {subject}")



            # =================================================

            # DETECÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O PAYPAL

            # =================================================



            if "paypal" in sender.lower():
                pass



                self.think(

                    "Pagamento PayPal detectado."

                )



                self.process_payment(subject)



        except Exception as e:
            pass



            print("\nERRO MONITORAMENTO:")



            print(e)



    # ========================================================

    # PROCESSAR PAGAMENTO

    # ========================================================



    def process_payment(self, subject):
        pass



        self.cursor.execute("""



        SELECT

            invoice_id,

            project_id



        FROM invoices



        WHERE status = 'PENDING'



        """)



        invoices = self.cursor.fetchall()



        for invoice in invoices:
            pass



            invoice_id = invoice[0]



            project_id = invoice[1]



            if invoice_id in subject:
                pass



                self.cursor.execute("""



                UPDATE invoices



                SET status = ?



                WHERE invoice_id = ?



                """, (



                    "PAID",

                    invoice_id

                ))



                self.conn.commit()



                self.release_project(project_id)



    # ========================================================

    # LIBERAR PROJETO

    # ========================================================



    def release_project(self, project_id):
        pass



        self.think(

            f"Liberando projeto {project_id}"

        )



        self.cursor.execute("""



        UPDATE projects



        SET status = ?



        WHERE project_id = ?



        """, (



            "PRODUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O LIBERADA",

            project_id

        ))



        self.conn.commit()



        print("\n================ LIBERAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O ================")



        print(f"\nPROJECT ID:")

        print(project_id)



        print("\nSTATUS:")

        print("PRODUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O LIBERADA")



    # ========================================================

    # CONSULTAR FATURAS

    # ========================================================



    def show_invoices(self):
        pass



        print("\n================ FATURAS ================")



        self.cursor.execute("""



        SELECT

            invoice_id,

            project_id,

            amount,

            status



        FROM invoices



        """)



        invoices = self.cursor.fetchall()



        for invoice in invoices:
            pass



            print("\n--------------------------------")



            print(f"INVOICE: {invoice[0]}")



            print(f"PROJECT: {invoice[1]}")



            print(f"VALOR: R$ {invoice[2]:,.2f}")



            print(f"STATUS: {invoice[3]}")



# ============================================================

# EXECUÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



if __name__ == "__main__":
    pass



    engine = IOTECBillingEngine()



    print("\n================================================")

    print("      IOTEC BILLING INTELLIGENCE ENGINE")

    print("================================================")



    print("\n1 - Gerar invoice")

    print("2 - Monitorar pagamentos")

    print("3 - Consultar invoices")



    option = input("\n>>> ")



    # ========================================================

    # GERAR FATURA

    # ========================================================



    if option == "1":
        pass



        project_id = input(

            "\nPROJECT ID:\n\n>>> "

        )



        client_email = input(

            "\nEMAIL CLIENTE:\n\n>>> "

        )



        amount = float(



            input(

                "\nVALOR:\n\n>>> "

            )

        )



        invoice_id = engine.generate_invoice(



            project_id,

            client_email,

            amount

        )



        engine.send_invoice_email(



            client_email,

            invoice_id,

            amount

        )



        phone = input(

            "\nWHATSAPP CLIENTE:\n\n>>> "

        )



        engine.whatsapp_invoice(



            phone,

            invoice_id,

            amount

        )



    # ========================================================

    # MONITORAR

    # ========================================================



    elif option == "2":
        pass



        engine.monitor_payments()



    # ========================================================

    # CONSULTAR

    # ========================================================



    elif option == "3":
        pass



        engine.show_invoices()




