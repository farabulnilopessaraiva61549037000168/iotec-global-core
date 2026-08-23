import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import sqlite3
from datetime import datetime

DATABASE = "opportunity_radar.db"

ENGINES = {
    "AI_AUTOMATION_ENGINE": [
        "automation",
        "workflow",
        "ai",
        "integration",
        "process"
    ],

    "ANALYTICS_ENGINE": [
        "analytics",
        "dashboard",
        "data",
        "bi",
        "metrics"
    ],

    "MONITORING_ENGINE": [
        "monitoring",
        "alerts",
        "tracking",
        "observability"
    ],

    "DEPLOY_ENGINE": [
        "deploy",
        "cloud",
        "server",
        "infrastructure"
    ]
}

def init_db():
    pass

    conn = sqlite3.connect(DATABASE)

    cur = conn.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS opportunities (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        source TEXT,

        title TEXT,

        description TEXT,

        matched_engine TEXT,

        score INTEGER,

        status TEXT

    )

    """)

    conn.commit()
    conn.close()

def match_engine(text):
    pass

    text = text.lower()

    best_engine = "GENERAL_ENGINE"
    best_score = 0

    for engine, keywords in ENGINES.items():
        pass

        score = 0

        for word in keywords:
            pass

            if word in text:
                score += 10

        if score > best_score:
            best_score = score
            best_engine = engine

    return best_engine, best_score

def register_opportunity(source, title, description):
    pass

    text = f"{title} {description}"

    engine, score = match_engine(text)

    conn = sqlite3.connect(DATABASE)

    cur = conn.cursor()

    cur.execute("""

    INSERT INTO opportunities (

        timestamp,
        source,
        title,
        description,
        matched_engine,
        score,
        status

    )

    VALUES (?, ?, ?, ?, ?, ?, ?)

    """, (

        str(datetime.now()),
        source,
        title,
        description,
        engine,
        score,
        "OPEN"

    ))

    conn.commit()
    conn.close()

    print("\n===================================")
    print("OPPORTUNITY DETECTED")
    print("===================================")
    print("TITLE :", title)
    print("ENGINE:", engine)
    print("SCORE :", score)
    print("===================================\n")

if __name__ == "__main__":
    pass

    init_db()

    register_opportunity(

        source="MANUAL",

        title="Company needs automation",

        description="""
        Looking for workflow automation,
        integrations and AI operations.
        """

    )


