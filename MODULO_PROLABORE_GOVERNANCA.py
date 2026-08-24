import datetime

class GovernancaFinanceira:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cnpj = "61.549.037/0001-68"

    def print_prolabore_structure(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 🏛️  IOTEC GOVERNANCE CORE | ESTRUTURA DE PRÓ-LABORE & DIVIDENDOS DO SÓCIO                ")
        print("==========================================================================================")
        print(f" [TITULAR DA PROPRIEDADE : {self.owner}]")
        print(f" [CNPJ INSTITUCIONAL    : {self.cnpj}]")
        print(f" [TIMESTAMP             : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ 1. REMUNERAÇÃO FORMAL DO SÓCIO (PRÓ-LABORE) ] ─────────────────────────────────────")
        print("  • Valor Fixo Recomendado : 1 Salário Mínimo (Mapeado para DECORE / Comprovação de Renda)")
        print("  • Incidência Tributária  : Alíquota mínima de INSS (Proteção e eficiência fiscal no CPF)\n")

        print(" ─── [ 2. RETIRADA PATRIMONIAL (DISTRIBUIÇÃO DE LUCROS) ] ───────────────────────────────")
        print("  • Fonte de Custeio       : Excedente da margem de 100% após liquidação da parcela PJ")
        print("  • Status Fiscal          : ISENTO de Imposto de Renda Pessoa Física (IRPF)")
        print("  • Destinação             : Formação de patrimônio pessoal (Veículo / Imóvel)\n")

        print("==========================================================================================")
        print(" ✅ REGRAS DE RETIRADA PATRIMONIAL CONFIGURADAS E REGISTRADAS.")
        print("==========================================================================================")

if __name__ == "__main__":
    gov = GovernancaFinanceira()
    gov.print_prolabore_structure()
