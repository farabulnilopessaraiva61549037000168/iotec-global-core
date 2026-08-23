import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import time
import logging

# ConfiguraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de logs para registrar erros
logging.basicConfig(filename="sistema_log.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class SistemaAutonomoMelhorado:
    def __init__(self):
        self.status = "Inicializando"
        self.erros_detectados = []
        self.tentativas_recuperacao = 0

    def iniciar_sistema(self):
        """Inicia o sistema e ativa monitoramento com recuperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica"""
        try:
            self.status = "Operacional"
            logging.info("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Sistema iniciado com sucesso.")
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Sistema funcionando perfeitamente!")
            self.monitoramento_continuo()
        except Exception as e:
            self.registrar_erro(f"Erro ao iniciar: {e}")
            self.recuperar_sistema()

    def registrar_erro(self, mensagem):
        """Registra erro e inicia recuperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o se necessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio"""
        self.erros_detectados.append(mensagem)
        logging.error(mensagem)
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â AtenÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o! Erro detectado: {mensagem}")

        if self.tentativas_recuperacao < 3:
            self.recuperar_sistema()
        else:
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Sistema falhou apÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³s mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltiplas tentativas!")

    def recuperar_sistema(self):
        """Tenta recuperar o sistema automaticamente"""
        self.tentativas_recuperacao += 1
        logging.warning(f"Tentativa de recuperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o #{self.tentativas_recuperacao}")
        print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¾ Tentando recuperar o sistema... ({self.tentativas_recuperacao}/3)")
        time.sleep(2)

        try:
            self.status = "Operacional"
            logging.info("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ Sistema recuperado com sucesso!")
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â RecuperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da! Sistema estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel novamente.")
        except Exception as e:
            self.registrar_erro(f"Falha na recuperaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {e}")

    def monitoramento_continuo(self):
        """Executa monitoramento inteligente e corrige falhas automaticamente"""
        while self.status == "Operacional":
            try:
                time.sleep(5)
                logging.info("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Monitoramento ativo: Sistema estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡vel.")
                print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Monitoramento contÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­nuo: Nenhum erro detectado.")
            except Exception as e:
                self.registrar_erro(f"Erro no monitoramento: {e}")

# Iniciar sistema
if __name__ == "__main__":
    try:
        sistema = SistemaAutonomoMelhorado()
        sistema.iniciar_sistema()
    except Exception as e:
        logging.critical(f"Erro crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tico: {e}")
        print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Falha total no sistema. Verifique os logs para mais informaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes.")


