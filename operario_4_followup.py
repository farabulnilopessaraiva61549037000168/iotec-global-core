# -*- coding: utf-8 -*-
import pandas as pd
import os
import smtplib
import time
import random
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_REMETENTE = "brunofarabulini@gmail.com"
SENHA_REMETENTE = "ncerjdjqbkdshcdp"

TEMPLATE_FOLLOWUP = """
Olá, equipe da {empresa},

Espero que estejam bem.

Estou passando apenas para reforçar o contato anterior referente à nossa infraestrutura de automação B2B (IOTEC). 

Conseguiram avaliar como a solução pode otimizar a captação de clientes e reduzir custos operacionais no setor de vocês?

Se quiserem conferir o portal de ativação e a proposta completa, o link oficial segue abaixo:
https://picpay.me/iotec/297

Permaneco à disposição para esclarecer qualquer dúvida técnica.

Atenciosamente,

Bruna Farabulini
Diretoria de Operações | IOTEC
"""

def executar_followup():
    if not os.path.exists(CSV_PATH):
        print("[-] Arquivo esteira_leads.csv nao encontrado.")
        return

    df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')
    df.columns = [c.strip().capitalize() for c in df.columns]

    if 'Status' not in df.columns:
        print("[-] Coluna 'Status' nao encontrada no CSV.")
        return

    df['Status'] = df['Status'].astype(str).str.strip()
    fila = df[df['Status'] == 'CONTATADO']

    if fila.empty:
        print("[!] Nenhum lead com status 'CONTATADO' pendente de follow-up.")
        return

    total = len(fila)
    hora_atual = datetime.now().strftime("%H:%M")
    print(f"\n[+] [{hora_atual}] Iniciando Follow-up (Operario 4) para {total} lead(s)...")

    for i, (idx, row) in enumerate(fila.iterrows(), start=1):
        empresa = str(row.get('Empresa', 'Empresa')).strip()
        email_dest = str(row.get('Email', '')).strip()

        if not email_dest or '@' not in email_dest:
            continue

        assunto = f"Re: Oportunidade de Automação B2B - {empresa}"
        corpo = TEMPLATE_FOLLOWUP.format(empresa=empresa)

        print(f"[>] Follow-up ({i}/{total}) | {empresa} ({email_dest})")

        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_REMETENTE
            msg['To'] = email_dest
            msg['Subject'] = assunto
            msg.attach(MIMEText(corpo, 'plain', 'utf-8'))

            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.starttls()
            server.login(EMAIL_REMETENTE, SENHA_REMETENTE)
            server.send_message(msg)
            server.quit()

            print("    [OK] Follow-up entregue com sucesso!")
            df.loc[idx, 'Status'] = 'FOLLOWUP_ENVIADO'

            if i < total:
                tempo = random.randint(5, 10)
                print(f"    [WAIT] Aguardando {tempo}s para proximo envio...")
                time.sleep(tempo)

        except Exception as e:
            print(f"    [ERRO] Falha ao enviar follow-up: {e}")

    df.to_csv(CSV_PATH, sep=';', index=False, encoding='utf-8-sig')
    print("\n[+] Rodada de Follow-up concluida com sucesso!")

if __name__ == "__main__":
    executar_followup()