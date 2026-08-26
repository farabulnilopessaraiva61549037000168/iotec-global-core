import os
import sqlite3
import re

class GatewayKeyChecker:
    def __init__(self):
        self.root_dir = r"C:\IOTEC"
        self.db_path = os.path.join(self.root_dir, "iotec.db")

    def verificar_banco(self):
        print(" [1/2] 🔍 Buscando chaves e tokens gravados no banco `iotec.db`...")
        if not os.path.exists(self.db_path):
            print("  ⚠️ Banco iotec.db não encontrado.")
            return

        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Lista tabelas existentes
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tabelas = [t[0] for t in cursor.fetchall()]
            
            encontrado = False
            for tab in tabelas:
                try:
                    cursor.execute(f"SELECT * FROM {tab}")
                    cols = [description[0] for description in cursor.description]
                    rows = cursor.fetchall()
                    for row in rows:
                        row_str = str(row).lower()
                        if "asaas" in row_str or "remessa" in row_str or "api_key" in row_str or "token" in row_str:
                            print(f"  📌 Registro localizado na tabela [{tab}]:")
                            for col_name, val in zip(cols, row):
                                print(f"     - {col_name}: {val}")
                            encontrado = True
                except Exception:
                    continue
            
            if not encontrado:
                print("  ℹ️ Nenhuma chave explicita do Asaas ou Remessa Online foi encontrada nas tabelas do iotec.db.")
            conn.close()
        except Exception as e:
            print(f"  ⚠️ Erro ao consultar iotec.db: {e}")

    def verificar_arquivos_locais(self):
        print("\n [2/2] 🔍 Buscando arquivos .env, configs e scripts locais por chaves ou tokens...")
        padroes = {
            "ASAAS": [r"asaas[_\-]?api[_\-]?key", r"asaas[_\-]?token", r"\$aact_[a-zA-Z0-9]+"],
            "REMESSA": [r"remessa[_\-]?token", r"remessa[_\-]?key", r"remessa[_\-]?client[_\-]?id"]
        }

        arquivos_analisados = 0
        chaves_encontradas = []

        for root, dirs, files in os.walk(self.root_dir):
            if "BACKUP_ESTAVEL_OFICIAL" in root or ".git" in root or "node_modules" in root:
                continue
            for file in files:
                if file.endswith(('.env', '.py', '.json', '.txt', '.js', '.ini')):
                    filepath = os.path.join(root, file)
                    arquivos_analisados += 1
                    try:
                        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                            conteudo = f.read()
                            for gw, regex_list in padroes.items():
                                for reg in regex_list:
                                    matches = re.findall(reg, conteudo, re.IGNORECASE)
                                    if matches:
                                        chaves_encontradas.append((gw, file, matches[0]))
                    except Exception:
                        continue

        print(f"  ✅ {arquivos_analisados} arquivos de configuração/código analisados.")
        if chaves_encontradas:
            for gw, arq, match in chaves_encontradas:
                print(f"  🔑 [{gw}] Encontrado no arquivo `{arq}`: {match}")
        else:
            print("  ℹ️ Nenhuma chave de API ou Token do Asaas/Remessa foi encontrada nos arquivos locais.")

if __name__ == "__main__":
    checker = GatewayKeyChecker()
    checker.verificar_banco()
    checker.verificar_arquivos_locais()
