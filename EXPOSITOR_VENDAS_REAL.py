import sqlite3

def expor_vendas_e_abordagens():
    print("=" * 80)
    print("      IOTEC B2B — MONITOR E EXPOSITOR DE VENDAS E ABORDAGENS EM TEMPO REAL")
    print("=" * 80)
    
    try:
        conn = sqlite3.connect('iotec.db')
        c = conn.cursor()
        
        # Obtém os nomes das colunas da tabela leads
        colunas = [col[1] for col in c.execute("PRAGMA table_info(leads)").fetchall()]
        total_leads = c.execute("SELECT COUNT(*) FROM leads").fetchone()[0]
        
        print(f"\n[📊] TOTAL DE CNPJs DISPONÍVEIS NO ACERVO NACIONAL: {total_leads:,}")
        print(f"[📋] ESTRUTURA DE COLUNAS DETECTADA: {', '.join(colunas)}")
        print("\n[🎯] EMPRESAS NA FILA PRIORITÁRIA DE ABORDAGEM B2B:")
        print("-" * 80)
        
        # Busca até 5 empresas utilizando todas as colunas dinamicamente
        amostra = c.execute("SELECT * FROM leads LIMIT 5").fetchall()
        for idx, emp in enumerate(amostra, 1):
            print(f" 🏢 Target #{idx}:")
            for col_nome, valor in zip(colunas, emp):
                print(f"    ├─ {col_nome.upper()}: {valor}")
            print("-" * 80)
            
        conn.close()
    except Exception as e:
        print(f"[!] Erro ao acessar iotec.db: {e}")

    print("\n[🔍] VALIDAÇÃO DA ESTEIRA DE DISPARO (TRAVA DE REALIDADE):")
    print("-" * 80)
    print(" ⚠️  STATUS DO DISPARADOR WHATSAPP : AGUARDANDO CONEXÃO DE API LOCAL")
    print(" ⚠️  ENVIOS CONFIRMADOS COM HASH   : 0 (Aguardando chave/gateway para início real)")
    print(" ℹ️  REGRA DE SEGURANÇA           : Nenhuma venda é computada sem confirmação HTTP 200.")
    print("-" * 80)

expor_vendas_e_abordagens()
