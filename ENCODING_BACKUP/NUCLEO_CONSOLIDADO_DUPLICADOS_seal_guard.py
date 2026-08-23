import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import json
import hashlib
from pathlib import Path
from datetime import datetime

BASE = Path("C:/IOTEC")
SEAL_FILE = BASE / "STATE" / "seal_registry.json"
LOG_FILE = BASE / "LOGS" / "seal_events.log"

CRITICAL_PATHS = [
    BASE / "CONFIG",
    BASE / "CORE",
    BASE / "MODULES"
]

def now():
    return datetime.now().isoformat(timespec="seconds")

def hash_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(4096):
            h.update(chunk)
    return h.hexdigest()

def scan_files():
    files = {}
    for root in CRITICAL_PATHS:
        if not root.exists():
            continue
        for f in root.rglob("*"):
            if f.is_file():
                try:
                    files[str(f)] = hash_file(f)
                except:
                    continue
    return files

def save_registry(data):
    SEAL_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(SEAL_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def load_registry():
    if not SEAL_FILE.exists():
        return {}
    return json.loads(SEAL_FILE.read_text(encoding="utf-8"))

def log_event(msg):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{now()}] {msg}\n")

def seal():
    files = scan_files()
    registry = {
        "created_at": now(),
        "files": files,
        "ruptures": {}
    }
    save_registry(registry)
    print("Lacre criado com sucesso.")

def verify():
    registry = load_registry()
    if not registry:
        print("Nenhum lacre encontrado.")
        return

    current = scan_files()
    old = registry.get("files", {})
    ruptures = registry.get("ruptures", {})

    broken = []

    for path, old_hash in old.items():
        new_hash = current.get(path)

        if new_hash != old_hash:
            broken.append(path)
            ruptures[path] = ruptures.get(path, 0) + 1
            log_event(f"RUPTURA: {path} (vezes: {ruptures[path]})")

    registry["ruptures"] = ruptures
    save_registry(registry)

    if not broken:
        print("Sistema ?ntegro.")
    else:
        print("RUPTURA DETECTADA:")
        for b in broken:
            print(" -", b)

        for path, count in ruptures.items():
            if count >= 2:
                print(f"ALERTA CR?TICO: {path} rompeu {count} vezes!")

if __name__ == "__main__":
    import sys
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""

    if cmd == "seal":
        seal()
    elif cmd == "verify":
        verify()
    else:
        print("Use: seal | verify")


