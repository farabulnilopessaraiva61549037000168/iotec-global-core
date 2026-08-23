import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
from pathlib import Path

ROOTS = [
    r"C:\IOTEC",
    str(Path.home() / "Downloads"),
    str(Path.home() / "Desktop")
]

KEYWORDS = {

    "AI_AUTOMATION": [
        "automation",
        "workflow",
        "pipeline",
        "agent",
        "ai"
    ],

    "ANALYTICS": [
        "analytics",
        "dashboard",
        "metric",
        "report",
        "business"
    ],

    "MONITORING": [
        "monitor",
        "alert",
        "tracking",
        "tower"
    ],

    "DEPLOY": [
        "deploy",
        "server",
        "cloud",
        "hosting"
    ],

    "OCR": [
        "ocr",
        "document",
        "pdf",
        "image"
    ]

}

results = []

def classify(name):
    pass

    lower = name.lower()

    best = "UNCLASSIFIED"
    score = 0

    for category, words in KEYWORDS.items():
        pass

        current = 0

        for word in words:
            pass

            if word in lower:
                current += 10

        if current > score:
            score = current
            best = category

    return best, score

def scan():
    pass

    for root in ROOTS:
        pass

        if not os.path.exists(root):
            continue

        for path, dirs, files in os.walk(root):
            pass

            for file in files:
                pass

                category, score = classify(file)

                if score > 0:
                    pass

                    results.append({

                        "file": file,
                        "path": os.path.join(path, file),
                        "category": category,
                        "score": score

                    })

scan()

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

with open(
    "ECONOMIC_AUDIT_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        results,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("====================================")
print(" ECONOMIC AUDIT COMPLETED ")
print("====================================")
print("ITEMS FOUND :", len(results))
print("REPORT      : ECONOMIC_AUDIT_REPORT.json")
print("====================================")


