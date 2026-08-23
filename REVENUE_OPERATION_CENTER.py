import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# REVENUE_OPERATION_CENTER.py

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
        whatsapp TEXT,

        service TEXT,
        message TEXT,

        origin TEXT,

        sector TEXT,
        score INTEGER,
        priority TEXT,

        pipeline TEXT,
        payment_status TEXT,
        operational_status TEXT

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

    mapping = {

        "automation": "AI_AUTOMATION",
        "analytics": "ANALYTICS",
        "dashboard": "DASHBOARD",
        "monitoring": "MONITORING",
        "deploy": "DEPLOY",
        "ocr": "OCR",
        "ai": "AI_OPERATIONS"

    }

    for key in mapping:
        pass

        if key in service:
            return mapping[key]

    return "GENERAL"

# ============================================================
# SCORE ENGINE
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
        "monitoring",
        "integration",
        "infrastructure",
        "operations",
        "ai",
        "deploy",
        "control",
        "intelligence"

    ]

    for word in premium_words:
        pass

        if word in text:
            score += 10

    return score

# ============================================================
# PRIORITY
# ============================================================

def priority(score):
    pass

    if score >= 60:
        return "CRITICAL"

    if score >= 40:
        return "HIGH"

    if score >= 20:
        return "MEDIUM"

    return "LOW"

# ============================================================
# PIPELINE
# ============================================================

def pipeline_stage(score):
    pass

    if score >= 60:
        return "EXECUTIVE"

    if score >= 40:
        return "PRIORITY"

    if score >= 20:
        return "COMMERCIAL"

    return "QUEUE"

# ============================================================
# ROOT
# ============================================================

@app.route("/")

def home():
    pass

    return jsonify({

        "SYSTEM": "GLOBAL ENTERPRISE INTELLIGENCE",
        "STATUS": "ONLINE",
        "TOWER": "ACTIVE",
        "REVENUE_MODE": "ENABLED",
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
    whatsapp = data.get("whatsapp", "")

    service = data.get("service", "")
    message = data.get("message", "")

    origin = data.get("origin", "NETLIFY")

    sector = classify_sector(service)

    score = economic_score(service, message)

    priority_level = priority(score)

    pipeline = pipeline_stage(score)

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO leads (

        protocol,
        timestamp,

        name,
        email,
        company,
        whatsapp,

        service,
        message,

        origin,

        sector,
        score,
        priority,

        pipeline,

        payment_status,
        operational_status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        protocol,
        timestamp,

        name,
        email,
        company,
        whatsapp,

        service,
        message,

        origin,

        sector,
        score,
        priority_level,

        pipeline,

        "PENDING",
        "RECEIVED"

    ))

    conn.commit()
    conn.close()

    print("\n================================================")
    print(" NEW ENTERPRISE OPPORTUNITY ")
    print("================================================")
    print(f"PROTOCOL : {protocol}")
    print(f"NAME     : {name}")
    print(f"COMPANY  : {company}")
    print(f"WHATSAPP : {whatsapp}")
    print(f"SERVICE  : {service}")
    print(f"SECTOR   : {sector}")
    print(f"SCORE    : {score}")
    print(f"PRIORITY : {priority_level}")
    print(f"PIPELINE : {pipeline}")
    print("================================================\n")

    return jsonify({

        "success": True,

        "protocol": protocol,

        "sector": sector,

        "score": score,

        "priority": priority_level,

        "pipeline": pipeline,

        "payment_status": "PENDING",

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
        company,
        whatsapp,

        service,

        sector,
        score,

        priority,
        pipeline,

        payment_status,
        operational_status

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
            "company": row[3],
            "whatsapp": row[4],

            "service": row[5],

            "sector": row[6],
            "score": row[7],

            "priority": row[8],
            "pipeline": row[9],

            "payment_status": row[10],
            "operational_status": row[11]

        })

    return jsonify(data)

# ============================================================
# EXECUTIVE LEADS
# ============================================================

@app.route("/executive")

def executive():
    pass

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        protocol,
        company,
        service,
        score,
        priority,
        pipeline

    FROM leads

    WHERE score >= 40

    ORDER BY score DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    data = []

    for row in rows:
        pass

        data.append({

            "protocol": row[0],
            "company": row[1],
            "service": row[2],
            "score": row[3],
            "priority": row[4],
            "pipeline": row[5]

        })

    return jsonify(data)

# ============================================================
# REVENUE STATUS
# ============================================================

@app.route("/revenue")

def revenue():
    pass

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*) FROM leads

    """)

    total = cursor.fetchone()[0]

    cursor.execute("""

    SELECT COUNT(*) FROM leads
    WHERE score >= 40

    """)

    premium = cursor.fetchone()[0]

    conn.close()

    return jsonify({

        "total_leads": total,
        "premium_leads": premium,
        "revenue_mode": "ACTIVE",
        "tower": "ONLINE"

    })

# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    pass

    app.run(
        host="0.0.0.0",
        port=3000,
        debug=True
    )




