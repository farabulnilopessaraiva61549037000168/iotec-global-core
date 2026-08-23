import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¥ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo IA VIVA ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â ProtÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³tipo Inicial

import os
import time
from datetime import datetime


class NucleoDeDadosVivo:
    def __init__(self, caminho_dados):
        self.caminho = caminho_dados
        self.blocos_conhecimento = {}
        self.logs = []

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¥ Leitura de Dados
    def varrer_dados(self):
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Iniciando varredura de dados...")
        for pasta, subpastas, arquivos in os.walk(self.caminho):
            for arquivo in arquivos:
                caminho_completo = os.path.join(pasta, arquivo)
                self.blocos_conhecimento[caminho_completo] = {
                    "nome": arquivo,
                    "tipo": arquivo.split(".")[-1],
                    "status": "pendente"
                }
        self.logar("Varredura completa com " + str(len(self.blocos_conhecimento)) + " arquivos.")

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â Processamento Simples
    def processar_dados(self):
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Processando dados...")
        for caminho, info in self.blocos_conhecimento.items():
            info["status"] = "processado"
            time.sleep(0.1)  # Simula processamento
        self.logar("Todos os dados foram processados.")

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de Atendimento
    def simular_atendimento(self, comando):
        resposta = f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒâ€šÃ‚Â¨ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pediu: '{comando}'. Estou analisando..."
        print(resposta)
        self.logar(f"Atendimento simulado: {comando}")
        return resposta

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Logs
    def logar(self, mensagem):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.logs.append(f"[{timestamp}] {mensagem}")
        print(f"[{timestamp}] {mensagem}")

    # ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å" RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio
    def gerar_relatorio(self):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio de OperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes:\n")
        for linha in self.logs:
            print(linha)


# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ INICIANDO O NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO

if __name__ == "__main__":
    caminho = input("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ Insira o caminho da pasta de dados: ")

    ia = NucleoDeDadosVivo(caminho)
    ia.varrer_dados()
    ia.processar_dados()

    while True:
        comando = input("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Cliente diz (ou 'sair' para encerrar): ")
        if comando.lower() == 'sair':
            break
        ia.simular_atendimento(comando)

    ia.gerar_relatorio()


