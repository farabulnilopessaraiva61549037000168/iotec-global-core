import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC / IBEX
# TOWER SIGNAL MAPPER ENGINE
# ============================================================
#
# OBJETIVO:
# - descobrir quais interfaces respondem ÃƒÆ'Ã†â€™  torre
# - detectar websocket/socketio
# - detectar fetch/api/status
# - detectar rotas /lead
# - detectar heartbeat
# - detectar comunicaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o realtime
# - classificar interfaces:
#
#   ONLINE
#   PASSIVE
#   BROKEN
#   TOWER_CONNECTED
#
# ============================================================

import os
import re
import json
import requests
from datetime import datetime

# ============================================================
# BASE
# ============================================================

BASE_PATH = r"C:\IOTEC"

# ============================================================
# DIRETÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIOS
# ============================================================

REPORT_DIR = os.path.join(
    BASE_PATH,
    "TOWER_SIGNAL_REPORTS"
)

os.makedirs(
    REPORT_DIR,
    exist_ok=True
)

# ============================================================
# LOG
# ============================================================

def log(message):
    pass

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    line = f"[{timestamp}] {message}"

    print(line)

    with open(

        os.path.join(
            REPORT_DIR,
            "TOWER_SIGNAL_MAPPER.log"
        ),

        "a",
        encoding="utf-8"

    ) as f:

        f.write(line + "\n")

# ============================================================
# TESTE TORRE
# ============================================================

TOWER_ONLINE = False

try:
    pass

    response = requests.get(
        "http://127.0.0.1:8080/api/status",
        timeout=3
    )

    if response.status_code == 200:
        pass

        TOWER_ONLINE = True

        log(
            "TORRE ONLINE DETECTADA."
        )

except:
    pass

    log(
        "TORRE NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O RESPONDE."
    )

# ============================================================
# MAPA
# ============================================================

CATALOG = {

    "timestamp":
        str(datetime.now()),

    "tower_online":
        TOWER_ONLINE,

    "connected":
        [],

    "passive":
        [],

    "broken":
        [],

    "socketio":
        [],

    "lead_routes":
        [],

    "heartbeat":
        [],

    "api_status":
        []
}

# ============================================================
# DETECTORES
# ============================================================

SOCKET_PATTERNS = [

    "socket.io",
    "SocketIO",
    "io.connect",
    "websocket",
    "socket.emit",
    "socket.on"
]

API_PATTERNS = [

    "/api/status",
    "fetch(",
    "axios",
    "XMLHttpRequest"
]

LEAD_PATTERNS = [

    "/lead",
    "submit",
    "form"
]

HEARTBEAT_PATTERNS = [

    "heartbeat",
    "system_status",
    "payment_received",
    "new_lead"
]

# ============================================================
# SCAN HTML
# ============================================================

log(
    "ESCANEANDO INTERFACES..."
)

for root, dirs, files in os.walk(BASE_PATH):
    pass

    for file in files:
        pass

        if not file.lower().endswith(".html"):
            continue

        full_path = os.path.join(
            root,
            file
        )

        try:
            pass

            with open(

                full_path,

                "r",

                encoding="utf-8",

                errors="ignore"

            ) as f:

                content = f.read()

            interface = {

                "file":
                    file,

                "path":
                    full_path,

                "status":
                    "PASSIVE",

                "signals":
                    []
            }

            score = 0

            # ================================================
            # SOCKET
            # ================================================

            for pattern in SOCKET_PATTERNS:
                pass

                if pattern.lower() in content.lower():
                    pass

                    score += 5

                    interface[
                        "signals"
                    ].append(
                        pattern
                    )

                    CATALOG[
                        "socketio"
                    ].append(
                        file
                    )

            # ================================================
            # API
            # ================================================

            for pattern in API_PATTERNS:
                pass

                if pattern.lower() in content.lower():
                    pass

                    score += 3

                    interface[
                        "signals"
                    ].append(
                        pattern
                    )

                    CATALOG[
                        "api_status"
                    ].append(
                        file
                    )

            # ================================================
            # LEAD
            # ================================================

            for pattern in LEAD_PATTERNS:
                pass

                if pattern.lower() in content.lower():
                    pass

                    score += 2

                    interface[
                        "signals"
                    ].append(
                        pattern
                    )

                    CATALOG[
                        "lead_routes"
                    ].append(
                        file
                    )

            # ================================================
            # HEARTBEAT
            # ================================================

            for pattern in HEARTBEAT_PATTERNS:
                pass

                if pattern.lower() in content.lower():
                    pass

                    score += 4

                    interface[
                        "signals"
                    ].append(
                        pattern
                    )

                    CATALOG[
                        "heartbeat"
                    ].append(
                        file
                    )

            # ================================================
            # CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
            # ================================================

            if score >= 10:
                pass

                interface[
                    "status"
                ] = "TOWER_CONNECTED"

                CATALOG[
                    "connected"
                ].append(
                    interface
                )

                log(
                    f"TOWER_CONNECTED: {file}"
                )

            elif score >= 4:
                pass

                interface[
                    "status"
                ] = "ONLINE"

                CATALOG[
                    "passive"
                ].append(
                    interface
                )

                log(
                    f"ONLINE: {file}"
                )

            else:
                pass

                interface[
                    "status"
                ] = "PASSIVE"

                CATALOG[
                    "passive"
                ].append(
                    interface
                )

        except Exception as e:
            pass

            CATALOG[
                "broken"
            ].append({

                "file":
                    file,

                "error":
                    str(e)
            })

            log(
                f"BROKEN: {file}"
            )

# ============================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ============================================================

REPORT_FILE = os.path.join(

    REPORT_DIR,

    "TOWER_CONNECTION_REPORT.json"
)

with open(

    REPORT_FILE,

    "w",

    encoding="utf-8"

) as f:

    json.dump(

        CATALOG,

        f,

        indent=4,

        ensure_ascii=False
    )

# ============================================================
# RESUMO
# ============================================================

print("")
print("================================================")
print(" IOTEC / IBEX TOWER SIGNAL MAPPER")
print("================================================")
print("")

print(
    f"TORRE ONLINE: "
    f"{CATALOG['tower_online']}"
)

print(
    f"TOWER CONNECTED: "
    f"{len(CATALOG['connected'])}"
)

print(
    f"PASSIVE: "
    f"{len(CATALOG['passive'])}"
)

print(
    f"BROKEN: "
    f"{len(CATALOG['broken'])}"
)

print(
    f"SOCKETIO SIGNALS: "
    f"{len(CATALOG['socketio'])}"
)

print(
    f"LEAD ROUTES: "
    f"{len(CATALOG['lead_routes'])}"
)

print(
    f"HEARTBEAT SIGNALS: "
    f"{len(CATALOG['heartbeat'])}"
)

print("")
print("================================================")
print(" SIGNAL MAPPING COMPLETE")
print("================================================")
print("")

log(
    "TOWER SIGNAL MAPPER FINALIZADO."
)




