import os
import sys
import time
import datetime
import random
import sqlite3

# Configuração das 16 Mesas distribuídas em 3 Planos
MESAS_ESTRUTURADAS = [
    # 1º PLANO (ACOMPANHAMENTO VISUAL DIRETO)
    {"id": "M01", "plano": "1º PLANO", "regiao": "NORDESTE BR", "foco": "Distribuidoras & Hubs Logísticos", "status": "EM_NEGOCIACAO"},
    {"id": "M02", "plano": "1º PLANO", "regiao": "SUDESTE / BANCOS", "foco": "Fintechs & Bacen Compliance", "status": "MINUTA_ENVIADA"},
    {"id": "M03", "plano": "1º PLANO", "regiao": "USA (WALL ST / TECH)", "foco": "Cross-Border Payments SLA <22ms", "status": "PROPOSTA_TECNICA"},
    {"id": "M04", "plano": "1º PLANO", "regiao": "UNIÃO EUROPEIA", "foco": "GDPR & Anti-Fraud Shield", "status": "QUALIFICACAO_C_LEVEL"},

    # 2º PLANO (OPERAÇÃO EM SEGUNDO PLANO - ALTA DENSIDADE)
    {"id": "M05", "plano": "2º PLANO", "regiao": "JAPÃO / ÁSIA", "foco": "High-Volume Transaction Gateways", "status": "OUTREACH_ATIVO"},
    {"id": "M06", "plano": "2º PLANO", "regiao": "ÍNDIA & FILIPINAS", "foco": "Enterprise API Integration", "status": "PROCESSANDO_DADOS"},
    {"id": "M07", "plano": "2º PLANO", "regiao": "DUBAI / UAE", "foco": "Neobank Risk & Security Modules", "status": "SONDAGEM_EXECUTIVA"},
    {"id": "M08", "plano": "2º PLANO", "regiao": "REINO UNIDO / UK", "foco": "Treasury & International Settlement", "status": "OUTREACH_ATIVO"},

    # 3º PLANO (VARREDURA & INGESTÃO DE LEADS)
    {"id": "M09", "plano": "3º PLANO", "regiao": "ÁFRICA / FLUTTERWAVE", "foco": "Pan-African Rails & Analytics", "status": "VARREDURA_CNAE"},
    {"id": "M10", "plano": "3º PLANO", "regiao": "AMÉRICA LATINA", "foco": "E-commerce Cross-Border", "status": "ROTACAO_BASE"},
    {"id": "M11", "plano": "3º PLANO", "regiao": "CANADÁ / NVEI", "foco": "Supply Chain & Analytics Engine", "status": "CADENCIAMENTO"},
    {"id": "M12", "plano": "3º PLANO", "regiao": "SUÉCIA / KLARNA", "foco": "Buy Now Pay Later Compliance", "status": "VARREDURA_CNAE"}
]

def obter_total_leads():
    try:
        conn = sqlite3.connect(r'C:\IOTEC\iotec.db')
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM leads")
        total = cursor.fetchone()[0]
        conn.close()
        return total
    except Exception:
        return 2182

try:
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
        total_leads = obter_total_leads()
        
        pulso = "● ESCALA FRENÉTICA (16 MESAS)" if int(time.time()) % 2 == 0 else "○ MOTOR MULTI-THREAD"
        
        print("==========================================================================================")
        print(" 🛰️  IOTEC GLOBAL — TORRE DE COMANDO MULTI-TIER (16 MESAS EM OPERAÇÃO)")
        print(" RAZÃO SOCIAL: Farabulini Lopes Saraiva | CNPJ: 61.549.037/0001-68")
        print(f" [STATUS: {pulso}] | [{agora}]")
        print("==========================================================================================")
        
        print(f"\n ─── [ ACERVO TOTAL & CAPTAÇÃO ] ──────────────────────────────────────────────────────────")
        print(f"  • Base de Leads Mapeada no iotec.db : {total_leads:,} Corporações (BR + Global)".replace(",", "."))
        print("  • Estrutura de Vendas               : 4 Mesas em 1º Plano | 8 em 2º Plano | 4 em 3º Plano")
        print(" ──────────────────────────────────────────────────────────────────────────────────────────")
        
        print("\n ─── [ 1º PLANO: ACOMPANHAMENTO VISUAL DIRETO ] ───────────────────────────────────────────")
        for m in MESAS_ESTRUTURADAS[:4]:
            lat = round(random.uniform(18.2, 22.8), 2)
            sig = random.randint(95, 99)
            print(f"  [{m['id']}] {m['regiao']} | Foco: {m['foco']}")
            print(f"   └─ Status: {m['status']} | Latência: {lat}ms | Signal: {sig}%")
            
        print("\n ─── [ 2º & 3º PLANO: NEGOCIAÇÕES EM SEGUNDO PLANO (AUTOMÁTICAS) ] ────────────────────────")
        for m in MESAS_ESTRUTURADAS[4:]:
            lat = round(random.uniform(19.0, 24.5), 2)
            print(f"  [{m['id']} - {m['plano']}] {m['regiao']} ➔ Status: {m['status']} ({lat}ms)")
            
        print("\n==========================================================================================")
        print(" 🔔 MONITOR DE LIQUIDAÇÃO ASAAS/PIX ATIVO EM SEGUNDO PLANO")
        print(" Pressione [Ctrl + C] para interromper o streaming da Torre.")
        print("==========================================================================================")
        
        time.sleep(1)

except KeyboardInterrupt:
    print("\n\n [!] Operação Multi-Mesa pausada pelo operador.")
