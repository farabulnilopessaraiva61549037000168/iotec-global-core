import sqlite3
from datetime import datetime
import zoneinfo

FUSOS_E_PAISES = {
    "BR": {"fuso": "America/Fortaleza", "ddi": "55", "lang": "pt"},
    "US": {"fuso": "America/New_York", "ddi": "1", "lang": "en"},
    "DE": {"fuso": "Europe/Berlin", "ddi": "49", "lang": "de"},
    "AE": {"fuso": "Asia/Dubai", "ddi": "971", "lang": "ar"},
    "JP": {"fuso": "Asia/Tokyo", "ddi": "81", "lang": "ja"},
    "AU": {"fuso": "Australia/Sydney", "ddi": "61", "lang": "en"}
}

def inicializar_banco_estrategico():
    conn = sqlite3.connect(r"C:\IOTEC\iotec_kernel.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS iotec_corporate_leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT NOT NULL,
            pais_codigo TEXT NOT NULL,
            telefone TEXT NOT NULL,
            setor TEXT,
            score_match REAL,
            status TEXT DEFAULT 'MAPEADO'
        )
    ''')
    
    c.execute("SELECT COUNT(*) FROM iotec_corporate_leads")
    if c.fetchone()[0] == 0:
        leads_iniciais = [
            ("Bossa Invest", "BR", "5511999991111", "Venture Capital / SaaS", 94.5),
            ("Delaware Tech Partners", "US", "13025550123", "Holding & Cloud", 98.0),
            ("Berlin Innovation Hub", "DE", "49301234567", "B2B Automation", 91.2),
            ("Tokyo Global Ventures", "JP", "81312345678", "Enterprise Tech", 88.7),
            ("Sydney Capital Group", "AU", "61298765432", "Growth Fund", 93.4)
        ]
        c.executemany('''
            INSERT INTO iotec_corporate_leads (empresa, pais_codigo, telefone, setor, score_match)
            VALUES (?, ?, ?, ?, ?)
        ''', leads_iniciais)
        conn.commit()
    conn.close()

def calcular_janela_e_prioridade():
    conn = sqlite3.connect(r"C:\IOTEC\iotec_kernel.db")
    c = conn.cursor()
    leads = c.execute("SELECT id, empresa, pais_codigo, telefone, setor, score_match, status FROM iotec_corporate_leads ORDER BY score_match DESC").fetchall()
    
    print("\n=========================================================================================")
    print("      USINA IOTEC — NÚCLEO DE NAVEGAÇÃO ESTRATÉGICA & PROSPECÇÃO HUMANIZADA (24/7)       ")
    print("=========================================================================================")
    print(f" {'EMPRESA ALVO':<24} | {'PAÍS':<4} | {'HORA LOCAL':<19} | {'SCORE':<6} | {'STATUS / AÇÃO ESTRATÉGICA'}")
    print("-----------------------------------------------------------------------------------------")

    for l_id, emp, pais, tel, setor, score, status in leads:
        info_pais = FUSOS_E_PAISES.get(pais, FUSOS_E_PAISES["US"])
        dt_local = datetime.now(zoneinfo.ZoneInfo(info_pais["fuso"]))
        hora_str = dt_local.strftime("%Y-%m-%d %H:%M:%S")
        hora_int = dt_local.hour

        if 9 <= hora_int < 17:
            janela = "\033[92m[JANELA ABERTA]\033[0m"
            acao = "Aproximação Executiva Ativa"
        else:
            janela = "\033[93m[AGUARDANDO HORA UTIL]\033[0m"
            acao = "Enfileirado para abertura do fuso"

        print(f" {emp:<24} | {pais:<4} | {hora_str} | {score}% | {janela} {acao}")

    print("=========================================================================================\n")
    conn.close()

if __name__ == "__main__":
    inicializar_banco_estrategico()
    calcular_janela_e_prioridade()
