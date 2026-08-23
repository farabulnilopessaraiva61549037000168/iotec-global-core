import os
import sqlite3
import json
from datetime import datetime

ROOT_DIR = r"C:\IOTEC"
REPORT_FILE = os.path.join(ROOT_DIR, "RELATORIO_RASTREAMENTO_OPERACOES.txt")

def log_report(data):
    with open(REPORT_FILE, "a", encoding="utf-8") as f:
        f.write(data + "\n")
    print(data)

def analisar_bancos_sqlite():
    log_report("="*60)
    log_report(f"RASTREAMENTO DE OPERAÇÕES IOTEC - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_report("="*60 + "\n")

    bancos = [f for f in os.listdir(ROOT_DIR) if f.endswith(".db")]
    
    if not bancos:
        log_report("Nenhum banco de dados .db encontrado na raiz.")
        return

    for db_name in bancos:
        db_path = os.path.join(ROOT_DIR, db_name)
        log_report(f"\n[ANALISANDO BANCO: {db_name}]")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Listar tabelas
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tabelas = cursor.fetchall()
            
            for tab in tabelas:
                nome_tabela = tab[0]
                cursor.execute(f"SELECT COUNT(*) FROM {nome_tabela}")
                total_registros = cursor.fetchone()[0]
                log_report(f"  └─ Tabela '{nome_tabela}': {total_registros} registro(s)")
                
                # Se houver registros, exibe os últimos 3 para diagnóstico
                if total_registros > 0:
                    cursor.execute(f"SELECT * FROM {nome_tabela} ORDER BY ROWID DESC LIMIT 3")
                    amostras = cursor.fetchall()
                    for idx, amostra in enumerate(amostras, 1):
                        log_report(f"       Exemplo {idx}: {amostra}")
            conn.close()
        except Exception as e:
            log_report(f"  └─ Erro ao ler {db_name}: {str(e)}")

if __name__ == "__main__":
    if os.path.exists(REPORT_FILE):
        os.remove(REPORT_FILE)
    analisar_bancos_sqlite()
    print(f"\nRelatório gerado com sucesso em: {REPORT_FILE}")
