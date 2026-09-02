import time
import sqlite3
from datetime import datetime
import zoneinfo

def get_kernel_metrics():
    try:
        conn = sqlite3.connect(r"C:\IOTEC\iotec_kernel.db")
        c = conn.cursor()
        leads = c.execute("SELECT COUNT(*) FROM iotec_investor_leads").fetchone()[0]
        v_room = c.execute("SELECT COUNT(*) FROM iotec_investor_virtual_room").fetchone()[0]
        conn.close()
        return leads, v_room
    except Exception:
        return 0, 0

def gerar_painel_telemetria():
    leads, v_room = get_kernel_metrics()
    
    hubs = [
        ("Brasil (BRT / B3)", "America/Fortaleza", "10:00 - 17:50", "Custódia, Reconciliação & Encerramento"),
        ("EUA (EDT / Delaware)", "America/New_York", "09:30 - 16:00", "Holding, Captação Dólar & Mútuos"),
        ("Reino Unido (BST / LSE)", "Europe/London", "08:00 - 16:30", "Pontes com Fundos Europeus"),
        ("Alemanha (CEST / DAX)", "Europe/Berlin", "09:00 - 17:30", "Processamento Baixa Latência"),
        ("Emirados (GST / Dubai)", "Asia/Dubai", "10:00 - 15:00", "Prospecção Oriente Médio"),
        ("Japão (JST / TSE)", "Asia/Tokyo", "09:00 - 15:00", "Varredura Transacional & Webhooks"),
        ("Cingapura (SGT / SGX)", "Asia/Singapore", "09:00 - 17:00", "Hub Tecnológico Ásia"),
        ("Austrália (AEST / ASX)", "Australia/Sydney", "10:00 - 16:00", "Pico Baileys & Triagem Investidores")
    ]

    print("\033[H\033[J", end="") # Limpa a tela no terminal
    print("=========================================================================================")
    print("          USINA GLOBAL IOTEC — TELEMETRIA DE MERCADOS & NÚCLEO EM TEMPO REAL            ")
    print("=========================================================================================")
    print(f" METRICAS DO KERNEL | Investidores Mapeados: {leads} | Sala Virtual: {v_room} | Status: 100% ONLINE")
    print("-----------------------------------------------------------------------------------------")
    print(f" {'PAÍS / MERCADO':<24} | {'HORA LOCAL':<19} | {'JANELA COMERCIAL':<13} | {'STATUS / AÇÃO DO NÚCLEO'}")
    print("-----------------------------------------------------------------------------------------")

    for nome, fuso, janela, acao in hubs:
        dt = datetime.now(zoneinfo.ZoneInfo(fuso))
        hora_str = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        # Define status operacional com base no horário de pico local (aprox. 09h às 17h)
        hora_int = dt.hour
        if 9 <= hora_int < 17:
            status = "\033[92m[OPERANDO / ABERTO]\033[0m"
        else:
            status = "\033[91m[FECHADO / SEGUNDO PLANO]\033[0m"

        print(f" {nome:<24} | {hora_str} | {janela:<13} | {status} {acao}")

    print("=========================================================================================")
    print(" [USINA IOTEC] Pressione CTRL+C para fechar o reporter. O núcleo segue rodando em 2º plano.")

if __name__ == "__main__":
    try:
        while True:
            gerar_painel_telemetria()
            time.sleep(5) # Atualiza automaticamente a cada 5 segundos
    except KeyboardInterrupt:
        print("\n[IOTEC] Reporter finalizado. Serviço ativo em background.")
