import sqlite3
import datetime

DB_PATH = "C:\\IOTEC\\iotec.db"

def simular_caixa_multinivel():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Vendas simuladas por polo estratégico
    novas_vendas = [
        ('POLO-NE-01', 'Complexo Logístico Suape/Pécem', 'Módulo Gestão Logística Portuária', 3500.00, 'NORDESTE_BR'),
        ('POLO-CO-02', 'Exportadora Agrícola Grãos S.A.', 'Módulo Telemetria e Agro Distribuição', 2800.00, 'CENTRO_OESTE_BR'),
        ('POLO-LATAM-03', 'Sistemas de Pagamento Transfronteiriço', 'Gateway Multimoeda & Câmbio', 4200.00, 'LATAM_EXPORT'),
        ('POLO-EUR-04', 'EuroCorp Compliance & Security', 'Módulo Governance & Shield Corporate', 5000.00, 'EUROPA_B2B')
    ]

    print("============================================================")
    print(" 💰 IOTEC ENGINE — CONVERSÃO DE CONTRATOS POR POLO GLOBAL  ")
    print("============================================================\n")

    total_novos_creditos = 0.0

    for cid, empresa, prod, valor, polo in novas_vendas:
        cursor.execute('''
            INSERT INTO transacoes_caixa (cliente_id, razao_social, produto_servico, valor, tipo_receita)
            VALUES (?, ?, ?, ?, 'RECORRENTE_MENSAL')
        ''', (cid, empresa, f"[{polo}] {prod}", valor))
        
        total_novos_creditos += valor
        print(f" 💳 [PAGAMENTO CONFIRMADO] {polo:<15} | {empresa}")
        print(f"    └─ Produto: {prod} | Entrada: R$ {valor:,.2f}")

    conn.commit()

    # Leitura do Faturamento Total
    cursor.execute("SELECT SUM(valor) FROM transacoes_caixa")
    faturamento_total = cursor.fetchone()[0] or 0.0

    print("\n============================================================")
    print(f" 📈 NOVO FATURAMENTO RECORRENTE ACUMULADO: R$ {faturamento_total:,.2f}")
    print("============================================================\n")

    conn.close()

if __name__ == "__main__":
    simular_caixa_multinivel()
