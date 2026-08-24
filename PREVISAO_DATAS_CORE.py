import datetime

class CalendarForecastEngine:
    def __init__(self):
        self.now = datetime.datetime.now()

    def calcular_datas_fechamento(self):
        # Janelas de tempo calculadas por nivel de engajamento do lead
        fechamento_critico = self.now + datetime.timedelta(hours=24)   # Engajamento Alto (CTI/UTI)
        fechamento_quente  = self.now + datetime.timedelta(days=3)     # Engajamento Médio
        fechamento_padrao  = self.now + datetime.timedelta(days=7)     # Engajamento Inicial

        print("==========================================================================================")
        print(" 📅  IOTEC TIME-TO-CASH ENGINE | PREVISÃO DE DATAS DE LIQUIDAÇÃO                         ")
        print("==========================================================================================")
        print(f" [DATA/HORA ATUAL    : {self.now.strftime('%d/%m/%Y %H:%M')}]")
        print("==========================================================================================\n")

        print(" ─── [ CRONOGRAMA PREDITIVO DE FECHAMENTO POR NÍVEL DE ENGAJAMENTO ] ─────────────────────")
        print(f"  🔥 ALTO ENGAJAMENTO (UTI - Demo Vista + Resposta)   ──► Data Prevista: {fechamento_critico.strftime('%d/%m/%Y (até %H:%M)')}")
        print(f"  ⚡ MÉDIO ENGAJAMENTO (Proposta Aberta / Em Análise)  ──► Data Prevista: {fechamento_quente.strftime('%d/%m/%Y')}")
        print(f"  🌱 ENGAJAMENTO PADRÃO (Abordagem Inicial Enviada)   ──► Data Prevista: {fechamento_padrao.strftime('%d/%m/%Y')}\n")

        print(" ─── [ PROJEÇÃO DE FLUXO DE CAIXA NO ASAAS ] ─────────────────────────────────────────────")
        print(f"  • Previsão Lote 01 (2 Fechamentos UTI) : R$ 1.798,00 até {fechamento_critico.strftime('%d/%m/%Y')}")
        print(f"  • Previsão Lote 02 (5 Fechamentos Med) : R$ 4.495,00 até {fechamento_quente.strftime('%d/%m/%Y')}")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = CalendarForecastEngine()
    engine.calcular_datas_fechamento()
