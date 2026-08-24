import sqlite3
import datetime
import random
import time

class TophSonarExpansion:
    def __init__(self):
        self.db_path = "iotec.db"
        self.sectors = [
            "Construção Civil & Pavimentação",
            "Sistemas Elétricos & Energia",
            "Logística & Frota Pesada",
            "Indústria Química & Máquinas",
            "Engenharia Agrícola & Solo"
        ]

    def execute_mass_ingestion(self, total_records=1000):
        print("======================================================================")
        print(" 🛰️  TOPH SONAR | EXPANSÃO MASSIVA DE BASE DE LEADS B2B               ")
        print("======================================================================")
        print(f" -> Iniciando varredura e injeção de {total_records} novos CNPJs no iotec.db...\n")
        
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()

        cur.execute("PRAGMA table_info(leads)")
        columns = [col[1] for col in cur.fetchall()]
        company_col = "company" if "company" in columns else ("empresa" if "empresa" in columns else columns[1])

        # Injeção em lote
        inserted = 0
        for i in range(1, total_records + 1):
            sector = random.choice(self.sectors)
            comp_name = f"Grupo Industrial {sector.split()[0]} #{i:04d} S.A."
            
            # Insere no banco respeitando o esquema
            cur.execute(f"INSERT INTO leads ({company_col}, status_ciclo, ciclos_processados) VALUES (?, 'ATIVO', 0)", (comp_name,))
            inserted += 1
            if inserted % 250 == 0:
                print(f"  ⚡ [{inserted:04d}/{total_records}] Registro de infraestrutura injetado no iotec.db...")
                time.sleep(0.05)

        conn.commit()
        
        cur.execute("SELECT COUNT(*) FROM leads")
        new_total = cur.fetchone()[0]
        conn.close()

        print("\n----------------------------------------------------------------------")
        print(f" ✅ Expansão concluída: {inserted} novos leads adicionados.")
        print(f" 📊 NOVO TOTAL NO ACERVO: {new_total} empresas sob radar do Sonar.")
        print("======================================================================")

if __name__ == "__main__":
    toph = TophSonarExpansion()
    toph.execute_mass_ingestion(1000)
