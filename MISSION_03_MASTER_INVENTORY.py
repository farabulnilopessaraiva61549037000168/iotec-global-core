import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import json
import re

ROOT = r"C:\IOTEC"

inventory = {
    "html": [],
    "javascript": [],
    "python": [],
    "bridges": [],
    "forms": [],
    "endpoints": [],
    "render_urls": [],
    "netlify_urls": []
}

print("\n===================================")
print(" IOTEC MASTER INVENTORY")
print("===================================\n")

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        path = os.path.join(root, file)

        try:
            pass

            if file.endswith(".html"):
                inventory["html"].append(path)

            elif file.endswith(".js"):
                inventory["javascript"].append(path)

            elif file.endswith(".py"):
                inventory["python"].append(path)

            if any(x in file.lower() for x in [
                "bridge",
                "netlify",
                "render",
                "lead"
            ]):
                inventory["bridges"].append(path)

            if file.endswith((".html", ".js", ".py")):
                pass

                try:
                    content = open(
                        path,
                        "r",
                        encoding="utf-8",
                        errors="ignore"
                    ).read()
                except:
                    continue

                if "sendLead" in content:
                    inventory["forms"].append(path)

                endpoints = re.findall(
                    r'["']([^"']*/new-lead[^"']*)["']',
                    content
                )

                for e in endpoints:
                    inventory["endpoints"].append({
                        "file": path,
                        "endpoint": e
                    })

                renders = re.findall(
                    r'https://[a-zA-Z0-9\-]+\.onrender\.com',
                    content
                )

                for r in renders:
                    inventory["render_urls"].append({
                        "file": path,
                        "url": r
                    })

                netlifys = re.findall(
                    r'https://[a-zA-Z0-9\-]+\.netlify\.app',
                    content
                )

                for n in netlifys:
                    inventory["netlify_urls"].append({
                        "file": path,
                        "url": n
                    })

        except:
            pass

report = "MISSION_03_MASTER_INVENTORY.json"

with open(report, "w", encoding="utf-8") as f:
    json.dump(
        inventory,
        f,
        indent=4,
        ensure_ascii=False
    )

print("HTML FILES      :", len(inventory["html"]))
print("JS FILES        :", len(inventory["javascript"]))
print("PY FILES        :", len(inventory["python"]))
print("BRIDGES         :", len(inventory["bridges"]))
print("FORMS           :", len(inventory["forms"]))
print("ENDPOINTS       :", len(inventory["endpoints"]))
print("RENDER URLS     :", len(inventory["render_urls"]))
print("NETLIFY URLS    :", len(inventory["netlify_urls"]))

print("\nREPORT:")
print(report)

print("\n===================================")
print(" INVENTORY COMPLETED")
print("===================================")




