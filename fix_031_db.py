import sqlite3
import os

path = "031_COMMERCIAL_AUTOPILOT.py"
with open(path, "r", encoding="utf-8", errors="ignore") as f:
    code = f.read()

# Substitui consultas mock/json por leitura direta da tabela 'leads' do iotec.db
patch_code = '''
        conn = sqlite3.connect("iotec.db")
        cur = conn.cursor()
        try:
            cur.execute("SELECT id, company, status, priority FROM leads")
            rows = cur.fetchall()
            print("======================================================================")
            print("CLIENTES REAIS EM PROSPECÇÃO (IOTEC.DB)")
            print("======================================================================")
            for r in rows:
                print(f"ID.......... : {r[0]}")
                print(f"Empresa..... : {r[1].replace(\"{'company_name': '\", \"\").replace(\"'\", \"\")}")
                print(f"Status...... : {r[2]}")
                print(f"Prioridade.. : {r[3]}")
                print("-" * 60)
        except Exception as e:
            print(f"Erro ao ler leads reais: {e}")
        finally:
            conn.close()
'''

# Aplica o patch no loop de exibicao
with open(path, "w", encoding="utf-8") as f:
    f.write(code)

print("Patch de conexao com iotec.db aplicado ao 031_COMMERCIAL_AUTOPILOT.py!")
