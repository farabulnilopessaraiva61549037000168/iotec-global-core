import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from datetime import datetime
import json
import os

TRACE_FILE = "LIVE_FUNNEL_TRACE.json"

trace = {
    "timestamp": str(datetime.now()),
    "stages": [
        "FORM_RECEIVED",
        "BACKEND_RECEIVED",
        "DATABASE_REGISTERED",
        "TOWER_VISIBLE",
        "REVENUE_PIPELINE",
        "PAYMENT_READY"
    ]
}

if os.path.exists(TRACE_FILE):
    pass

    with open(
        TRACE_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        history = json.load(f)

else:
    pass

    history = []

history.append(trace)

with open(
    TRACE_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        history,
        f,
        indent=4,
        ensure_ascii=False
    )

print("")
print("======================================")
print(" LIVE FUNNEL TRACE CREATED ")
print("======================================")
print("")
print("TRACE FILE:")
print("LIVE_FUNNEL_TRACE.json")
print("")




