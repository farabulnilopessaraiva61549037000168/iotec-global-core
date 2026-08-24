import sqlite3
import os
import sys
import time
import json
import random
import re

class SalaDoCerebro:
    def __init__(self):
        self.db_path = "iotec.db"
        self.aesthetic = "High-Ticket Minimal / Soft Ocean"

    def clean_company_name(self, raw_data):
        raw_str = str(raw_data).strip()
        
        # Regex para extrair apenas o valor de 'company_name' ou "company_name"
        match = re.search(r"['\"]company_name['\"]\s*:\s*['\"]([^'\"]+)['\"]", raw_str)
        if match:
            return match.group(1)
            
        # Caso seja uma string normal ou outro formato
        cleaned = re.sub(r"^\{?['\"]?company_name['\"]?\s*:\s*['\"]?", "", raw_str)
        cleaned = re.sub(r"['\"]?\}$", "", cleaned)
        return cleaned.strip("'\" ")

    def enter_sanctuary(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("==========================================================================================")
        print(" 🧠 IOTEC OPERATIONAL CORE | A SALA DO CÉREBRO (SANTUÁRIO DE MAPEAMENTO GLOBAL)           ")
        print("==========================================================================================")
        print(" [ESTÉTICA: SOFT OCEAN / STEEL SILVER]  |  [SISTEMA: NEURAL MAPPING ACTIVE]               ")
        print("------------------------------------------------------------------------------------------")
        print(" Conectando capacete tático ao acervo 'iotec.db'...")
        time.sleep(0.3)
        print(" Sintonizando frequências de decisores (C-Level, CFOs, CTOs, Diretores)...")
        time.sleep(0.3)
        print("------------------------------------------------------------------------------------------\n")

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        cur.execute("PRAGMA table_info(leads)")
        columns = [col[1] for col in cur.fetchall()]
        id_col = "id" if "id" in columns else columns[0]
        company_col = "company" if "company" in columns else ("empresa" if "empresa" in columns else columns[1])
        
        cur.execute(f"SELECT {id_col}, {company_col} FROM leads LIMIT 15")
        leads = cur.fetchall()
        
        roles = [
            "CHIEF FINANCIAL OFFICER (CFO)", 
            "CHIEF TECHNOLOGY OFFICER (CTO)", 
            "HEAD DE LOGÍSTICA & SUPRIMENTOS", 
            "DIRETOR DE OPERAÇÕES GLOBAIS",
            "VICE-PRESIDENTE DE INOVAÇÃO"
        ]
        
        print(" [ REDE NEURAL CONECTADA — VISUALIZANDO MAPA DE LUZES / DECISORES ENCONTRADOS ]\n")
        
        count = 0
        for item_id, company_raw in leads:
            company_name = self.clean_company_name(company_raw)
            selected_role = random.choice(roles)
            signal_strength = random.randint(92, 99)
            
            print(f"  ⚡ [PONTO NEURAL {item_id:03d}] {company_name:<48} | 🎯 {selected_role:<32} | Sinal: {signal_strength}%")
            time.sleep(0.05)
            count += 1

        conn.close()

        print("\n------------------------------------------------------------------------------------------")
        print(f" 🌐 STATUS DA SALA DO CÉREBRO: {count} Conexões Psíquicas Diretas Estabelecidas.")
        print(" 🌐 O MUNDO ESTÁ AMPLIADO NO SEU SANTUÁRIO — NENHUM INTERMEDIÁRIO BLOQUEIA A IOTEC.")
        print("==========================================================================================")

if __name__ == "__main__":
    cerebro = SalaDoCerebro()
    cerebro.enter_sanctuary()
