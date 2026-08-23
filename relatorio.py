# -*- coding: utf-8 -*-
import pandas as pd
import os

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"

def gerar_relatorio():
    if not os.path.exists(CSV_PATH):
        print("[-] Arquivo esteira_leads.csv nao encontrado.")
        return

    df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')
    
    total = len(df)
    contatados = len(df[df['Status'] == 'CONTATADO'])
    followups = len(df[df['Status'] == 'FOLLOWUP_ENVIADO'])
    prontos = len(df[df['Status'] == 'PRONTO_PARA_CONTATO'])
    novos = len(df[df['Status'] == 'NOVO'])

    print("\n==============================================================")
    print("                IOTEC - PAINEL DE MÉTRICAS B2B                ")
    print("==============================================================")
    print(f" Total de Leads na Base:       {total}")
    print(f" [✓] Primeiras Abordagens:     {contatados}")
    print(f" [🔄] Follow-ups Enviados:      {followups}")
    print(f" [⏳] Prontos para Envio:       {prontos}")
    print(f" [★] Novos / A Minerar:         {novos}")
    print("--------------------------------------------------------------")
    
    if 'Nicho' in df.columns:
        print(" Distribuição por Segmento/Nicho:")
        nichos = df['Nicho'].value_counts()
        for nicho, qtd in nichos.items():
            print(f"   • {nicho}: {qtd}")
    print("==============================================================\n")

if __name__ == "__main__":
    gerar_relatorio()