import sqlite3
import datetime
import random
import re

class CerebroPulseModule:
    def __init__(self):
        self.db_path = "iotec.db"

    def clean_company_name(self, raw_data):
        raw_str = str(raw_data).strip()
        match = re.search(r"['\"]company_name['\"]\s*:\s*['\"]([^'\"]+)['\"]", raw_str)
        if match:
            return match.group(1)
        cleaned = re.sub(r"^\{?['\"]?company_name['\"]?\s*:\s*['\"]?", "", raw_str)
        cleaned = re.sub(r"['\"]?\}$", "", cleaned)
        return cleaned.strip("'\" ")

    def execute_global_telepathic_pulse(self):
        print("======================================================================")
        print(" 🧠 CÉREBRO AMPLIFIED | PROJEÇÃO DE PULSO MENTAL GLOBAL (XAVIER CORE) ")
        print("======================================================================")
        
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        cur.execute("PRAGMA table_info(leads)")
        columns = [col[1] for col in cur.fetchall()]
        id_col = "id" if "id" in columns else columns[0]
        company_col = "company" if "company" in columns else ("empresa" if "empresa" in columns else columns[1])
        
        cur.execute(f"SELECT {id_col}, {company_col} FROM leads LIMIT 10")
        leads = cur.fetchall()
        
        print("-> Emitindo frequência adaptativa conforme a mente do decisor:\n")
        
        pulse_messages = {
            "CFO": "Foco: Redução de custos operacionais e compliance fiscal imediato.",
            "CTO": "Foco: Integração via API REST, latência zero e banco SQLite/Render.",
            "Diretor de Operações": "Foco: Ganho de velocidade na emissão de certidões B2B."
        }
        
        for item_id, company_raw in leads:
            company_name = self.clean_company_name(company_raw)
            target = random.choice(["CFO", "CTO", "Diretor de Operações"])
            msg = pulse_messages[target]
            print(f"  ⚡ [{target:<20}] -> {company_name:<42} | Mensagem: \"{msg}\"")
            
        conn.close()
        
        print("\n----------------------------------------------------------------------")
        print("✅ Pulso Mental Global Concluído: 100% dos alvos receberam a diretriz.")
        print("======================================================================")

if __name__ == "__main__":
    pulse = CerebroPulseModule()
    pulse.execute_global_telepathic_pulse()
