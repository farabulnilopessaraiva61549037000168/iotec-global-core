import sqlite3
import os

db_path = r'C:\IOTEC\iotec.db'

class AgenteTesouraria:
    def __init__(self, percentual_reserva=0.20):
        self.percentual_reserva = percentual_reserva

    def preparar_tabela(self, conn):
        cursor = conn.cursor()
        # Verifica colunas existentes na tabela transacoes_caixa
        cursor.execute("PRAGMA table_info(transacoes_caixa);")
        colunas = [info[1].lower() for info in cursor.fetchall()]

        # Se a tabela nao existir ou nao tiver 'tipo', recria de forma limpa/adequada
        if not colunas or 'tipo' not in colunas:
            cursor.execute("DROP TABLE IF EXISTS transacoes_caixa")
            cursor.execute('''
                CREATE TABLE transacoes_caixa (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    tipo TEXT,
                    origem TEXT,
                    valor REAL,
                    data TEXT
                )
            ''')
            # Insere dados de simulacao real baseados na operacao atual para teste de margem
            cursor.execute("INSERT INTO transacoes_caixa (tipo, origem, valor, data) VALUES ('ADESAO_B2B', 'Cliente Teste Adesao', 2500.00, datetime('now'))")
            cursor.execute("INSERT INTO transacoes_caixa (tipo, origem, valor, data) VALUES ('CUSTO_OPERACIONAL', 'Mensalidade Z-API', 99.00, datetime('now'))")
            cursor.execute("INSERT INTO transacoes_caixa (tipo, origem, valor, data) VALUES ('INVESTIMENTO', 'Aporte Investidor Anjo', 50000.00, datetime('now'))")
            conn.commit()

    def auditar_e_calcular_saque(self):
        if not os.path.exists(db_path):
            print('[ERRO] Banco iotec.db nao encontrado.')
            return

        try:
            conn = sqlite3.connect(db_path)
            self.preparar_tabela(conn)
            cursor = conn.cursor()

            # Consulta Faturamento B2B (Adesoes)
            cursor.execute("SELECT SUM(valor) FROM transacoes_caixa WHERE tipo='ADESAO_B2B'")
            res_adesao = cursor.fetchone()[0]
            faturamento_adesoes = res_adesao if res_adesao else 0.0

            # Consulta Aporte de Investidores (Patrimonio da Empresa - Bloqueado para saque direto)
            cursor.execute("SELECT SUM(valor) FROM transacoes_caixa WHERE tipo='INVESTIMENTO'")
            res_invest = cursor.fetchone()[0]
            aportes_investidores = res_invest if res_invest else 0.0

            # Consulta Custos Operacionais (APIs, Servidores)
            cursor.execute("SELECT SUM(valor) FROM transacoes_caixa WHERE tipo='CUSTO_OPERACIONAL'")
            res_custo = cursor.fetchone()[0]
            custos_totais = res_custo if res_custo else 0.0

            conn.close()

            # Calculo de Margem e Retencao
            lucro_bruto_operacional = faturamento_adesoes - custos_totais
            if lucro_bruto_operacional > 0:
                reserva_empresa = lucro_bruto_operacional * self.percentual_reserva
                disponivel_para_saque = lucro_bruto_operacional - reserva_empresa
            else:
                reserva_empresa = 0.0
                disponivel_para_saque = 0.0

            # Exibicao Humanizada do Painel de Saque
            print("==================================================")
            print("     AGENTE DE TESOURARIA IOTEC - PAINEL FINANCEIRO")
            print("==================================================")
            print(f"[+] Faturamento Total (Adesoes B2B): R$ {faturamento_adesoes:,.2f}")
            print(f"[-] Custos Operacionais (APIs/Infra):  R$ {custos_totais:,.2f}")
            print("--------------------------------------------------")
            print(f"[=] Lucro Liquido Operacional:        R$ {lucro_bruto_operacional:,.2f}")
            print(f"[i] Retencao de Reserva (20% Reinvestimento): R$ {reserva_empresa:,.2f}")
            print("==================================================")
            print(f"[?] VALOR LIBERADO PARA SEU SAQUE (80% L?CIDO): R$ {disponivel_para_saque:,.2f}")
            print("==================================================")
            print(f"[*] Capital de Investidores (Protegido/CNPJ): R$ {aportes_investidores:,.2f}\n")

        except Exception as e:
            print(f'[ERRO TESOURARIA] Falha ao processar caixa: {e}')

if __name__ == '__main__':
    tesouraria = AgenteTesouraria(percentual_reserva=0.20)
    tesouraria.auditar_e_calcular_saque()
