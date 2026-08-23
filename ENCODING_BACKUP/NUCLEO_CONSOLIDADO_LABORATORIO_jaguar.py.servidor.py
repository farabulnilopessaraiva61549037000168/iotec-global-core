import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# painel_jaguar.py (servidor)
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha-mestra-jaguar'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return 'Painel Jaguar Online'

@socketio.on('connect')
def on_connect():
    print('Painel Web conectado.')
    emit('server_response', {'data': 'ConexÃƒÆ'Ã†â€™o estabelecida com Painel Jaguar'})

@socketio.on('command')
def handle_command(json):
    print(f'Comando recebido: {json}')
    emit('server_response', {'data': f'Executando comando: {json}'})
    # Aqui vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pode processar o comando e executar no desktop

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)


