import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<!-- painel_r.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Painel R Class - Jaguar</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.4.1/socket.io.js"></script>
</head>
<body>
    <h1>Painel R Class Online</h1>
    <input type="text" id="comando" placeholder="Digite seu comando">
    <button onclick="enviar()">Enviar Comando</button>
    <p id="resposta"></p>

    <script>
        const socket = io('http://localhost:5000');

        socket.on('connect', () => {
            console.log('Conectado ao Painel Jaguar');
        });

        socket.on('server_response', (msg) => {
            document.getElementById('resposta').innerText = msg.data;
        });

        function enviar() {
            const comando = document.getElementById('comando').value;
            socket.emit('command', {'comando': comando});
        }
    </script>
</body>
</html>



