import time
import sqlite3
import datetime
import subprocess

DB_PATH = "C:\\IOTEC\\iotec.db"

class DaemonLucroContinuo:
    def __init__(self):
        print("===============================================================================")
        print(" 💰 IOTEC ENGINE — GERADOR DE RECORRÊNCIA B2B & ESCALA CONTINUA")
        print(" EMISSOR: Farabulini Lopes Saraiva | CNPJ: 61.549.037/0001-68")
        print("===============================================================================\n")

    def exibir_relatorio_rotatividade(self):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        print(" 📊 [STATUS DE CAMADAS DO ACERVO PROFUNDO (582K MÓDULOS)]")
        cursor.execute('''
            SELECT camada_nucleo, COUNT(modulo_hash), SUM(quantidade_exposicoes)
            FROM controle_exposicao_modulos
            GROUP BY camada_nucleo
        ''')
        
        relatorio = cursor.fetchall()
        for camada, total_mod, exposicoes in relatorio:
            print(f"  ├─ {camada:<45} | Módulos: {total_mod} | Total Exposições: {exposicoes}")
        
        conn.close()
        print(" -------------------------------------------------------------------------------")

    def executar_ciclo(self):
        while True:
            horario = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            print(f"\n[{horario}] 🚀 Iniciando ciclo de ofertas e escavação de acervo...")

            # 1. Executa o Motor Integrado (Call Center Virtual + Escavação)
            try:
                subprocess.run(["python", "C:\\IOTEC\\MOTOR_INTEGRADO_GLOBAL.py"], check=True)
            except Exception as e:
                print(f" [!] Erro ao rodar Motor Integrado: {e}")

            # 2. Exibe o relatório de rotatividade do acervo no banco
            self.exibir_relatorio_rotatividade()

            print(" [✔] Ciclo concluído com sucesso. Próxima varredura e oferta em 15 minutos.")
            print("===============================================================================")
            time.sleep(900) # Reexecuta a cada 15 minutos

if __name__ == "__main__":
    daemon = DaemonLucroContinuo()
    daemon.executar_ciclo()
