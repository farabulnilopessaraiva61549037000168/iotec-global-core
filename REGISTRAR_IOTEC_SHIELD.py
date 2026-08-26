import sqlite3

DB_PATH = "C:\\IOTEC\\iotec.db"

def registrar_shield_anti_spam():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT OR REPLACE INTO catalogo_global_produtos
        (codigo_produto, nome_solucao, categoria_nicho, polo_alvo, ticket_sugerido, descricao_comercial, arquivo_origem)
        VALUES (
            'PROD-SHIELD-01',
            'IOTEC HYPERCORE & CPU SHIELD (ANTI-SPAM & LIMPEZA)',
            'SEGURANCA_E_INFRAESTRUTURA',
            'Corporativo Global',
            1200.00,
            'Escudo de proteção contra spam, robocalls, entulhamento de caixa de entrada e consumo supérfluo de RAM/Disco.',
            'IOTEC_HYPERCORE_SHIELD'
        )
    ''')

    conn.commit()
    conn.close()

    print("============================================================")
    print(" 🛡️ IOTEC SHIELD ANTI-SPAM REGISTRADO COM SUCESSO!")
    print("============================================================")
    print(" ├─ Categoria: Segurança & Infraestrutura Corporativa")
    print(" ├─ Proposta: Alívio Técnico, Filtro de Ruído e Limpeza de RAM")
    print(" └─ Ticket Sugerido: R$ 1.200,00 / mês (Recorrente)")
    print("============================================================\n")

if __name__ == "__main__":
    registrar_shield_anti_spam()
