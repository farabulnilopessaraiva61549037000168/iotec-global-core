import time
import sqlite3
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='[TELEMETRIA IOTEC] %(asctime)s - %(message)s')

def get_active_pipeline():
    """Lê as empresas reais direto do iotec_kernel.db."""
    conn = sqlite3.connect("C:\\IOTEC\\iotec_kernel.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT razao_social, cnpj, setor, score_potencial, status_qualificacao 
        FROM empresas_qualificadas 
        ORDER BY score_potencial DESC
    """)
    empresas = cursor.fetchall()
    conn.close()
    return empresas

def run_live_telemetry_loop():
    """Injeta a rotação dinâmica de empresas na telemetria de produção."""
    logging.info("=== INICIANDO MOTOR DE TELEMETRIA DINÂMICA DO PIPELINE ===")
    
    ciclo = 1
    while True:
        empresas = get_active_pipeline()
        
        if not empresas:
            logging.warning("Nenhuma empresa encontrada no iotec_kernel.db. Aguardando a Sonda Rover...")
        else:
            print(f"\n--- [CICLO DE TELEMETRIA #{ciclo} - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}] ---")
            for emp in empresas:
                nome, cnpj, setor, score, status = emp
                
                # Simula o avanço do status da esteira conforme o ciclo
                fase_atendimento = "SECRETARIA_TRIAGEM" if ciclo % 2 != 0 else "CONSULTOR_PROPOSTA"
                
                print(f" -> [ALVO ATIVO]: {nome:<35} | CNPJ: {cnpj} | Score: {score}/100")
                print(f"    Setor: {setor:<22} | Estágio: {fase_atendimento} | Status: {status}")
                print("-" * 80)
                time.sleep(2)  # Intervalo de leitura entre alvos
        
        ciclo += 1
        time.sleep(10)  # Tempo de rotação do ciclo completo

if __name__ == "__main__":
    run_live_telemetry_loop()
