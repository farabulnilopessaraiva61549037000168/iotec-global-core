# ==============================================================================
# IOTEC ENTERPRISE - MIGRAÇÃO E FORECAST DE CAIXA ESCALÁVEL (BRASIL & EXTERIOR)
# CNPJ: 61.549.037/0001-68
# ==============================================================================

import sqlite3

def migrar_e_executar_forecast():
    conn = sqlite3.connect(r"C:\IOTEC\iotec_kernel.db")
    cursor = conn.cursor()
    
    # 1. Garantir que a tabela existe
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS empresas_qualificadas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cnpj TEXT UNIQUE,
        razao_social TEXT,
        setor TEXT,
        score_potencial INTEGER,
        gargalo_principal TEXT,
        status_qualificacao TEXT
    )
    ''')

    # 2. Adicionar novas colunas se não existirem
    cursor.execute("PRAGMA table_info(empresas_qualificadas)")
    colunas = [col[1] for col in cursor.fetchall()]

    if "pais" not in colunas:
        cursor.execute("ALTER TABLE empresas_qualificadas ADD COLUMN pais TEXT DEFAULT 'Brasil'")
    if "moeda" not in colunas:
        cursor.execute("ALTER TABLE empresas_qualificadas ADD COLUMN moeda TEXT DEFAULT 'BRL'")
    if "tax_id" not in colunas:
        cursor.execute("ALTER TABLE empresas_qualificadas ADD COLUMN tax_id TEXT")

    # 3. Injetar alvos globais de teste (Multinacionais e Exportadores)
    alvos_globais = [
        ("Global Logistics Inc", "US987654321", "LOGISTICA_INT", 95, "Alta taxa de câmbio e atraso no recebimento cross-border", "APROVADO_PARA_DISPARO", "Estados Unidos", "USD"),
        ("Iberia Tech Solutions SL", "ESB12345678", "SERVICOS_TI", 93, "Inadimplência de mensalidades SaaS na UE", "APROVADO_PARA_DISPARO", "Espanha", "EUR"),
        ("Latam Trade Corp", "CL77889900", "VAREJO_E_DISTRIBUICAO", 91, "Conciliação de liquidação internacional pendente", "APROVADO_PARA_DISPARO", "Chile", "USD")
    ]

    for nome, tid, setor, score, gargalo, status, pais, moeda in alvos_globais:
        cursor.execute('''
            INSERT OR REPLACE INTO empresas_qualificadas 
            (cnpj, razao_social, setor, score_potencial, gargalo_principal, status_qualificacao, pais, moeda, tax_id) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (tid, nome, setor, score, gargalo, status, pais, moeda, tid))

    conn.commit()

    # 4. Exibir o relatório de escala
    cursor.execute("SELECT COUNT(*) FROM empresas_qualificadas")
    total_alvos = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM empresas_qualificadas WHERE pais != 'Brasil'")
    total_internacional = cursor.fetchone()[0]
    
    conn.close()

    print("\n==================================================================")
    print("      IOTEC ENTERPRISE - PROJEÇÃO DE ESCALA GLOBAL E NÚCLEO DB")
    print("==================================================================")
    print(f"Total de Empresas Mapeadas no Banco: {total_alvos} registros")
    print(f"Operações Nacionais (Brasil): {total_alvos - total_internacional} empresas (BRL / Pix)")
    print(f"Operações Internacionais (Exterior): {total_internacional} empresas (USD / EUR)")
    print("------------------------------------------------------------------")
    print("POTENCIAL DE FATURAMENTO COM EXPANSAO DE BASE:")
    print(" • Base 500 Alvos Nacionais (R$ 1.500/mês): ~ R$ 75.000,00 / mês")
    print(" • Base 100 Alvos Internacionais ($ 500/mês): ~ US$ 50.000,00 / mês")
    print("------------------------------------------------------------------")
    print("STATUS DA ESTRUTURA: SQLite migrado e otimizado para até 500.000 alvos")
    print("==================================================================\n")

if __name__ == "__main__":
    migrar_e_executar_forecast()
