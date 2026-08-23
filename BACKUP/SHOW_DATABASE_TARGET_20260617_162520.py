import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# SHOW_DATABASE_TARGET.py

with open(
    "ENTERPRISE_RENDER_READY.py",
    "r",
    encoding="utf-8",
    errors="ignore"
) as f:

    for n, line in enumerate(f, start=1):
        pass

        if "DATABASE" in line or "sqlite3.connect" in line:
            pass

            print(f"{n}: {line.rstrip()}")


