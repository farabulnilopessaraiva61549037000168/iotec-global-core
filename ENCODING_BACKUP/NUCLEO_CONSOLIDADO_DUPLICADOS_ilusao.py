import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request, redirect
import time

app = Flask(__name__)

# IlusÃƒÆ'Ã†â€™o para bots: uma armadilha que simula um site real
@app.route('/painel')
def ilusao():
    print("Invasor detectado: ", request.remote_addr)
    time.sleep(5)  # Simula lentidÃƒÆ'Ã†â€™o para desencorajar
    return redirect("https://google.com")  # Redireciona para fora

# Canal verdadeiro sÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ para quem conhece o jutsu
@app.route('/painel-seguro')
def painel_secreto():
    return "Painel verdadeiro do nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo de dados - Acesso autorizado."

if __name__ == "__main__":
    app.run()


