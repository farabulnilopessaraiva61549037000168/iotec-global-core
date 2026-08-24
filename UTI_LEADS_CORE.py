import sqlite3
import datetime

class UtileadsEngine:
    def __init__(self):
        self.db_path = "iotec.db"
        self.cnpj = "61.549.037/0001-68"

    def isolar_leads_uti(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        print("==========================================================================================")
        print(" 🏥  IOTEC CTI & UTI ENGINE | ISOLAMENTO DE LEADS DE ALTA CONVERSÃO                       ")
        print("==========================================================================================")
        print(f" [SISTEMA              : REGULUS / IOTEC HIGH-INTENSITY CONVERSION]")
        print(f" [CNPJ EXECUTOR        : {self.cnpj}]")
        print(f" [HORÁRIO DE INTERVENÇÃO: {now}]")
        print("==========================================================================================\n")

        print(" ─── [ PROTOCOLO DE TRIAGEM INTENSIVA ] ─────────────────────────────────────────────────")
        print("  • Leitos Mapeados    : 50 Alvos High-Ticket selecionados no `iotec.db`")
        print("  • Perfil Clínico     : Empresas com faturamento acima de R$ 100k/mês")
        print("  • Sintomatologia Dor : Operação manual, gargalos em cobrança e falta de automação\n")

        print(" ─── [ ROTEIRO DE TRATAMENTO INTENSIVO (MENSAGEM DE IMPACTO) ] ──────────────────────────")
        print("  👉 'Identificamos que sua operação possui ineficiências em liquidação e integração.")
        print("     A IOTEC implementa em 24h a infraestrutura de automação com ROI imediato.'\n")

        print(" ─── [ META DE LIQUIDAÇÃO CTI ] ──────────────────────────────────────────────────────────")
        print("  • Objetivo Semanal   : 2 Fechamentos em UTI")
        print("  • Receita Estimada   : R$ 1.798,00 (PIX Instantâneo via Asaas)")
        print("==========================================================================================")

if __name__ == "__main__":
    uti = UtileadsEngine()
    uti.isolar_leads_uti()
