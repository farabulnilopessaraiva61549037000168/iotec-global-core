import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

import json

from datetime import datetime



ROOT = input("Digite o caminho do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo: ").strip()



report = {

    "timestamp": str(datetime.now()),

    "root": ROOT,

    "total_files": 0,

    "py_files": 0,

    "json_files": 0,

    "js_files": 0,

    "html_files": 0,

    "active_modules": [],

    "dead_files": [],

    "orchestration_candidates": [],

    "errors": []

}



ORCHESTRATION_KEYWORDS = [

    "orchestrator", "engine", "core", "brain", "manager",

    "pipeline", "controller", "boot", "master", "central"

]



def classify_file(path):
    pass

    name = path.lower()



    if any(k in name for k in ORCHESTRATION_KEYWORDS):
        pass

        report["orchestration_candidates"].append(path)



    if path.endswith(".py"):
        pass

        report["py_files"] += 1

    elif path.endswith(".json"):
        pass

        report["json_files"] += 1

    elif path.endswith(".js"):
        pass

        report["js_files"] += 1

    elif path.endswith(".html"):
        pass

        report["html_files"] += 1



def scan():
    pass

    for root, dirs, files in os.walk(ROOT):
        pass

        for f in files:
            pass

            full = os.path.join(root, f)

            report["total_files"] += 1



            try:
                pass

                classify_file(full)



                if f.endswith(".py"):
                    pass

                    # tenta validar se arquivo estÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ vivo (nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o vazio)

                    if os.path.getsize(full) > 10:
                        pass

                        report["active_modules"].append(full)

                    else:
                        pass

                        report["dead_files"].append(full)



            except Exception as e:
                pass

                report["errors"].append({

                    "file": full,

                    "error": str(e)

                })



def generate_summary():
    pass

    return {

        "TOTAL_ARQUIVOS": report["total_files"],

        "MODULOS_PY": report["py_files"],

        "ORQUESTRADORES_POSSIVEIS": len(report["orchestration_candidates"]),

        "MODULOS_ATIVOS": len(report["active_modules"]),

        "ARQUIVOS_MORTOS": len(report["dead_files"]),

        "ERROS": len(report["errors"]),

        "STATUS": "SAUDAVEL" if len(report["errors"]) < 50 else "INSTAVEL"

    }



def print_dashboard(summary):
    pass

    print("\n" + "="*50)

    print(" IOTEC CONTROL PANEL")

    print("="*50)



    for k, v in summary.items():
        pass

        print(f"{k}: {v}")



    print("\n--- TOP ORCHESTRATORS ---")

    for item in report["orchestration_candidates"][:10]:
        pass

        print(item)



    print("\n--- ACTIVE MODULES SAMPLE ---")

    for item in report["active_modules"][:10]:
        pass

        print(item)



    print("\n--- DEAD FILES SAMPLE ---")

    for item in report["dead_files"][:10]:
        pass

        print(item)



def save():
    pass

    with open("IOTEC_CONTROL_REPORT.json", "w", encoding="utf-8") as f:
        pass

        json.dump(report, f, indent=4, ensure_ascii=False)



scan()

summary = generate_summary()

print_dashboard(summary)

save()



print("\nRelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio salvo em: IOTEC_CONTROL_REPORT.json")




