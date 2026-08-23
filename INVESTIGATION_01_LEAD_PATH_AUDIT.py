import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import re

ROOT = r"C:\IOTEC"

print("\n========================================")
print(" LEAD PATH AUDIT")
print("========================================\n")

hits = []

patterns = [
    "sendLead",
    "/new-lead",
    "fetch(",
    "onrender.com",
    "netlify.app",
    "ENTERPRISE_RENDER_READY",
    "REAL_LEAD_BRIDGE"
]

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if not file.endswith((".html", ".js", ".py")):
            continue

        path = os.path.join(root, file)

        try:
            pass

            with open(
                path,
                "r",
                encoding="utf-8",
                errors="ignore"
            ) as f:

                content = f.read()

            score = 0

            for p in patterns:
                if p in content:
                    score += 1

            if score > 0:
                pass

                hits.append({
                    "score": score,
                    "file": path
                })

        except:
            pass

hits.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("TOP SUSPECT FILES\n")

for item in hits[:50]:
    pass

    print(
        f"[{item['score']}] "
        f"{item['file']}"
    )

print("\n========================================")
print(" TOTAL SUSPECT FILES:", len(hits))
print("========================================")




