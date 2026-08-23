import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC TOWER DISCOVERY ENGINE
# DESCOBRE A TOPOLOGIA REAL DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# SOMENTE LEITURA
# ==========================================================

import os
import re
import json
from datetime import datetime

ROOT = r"C:\IOTEC"

OUTPUT = r"C:\IOTEC\IOTEC_MASTER_TOPOLOGY.json"

TARGETS = [

    "IOTEC_CONTROL_TOWER_ENGINE.py",
    "IOTEC_CORE_MANAGER.py",
    "IOTEC_CORE_RUNNER.py",
    "ORCHESTRATOR_ENGINE.py",
    "nucleus_orchestrator.py",
    "IOTEC_CENTRAL_BRAIN.py",
    "IOTEC_UNIFIED_BRAIN.py",
    "IOTEC_MEMORY_ENGINE.py",
    "REVENUE_OPERATION_CENTER.py",
    "SALES_BRAIN.py",
    "CRM_ENGINE.py"
]

topology = {

    "generated": str(datetime.now()),

    "nodes": {},

    "summary": {

        "files_found": 0,
        "imports_found": 0,
        "functions_found": 0,
        "sqlite_usage": 0,
        "json_usage": 0
    }
}

# ==========================================================
# LOCALIZA ARQUIVOS
# ==========================================================

targets_found = {}

for root, dirs, files in os.walk(ROOT):
    pass

    for file in files:
        pass

        if file in TARGETS:
            pass

            targets_found[file] = os.path.join(root, file)

# ==========================================================
# ANALISA
# ==========================================================

for name, path in targets_found.items():
    pass

    try:
        pass

        with open(
            path,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            content = f.read()

        imports = re.findall(
            r"import\s+([a-zA-Z0-9_\.]+)",
            content
        )

        imports += re.findall(
            r"from\s+([a-zA-Z0-9_\.]+)\s+import",
            content
        )

        functions = re.findall(
            r"def\s+([a-zA-Z0-9_]+)\s*\(",
            content
        )

        sqlite_found = (
            "sqlite3" in content.lower()
        )

        json_found = (
            "json" in content.lower()
        )

        topology["nodes"][name] = {

            "path": path,

            "imports": imports,

            "functions": functions,

            "function_count": len(functions),

            "sqlite": sqlite_found,

            "json": json_found
        }

        topology["summary"]["files_found"] += 1
        topology["summary"]["imports_found"] += len(imports)
        topology["summary"]["functions_found"] += len(functions)

        if sqlite_found:
            topology["summary"]["sqlite_usage"] += 1

        if json_found:
            topology["summary"]["json_usage"] += 1

    except Exception as e:
        pass

        topology["nodes"][name] = {
            "error": str(e)
        }

# ==========================================================
# SALVA
# ==========================================================

with open(
    OUTPUT,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        topology,
        f,
        indent=4,
        ensure_ascii=False
    )

# ==========================================================
# RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO
# ==========================================================

print("")
print("===================================")
print("IOTEC TOWER DISCOVERY ENGINE")
print("===================================")
print("")

print(
    "ARQUIVOS ANALISADOS:",
    topology["summary"]["files_found"]
)

print(
    "IMPORTS:",
    topology["summary"]["imports_found"]
)

print(
    "FUNCOES:",
    topology["summary"]["functions_found"]
)

print(
    "SQLITE:",
    topology["summary"]["sqlite_usage"]
)

print(
    "JSON:",
    topology["summary"]["json_usage"]
)

print("")
print("TOPOLOGIA:")
print(OUTPUT)

print("")
print("CONCLUIDO")




