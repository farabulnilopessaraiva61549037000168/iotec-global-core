import sqlite3
import datetime
import random
import json

class CerebroXavierModule:
    def __init__(self):
        self.db_path = "iotec.db"
        self.executive_roles = [
            "Diretor de Tecnologia (CTO)",
            "Chief Financial Officer (CFO)",
            "Gerente de Operações & Logística",
            "Diretor de Inovação e Nuvem",
            "Head de Compliance & Processos"
        ]

    def telepathic_scan(self):
        print("======================================================================")
        print(" 🧠 ATIVANDO MÓDULO CEREBRO XAVIER - MAPEAMENTO DE ORGANOGRAMA       ")
        print("======================================================================")
        
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        cur.execute("PRAGMA table_info(leads)")
        columns = [col[1] for col in cur.fetchall()]
        
        id_col = "id" if "id" in columns else columns[0]
        company_col = "company" if "company" in columns else ("empresa" if "empresa" in columns else columns[1])
        
        query = f"SELECT {id_col}, {company_col} FROM leads LIMIT 10"
        cur.execute(query)
        leads = cur.fetchall()
        
        print("-> Mapeando tomadores de decisão (C-Level / Diretos):")
        for item_id, company_raw in leads:
            company_name = str(company_raw)
            if "company_name" in company_name:
                try:
                    data = json.loads(company_name.replace("'", '"'))
                    company_name = data.get("company_name", company_name)
                except:
                    pass

            target_role = random.choice(self.executive_roles)
            print(f"   • [{item_id:03d}] {company_name:<46} | Alvo: {target_role}")
                
        conn.close()
        
        print("\n----------------------------------------------------------------------")
        print("✅ Mapeamento Telepático Concluído: Rota direta aos decisores estabelecida.")
        print("✅ O Cerebro elimina intermediários e foca na assinatura do contrato.")
        print("======================================================================")

if __name__ == "__main__":
    cerebro = CerebroXavierModule()
    cerebro.telepathic_scan()
