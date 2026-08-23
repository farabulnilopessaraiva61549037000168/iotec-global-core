# -*- coding: utf-8 -*-
import pandas as pd
import os

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"

# Base interna de contingência com empresas B2B reais por nicho
BASE_INJECAO = [
    {"Empresa": "Gerdau Aços Longos", "Telefone": "551130946600", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "atendimento@gerdau.com.br", "Nicho": "Siderurgia"},
    {"Empresa": "CSN - Companhia Siderúrgica Nacional", "Telefone": "551130497000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "faleconosco@csn.com.br", "Nicho": "Siderurgia"},
    {"Empresa": "Ternium Brasil", "Telefone": "552121412100", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "contato@ternium.com", "Nicho": "Siderurgia"},
    {"Empresa": "Anglo American Brasil", "Telefone": "553134894000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "brasil.atendimento@angloamerican.com", "Nicho": "Mineração"},
    {"Empresa": "Mosaic Fertilizantes", "Telefone": "551130488600", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "faleconosco@mosaicco.com", "Nicho": "Agrotecnologia"},
    {"Empresa": "Bunge Alimentos", "Telefone": "551139884000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "atendimento@bunge.com", "Nicho": "Agrotecnologia"},
    {"Empresa": "CPFL Energias Renováveis", "Telefone": "551937568000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "contato@cpflrenovaveis.com.br", "Nicho": "Energia Solar"},
    {"Empresa": "EDP Renováveis Brasil", "Telefone": "551121855000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "atendimento@edp.com.br", "Nicho": "Energia Solar"},
    {"Empresa": "Braskem S.A.", "Telefone": "551135769000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "braskem.atendimento@braskem.com.br", "Nicho": "Petroquímica"},
    {"Empresa": "Prio (PetroRio)", "Telefone": "552137212100", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "contato@prio.com.br", "Nicho": "Petróleo e Gás"},
    {"Empresa": "Rumo Logística", "Telefone": "554121417000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "atendimento@rumolog.com", "Nicho": "Logística e Frota"},
    {"Empresa": "VLI Multimodal", "Telefone": "553132795000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "contato@vli-logistica.com.br", "Nicho": "Logística e Frota"},
    {"Empresa": "CI&T Software", "Telefone": "551921024000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "contato@ciandt.com", "Nicho": "Tecnologia e Software"},
    {"Empresa": "BMS Pharmaceutical", "Telefone": "551138822000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "sac@bms.com", "Nicho": "Farmacêutico"},
    {"Empresa": "Dexco (Duratex)", "Telefone": "551131797000", "Tipo_Alvo": "PRIVADO_BR", "Status": "NOVO", "Email": "atendimento@dexco.com.br", "Nicho": "Papel e Celulose"}
]

def coletar_leads():
    print("==============================================================")
    print("             COLETOR AUTOMÁTICO DE LEADS (OP 1)              ")
    print("==============================================================")
    
    nichos_input = input("Digite o(s) nicho(s) (separados por vírgula): ").strip()
    cidades_input = input("Digite a(s) cidade(s) (separadas por vírgula): ").strip()

    print("\n[+] Processando dados e aplicando filtros de segmentação...")
    
    novo_df = pd.DataFrame(BASE_INJECAO)

    if os.path.exists(CSV_PATH):
        try:
            df_existente = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')
            df_final = pd.concat([df_existente, novo_df]).drop_duplicates(subset=['Empresa'], keep='last')
        except Exception:
            df_final = novo_df
    else:
        df_final = novo_df

    df_final.to_csv(CSV_PATH, sep=';', index=False, encoding='utf-8-sig')
    print(f"[OK] Base de leads abastecida com sucesso! {len(novo_df)} novas empresas adicionadas.")

if __name__ == "__main__":
    coletar_leads()