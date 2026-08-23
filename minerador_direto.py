# -*- coding: utf-8 -*-
import requests
import time
import re
import argparse
import urllib.parse
import csv
import os
from datetime import datetime

def limpar_telefone(telefone_raw):
    if not telefone_raw:
        return ""
    return re.sub(r"\D", "", str(telefone_raw))

def validar_e_classificar_telefone(telefone_raw):
    num = limpar_telefone(telefone_raw)
    if len(num) in [12, 13] and num.startswith("55"):
        num = num[2:]

    if len(num) in [10, 11]:
        ddd = num[:2]
        corpo = num[2:]
        if (len(corpo) == 9 and corpo.startswith("9")) or (len(corpo) == 8 and corpo[0] in ["8", "9"]):
            return {"valido": True, "tipo": "MOVEL", "numero_formatado": f"55{ddd}{corpo}"}
        else:
            return {"valido": False, "tipo": "FIXO/PABX", "numero_formatado": num}
            
    return {"valido": False, "tipo": "INVALIDO", "numero_formatado": num}

def carregar_numeros_existentes(arquivo_saida):
    existentes = set()
    if os.path.isfile(arquivo_saida):
        try:
            with open(arquivo_saida, mode='r', encoding='utf-8-sig') as f:
                reader = csv.reader(f, delimiter=';')
                header = next(reader, None)
                for row in reader:
                    if len(row) >= 4:
                        existentes.add(row[3].strip())
        except Exception:
            pass
    return existentes

def buscar_leads_open_scraping(termo_busca):
    variacoes = [
        f'"{termo_busca}" whatsapp',
        f'"{termo_busca}" contato'
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    leads = []
    unicos = set()

    for query in variacoes:
        termo_encoded = urllib.parse.quote(query)
        url = f"https://html.duckduckgo.com/html/?q={termo_encoded}"

        try:
            response = requests.get(url, headers=headers, timeout=10)
            regex_tel = r'(?:\+?55\s?)?(?:\(?\d{2}\)?\s?)?(?:9?\d{4}[-\s]?\d{4})'
            telefones_encontrados = re.findall(regex_tel, response.text)
            
            for tel in telefones_encontrados:
                limpo = limpar_telefone(tel)
                if len(limpo) in [12, 13] and limpo.startswith("55"):
                    limpo = limpo[2:]
                
                if limpo not in unicos and len(limpo) in [10, 11]:
                    unicos.add(limpo)
                    leads.append({
                        "termo": termo_busca,
                        "nome": f"Lead Comercial ({termo_busca})",
                        "telefone_bruto": tel
                    })
            time.sleep(0.5)
        except Exception as e:
            print(f"Erro na conexao de busca: {str(e)}")

    return leads

def salvar_csv(leads_ouro, arquivo_saida="C:\\IOTEC\\leads_ouro.csv"):
    file_exists = os.path.isfile(arquivo_saida)
    
    with open(arquivo_saida, mode='a', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f, delimiter=';')
        if not file_exists:
            writer.writerow(["Data_Extracao", "Termo_Busca", "Nome_Lead", "WhatsApp_Formatado", "Status"])
            
        data_hoje = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for lead in leads_ouro:
            writer.writerow([data_hoje, lead["termo"], lead["nome"], lead["whatsapp"], "OURO_VALIDADO"])

def executar_mineracao(termos, arquivo_saida="C:\\IOTEC\\leads_ouro.csv"):
    print("\n" + "="*70)
    print("IOTEC - REFINARIA DE DADOS (v6.2 - UTF8 CLEAN & ANTI-DUPLICIDADE)")
    print(f"TOTAL DE TERMOS A PROCESSAR: {len(termos)}")
    print("="*70 + "\n")

    numeros_ja_salvos = carregar_numeros_existentes(arquivo_saida)
    print(f"[BASE EXISTENTE] {len(numeros_ja_salvos)} numeros ja registrados no CSV.\n")

    total_ouro_geral = []
    total_duplicados = 0
    total_cascalho_geral = 0

    for idx, termo in enumerate(termos, 1):
        termo_limpo = termo.strip().replace('\ufeff', '')
        print(f"[{idx}/{len(termos)}] Minerando: '{termo_limpo}'...")
        leads = buscar_leads_open_scraping(termo_limpo)
        
        ouro_termo = []

        for item in leads:
            nome = item["nome"]
            tel_bruto = item["telefone_bruto"]
            classificacao = validar_e_classificar_telefone(tel_bruto)

            if classificacao["valido"] and classificacao["tipo"] == "MOVEL":
                numero_fmt = classificacao['numero_formatado']
                
                if numero_fmt in numeros_ja_salvos:
                    print(f"  [SKIP DUPLICADO] Whats: {numero_fmt}")
                    total_duplicados += 1
                else:
                    print(f"  --> [NOVO OURO] Whats: {numero_fmt}")
                    obj_ouro = {
                        "termo": termo_limpo,
                        "nome": nome,
                        "whatsapp": numero_fmt
                    }
                    ouro_termo.append(obj_ouro)
                    total_ouro_geral.append(obj_ouro)
                    numeros_ja_salvos.add(numero_fmt)
            else:
                total_cascalho_geral += 1

        if ouro_termo:
            salvar_csv(ouro_termo, arquivo_saida)
            print(f"  [+] {len(ouro_termo)} novos leads salvos em {arquivo_saida}")
        else:
            print("  [-] Nenhum novo WhatsApp inedito para este termo.")
        
        print("-" * 50)
        time.sleep(1)

    print("\n" + "="*70)
    print("RELATORIO FINAL DE REFINO EM LOTE (v6.2):")
    print(f"Novos Leads de Ouro Adicionados: {len(total_ouro_geral)}")
    print(f"Leads Duplicados Descartados: {total_duplicados}")
    print(f"Cascalho Eliminado: {total_cascalho_geral}")
    print(f"Arquivo CSV Atualizado: {arquivo_saida}")
    print("="*70 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IOTEC Lead Miner Direct - v6.2")
    parser.add_argument("--termo", type=str, help="Termo unico de busca")
    parser.add_argument("--lista", type=str, help="Caminho para arquivo .txt com lista de termos")
    parser.add_argument("--saida", type=str, default="C:\\IOTEC\\leads_ouro.csv", help="Caminho do CSV")
    args = parser.parse_args()

    termos_processar = []

    if args.lista and os.path.exists(args.lista):
        with open(args.lista, "r", encoding="utf-8-sig") as f:
            termos_processar = [line.strip() for line in f if line.strip()]
    elif args.termo:
        termos_processar = [args.termo]
    else:
        termos_processar = ["Imobiliaria em Campinas", "Restaurante em Campinas"]

    executar_mineracao(termos=termos_processar, arquivo_saida=args.saida)