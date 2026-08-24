import sqlite3
import datetime
import time
import os
import sys
import re

def clean_company_name(raw_data):
    raw_str = str(raw_data).strip()
    match = re.search(r"['\"]company_name['\"]\s*:\s*['\"]([^'\"]+)['\"]", raw_str)
    if match:
        return match.group(1)
    cleaned = re.sub(r"^\{?['\"]?company_name['\"]?\s*:\s*['\"]?", "", raw_str)
    cleaned = re.sub(r"['\"]?\}$", "", cleaned)
    return cleaned.strip("'\" ")

def render_chronometer(seconds_to_wait):
    print("\n [ ⏱️ CRONÔMETRO DE INTERVALO ENTRE CICLOS ]")
    for remaining in range(seconds_to_wait, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer_str = f"{mins:02d}:{secs:02d}"
        sys.stdout.write(f"\r  ⏳ Próxima varredura em: [{timer_str}] — Mantenha o terminal ativo...")
        sys.stdout.flush()
        time.sleep(1)
    sys.stdout.write("\r  ✅ Cronômetro zerado! Pronto para novo ciclo operacional.           \n")

def run_sync_pipeline():
    start_time = datetime.datetime.now()
    
    print("======================================================================")
    print(" ⏳ IOTEC AUTOMATED PIPELINE | INÍCIO DO CICLO OPERACIONAL            ")
    print("======================================================================")
    print(f" 🕒 MARCA DE TEMPO INICIAL : {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("----------------------------------------------------------------------\n")

    conn = sqlite3.connect("iotec.db")
    cur = conn.cursor()

    cur.execute("PRAGMA table_info(leads)")
    columns = [col[1] for col in cur.fetchall()]
    
    if "status_ciclo" not in columns:
        cur.execute("ALTER TABLE leads ADD COLUMN status_ciclo TEXT DEFAULT 'ATIVO'")
    if "ciclos_processados" not in columns:
        cur.execute("ALTER TABLE leads ADD COLUMN ciclos_processados INTEGER DEFAULT 0")
    conn.commit()

    cur.execute("UPDATE leads SET status_ciclo = 'EM_SEGUNDO_PLANO' WHERE status_ciclo = 'ATIVO' AND ciclos_processados >= 1")
    cur.execute("UPDATE leads SET ciclos_processados = ciclos_processados + 1 WHERE status_ciclo != 'DESCONSIDERADO'")
    cur.execute("UPDATE leads SET status_ciclo = 'DESCONSIDERADO' WHERE ciclos_processados > 5")
    conn.commit()

    id_col = "id" if "id" in columns else columns[0]
    company_col = "company" if "company" in columns else ("empresa" if "empresa" in columns else columns[1])
    
    cur.execute(f"SELECT {id_col}, {company_col}, status_ciclo, ciclos_processados FROM leads WHERE status_ciclo != 'DESCONSIDERADO' LIMIT 10")
    current_batch = cur.fetchall()

    print(" [ ROTAÇÃO DE LEADS E CICLO DE PROSPECÇÃO ACTIVE ]\n")
    for item_id, company_raw, status_ciclo, ciclos in current_batch:
        comp_str = clean_company_name(company_raw)[:42]
        print(f"  • [{item_id:03d}] {comp_str:<42} | Status: {status_ciclo:<16} | Ciclo: #{ciclos}")
        time.sleep(0.04)

    conn.close()

    end_time = datetime.datetime.now()
    duration = (end_time - start_time).total_seconds()

    print("\n----------------------------------------------------------------------")
    print(f" 🕒 MARCA DE TEMPO FINAL   : {end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f" ⏱️  DURAÇÃO DO PROCESSAMENTO: {duration:.2f} segundos")
    print("======================================================================")

    render_chronometer(5)

if __name__ == "__main__":
    run_sync_pipeline()
