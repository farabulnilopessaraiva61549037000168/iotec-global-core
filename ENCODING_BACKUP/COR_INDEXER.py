import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC / IBEX
# CORE INDEXER + CURATOR ENGINE
# ============================================================
#
# OBJETIVO:
# - mapear todo o nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo
# - detectar duplicados
# - detectar conflitos
# - detectar versÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes paralelas
# - catalogar mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos
# - detectar arquivos quebrados
# - detectar interfaces suspeitas
# - preservar histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico
# - criar curadoria central
# - impedir perda estrutural
#
# ============================================================

import os
import re
import json
import hashlib
import unicodedata
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
    "CORE_REPORTS"
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
            "CORE_INDEXER.log"
        ),
        "a",
        encoding="utf-8"
    ) as f:

        f.write(line + "\n")

# ============================================================
# NORMALIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def normalize_name(name):
    pass

    normalized = unicodedata.normalize(
        "NFKD",
        name
    )

    normalized = normalized.encode(
        "ASCII",
        "ignore"
    ).decode("ASCII")

    normalized = normalized.replace(
        " ",
        "_"
    )

    normalized = re.sub(
        r"[^a-zA-Z0-9_\.]",
        "",
        normalized
    )

    normalized = re.sub(
        r"_+",
        "_",
        normalized
    )

    return normalized

# ============================================================
# HASH
# ============================================================

def file_hash(path):
    pass

    try:
        pass

        with open(path, "rb") as f:
            pass

            return hashlib.md5(
                f.read()
            ).hexdigest()

    except:
        pass

        return None

# ============================================================
# ESTRUTURA CENTRAL
# ============================================================

CATALOG = {

    "timestamp":
        str(datetime.now()),

    "total_python":
        0,

    "total_html":
        0,

    "duplicates":
        [],

    "broken":
        [],

    "conflicts":
        [],

    "interfaces":
        [],

    "modules":
        [],

    "watchdog":
        [],

    "paypal":
        [],

    "lead_routes":
        [],

    "observability":
        []
}

# ============================================================
# MAPAS INTERNOS
# ============================================================

name_map = {}
hash_map = {}

# ============================================================
# SCAN
# ============================================================

log("INICIANDO CORE INDEXER...")

for root, dirs, files in os.walk(BASE_PATH):
    pass

    for file in files:
        pass

        full_path = os.path.join(
            root,
            file
        )

        ext = os.path.splitext(file)[1].lower()

        # ====================================================
        # PYTHON
        # ====================================================

        if ext == ".py":
            pass

            CATALOG["total_python"] += 1

            normalized = normalize_name(file)

            file_md5 = file_hash(
                full_path
            )

            module = {

                "name": file,

                "normalized":
                    normalized,

                "path":
                    full_path,

                "hash":
                    file_md5
            }

            CATALOG["modules"].append(
                module
            )

            # ================================================
            # DUPLICADOS
            # ================================================

            if normalized in name_map:
                pass

                CATALOG["duplicates"].append({

                    "normalized":
                        normalized,

                    "original":
                        file,

                    "conflict_with":
                        name_map[normalized]
                })

                log(
                    f"DUPLICADO: {file}"
                )

            else:
                pass

                name_map[normalized] = file

            # ================================================
            # HASH DUPLICADO
            # ================================================

            if file_md5:
                pass

                if file_md5 in hash_map:
                    pass

                    CATALOG["conflicts"].append({

                        "file":
                            file,

                        "same_as":
                            hash_map[file_md5]
                    })

                    log(
                        f"HASH DUPLICADO: {file}"
                    )

                else:
                    pass

                    hash_map[file_md5] = file

            # ================================================
            # VERIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CONTEÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡DO
            # ================================================

            try:
                pass

                with open(
                    full_path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                # ============================================
                # WATCHDOG
                # ============================================

                if "debug=False, use_reloader=False" in content:
                    pass

                    CATALOG["watchdog"].append(
                        file
                    )

                    log(
                        f"WATCHDOG DETECTADO: {file}"
                    )

                # ============================================
                # PAYPAL
                # ============================================

                if (
                    "paypal" in content.lower()
                ):

                    CATALOG["paypal"].append(
                        file
                    )

                # ============================================
                # /lead
                # ============================================

                if "/lead" in content:
                    pass

                    CATALOG["lead_routes"].append(
                        file
                    )

                # ============================================
                # OBSERVABILITY
                # ============================================

                if (
                    "observability"
                    in content.lower()
                ):

                    CATALOG["observability"].append(
                        file
                    )

            except Exception as e:
                pass

                CATALOG["broken"].append({

                    "file":
                        file,

                    "error":
                        str(e)
                })

                log(
                    f"ERRO LEITURA: {file}"
                )

        # ====================================================
        # HTML
        # ====================================================

        elif ext == ".html":
            pass

            CATALOG["total_html"] += 1

            size = os.path.getsize(
                full_path
            )

            interface = {

                "file":
                    file,

                "size":
                    size,

                "path":
                    full_path,

                "status":
                    "OK"
            }

            if size < 1500:
                pass

                interface["status"] = (
                    "SUSPECT"
                )

                log(
                    f"INTERFACE SUSPEITA: {file}"
                )

            CATALOG["interfaces"].append(
                interface
            )

# ============================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO FINAL
# ============================================================

REPORT_FILE = os.path.join(
    REPORT_DIR,
    "CORE_CATALOG.json"
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
print(" IOTEC / IBEX CORE INDEXER")
print("================================================")
print("")

print(
    f"PYTHON FILES: "
    f"{CATALOG['total_python']}"
)

print(
    f"HTML FILES: "
    f"{CATALOG['total_html']}"
)

print(
    f"DUPLICATES: "
    f"{len(CATALOG['duplicates'])}"
)

print(
    f"CONFLICTS: "
    f"{len(CATALOG['conflicts'])}"
)

print(
    f"BROKEN: "
    f"{len(CATALOG['broken'])}"
)

print(
    f"WATCHDOG: "
    f"{len(CATALOG['watchdog'])}"
)

print(
    f"PAYPAL MODULES: "
    f"{len(CATALOG['paypal'])}"
)

print(
    f"LEAD ROUTES: "
    f"{len(CATALOG['lead_routes'])}"
)

print(
    f"OBSERVABILITY MODULES: "
    f"{len(CATALOG['observability'])}"
)

print("")
print("================================================")
print(" CORE CATALOG GENERATED")
print("================================================")
print("")

log("CORE INDEXER FINALIZADO.")


