import sqlite3

def verificar_tabelas_leads():
    conn = sqlite3.connect('iotec.db')
    c = conn.cursor()
    tabelas = [t[0] for t in c.execute("SELECT name FROM sqlite_master WHERE type='table';").fetchall()]
    
    print("================================================================================")
    print("            IOTEC B2B — SANEAMENTO E AUDITORIA DE FONTES DE LEADS")
    print("================================================================================")
    print(f"[📋] Tabelas encontradas no iotec.db: {tabelas}\n")
    
    for tab in tabelas:
        if 'sqlite' in tab: continue
        total = c.execute(f"SELECT COUNT(*) FROM {tab}").fetchone()[0]
        colunas = [col[1] for col in c.execute(f"PRAGMA table_info({tab})").fetchall()]
        print(f"📌 TABELA: {tab}")
        print(f"   ├─ Total de Registros: {total:,}")
        print(f"   └─ Estrutura de Colunas: {', '.join(colunas)}")
        
        # Amostra de 1 registro para checar integridade real
        if total > 0:
            amostra = c.execute(f"SELECT * FROM {tab} LIMIT 1").fetchone()
            print(f"   └─ Amostra de Dado Real: {amostra}\n")
        else:
            print("   └─ Tabela vazia.\n")
            
    conn.close()

verificar_tabelas_leads()
