# -*- coding: utf-8 -*-
import os
import subprocess
import time

RAIZ_C = r"C:\\"

def mapear_todos_os_nucleos():
    prefixos = ("IOTE", "NUCLEO", "REGULUS", "NEO")
    try:
        pastas = [d for d in os.listdir(RAIZ_C) 
                  if os.path.isdir(os.path.join(RAIZ_C, d)) 
                  and d.upper().startswith(prefixos)]
        return sorted(pastas)
    except Exception:
        return []

def executar_orquestrador():
    ciclo = 1
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        modulos = mapear_todos_os_nucleos()

        print("=" * 85)
        print(f"🏛️ CENTRO DE COMANDO IOTEC - MATRIZ DE NÚCLEOS & REGULUS (CICLO Nº {ciclo})")
        print("=" * 85)
        print(f"[🌐] TOTAL DE MÓDULOS E NÚCLEOS INTEGRADOS EM C:\\ : {len(modulos)} ESTRUTURAS")
        print("-" * 85)

        # Exibe em 3 colunas
        for i in range(0, len(modulos), 3):
            p1 = modulos[i]
            p2 = modulos[i+1] if i+1 < len(modulos) else ""
            p3 = modulos[i+2] if i+2 < len(modulos) else ""
            print(f"  ⚡ {p1:<28} | {p2:<28} | {p3}")

        print("=" * 85)

        # Execução das Salas de Caça Sincronizadas
        print("\n[1/5] ⛏️ AGENTE 1 (MINERAÇÃO): Coletando novos prospects B2B...")
        subprocess.run(["python", r"C:\IOTEC\operario_1_minerador.py"])

        print("\n[2/5] 🧹 AGENTE 2 (HIGIENIZAÇÃO): Validando registros da esteira...")
        subprocess.run(["python", r"C:\IOTEC\operario_2_higienizador.py"])

        print("\n[3/5] 📞 AGENTE 3 (DISPARO & VENDAS): Disparando ofertas com links de cobrança...")
        subprocess.run(["python", r"C:\IOTEC\operario_3_contatador.py"])

        print("\n[4/5] ⏳ AGENTE 4 (MATURAÇÃO): Controlando tempo de cooldown de leads...")
        subprocess.run(["python", r"C:\IOTEC\operario_4_reciclador.py"])

        print("\n[5/5] 💵 AGENTE 5 (AUDITORIA DE CAIXA): Verificando saldo e conciliação...")
        subprocess.run(["python", r"C:\IOTEC\operario_5_financeiro.py"])

        print("\n" + "="*85)
        print(f"[OK] CICLO INTEGRAÇÃO Nº {ciclo} CONCLUÍDO COM {len(modulos)} ESTRUTURAS ATIVAS!")
        print("[⏳] Reiniciando varredura em 60 segundos...")
        print("="*85)
        time.sleep(60)
        ciclo += 1

if __name__ == "__main__":
    executar_orquestrador()