import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC CAPABILITY POWER AUDITOR
# AUDITORIA DE POTÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA DOS MOTORES
# NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O ALTERA NADA
# ==========================================================

import json
import os
from datetime import datetime

TOPOLOGY = r"C:\IOTEC\IOTEC_MASTER_TOPOLOGY.json"

OUTPUT_JSON = r"C:\IOTEC\IOTEC_CAPABILITY_POWER_REPORT.json"
OUTPUT_TXT  = r"C:\IOTEC\IOTEC_CAPABILITY_POWER_REPORT.txt"

with open(
    TOPOLOGY,
    "r",
    encoding="utf-8"
) as f:

    topo = json.load(f)

report = {

    "generated": str(datetime.now()),

    "motors": [],

    "ranking": []
}

# ==========================================================
# SCORE
# ==========================================================

for motor, data in topo["nodes"].items():
    pass

    if "error" in data:
        continue

    score = 0

    imports = len(data.get("imports", []))
    funcs   = data.get("function_count", 0)

    score += funcs * 5
    score += imports * 2

    if data.get("sqlite"):
        score += 20

    if data.get("json"):
        score += 10

    path = data.get("path", "")

    tags = []

    try:
        pass

        if os.path.exists(path):
            pass

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as fp:

                content = fp.read().lower()

            checks = {

                "FLASK": [
                    "flask"
                ],

                "API": [
                    "requests",
                    "api",
                    "endpoint"
                ],

                "AI": [
                    "openai",
                    "gpt",
                    "llm",
                    "agent"
                ],

                "DATABASE": [
                    "sqlite3",
                    "postgres",
                    "mysql"
                ],

                "AUTOMATION": [
                    "thread",
                    "scheduler",
                    "loop",
                    "monitor"
                ],

                "COMMERCIAL": [
                    "lead",
                    "proposal",
                    "sales",
                    "crm"
                ],

                "REVENUE": [
                    "revenue",
                    "economic",
                    "pricing"
                ]
            }

            for tag, words in checks.items():
                pass

                found = False

                for word in words:
                    pass

                    if word in content:
                        pass

                        found = True
                        break

                if found:
                    pass

                    tags.append(tag)

            score += len(tags) * 15

    except:
        pass

    report["motors"].append({

        "motor": motor,

        "score": score,

        "functions": funcs,

        "imports": imports,

        "tags": tags

    })

# ==========================================================
# RANKING
# ==========================================================

ranking = sorted(

    report["motors"],

    key=lambda x: x["score"],

    reverse=True

)

report["ranking"] = ranking

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
    f.write("IOTEC CAPABILITY POWER AUDITOR\n")
    f.write("===================================\n\n")

    pos = 1

    for item in ranking:
        pass

        f.write(
            f"{pos}ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº {item['motor']}\n"
        )

        f.write(
            f"POWER SCORE: {item['score']}\n"
        )

        f.write(
            f"FUNCTIONS: {item['functions']}\n"
        )

        f.write(
            f"IMPORTS: {item['imports']}\n"
        )

        f.write(
            f"TAGS: {', '.join(item['tags'])}\n"
        )

        f.write("\n")

        pos += 1

# ==========================================================
# CONSOLE
# ==========================================================

print("")
print("===================================")
print("IOTEC CAPABILITY POWER AUDITOR")
print("===================================")
print("")

for i, item in enumerate(ranking[:10], start=1):
    pass

    print(
        f"{i}ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº {item['motor']} | SCORE {item['score']}"
    )

print("")
print("JSON:")
print(OUTPUT_JSON)

print("")
print("TXT:")
print(OUTPUT_TXT)

print("")
print("CONCLUIDO")


