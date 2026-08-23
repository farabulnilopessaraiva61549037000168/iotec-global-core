import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import re
import sqlite3

FILE = "REAL_LEAD_BRIDGE.py"

with open(FILE, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

match = re.search(r'DATABASE\s*=\s*['"](.+?)['"]', content)

if not match:
    print("DATABASE NOT FOUND")
    exit()

db = match.group(1)

print("")
print("DATABASE:", db)
print("")

try:
    pass

    conn = sqlite3.connect(db)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """)

    tables = cursor.fetchall()

    print("TABLES FOUND:")
    print("")

    for t in tables:
        print("-", t[0])

    print("")

    try:
        pass

        cursor.execute("PRAGMA table_info(leads)")
        cols = cursor.fetchall()

        print("LEADS COLUMNS:")
        print("")

        for c in cols:
            print(c)

    except Exception as e:
        print("ERROR READING LEADS:", e)

    conn.close()

except Exception as e:
    pass

    print("DATABASE ERROR:")
    print(e)




