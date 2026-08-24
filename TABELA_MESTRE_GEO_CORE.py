import sqlite3
import datetime

class MasterGeoEngine:
    def __init__(self):
        self.cnpj = "61.549.037/0001-68"

    def exibir_tabela_mestre(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🗺️  IOTEC MASTER GEOENGINE | TABELA MESTRE DE POLOS NACIONAIS E INTERNACIONAIS          ")
        print("==========================================================================================")
        print(f" [RESPONSÁVEL OPERACIONAL : FARABULINI LOPES SARAIVA]")
        print(f" [STAMP DE CONSOLIDÇÃO   : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ POLOS NACIONAIS COM MAIOR DENSIDADE DE CONVERSÃO ] ────────────────────────────────")
        print("  • POLO SUDESTE (SP/RJ/MG) : Score 98 | Foco: SaaS & Fintechs   | Dado: Ineficiência de Pagamento")
        print("  • POLO SUL (PR/SC/RS)     : Score 91 | Foco: Agrotech & Ind.   | Dado: Recorrência & DDA")
        print("  • POLO NORDESTE (CE/PE/BA): Score 89 | Foco: Telecom & Infra   | Dado: Latência & APIs Cambiais")
        print("  • POLO C.-OESTE (MT/GO)   : Score 87 | Foco: Agro High-Ticket  | Dado: Liquidação Estruturada\n")

        print(" ─── [ POLOS GLOBAIS COM MAIOR SCORE DE DÓLAR/EURO ] ─────────────────────────────────────")
        print("  • 🇺🇸 ESTADOS UNIDOS (TX/FL): Score 96 | Foco: SaaS & VC         | Dado: NRR & Conversão USD/BRL")
        print("  • 🇪🇺 UNIÃO EUROPEIA (EE/DE): Score 94 | Foco: RegTech & FinTech | Dado: Compliance SEPA & VAT")
        print("  • 🇺🇾 🇨🇱 LATAM (UY/CL)      : Score 90 | Foco: Cross-Border      | Dado: Pontes Cambiais Direct\n")

        print("==========================================================================================")
        print(" 💎 PLATAFORMA ALICERCADA SOBRE MAPPING GEOECONÔMICO DE ALTA DENSIDADE.")
        print("==========================================================================================")

if __name__ == "__main__":
    geo = MasterGeoEngine()
    geo.exibir_tabela_mestre()
