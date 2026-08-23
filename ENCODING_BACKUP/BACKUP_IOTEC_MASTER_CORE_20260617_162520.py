import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import importlib.util
import importlib.machinery
import traceback

ROOT = os.path.dirname(os.path.abspath(__file__))

# ============================
# REGISTRO CENTRAL DO SISTEMA
# ============================

SYSTEM_MAP = {
    "commercial": [],
    "orchestration": [],
    "operational": [],
    "unknown": []
}

ACTIVE_MODULES = []

# ============================
# DESCUBRE MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# ============================

def discover_modules():
    print("\n[MASTER_CORE] Escaneando nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo...\n")

    for root, dirs, files in os.walk(ROOT):
        for file in files:
            if file.endswith(".py") and file != "IOTEC_MASTER_CORE.py":
                path = os.path.join(root, file)

                name = file.lower()

                if "cerebro" in name or "commercial" in name:
                    SYSTEM_MAP["commercial"].append(path)

                elif "orchestrator" in name or "core" in name or "engine" in name:
                    SYSTEM_MAP["orchestration"].append(path)

                elif "agent" in name or "pipeline" in name or "worker" in name:
                    SYSTEM_MAP["operational"].append(path)

                else:
                    SYSTEM_MAP["unknown"].append(path)

# ============================
# CARREGA MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO SEGURO
# ============================

def safe_import(module_path):
    try:
        module_name = os.path.splitext(os.path.basename(module_path))[0]
        spec = importlib.util.spec_from_file_location(module_name, module_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        ACTIVE_MODULES.append(module_name)
        return module
    except Exception as e:
        print(f"[ERROR] Falha ao carregar {module_path}")
        print(traceback.format_exc())
        return None

# ============================
# INICIALIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO SISTEMA
# ============================

def boot_system():
    print("\n===================================")
    print("IOTEC MASTER CORE STARTING")
    print("===================================\n")

    discover_modules()

    print("\n[MASTER_CORE] Resumo do sistema:")
    for k, v in SYSTEM_MAP.items():
        print(f"  {k}: {len(v)} mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos")

    print("\n[MASTER_CORE] Inicializando mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­ticos...\n")

    # carrega primeiro orquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
    for m in SYSTEM_MAP["orchestration"][:5]:
        safe_import(m)

    # depois comercial
    for m in SYSTEM_MAP["commercial"][:3]:
        safe_import(m)

    print("\n[MASTER_CORE] Sistema ativo.")
    print(f"[MASTER_CORE] MÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos carregados: {len(ACTIVE_MODULES)}")

# ============================
# LOOP PRINCIPAL
# ============================

def run():
    boot_system()

    print("\n[MASTER_CORE] Sistema em execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.\n")

    while True:
        cmd = input("IOTEC > ").strip().lower()

        if cmd == "status":
            print("\n--- STATUS ---")
            print(f"Ativos: {len(ACTIVE_MODULES)} mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³dulos")
            print("OrquestraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:", len(SYSTEM_MAP["orchestration"]))
            print("Comercial:", len(SYSTEM_MAP["commercial"]))
            print("Operacional:", len(SYSTEM_MAP["operational"]))

        elif cmd == "modules":
            print("\n--- MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS ATIVOS ---")
            for m in ACTIVE_MODULES:
                print(m)

        elif cmd == "exit":
            print("Encerrando MASTER CORE...")
            break

        else:
            print("Comandos: status | modules | exit")

# ============================
# START
# ============================

if __name__ == "__main__":
    run()


