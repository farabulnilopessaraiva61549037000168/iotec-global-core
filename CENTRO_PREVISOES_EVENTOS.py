import math
import datetime

class ForecastByEvents:
    def __init__(self):
        self.total_leads = 2155
        self.ticket_high = 899.00
        self.ticket_lite = 299.00

    def calcular_estatistica_eventos(self):
        # Eventos do Funil Digital (Valores Probabilísticos Atmosféricos)
        prob_e1_entrega = 0.85      # 85% recebem a abordagem
        prob_e2_interacao = 0.18    # 18% interagem com o sistema/demo
        prob_e3_fechamento = 0.12   # 12% dos que interagem efetuam a compra
        
        # Probabilidade Composta de Evento P(E)
        p_conversao = prob_e1_entrega * prob_e2_interacao * prob_e3_fechamento  # ~1.836%
        
        leads_convertidos = math.floor(self.total_leads * p_conversao)
        receita_prevista_high = leads_convertidos * self.ticket_high
        receita_prevista_lite = leads_convertidos * self.ticket_lite
        
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🛰️  IOTEC METEOROLOGICAL FORECAST ENGINE | PREVISÃO POR FENÔMENOS DIGITAIS               ")
        print("==========================================================================================")
        print(f" [SISTEMA DE EVENTOS : REGULUS EVENT-DRIVEN MODEL]")
        print(f" [PROCESSADO EM      : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ FENÔMENOS ATMOSFÉRICOS MEDIDOS NA BASE (2.155 LEADS) ] ───────────────────────────")
        print(f"  • P(E1) Taxa de Entrega / Alcance  : {prob_e1_entrega*100:.1f}%")
        print(f"  • P(E2) Taxa de Engajamento / Demo  : {prob_e2_interacao*100:.1f}%")
        print(f"  • P(E3) Taxa de Fechamento / Aceite: {prob_e3_fechamento*100:.1f}%")
        print(f"  • PROBABILIDADE COMPOSTA P(E)       : {p_conversao*100:.3f}%\n")

        print(" ─── [ PREVISÃO MATEMÁTICA DE PRECIPITAÇÃO FINANCEIRA (CAIXA) ] ──────────────────────────")
        print(f"  • Previsão de Eventos de Fechamento : {leads_convertidos} Clientes Ativos")
        print(f"  • Receita Prevista (Cenário High)   : R$ {receita_prevista_high:,.2f} / mês")
        print(f"  • Receita Prevista (Cenário Lite)   : R$ {receita_prevista_lite:,.2f} / mês")
        print("==========================================================================================")

if __name__ == "__main__":
    engine = ForecastByEvents()
    engine.calcular_estatistica_eventos()
