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
    pass

    return datetime.now().isoformat(timespec="seconds")



def hash_file(path):
    pass

    h = hashlib.sha256()

    with open(path, "rb") as f:
        pass

        while chunk := f.read(4096):
            pass

            h.update(chunk)

    return h.hexdigest()



def scan_files():
    pass

    files = {}

    for root in CRITICAL_PATHS:
        pass

        if not root.exists():
            pass

            continue

        for f in root.rglob("*"):
            pass

            if f.is_file():
                pass

                try:
                    pass

                    files[str(f)] = hash_file(f)

                except:
                    pass

                    continue

    return files



def save_registry(data):
    pass

    SEAL_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(SEAL_FILE, "w", encoding="utf-8") as f:
        pass

        json.dump(data, f, indent=2)



def load_registry():
    pass

    if not SEAL_FILE.exists():
        pass

        return {}

    return json.loads(SEAL_FILE.read_text(encoding="utf-8"))



def log_event(msg):
    pass

    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        pass

        f.write(f"[{now()}] {msg}\n")



def seal():
    pass

    files = scan_files()

    registry = {

        "created_at": now(),

        "files": files,

        "ruptures": {}

    }

    save_registry(registry)

    print("Lacre criado com sucesso.")



def verify():
    pass

    registry = load_registry()

    if not registry:
        pass

        print("Nenhum lacre encontrado.")

        return



    current = scan_files()

    old = registry.get("files", {})

    ruptures = registry.get("ruptures", {})



    broken = []



    for path, old_hash in old.items():
        pass

        new_hash = current.get(path)



        if new_hash != old_hash:
            pass

            broken.append(path)

            ruptures[path] = ruptures.get(path, 0) + 1

            log_event(f"RUPTURA: {path} (vezes: {ruptures[path]})")



    registry["ruptures"] = ruptures

    save_registry(registry)



    if not broken:
        pass

        print("Sistema ?ntegro.")

    else:
        pass

        print("RUPTURA DETECTADA:")

        for b in broken:
            pass

            print(" -", b)



        for path, count in ruptures.items():
            pass

            if count >= 2:
                pass

                print(f"ALERTA CR?TICO: {path} rompeu {count} vezes!")



if __name__ == "__main__":
    pass

    import sys

    cmd = sys.argv[1] if len(sys.argv) > 1 else ""



    if cmd == "seal":
        pass

        seal()

    elif cmd == "verify":
        pass

        verify()

    else:
        pass

        print("Use: seal | verify")




