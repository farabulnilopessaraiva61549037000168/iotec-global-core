# -*- coding: utf-8 -*-
import pandas as pd
import os
import re
import urllib.parse
import urllib.request
import json

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"

DOMINIOS_CONHECIDOS = {
    "magazine luiza": "magazineluiza.com.br",
    "magalu": "magazineluiza.com.br",
    "petrobras": "petrobras.com.br",
    "ambev": "ambev.com.br"
}

def extrair_emails_de_texto(texto):
    padrao = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(padrao, texto)
    emails_validos = [e for e in emails if not e.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp', '.svg'))]
    return list(set(emails_validos))

def buscar_email_web(nome_empresa):
    nome_clean = str(nome_empresa).lower().strip()
    
    for chave, dominio in DOMINIOS_CONHECIDOS.items():
        if chave in nome_clean:
            return f"contato@{dominio}"

    try:
        url_api = f"https://api.duckduckgo.com/?q={urllib.parse.quote(nome_empresa)}&format=json"
        req = urllib.request.Request(url_api, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=8) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            texto_busca = json.dumps(data)
            emails = extrair_emails_de_texto(texto_busca)
            if emails:
                return emails[0]
    except Exception:
        pass

    empresa_slug = re.sub(r'[^a-zA-Z0-9]', '', nome_clean)
    if empresa_slug:
        return f"contato@{empresa_slug}.com.br"

    return None

def minerar():
    if not os.path.exists(CSV_PATH):
        print("[-] Arquivo esteira_leads.csv nao encontrado.")
        return

    df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')

    if 'Email' not in df.columns:
        df['Email'] = ''
    if 'Tipo_Alvo' not in df.columns:
        df['Tipo_Alvo'] = 'PRIVADO_BR'
    if 'Status' not in df.columns:
        df['Status'] = 'NOVO'

    # Converte explicitamente a coluna Email para texto
    df['Email'] = df['Email'].fillna('').astype(str)

    leads_sem_email = df[~df['Email'].str.contains('@', na=False)]

    if leads_sem_email.empty:
        print("[!] Todos os leads ja possuem e-mail cadastrado.")
        return

    print(f"[+] Minerando e-mails para {len(leads_sem_email)} empresas...")

    for idx, row in leads_sem_email.iterrows():
        empresa = str(row.get('Empresa', ''))
        if not empresa or empresa == 'nan':
            continue

        print(f"[>] Processando e-mail para: {empresa}...")
        email_encontrado = buscar_email_web(empresa)

        if email_encontrado:
            print(f"    [OK] E-mail definido: {email_encontrado}")
            df.loc[idx, 'Email'] = email_encontrado
            df.loc[idx, 'Status'] = 'PRONTO_PARA_CONTATO'
        else:
            print("    [-] Nao foi possivel inferir e-mail.")

        df.to_csv(CSV_PATH, sep=';', index=False, encoding='utf-8-sig')

    print("\n[+] Mineracao e atualizacao concluidas com sucesso!")

if __name__ == "__main__":
    minerar()