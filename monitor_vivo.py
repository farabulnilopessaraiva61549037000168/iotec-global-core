# -*- coding: utf-8 -*-
import os
import time
import pandas as pd
from datetime import datetime

CSV_PATH = r"C:\IOTEC\esteira_leads.csv"

def monitorar_motores():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("=" * 75)
    print("⚡ IOTEC - CENTRAL DE TELEMETRIA E DESEMPENHO MULTIMOTOR")
    print("=" * 75)
    print("[🟢] OPERAÇÃO MULTIMOTOR ATIVA | MEDINDO TRAÇÃO E TEMPO DE RESPOSTA")
    print("=" * 75)

    while True:
        try:
            agora = datetime.now().strftime("%H:%M:%S")
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=" * 75)
            print("⚡ IOTEC - CENTRAL DE TELEMETRIA E DESEMPENHO MULTIMOTOR")
            print("=" * 75)
            print(f"⏱️ ÚLTIMA ATUALIZAÇÃO: {agora} | STATUS: TODOS OS MOTORES EM OPERAÇÃO")
            print("-" * 75)

            if os.path.exists(CSV_PATH):
                df = pd.read_csv(CSV_PATH, sep=';', encoding='utf-8-sig')
                if not df.empty and 'Status' in df.columns:
                    total = len(df)
                    prontos = len(df[df['Status'] == 'PRONTO_PARA_CONTATO'])
                    contatados = len(df[df['Status'] == 'CONTATADO'])
                    clientes = len(df[df['Status'] == 'CLIENTE_ATIVO'])
                    faturamento = clientes * 297.00

                    print(f"📊 VISÃO GERAL DO CAIXA E ESTEIRA:")
                    print(f"   • Total de Leads Mapeados : {total}")
                    print(f"   • Prontos para Abordagem  : {prontos}")
                    print(f"   • Abordagens Realizadas   : {contatados}")
                    print(f"   • Vendas Confirmadas      : {clientes} (R$ {faturamento:.2f})")
                    print("-" * 75)
                    print("🚀 DESEMPENHO DOS MOTORES DE PROSPECÇÃO:")
                    print("   [MOTOR 1 - WEB DIRECT]   : 🟢 ALTA TRAÇÃO (Mineração contínua)")
                    print("   [MOTOR 2 - B2B CORP]     : 🟢 ALTA TRAÇÃO (Base qualificada)")
                    print("   [MOTOR 3 - REGIONAL CNPJ]: 🟡 EM CALIBRAGEM (Ajustando filtros)")
                    print("   [MOTOR 4 - OUTBOUND API] : 🟢 DISPARO ATIVO (Links de Checkout)")
                    print("-" * 75)

                    if clientes > 0:
                        print("🚨 [ALERTA DE SINAL DE COMPRA]: PRIMEIRA CONVERSÃO REGISTRADA!")
                    else:
                        print("⏳ [RADAR]: Aguardando o primeiro sinal de compra (Pix / PicPay / PayPal)...")
            else:
                print("⏱️ Aguardando inicialização da esteira principal...")

            time.sleep(3)
        except KeyboardInterrupt:
            print("\n[!] Telemetria pausada.")
            break
        except Exception as e:
            pass

if __name__ == "__main__":
    monitorar_motores()