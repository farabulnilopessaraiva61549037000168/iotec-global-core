import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC DATA HIGHWAY DISCOVERY
# DESCOBRE RODOVIAS DE DADOS DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ==========================================================

import os
import re
import json
from collections import defaultdict
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_DATA_HIGHWAY_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_DATA_HIGHWAY_REPORT.txt"

# ==========================================================
# EXPRESSÃƒÆ'Ã†â€™ES
# ==========================================================

SQLITE_PATTERN = r"sqlite3\.connect\s*\(\s*r?["']([^"']+)["']"
OPEN_PATTERN = r"open\s*\(\s*r?["']([^"']+)["']"
JSON_PATTERN = r"["']([^"']+\.json)["']"

# ==========================================================
# ESTRUTURAS
# ==========================================================

db_usage = defaultdict(list)
json_usage = defaultdict(list)
file_usage = defaultdict(list)

report = {
    "generated": str(datetime.now()),
    "files_scanned": 0,
    "databases": {},
    "jsons": {},
    "shared_files": {}
}

# ==========================================================
# SCAN
# ==========================================================

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if not file.lower().endswith(".py"):
            continue

        path = os.path.join(root, file)

        try:
            pass

            content = open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ).read()

            report["files_scanned"] += 1

            # -----------------------------
            # SQLITE
            # -----------------------------

            for db in re.findall(
                SQLITE_PATTERN,
                content,
                flags=re.IGNORECASE
            ):

                db_usage[db].append(file)

            # -----------------------------
            # JSON
            # -----------------------------

            for js in re.findall(
                JSON_PATTERN,
                content,
                flags=re.IGNORECASE
            ):

                json_usage[js].append(file)

            # -----------------------------
            # OPEN
            # -----------------------------

            for fpath in re.findall(
                OPEN_PATTERN,
                content,
                flags=re.IGNORECASE
            ):

                if "." in fpath:
                    file_usage[fpath].append(file)

        except:
            pass

# ==========================================================
# CONSOLIDA
# ==========================================================

for db, users in db_usage.items():
    pass

    report["databases"][db] = {
        "users": sorted(list(set(users))),
        "count": len(set(users))
    }

for js, users in json_usage.items():
    pass

    report["jsons"][js] = {
        "users": sorted(list(set(users))),
        "count": len(set(users))
    }

for fpath, users in file_usage.items():
    pass

    unique = sorted(list(set(users)))

    if len(unique) > 1:
        pass

        report["shared_files"][fpath] = {
            "users": unique,
            "count": len(unique)
        }

# ==========================================================
# JSON
# ==========================================================

with open(
    OUTPUT_JSON,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# TXT
# ==========================================================

with open(
    OUTPUT_TXT,
    "w",
    encoding="utf-8"
) as f:

    f.write("\n")
    f.write("===================================\n")
    f.write("IOTEC DATA HIGHWAY DISCOVERY\n")
    f.write("===================================\n\n")

    f.write(
        f"FILES SCANNED: {report['files_scanned']}\n\n"
    )

    f.write("DATABASE HIGHWAYS\n")
    f.write("-----------------\n")

    ordered_db = sorted(
        report["databases"].items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )

    for db, info in ordered_db[:50]:
        pass

        f.write(
            f"{db} -> {info['count']} motores\n"
        )

    f.write("\n")
    f.write("JSON HIGHWAYS\n")
    f.write("-----------------\n")

    ordered_json = sorted(
        report["jsons"].items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )

    for js, info in ordered_json[:50]:
        pass

        f.write(
            f"{js} -> {info['count']} motores\n"
        )

    f.write("\n")
    f.write("SHARED FILES\n")
    f.write("-----------------\n")

    ordered_shared = sorted(
        report["shared_files"].items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )

    for fname, info in ordered_shared[:50]:
        pass

        f.write(
            f"{fname} -> {info['count']} motores\n"
        )

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC DATA HIGHWAY DISCOVERY")
print("===================================")
print("")

print("FILES:", report["files_scanned"])
print("DATABASES:", len(report["databases"]))
print("JSONS:", len(report["jsons"]))
print("SHARED FILES:", len(report["shared_files"]))

print("")
print("RELATORIOS:")
print(OUTPUT_JSON)
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")




