import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>JAGUAR - Glass Panel</title>
    <style>
        body {
            background-color: #000;
            color: #00FF00;
            font-family: 'Consolas', monospace;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }
        .caixa {
            border: 2px solid #00FF00;
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(8px);
            background: rgba(0, 0, 0, 0.7);
        }
        h1 {
            text-shadow: 0 0 10px #00FF00;
        }
        button {
            background-color: lime;
            border: none;
            padding: 10px 20px;
            color: black;
            font-weight: bold;
            cursor: pointer;
            margin: 5px;
        }
    </style>
</head>
<body>
    <div class="caixa">
        <h1>ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Jaguar Systems Web Panel</h1>
        <p>Status: ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ Online e Operacional</p>
        <button onclick="alert('Ativando mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulo de anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise...')">AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise</button>
        <button onclick="alert('Sincronizando dispositivos...')">Sincronizar</button>
        <button onclick="alert('Desligando o sistema...')">Desligar</button>
    </div>
</body>
</html>
"""

@app.route('/')
def painel():
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=False, use_reloader=False)



