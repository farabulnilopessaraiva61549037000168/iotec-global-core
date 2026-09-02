
"""
==========================================================
IOTEC CORE V2
Gerado automaticamente

Data:

2026-08-31 07:53:20.322299

==========================================================
"""

import os
import sqlite3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from iotec_wpp import enviar_boleto

DIR_FATURAS = r"C:\IOTEC\faturas"
DB_PATH = r"C:\IOTEC\iotec.db"
os.makedirs(DIR_FATURAS, exist_ok=True)

def inicializar_banco():
    """Cria a tabela de cobranças caso não exista e insere dados de teste."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cobrancas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            doc_cliente TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereco TEXT,
            tipo_mercado TEXT NOT NULL, -- 'BR' ou 'INTL'
            descricao TEXT NOT NULL,
            valor REAL NOT NULL,
            moeda TEXT DEFAULT 'BRL',
            status TEXT DEFAULT 'PENDENTE'
        )
    ''')
    
    # Inserir registros de teste se a tabela estiver vazia
    cursor.execute("SELECT COUNT(*) FROM cobrancas")
    if cursor.fetchone()[0] == 0:
        cursor.executemany('''
            INSERT INTO cobrancas (cliente, doc_cliente, telefone, endereco, tipo_mercado, descricao, valor, moeda, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'PENDENTE')
        ''', [
            ("Bruno_IOTEC", "000.000.000-00", "5588992073886", "Quixadá - CE", "BR", "Licença Plataforma IOTEC B2B", 150.00, "BRL"),
            ("Global Tech Solutions LLC", "US-987654321", "5588992073886", "100 Wall Street, NY", "INTL", "IOTEC Automation API License", 250.00, "USD")
        ])
        conn.commit()
    conn.close()

def gerar_fatura_nacional(caminho_output, cliente, doc_cliente, valor, descricao_servico):
    c = canvas.Canvas(caminho_output, pagesize=letter)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "IOTEC PLATAFORMA DE SERVIÇOS TÉCNICOS")
    c.setFont("Helvetica", 10)
    c.drawString(50, 735, "CNPJ: 61.549.037/0001-68 | Contato: IOTEC.BL@proton.me")
    c.line(50, 712, 550, 712)
    
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, 690, "FATURA DE COBRANÇA B2B / SERVIÇOS TÉCNICOS")
    c.setFont("Helvetica", 10)
    c.drawString(50, 665, f"Sacado/Cliente: {cliente}")
    c.drawString(50, 650, f"CPF/CNPJ: {doc_cliente}")
    
    c.setFillColor(colors.HexColor("#1e293b"))
    c.rect(50, 580, 500, 20, fill=True, stroke=False)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(60, 586, "DESCRIÇÃO DO SERVIÇO")
    c.drawString(450, 586, "VALOR (BRL)")
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 10)
    c.drawString(60, 555, descricao_servico)
    c.drawString(450, 555, f"R$ {valor:.2f}")
    c.line(50, 540, 550, 540)
    
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(430, 515, "TOTAL A PAGAR:")
    c.drawString(450, 515, f"R$ {valor:.2f}")
    c.save()
    return caminho_output

def gerar_commercial_invoice_intl(caminho_output, invoice_num, client_name, client_address, client_tax_id, amount_usd, service_desc):
    c = canvas.Canvas(caminho_output, pagesize=letter)
    c.setFont("Helvetica-Bold", 18)
    c.drawString(50, 750, "COMMERCIAL INVOICE")
    c.setFont("Helvetica-Bold", 11)
    c.drawString(380, 750, f"INVOICE #: {invoice_num}")
    
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, 715, "ISSUER / SERVICE PROVIDER:")
    c.setFont("Helvetica", 9)
    c.drawString(50, 701, "IOTEC TECHNICAL PLATFORM LTD | CNPJ: 61.549.037/0001-68")
    
    c.line(50, 665, 550, 665)
    c.setFont("Helvetica-Bold", 10)
    c.drawString(50, 648, "BILLED TO (CLIENT):")
    c.setFont("Helvetica", 9)
    c.drawString(50, 634, f"Company: {client_name}")
    c.drawString(50, 622, f"Address: {client_address}")
    c.drawString(50, 610, f"Tax ID / EIN / VAT: {client_tax_id}")
    
    c.setFillColor(colors.HexColor("#1e293b"))
    c.rect(50, 565, 500, 20, fill=True, stroke=False)
    c.setFillColor(colors.white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(60, 571, "DESCRIPTION OF TECHNICAL SERVICES")
    c.drawString(450, 571, "AMOUNT (USD)")
    
    c.setFillColor(colors.black)
    c.setFont("Helvetica", 9)
    c.drawString(60, 545, service_desc)
    c.drawString(450, 545, f"$ {amount_usd:.2f}")
    c.line(50, 530, 550, 530)
    
    c.setFont("Helvetica-Bold", 11)
    c.drawRightString(430, 505, "TOTAL AMOUNT DUE:")
    c.drawString(450, 505, f"$ {amount_usd:.2f}")
    c.save()
    return caminho_output

def processar_esteira_banco():
    """Lê cobranças pendentes do banco SQLite, gera PDFs e dispara via WhatsApp."""
    inicializar_banco()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT id, cliente, doc_cliente, telefone, endereco, tipo_mercado, descricao, valor, moeda FROM cobrancas WHERE status = 'PENDENTE'")
    cobrancas = cursor.fetchall()
    
    if not cobrancas:
        print("Nenhuma cobrança pendente para processar.")
        conn.close()
        return

    print(f"🚀 Processando {len(cobrancas)} cobrança(s) pendente(s) do banco de dados...")
    
    for cob in cobrancas:
        cob_id, cliente, doc_cliente, telefone, endereco, tipo_mercado, descricao, valor, moeda = cob
        
        if tipo_mercado == "BR":
            nome_pdf = f"Fatura_BR_{cob_id}_{cliente}.pdf"
            caminho_pdf = os.path.join(DIR_FATURAS, nome_pdf)
            gerar_fatura_nacional(caminho_pdf, cliente, doc_cliente, valor, descricao)
            msg = f"📄 *Fatura IOTEC* gerada no valor de R$ {valor:.2f}."
        else:
            nome_pdf = f"Invoice_INTL_{cob_id}_{cliente}.pdf"
            caminho_pdf = os.path.join(DIR_FATURAS, nome_pdf)
            invoice_num = f"INV-2026-{cob_id:03d}"
            gerar_commercial_invoice_intl(caminho_pdf, invoice_num, cliente, endereco or "International", doc_cliente, valor, descricao)
            msg = f"🌐 *Commercial Invoice IOTEC* ({invoice_num}) - Total: $ {valor:.2f} USD."

        # Enviar via Gateway WPPConnect
        res = enviar_boleto(telefone, caminho_pdf, nome_pdf, msg)
        
        if res.get("status") == "success":
            cursor.execute("UPDATE cobrancas SET status = 'ENVIADO' WHERE id = ?", (cob_id,))
            print(f"✔ Cobrança ID {cob_id} enviada para {cliente} ({telefone})")
        else:
            print(f"❌ Falha ao enviar cobrança ID {cob_id}: {res.get('error')}")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    processar_esteira_banco()