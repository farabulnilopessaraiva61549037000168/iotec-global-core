import threading
import time

def inicializar_agente_nuvem():
    try:
        import IOTEC_AGENTE_FABRICANTE_REAL
        print("[⚡ RENDER CORE] Thread do Agente Arquiteto inicializada com sucesso!")
        IOTEC_AGENTE_FABRICANTE_REAL.pulsar_engine_fabricante()
    except Exception as e:
        print(f"[-] Erro na thread do Agente Arquiteto na Render: {e}")

# Dispara a thread do fabricante em segundo plano assim que o Gunicorn/Flask carrega
t_arquiteto = threading.Thread(target=inicializar_agente_nuvem, daemon=True)
t_arquiteto.start()

# Mantém a importação da sua aplicação Flask principal para o Gunicorn responder na porta HTTP
try:
    from wsgi_cloud import app
except ImportError:
    from flask import Flask
    app = Flask(__name__)
    @app.route('/')
    def index():
        return "IOTEC ENGINE ONLINE — Agente Arquiteto Ativo em Nuvem", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
