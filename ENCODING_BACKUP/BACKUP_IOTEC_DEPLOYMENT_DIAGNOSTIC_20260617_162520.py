import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# IOTEC DEPLOYMENT DIAGNOSTIC
# =========================================================

import os
import importlib.util
import socket

print("=" * 60)
print("IOTEC DEPLOYMENT DIAGNOSTIC")
print("=" * 60)

# =========================================================
# CHECK FILES
# =========================================================

required_files = [
    "IOTEC_GLOBAL_CORE.py",
    "requirements.txt"
]

print("\n[CHECK] REQUIRED FILES\n")

for file in required_files:
    pass

    if os.path.exists(file):
        print(f"[OK] {file}")

    else:
        print(f"[MISSING] {file}")

# =========================================================
# CHECK REQUIREMENTS
# =========================================================

print("\n[CHECK] REQUIREMENTS CONTENT\n")

if os.path.exists("requirements.txt"):
    pass

    with open("requirements.txt", "r") as f:
        pass

        content = f.read()

        print(content)

        if "flask" in content.lower():
            print("[OK] Flask detected")

        else:
            print("[ERROR] Flask missing")

        if "gunicorn" in content.lower():
            print("[OK] Gunicorn detected")

        else:
            print("[ERROR] Gunicorn missing")

# =========================================================
# CHECK IMPORT
# =========================================================

print("\n[CHECK] PYTHON IMPORT\n")

try:
    pass

    spec = importlib.util.spec_from_file_location(
        "IOTEC_GLOBAL_CORE",
        "IOTEC_GLOBAL_CORE.py"
    )

    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)

    print("[OK] IOTEC_GLOBAL_CORE imported")

except Exception as e:
    pass

    print("[IMPORT ERROR]")
    print(e)

# =========================================================
# CHECK FLASK APP
# =========================================================

print("\n[CHECK] FLASK APP\n")

try:
    pass

    from IOTEC_GLOBAL_CORE import app

    print("[OK] Flask app detected")

except Exception as e:
    pass

    print("[FLASK ERROR]")
    print(e)

# =========================================================
# CHECK PORT
# =========================================================

print("\n[CHECK] PORT TEST\n")

PORT = int(os.environ.get("PORT", 5000))

try:
    pass

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    result = sock.connect_ex(("127.0.0.1", PORT))

    if result == 0:
        print(f"[WARNING] Port {PORT} already in use")

    else:
        print(f"[OK] Port {PORT} available")

    sock.close()

except Exception as e:
    pass

    print("[PORT ERROR]")
    print(e)

# =========================================================
# CHECK GUNICORN COMMAND
# =========================================================

print("\n[CHECK] RENDER START COMMAND\n")

expected = "gunicorn IOTEC_GLOBAL_CORE:app"

print(f"[EXPECTED] {expected}")

# =========================================================
# FINAL STATUS
# =========================================================

print("\n" + "=" * 60)
print("DIAGNOSTIC FINISHED")
print("=" * 60)

print("""
NEXT CHECKS:

1. VERIFY GITHUB UPDATED FILES
2. VERIFY RENDER START COMMAND
3. VERIFY REQUIREMENTS.TXT
4. VERIFY SERVICE LOGS
5. VERIFY PYTHON VERSION
""")


