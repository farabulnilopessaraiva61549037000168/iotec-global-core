import sqlite3

def expor_vendas_reais():
    print("=" * 80)
    print("      IOTEC B2B — EXPOSITOR DE ALVOS E VENDAS REAIS (DADOS FISCAIS VALIDADOS)")
    print("=" * 80)
    
    conn = sqlite3.connect('iotec.db')
    c = conn.cursor()
    
    # 1. Alvos de Alto Ticket (leads_qualificados)
    print("\n[🎯] FILA 01: LEADS DE ALTO TICKET (LOGÍSTICA / INFRA / FINTECHS)")
    print("-" * 80)
    qualificados = c.execute("SELECT cnpj, razao_social, cnae, porte, ticket_estimado, status_prospeccao FROM leads_qualificados LIMIT 5").fetchall()
    for q in qualificados:
        print(f" 🏢 Empresa : {q[1]}")
        print(f" 🆔 CNPJ    : {q[0]} | Porte: {q[3]}")
        print(f" 📌 CNAE    : {q[2]} | Ticket Estimado: R$ {q[4]:,.2f}")
        print(f" 🔄 Status  : {q[5]}")
        print("-" * 80)

    # 2. Central de Vendas (central_vendas_leads)
    print("\n[📞] FILA 02: CENTRAL DE VENDAS COM CONTATO DIRETO")
    print("-" * 80)
    central = c.execute("SELECT cnpj, razao_social, email, telefone, score_qualificacao, status_venda FROM central_vendas_leads LIMIT 5").fetchall()
    for cv in central:
        print(f" 🏢 Empresa : {cv[1]}")
        print(f" 🆔 CNPJ    : {cv[0]} | Score: {cv[4]}")
        print(f" ✉️ E-mail  : {cv[2]} | Tel: {cv[3]}")
        print(f" 🔄 Status  : {cv[5]}")
        print("-" * 80)

    conn.close()

expor_vendas_reais()
