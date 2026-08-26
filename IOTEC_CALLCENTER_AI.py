import sqlite3
import json
import time

DB_PATH = "C:\\IOTEC\\iotec_database.db"

class CallCenterIOTEC:
    def __init__(self):
        self._setup_db()

    def _setup_db(self):
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS solucoes_vendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cnpj TEXT,
                    dor_cliente TEXT,
                    solucao_desenvolvida TEXT,
                    status_pipeline TEXT,
                    valor_proposta REAL,
                    data_registro DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')

    def agente_sdr_escuta(self, cnpj: str, transcricao_atendimento: str) -> dict:
        print(f"[*] [AGENTE SDR] Analisando atendimento do CNPJ: {cnpj}...")
        dor = "Perda de estoque por falta de automação na contagem" if "estoque" in transcricao_atendimento.lower() else "Lentidão na emissão de cobranças"
        return {"cnpj": cnpj, "dor": dor, "transcricao": transcricao_atendimento}

    def agente_arquiteto_software(self, diagnostico: dict) -> dict:
        print(f"[*] [AGENTE ARQUITETO] Projetando software sob medida para dor: '{diagnostico['dor']}'...")
        solucao = {
            "nome_sistema": f"Sistema_Autonomo_IOTEC_{diagnostico['cnpj'][:6]}",
            "modulos": ["API de Captura", "Dashboard de Métricas", "Integração WhatsApp/Pix"],
            "tecnologias": ["Python", "SQLite", "Gateway Payments"]
        }
        diagnostico["solucao"] = solucao
        return diagnostico

    def agente_fechador_vendas(self, projeto: dict) -> float:
        valor = 1490.00
        print(f"[+] [AGENTE COMERCIAL] Proposta gerada no valor de R$ {valor:.2f}")
        print(f"[+] [DISPARO AUTOMÁTICO] Enviando checkout Pix/PayPal para o WhatsApp corporativo.")
        
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('''
                INSERT INTO solucoes_vendas (cnpj, dor_cliente, solucao_desenvolvida, status_pipeline, valor_proposta)
                VALUES (?, ?, ?, ?, ?)
            ''', (projeto["cnpj"], projeto["dor"], json.dumps(projeto["solucao"]), "OFERTA_DISPARADA", valor))
            
        return valor

if __name__ == "__main__":
    print("[+] Central de Atendimento & Software Factory IOTEC em Operação Continua...\n")
    engine = CallCenterIOTEC()
    
    # Exemplo de Atendimento de Entrada Minerado
    transcricao = "Nosso maior problema hoje é que perdemos muito tempo com estoque manual e pagamentos atrasados."
    
    p1 = engine.agente_sdr_escuta("12345678000199", transcricao)
    p2 = engine.agente_arquiteto_software(p1)
    engine.agente_fechador_vendas(p2)
