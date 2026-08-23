import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# MONEY_GATE.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

DATABASE = "enterprise.db"

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
        status TEXT,
        score INTEGER,
        sector TEXT

    )
    """)

    conn.commit()
    conn.close()

init_database()

def generate_protocol():
    pass

    return "GEI-" + datetime.now().strftime("%Y%m%d%H%M%S")

def classify_sector(service):
    pass

    service = service.lower()

    if "automation" in service:
        return "AI_AUTOMATION"

    if "deploy" in service:
        return "DEPLOY"

    if "analytics" in service:
        return "ANALYTICS"

    if "monitoring" in service:
        return "MONITORING"

    if "ai" in service:
        return "AI_OPERATIONS"

    return "GENERAL"

def economic_score(service, message):
    pass

    text = f"{service} {message}".lower()

    score = 0

    premium_words = [

        "enterprise",
        "automation",
        "dashboard",
        "ai",
        "analytics",
        "monitoring",
        "deploy",
        "infrastructure",
        "operations",
        "integration"

    ]

    for word in premium_words:
        pass

        if word in text:
            score += 10

    return score

@app.route("/")

def home():
    pass

    return jsonify({

        "SYSTEM": "GLOBAL ENTERPRISE INTELLIGENCE",
        "STATUS": "ONLINE",
        "TOWER": "ACTIVE",
        "CAPTURE": "READY"

    })

@app.route("/new-lead", methods=["POST"])

def new_lead():
    pass

    data = request.json

    protocol = generate_protocol()

    timestamp = str(datetime.now())

    name = data.get("name", "")
    email = data.get("email", "")
    service = data.get("service", "")
    message = data.get("message", "")
    origin = data.get("origin", "NETLIFY")

    sector = classify_sector(service)

    score = economic_score(service, message)

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
        status,
        score,
        sector

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        protocol,
        timestamp,
        name,
        email,
        service,
        message,
        origin,
        "RECEIVED",
        score,
        sector

    ))

    conn.commit()
    conn.close()

    print("\n================================================")
    print(" NEW OPPORTUNITY DETECTED ")
    print("================================================")
    print(f"PROTOCOL : {protocol}")
    print(f"NAME     : {name}")
    print(f"EMAIL    : {email}")
    print(f"SERVICE  : {service}")
    print(f"SECTOR   : {sector}")
    print(f"SCORE    : {score}")
    print("================================================\n")

    return jsonify({

        "success": True,
        "protocol": protocol,
        "sector": sector,
        "score": score,
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
        sector,
        score,
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
            "sector": row[5],
            "score": row[6],
            "status": row[7]

        })

    return jsonify(data)

if __name__ == "__main__":
    pass

    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )


