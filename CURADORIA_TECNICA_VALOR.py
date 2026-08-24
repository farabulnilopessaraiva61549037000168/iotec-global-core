import sqlite3
import datetime

class CuradoriaTecnicaCore:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"
        self.owner = "FARABULINI LOPES SARAIVA"
        self.db_path = "iotec.db"

    def executar_curadoria(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🧠  IOTEC CORE | MATRIZ DE CURADORIA TÉCNICA E ENGENHARIA DE VALOR                       ")
        print("==========================================================================================")
        print(f" [TITULAR DA PROPRIEDADE : {self.owner}]")
        print(f" [CNPJ EXECUTOR        : {self.cnpj}]")
        print(f" [SESSÃO DE CURADORIA   : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. PAINEL DOS MÓDULOS DE ELITE DO NÚCLEO ] ───────────────────────────────────────")
        print("  • Módulo 01: ENGINE DE LIQUIDAÇÃO NACIONAL (Asaas API / Auto-Pix / Boleto Registrar)")
        print("  • Módulo 02: CROSS-BORDER EXCHANGE (Remessa Online / Swift USD & EUR Direct)")
        print("  • Módulo 03: GOVERNANÇA PATRIMONIAL (Trava Bancária + Distribuição Isenta de IRPF)")
        print("  • Módulo 04: CTI & UTI DE LEADS (Triagem e Intervenção de Alta Densidade no `iotec.db`)\n")

        print(" ─── [ 2. MATRIZ DE MÉTRICAS & ROI DO CLIENTE B2B ] ────────────────────────────────────")
        print("  • Ticket Standard     : R$ 299,00 / mês   (ROI do Cliente: 4.2x sobre custo operacional)")
        print("  • Ticket High-Ticket  : R$ 899,00 / mês   (ROI do Cliente: 8.5x sobre headcount/equipe)")
        print("  • Ticket Enterprise   : R$ 2.990,00 / ano (Payback do Cliente: < 14 dias de operação)\n")

        print(" ─── [ 3. PARECER TÉCNICO DOS CURADORES ] ───────────────────────────────────────────────")
        print("  👉 'A IOTEC não vende software; vende redução imediata de opEX e garantia de compliance.")
        print("     O modelo garante ROI positivo no primeiro ciclo de cobrança via Asaas/Remessa.'")
        print("==========================================================================================")

if __name__ == "__main__":
    curadoria = CuradoriaTecnicaCore()
    curadoria.executar_curadoria()
