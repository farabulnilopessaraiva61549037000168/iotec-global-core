import datetime

class RegistroSocioCore:
    def __init__(self):
        self.owner = "FARABULINI LOPES SARAIVA"
        self.cpf = "011.902.313-01"
        self.cnpj = "61.549.037/0001-68"

    def print_socio_details(self):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        print("==========================================================================================")
        print(" 👤  IOTEC GOVERNANCE CORE | VINCULAÇÃO PATRIMONIAL DO SÓCIO ADMINISTRADOR                ")
        print("==========================================================================================")
        print(f" [TITULAR DA PROPRIEDADE INTELECTUAL : {self.owner}]")
        print(f" [CPF DO ADMINISTRADOR               : {self.cpf}]")
        print(f" [CNPJ DA PESSOA JURÍDICA            : {self.cnpj}]")
        print(f" [SISTEMA E PROJETO                  : REGULUS / IOTEC B2B CORE]")
        print(f" [TIMESTAMP DE SESSÃO                : {now}]")
        print("==========================================================================================\n")

        print(" ─── [ ESTRUTURA DE TITULARIDADE CONSOLIDADA ] ───────────────────────────────────────────")
        print("  • Documentação Física / Fiscal : CPF alinhado ao Contrato Social e Domicílio Bancário.")
        print("  • Conta de Destino de Dividendos: Vinculada para liquidação isenta de IR.")
        print("  • Score e Rating PJ             : Habilitado para atrelamento ao Dossiê Bradesco PJ.")
        print("==========================================================================================")

if __name__ == "__main__":
    reg = RegistroSocioCore()
    reg.print_socio_details()
