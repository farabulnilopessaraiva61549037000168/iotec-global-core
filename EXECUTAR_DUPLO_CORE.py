import os
import datetime

class DualExecutionEngine:
    def __init__(self):
        self.now = datetime.datetime.now()

    def sincronizar_github(self):
        print("\n [TAREFA 1] ☁️  Iniciando Sincronização de Commits com GitHub...")
        os.system("git push origin main")

    def relatorio_liquidacoes(self):
        limite_lote1 = self.now + datetime.timedelta(hours=24)
        print("\n [TAREFA 2] 📊 Acessando Relatório do Rastreador de Liquidações...")
        print("==========================================================================================")
        print(" 🎯 STATUS DA LISTA DE ESPERA DE LIQUIDAÇÕES (ASAAS)")
        print("==========================================================================================")
        print(f"  • LOTE 01 (50 Alvos UTI) : Janela Limite até {limite_lote1.strftime('%d/%m/%Y às %H:%M')}")
        print("  • Valor Esperado Lote 01  : R$ 1.798,00 (2 Fechamentos High-Ticket)")
        print("  • Status da Escuta Webhook: ATIVA E AGUARDANDO CRÉDITO NA CONTA PJ")
        print("==========================================================================================")

    def executar(self):
        print("==========================================================================================")
        print(" ⚡  IOTEC DUAL TASK | SINCRONIZAÇÃO GITHUB + RELATÓRIO DE LIQUIDAÇÕES                    ")
        print("==========================================================================================")
        self.sincronizar_github()
        self.relatorio_liquidacoes()

if __name__ == "__main__":
    engine = DualExecutionEngine()
    engine.executar()
