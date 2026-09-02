import logging, os, sys
os.makedirs(r"C:\IOTEC\LOGS", exist_ok=True)
logging.basicConfig(filename=r"C:\IOTEC\LOGS\governanca_agentes.log", level=logging.INFO, format="%(asctime)s - [GOVERNANCA IOTEC] - %(levelname)s - %(message)s")
sys.path.append(r"C:\IOTEC")
from iotec_license_engine import validar_licenca
class AgenteAutonomoIOTEC:
    def __init__(self, nome_agente, escopo_permitido, api_key):
        self.nome = nome_agente
        self.escopo = escopo_permitido
        self.api_key = api_key
        self.autenticado = False
    def autenticar(self):
        valido, msg = validar_licenca(self.api_key)
        if valido:
            self.autenticado = True
            logging.info(f"Agente '{self.nome}' autenticado. API Key: {self.api_key}")
            print(f"🟢 [{self.nome}] Autenticado e Operacional na Nuvem IOTEC.")
        else:
            self.autenticado = False
            logging.warning(f"Tentativa nao autorizada no agente '{self.nome}'. Motivo: {msg}")
            print(f"🔴 [{self.nome}] BLOQUEADO PELA GOVERNANCA: {msg}")
    def executar_tarefa(self, acao_solicitada, parametros):
        if not self.autenticado:
            print(f"⛔ [{self.nome}] Acao cancelada: Agente nao autenticado.")
            return False
        if acao_solicitada not in self.escopo:
            msg_erro = f"BLOQUEIO DE SEGURANCA: Acao '{acao_solicitada}' EXCEDE O ESCOPO do agente '{self.nome}'."
            logging.error(msg_erro)
            print(f"🚨 {msg_erro}")
            return False
        logging.info(f"Agente '{self.nome}' executou: {acao_solicitada} | Params: {parametros}")
        print(f"⚡ [{self.nome}] Tarefa '{acao_solicitada}' executada com sucesso.")
        return True
if __name__ == "__main__":
    escopo_auditor = ["CONSULTAR_DIVIDA", "ANALISAR_PRESCRICAO", "GERAR_MINUTA"]
    agente = AgenteAutonomoIOTEC("Agente_Auditor_Financeiro", escopo_auditor, "IOTEC-KEY-PRO-2026")
    agente.autenticar()
    agente.executar_tarefa("ANALISAR_PRESCRICAO", {"devedor": "Unopar", "anos": 5})
    agente.executar_tarefa("EFETUAR_PAGAMENTO_DIRETO", {"valor": 800.00})