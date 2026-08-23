import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ENTERPRISE_RENDER_READY.py

from flask import Flask, request, jsonify
from datetime import datetime
import sqlite3
import os

app = Flask(__name__)

DATABASE = "enterprise.db"

# ============================================================
# DATABASE
# ============================================================

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

        company TEXT,

        service TEXT,
        message TEXT,

        origin TEXT,

        sector TEXT,
        score INTEGER,

        priority TEXT,
        status TEXT

    )

    """)

    conn.commit()
    conn.close()

init_database()

# ============================================================
# PROTOCOL
# ============================================================

def generate_protocol():
    pass

    return "GEI-" + datetime.now().strftime("%Y%m%d%H%M%S")

# ============================================================
# CLASSIFICATION
# ============================================================

def classify_sector(service):
    pass

    service = service.lower()

    if "automation" in service:
        return "AI_AUTOMATION"

    if "analytics" in service:
        return "ANALYTICS"

    if "deploy" in service:
        return "DEPLOY"

    if "monitoring" in service:
        return "MONITORING"

    if "dashboard" in service:
        return "DASHBOARD"

    if "ai" in service:
        return "AI_OPERATIONS"

    return "GENERAL"

# ============================================================
# SCORE
# ============================================================

def economic_score(service, message):
    pass

    text = f"{service} {message}".lower()

    score = 0

    premium_words = [

        "enterprise",
        "automation",
        "analytics",
        "dashboard",
        "deploy",
        "monitoring",
        "operations",
        "integration",
        "infrastructure",
        "ai"

    ]

    for word in premium_words:
        pass

        if word in text:
            score += 10

    return score

# ============================================================
# PRIORITY
# ============================================================

def priority_level(score):
    pass

    if score >= 50:
        return "CRITICAL"

    if score >= 30:
        return "HIGH"

    if score >= 10:
        return "MEDIUM"

    return "LOW"

# ============================================================
# ROOT
# ============================================================


@app.route("/iotec-proof")
def proof():
    pass

    return jsonify({
        "proof": "ENTERPRISE_RENDER_READY_20260604"
    })

@app.route("/")

def home():
    pass

    return jsonify({

        "SYSTEM": "GLOBAL ENTERPRISE INTELLIGENCE",
        "STATUS": "ONLINE",
        "TOWER": "ACTIVE",
        "CAPTURE": "READY"

    })

# ============================================================
# NEW LEAD
# ============================================================

@app.route("/new-lead", methods=["POST"])

def new_lead():
    pass

    data = request.json

    protocol = generate_protocol()

    timestamp = str(datetime.now())

    name = data.get("name", "")
    email = data.get("email", "")
    company = data.get("company", "")

    service = data.get("service", "")
    message = data.get("message", "")

    origin = data.get("origin", "NETLIFY")

    sector = classify_sector(service)

    score = economic_score(service, message)

    priority = priority_level(score)

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO leads (

        protocol,
        timestamp,

        name,
        email,
        company,

        service,
        message,

        origin,

        sector,
        score,

        priority,
        status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        protocol,
        timestamp,

        name,
        email,
        company,

        service,
        message,

        origin,

        sector,
        score,

        priority,
        "RECEIVED"

    ))

    conn.commit()
    conn.close()

    print("\n================================================")
    print(" NEW OPPORTUNITY DETECTED ")
    print("================================================")
    print(f"PROTOCOL : {protocol}")
    print(f"NAME     : {name}")
    print(f"COMPANY  : {company}")
    print(f"SERVICE  : {service}")
    print(f"SECTOR   : {sector}")
    print(f"SCORE    : {score}")
    print(f"PRIORITY : {priority}")
    print("================================================\n")

    return jsonify({

        "success": True,

        "protocol": protocol,

        "sector": sector,
        "score": score,

        "priority": priority,

        "status": "RECEIVED"

    })

# ============================================================
# TOWER
# ============================================================

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
        company,

        service,

        sector,
        score,

        priority,
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
            "company": row[4],

            "service": row[5],

            "sector": row[6],
            "score": row[7],

            "priority": row[8],
            "status": row[9]

        })

    return jsonify(data)

# ============================================================
# HIGH PRIORITY
# ============================================================

@app.route("/priority")

def priority():
    pass

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        protocol,
        name,
        company,
        service,
        score,
        priority

    FROM leads

    WHERE score >= 30

    ORDER BY score DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:
        pass

        data.append({

            "protocol": row[0],
            "name": row[1],
            "company": row[2],
            "service": row[3],
            "score": row[4],
            "priority": row[5]

        })

    return jsonify(data)

# ============================================================
# RUN
# ============================================================

if __name__ == "__main__":
    pass

    app.run(

        host="0.0.0.0",
        port=3000,
        debug=True

    )


