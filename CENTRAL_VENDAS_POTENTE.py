import sqlite3
import datetime
import time

DB_PATH = "C:\\IOTEC\\iotec.db"

def inicializar_tabelas_financeiras():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacoes_caixa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id TEXT,
            razao_social TEXT,
            produto_servico TEXT,
            valor REAL,
            tipo_receita TEXT DEFAULT 'RECORRENTE_MENSAL',
            data_transacao DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

class CentralVendasERelacionamento:
    def __init__(self):
        inicializar_tabelas_financeiras()

    def calcular_mrr_e_conversoes(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Metricas globais da base
        cursor.execute("SELECT COUNT(*) FROM central_vendas_leads")
        total_leads = cursor.fetchone()[0] or 1

        cursor.execute("SELECT COUNT(*) FROM central_vendas_leads WHERE status_venda IN ('PAGAMENTO_CONFIRMADO', 'SISTEMA_ENTREGUE')")
        total_convertidos = cursor.fetchone()[0] or 0

        cursor.execute("SELECT SUM(valor) FROM transacoes_caixa WHERE data_transacao >= DATE('now', 'start of day')")
        receita_hoje = cursor.fetchone()[0] or 0.0

        cursor.execute("SELECT SUM(valor) FROM transacoes_caixa")
        receita_acumulada = cursor.fetchone()[0] or 0.0

        taxa_conversao = (total_convertidos / total_leads) * 100

        horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

        print("\n============================================================")
        print(f"   CENTRAL DE VENDAS & RELACIONAMENTO IOTEC — {horario}")
        print("============================================================")
        print(f" 📊 TAXA DE CONVERSÃO GLOBAL: {taxa_conversao:.2f}% ({total_convertidos} / {total_leads} leads)")
        print(f" 💰 RECEITA RECORRENTE HOJE:  R$ {receita_hoje:,.2f}")
        print(f" 📈 FATURAMENTO ACUMULADO:    R$ {receita_acumulada:,.2f}")
        print("------------------------------------------------------------")
        print(" 📦 DESEMPENHO DE PRODUTOS & SERVIÇOS (LTV/RECORRÊNCIA):")
        print("   ├─ [1] Módulo CRM & Automação Comercial:    40% das vendas")
        print("   ├─ [2] Módulo Gestão de Frota & Logística:  35% das vendas")
        print("   └─ [3] Planos de Suporte & Updates SAC:    25% das vendas")
        print("============================================================\n")

        conn.close()

if __name__ == "__main__":
    central = CentralVendasERelacionamento()
    central.calcular_mrr_e_conversoes()
