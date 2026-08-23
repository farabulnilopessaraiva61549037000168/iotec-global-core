import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# server.py
from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import threading, json, os, time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
DATA_FILE = "provas_db.json"

# load/save simples
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        db = json.load(f)
else:
    db = {"students": {}, "answers": []}

def save_db():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=2, ensure_ascii=False)

@app.route("/")
def index():
    return app.send_static_file("client.html")  # veremos o client abaixo

@app.route("/dashboard")
def dashboard():
    return app.send_static_file("dashboard.html")

# Tablet envia resposta
@socketio.on("answer_submitted")
def handle_answer(data):
    # data: {student_id, question_id, answer, correct (opt)}
    data["ts"] = time.time()
    db["answers"].append(data)
    sid = data.get("student_id")
    if sid:
        db["students"].setdefault(sid, {"last_seen": None, "answers": []})
        db["students"][sid]["answers"].append(data)
        db["students"][sid]["last_seen"] = data["ts"]
    save_db()
    # notifica dashboards conectados
    emit("progress_update", data, broadcast=True)

# tablet heartbeat
@socketio.on("heartbeat")
def hb(data):
    sid = data.get("student_id")
    if sid:
        db["students"].setdefault(sid, {"last_seen": None, "answers": []})
        db["students"][sid]["last_seen"] = time.time()
        save_db()
    emit("heartbeat_ack", {"ok": True})

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)


