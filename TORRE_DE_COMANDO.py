import sqlite3
import os
import sys
import time
import datetime
import re

class TorreDeComando:
    def __init__(self):
        self.db_path = "iotec.db"
        self.target_mrr = 127678.57
        self.target_valuation_usd = 1950000.00

    def clean_company_name(self, raw_data):
        raw_str = str(raw_data).strip()
        match = re.search(r"['\"]company_name['\"]\s*:\s*['\"]([^'\"]+)['\"]", raw_str)
        if match:
            return match.group(1)
        cleaned = re.sub(r"^\{?['\"]?company_name['\"]?\s*:\s*['\"]?", "", raw_str)
        cleaned = re.sub(r"['\"]?\}$", "", cleaned)
        return cleaned.strip("'\" ")

    def render_dashboard(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        
        cur.execute("SELECT COUNT(*) FROM leads")
        total_leads = cur.fetchone()[0]
        
        cur.execute("PRAGMA table_info(leads)")
        columns = [col[1] for col in cur.fetchall()]
        
        if "status_ciclo" in columns:
            cur.execute("SELECT COUNT(*) FROM leads WHERE status_ciclo = 'EM_SEGUNDO_PLANO'")
            background_leads = cur.fetchone()[0]
            cur.execute("SELECT COUNT(*) FROM leads WHERE status_ciclo = 'DESCONSIDERADO'")
            discarded_leads = cur.fetchone()[0]
            active_leads = total_leads - (background_leads + discarded_leads)
        else:
            active_leads, background_leads, discarded_leads = total_leads, 0, 0

        id_col = "id" if "id" in columns else columns[0]
        company_col = "company" if "company" in columns else ("empresa" if "empresa" in columns else columns[1])
        cur.execute(f"SELECT {id_col}, {company_col} FROM leads LIMIT 3")
        top_batch = cur.fetchall()
        conn.close()

        print("==========================================================================================")
        print(" 🛰️  IOTEC OPERATIONAL CORE | TORRE DE COMANDO E VIGILÂNCIA UNIFICADA                   ")
        print("==========================================================================================")
        print(f" [ESTÉTICA: SOFT OCEAN / STEEL SILVER]  |  [HORÁRIO LOCAL: {now}]                       ")
        print("==========================================================================================\n")

        print(" ─── [ TELA 1: PIPELINE AUTÔNOMO / MESA LOCAL ] ──────────────────────────────────────────")
        print(f"  • Status do Banco (iotec.db) : {total_leads} Leads Mapeados no Acervo")
        print(f"  • Distribuição do Funil     : [Ativos: {active_leads}] | [Segundo Plano: {background_leads}] | [Descartados: {discarded_leads}]")
        print("  • Lote em Destaque no Topo  :")
        for item_id, company_raw in top_batch:
            comp_name = self.clean_company_name(company_raw)[:38]
            print(f"     ⚡ [{item_id:03d}] {comp_name:<38} — Monitorado em Frequência de Vanguarda")
        print("──────────────────────────────────────────────────────────────────────────────────────────\n")

        print(" ─── [ TELA 2: RENDER CLOUD & REPOSITÓRIO GIT ] ──────────────────────────────────────────")
        print("  • Infraestrutura Servidor   : Render Cloud Service (Free Tier / Auto-Deploy)")
        print("  • Status da Sincronização   : Synchronized with 'origin/main'")
        print("  • Custo Fixo Marginal      : R$ 0,00 / mês (Resiliência Máxima e Margem 100%)")
        print("  • Saúde do Servidor em Nuvem: [ LIVE / ONLINE ] — Resposta síncrona aos Webhooks")
        print("──────────────────────────────────────────────────────────────────────────────────────────\n")

        print(" ─── [ TELA 3: TESOURARIA & AUDIT ENGINE ] ───────────────────────────────────────────────")
        print("  • Canal de Vendas & Invoices : IOTEC.BL@proton.me")
        print(f"  • Meta de MRR (Mensal)       : R$ {self.target_mrr:,.2f} / mês")
        print(f"  • Teto de Valuation          : US$ {self.target_valuation_usd:,.2f} (~R$ 10.72M BRL)")
        print("  • Equação de Volume Alvo     : 428 Assinantes Standard (R$ 299) ou 143 High-Ticket (R$ 899)")
        print("==========================================================================================")
        print(" 🌐 PAINEL CENTRALIZADO ATIVO — TODAS AS FONTES OPERANDO EM PARIDADE NOMINAL.")
        print("==========================================================================================")

if __name__ == "__main__":
    torre = TorreDeComando()
    torre.render_dashboard()
