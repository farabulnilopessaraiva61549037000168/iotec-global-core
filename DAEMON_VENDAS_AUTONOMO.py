import time
import datetime
import subprocess
from SISTEMA_AUTONOMO_GLOBAL import SistemaAutonomoGlobal

class DaemonVendasAutonomo:
    def __init__(self):
        self.sistema = SistemaAutonomoGlobal()

    def iniciar_loop_escala(self):
        print("===============================================================================")
        print(" 💰 IOTEC ENGINE — ESTEIRA AUTÔNOMA DE VENDAS B2B EM ESCALA GLOBAL")
        print(" EMISSOR: Farabulini Lopes Saraiva | CNPJ: 61.549.037/0001-68")
        print("===============================================================================\n")

        while True:
            horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            print(f"[{horario}] 🔄 Rodando ciclo de mineração, oferta e verificação de acervo...")

            # 1. Minera novos leads de alto ticket
            self.sistema.minerar_leads_autonomos()

            # 2. Exibe status do acervo no banco
            self.sistema.exibir_relatorio_acervo()

            # 3. Dispara o motor integrado de ofertas B2B
            try:
                subprocess.run(["python", "C:\\IOTEC\\MOTOR_INTEGRADO_GLOBAL.py"], check=True)
            except Exception as e:
                print(f" [!] Erro durante execução do Motor Integrado: {e}")

            print("\n [✔] Ciclo executado com sucesso. Próxima rodada autônoma em 15 minutos.")
            print("===============================================================================")
            time.sleep(900) # Loop de 15 minutos

if __name__ == "__main__":
    daemon = DaemonVendasAutonomo()
    daemon.iniciar_loop_escala()
