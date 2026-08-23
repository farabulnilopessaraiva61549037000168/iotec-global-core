import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import time

BASES = [

    r"C:\IOTEC",
    r"C:\IOTEC_OMEGA_X"
]

REAL_STATE = {

    "interfaces":0,
    "html":0,
    "python":0,
    "videos":0,
    "socketio":0,
    "paypal":0,
    "forms":0,
    "logs":0
}

def scan():
    pass

    global REAL_STATE

    REAL_STATE = {

        "interfaces":0,
        "html":0,
        "python":0,
        "videos":0,
        "socketio":0,
        "paypal":0,
        "forms":0,
        "logs":0
    }

    for BASE in BASES:
        pass

        if not os.path.exists(BASE):
            continue

        for root, dirs, files in os.walk(BASE):
            pass

            for file in files:
                pass

                full = os.path.join(root, file)

                lower = file.lower()

                # HTML
                if lower.endswith(".html"):
                    pass

                    REAL_STATE["interfaces"] += 1
                    REAL_STATE["html"] += 1

                    try:
                        pass

                        content = open(
                            full,
                            "r",
                            encoding="utf-8",
                            errors="ignore"
                        ).read().lower()

                    except:
                        continue

                    if "socket.io" in content:
                        pass

                        REAL_STATE["socketio"] += 1

                    if "paypal" in content:
                        pass

                        REAL_STATE["paypal"] += 1

                    if "<form" in content:
                        pass

                        REAL_STATE["forms"] += 1

                # PYTHON
                elif lower.endswith(".py"):
                    pass

                    REAL_STATE["python"] += 1

                # VIDEOS
                elif lower.endswith((
                    ".mp4",
                    ".mov",
                    ".webm"
                )):

                    REAL_STATE["videos"] += 1

                # LOGS
                elif lower.endswith(".log"):
                    pass

                    REAL_STATE["logs"] += 1

scan()

print("")
print("================================================")
print(" IOTEC REAL ECOSYSTEM")
print("================================================")
print("")

print("INTERFACES:", REAL_STATE["interfaces"])
print("HTML:", REAL_STATE["html"])
print("PYTHON:", REAL_STATE["python"])
print("VIDEOS:", REAL_STATE["videos"])
print("SOCKETIO:", REAL_STATE["socketio"])
print("PAYPAL:", REAL_STATE["paypal"])
print("FORMS:", REAL_STATE["forms"])
print("LOGS:", REAL_STATE["logs"])

print("")
print("================================================")
print(" REAL ECOSYSTEM ONLINE")
print("================================================")
print("")




