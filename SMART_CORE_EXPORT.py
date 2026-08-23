import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

from collections import Counter



# ======================================================

# CONFIG

# ======================================================



ROOT = input("Digite o caminho do nÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºcleo:\n> ").strip()



IGNORE_DIRS = {

    "node_modules",

    ".git",

    "__pycache__",

    "dist",

    "build",

    ".next",

    ".cache",

    "venv",

    ".venv"

}



IMPORTANT_WORDS = [

    "core",

    "api",

    "auth",

    "payment",

    "chat",

    "ai",

    "agent",

    "dashboard",

    "admin",

    "memory",

    "stripe",

    "whatsapp",

    "openai",

    "voice",

    "crm",

]



# ======================================================

# STORAGE

# ======================================================



extensions = Counter()

important_files = []

possible_products = []

folder_map = Counter()



total_files = 0

total_dirs = 0



# ======================================================

# SCAN

# ======================================================



for root, dirs, files in os.walk(ROOT):
    pass



    # remove pastas inÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âºteis

    dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]



    total_dirs += len(dirs)



    folder_name = os.path.basename(root)



    if folder_name:
        pass

        folder_map[folder_name] += 1



    for file in files:
        pass



        total_files += 1



        full = os.path.join(root, file)



        ext = os.path.splitext(file)[1].lower()



        if ext:
            pass

            extensions[ext] += 1



        name = file.lower()



        # importantes

        if any(word in name for word in IMPORTANT_WORDS):
            pass

            important_files.append(full)



        # possÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­veis produtos

        if any(word in name for word in [

            "dashboard",

            "crm",

            "chat",

            "automation",

            "agent",

            "ai"

        ]):

            possible_products.append(file)



# ======================================================

# REPORT

# ======================================================



lines = []



lines.append("===================================")

lines.append("IOTEC SMART CORE SUMMARY")

lines.append("===================================\n")



lines.append(f"Projeto analisado: {ROOT}\n")



lines.append(f"Total de arquivos: {total_files}")

lines.append(f"Total de pastas: {total_dirs}\n")



# tecnologias

lines.append("TOP TECNOLOGIAS:")



for ext, count in extensions.most_common(10):
    pass

    lines.append(f"{ext} -> {count}")



# estrutura

lines.append("\nTOP PASTAS:")



for folder, count in folder_map.most_common(15):
    pass

    lines.append(f"{folder}")



# mÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³dulos importantes

lines.append("\nMÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"DULOS IMPORTANTES:")



for item in important_files[:25]:
    pass

    lines.append(item)



# possÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â­veis produtos

lines.append("\nPOSSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂVEIS PRODUTOS:")



for item in list(set(possible_products))[:20]:
    pass

    lines.append(item)



# ======================================================

# SAVE

# ======================================================



output_file = "NUCLEO_INTELIGENTE_RESUMIDO.txt"



with open(output_file, "w", encoding="utf-8") as f:
    pass

    f.write("\n".join(lines))



print("\n===================================")

print("ANÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚ÂLISE FINALIZADA")

print("===================================\n")



print(f"Arquivo gerado:")

print(output_file)



print("\nEsse arquivo serÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â¡ pequeno e estratÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©gico.")






