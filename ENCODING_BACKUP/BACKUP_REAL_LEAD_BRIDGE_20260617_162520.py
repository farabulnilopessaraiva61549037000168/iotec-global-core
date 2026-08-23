import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# REAL_LEAD_BRIDGE.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

DATABASE = "tower.db"

def init_database():
    pass

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        protocol TEXT,
        timestamp TEXT,
        name TEXT,
        email TEXT,
        service TEXT,
        message TEXT,
        origin TEXT,
        status TEXT

    )
    """)

    conn.commit()
    conn.close()

init_database()

def create_protocol():
    pass

    now = datetime.now()

    return f"LEAD-{now.strftime('%Y%m%d%H%M%S')}"

@app.route("/")

def home():
    pass

    return jsonify({
        "tower": "ONLINE",
        "bridge": "CONNECTED",
        "status": "ACTIVE"
    })

@app.route("/new-lead", methods=["POST"])

def new_lead():
    pass

    data = request.json

    protocol = create_protocol()

    timestamp = str(datetime.now())

    name = data.get("name", "")
    email = data.get("email", "")
    service = data.get("service", "")
    message = data.get("message", "")
    origin = data.get("origin", "NETLIFY")

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leads (

        protocol,
        timestamp,
        name,
        email,
        service,
        message,
        origin,
        status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (

        protocol,
        timestamp,
        name,
        email,
        service,
        message,
        origin,
        "RECEIVED"

    ))

    conn.commit()
    conn.close()

    print("\n================================================")
    print(" NEW LEAD RECEIVED ")
    print("================================================")
    print(f"PROTOCOL : {protocol}")
    print(f"NAME     : {name}")
    print(f"EMAIL    : {email}")
    print(f"SERVICE  : {service}")
    print(f"ORIGIN   : {origin}")
    print("================================================\n")

    return jsonify({
        "success": True,
        "protocol": protocol,
        "status": "RECEIVED"
    })

@app.route("/tower")

def tower():
    pass

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        protocol,
        timestamp,
        name,
        email,
        service,
        status
    FROM leads
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:
        pass

        data.append({
            "protocol": row[0],
            "timestamp": row[1],
            "name": row[2],
            "email": row[3],
            "service": row[4],
            "status": row[5]
        })

    return jsonify(data)

if __name__ == "__main__":
    pass

    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )


