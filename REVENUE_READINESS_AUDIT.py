import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json

ROOT = r"C:\IOTEC"

CHECKS = {
    "FORMS": [
        "form",
        "button.html",
        "landing",
        "lead"
    ],
    "BACKEND": [
        "app.py",
        "flask",
        "fastapi",
        "render"
    ],
    "DATABASE": [
        ".db",
        "sqlite",
        "database"
    ],
    "PROPOSALS": [
        "proposal",
        "sales",
        "commercial",
        "revenue"
    ],
    "PAYMENTS": [
        "paypal",
        "stripe",
        "payment",
        "checkout"
    ]
}

results = {}

for category in CHECKS:
    pass

    results[category] = []

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        lower = file.lower()

        for category, patterns in CHECKS.items():
            pass

            for pattern in patterns:
                pass

                if pattern in lower:
                    pass

                    results[category].append(
                        os.path.join(root, file)
                    )

                    break

report = {
    "status": {},
    "details": results
}

print("")
print("================================================")
print(" REVENUE READINESS AUDIT ")
print("================================================")

for category in results:
    pass

    total = len(results[category])

    report["status"][category] = total

    print("")
    print(category)
    print("FOUND:", total)

    for item in results[category][:10]:
        pass

        print(item)

print("")
print("================================================")

funnel_score = 0

for category in results:
    pass

    if len(results[category]) > 0:
        funnel_score += 20

print("")
print("FUNNEL SCORE:", funnel_score, "/100")

if funnel_score >= 80:
    print("STATUS: NEAR COMMERCIAL READY")

elif funnel_score >= 60:
    print("STATUS: PARTIALLY READY")

else:
    print("STATUS: NEEDS COMMERCIAL WORK")

print("")
print("================================================")

with open(
    "REVENUE_READINESS_REPORT.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        report,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("REPORT GENERATED")
print("REVENUE_READINESS_REPORT.json")
print("")




