import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import os
from datetime import datetime

INPUT_FILE = "REVENUE_DISCOVERY_REPORT.json"

TOP_LIMIT = 50

assets = []

with open(
    INPUT_FILE,
    "r",
    encoding="utf-8"
) as f:

    data = json.load(f)

for category in data:
    pass

    for item in data[category]:
        pass

        try:
            pass

            path = item["path"]

            if not os.path.exists(path):
                continue

            size = os.path.getsize(path)

            modified = os.path.getmtime(path)

            assets.append({

                "category": category,

                "file": item["file"],

                "path": path,

                "size": size,

                "modified": modified

            })

        except:
            pass

assets.sort(

    key=lambda x: (

        x["size"],
        x["modified"]

    ),

    reverse=True

)

top_assets = assets[:TOP_LIMIT]

print("")
print("================================================")
print(" TOP ECONOMIC ASSETS ")
print("================================================")

for i, asset in enumerate(top_assets, start=1):
    pass

    print("")
    print(f"RANK      : {i}")

    print(
        "CATEGORY  :",
        asset["category"]
    )

    print(
        "FILE      :",
        asset["file"]
    )

    print(
        "SIZE(MB)  :",
        round(
            asset["size"] / 1024 / 1024,
            2
        )
    )

    print(
        "MODIFIED  :",
        datetime.fromtimestamp(
            asset["modified"]
        )
    )

print("")
print("================================================")

report = {

    "generated": str(datetime.now()),

    "top_assets": top_assets

}

with open(

    "TOP_ASSETS_REPORT.json",

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
print(
    "REPORT GENERATED:"
)

print(
    "TOP_ASSETS_REPORT.json"
)

print("")


