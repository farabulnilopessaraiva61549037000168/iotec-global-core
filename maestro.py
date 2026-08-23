# -*- coding: utf-8 -*-
import subprocess
import time

def rodar_agente(script_path, nome_agente):
    print(f"\n[>>>] SALA OPERACIONAL: Ativando {nome_agente}...")
    try:
        subprocess.run(["python", script_path], check=True)
    except Exception as e:
        print(f"[-] Erro na execucao de {nome_agente}: {e}")

def executar_centro_operacoes():
    ciclo = 1
    while True:
        print("\n" + "="*70)
        print(f"🏛️ CENTRO DE OPERACOES IOTEC - CICLO ININTERRUPTO Nº {ciclo}")
        print("="*70)

        # 1. Agente Minerador
        rodar_agente(r"C:\IOTEC\operario_1_minerador.py", "AGENTE 1 (MINERACAO DE MERCADO)")

        # 2. Agente Higienizador
        rodar_agente(r"C:\IOTEC\operario_2_higienizador.py", "AGENTE 2 (TRATAMENTO DE DADOS)")

        # 3. Agente Contatador (Vendas)
        rodar_agente(r"C:\IOTEC\operario_3_contatador.py", "AGENTE 3 (RELACIONAMENTO & VENDAS)")

        # 4. Agente Reciclador
        rodar_agente(r"C:\IOTEC\operario_4_reciclador.py", "AGENTE 4 (RE-POTENCIALIZACAO DE EMPRESAS)")

        # 5. Agente Auditor Financeiro
        rodar_agente(r"C:\IOTEC\operario_5_financeiro.py", "AGENTE 5 (AUDITORIA FINANCEIRA & CAIXA)")

        print("\n[+] Operacao do ciclo finalizada. Todas as salas em atividade.")
        print("[⏳] Aguardando 60 segundos para reiniciar varredura de mercado...")
        time.sleep(60)
        ciclo += 1

if __name__ == "__main__":
    executar_centro_operacoes()