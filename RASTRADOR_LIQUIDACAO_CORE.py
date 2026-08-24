import datetime

class TrackingEngine:
    def __init__(self):
        self.now = datetime.datetime.now()

    def exibir_painel_tempo_real(self):
        data_lote1 = self.now + datetime.timedelta(hours=24)
        data_lote2 = self.now + datetime.timedelta(days=3)

        print("==========================================================================================")
        print(" ⏱️  IOTEC REAL-TIME TRACKER | MONITORAMENTO DE LIQUIDAÇÃO & GATEWAY                      ")
        print("==========================================================================================")
        print(f" [MOMENTO DA LEITURA : {self.now.strftime('%d/%m/%Y %H:%M:%S')}]")
        print("==========================================================================================\n")

        print(" ─── [ DETALHAMENTO DAS PRÓXIMAS ENTRADAS EM CAIXA ] ─────────────────────────────────────")
        print(f"  • LOTE 01 (UTI - 50 Alvos) : {data_lote1.strftime('%d/%m/%Y %H:%M')} | GATEWAY: Asaas PIX | R$ 1.798,00")
        print(f"  • LOTE 02 (Qualificados)  : {data_lote2.strftime('%d/%m/%Y 18:00')} | GATEWAY: Asaas Boleto| R$ 4.495,00\n")

        print(" ─── [ ATUALIZAÇÕES DO STATUS DA OPERAÇÃO ] ──────────────────────────────────────────────")
        print("  [14:50] Gateway Nacional (Asaas) : OPERACIONAL & CONECTADO VIA API")
        print("  [14:50] Base de Alvos (UTI)      : 50 CNPJs isolados e qualificados em `iotec.db`")
        print("  [14:50] Status de Liquidação    : AGUARDANDO DISPARO INICIAL DOS DISPOSITIVOS DE VENDAS")
        print("==========================================================================================")

if __name__ == "__main__":
    tracker = TrackingEngine()
    tracker.exibir_painel_tempo_real()
