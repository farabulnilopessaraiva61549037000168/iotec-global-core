import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from flask import Flask, request



app = Flask(__name__)



@app.route("/evento", methods=["POST"])

def evento():
    pass

    data = request.json

    print("EVENTO RECEBIDO:", data)



    # Aqui vocÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âª conecta com seu orquestrador depois



    return {"status": "ok"}



app.run(port=5000)







