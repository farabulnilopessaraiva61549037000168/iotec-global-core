import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

print("")
print("==========================================")
print(" IOTEC INTERFACE RESTORATION")
print("==========================================")
print("")

# ==========================================
# FILES
# ==========================================

files = [

    r"C:\Tecnologia\showroom\index.html",
    r"C:\Tecnologia\IOTEC BL ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Tecnologia que transforma.htm"
]

# ==========================================
# REPLACEMENTS
# ==========================================

replacements = {

    "InovaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "InovaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "negÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³cio": "negÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³cio",
    "transformaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "transformaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "soluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âµes": "soluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes",
    "gestÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "gestÃƒÆ'Ã†â€™o",
    "informaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "informaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "produÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "produÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "operaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "integraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "integraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "configuraÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "configuraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "otimizaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "otimizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "evoluÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o": "evoluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â·": "ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â·",
    "ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡": ""
}

# ==========================================
# PROCESS
# ==========================================

for file_path in files:
    pass

    path = Path(file_path)

    if not path.exists():
        pass

        print(f"[ERROR] FILE NOT FOUND:")
        print(file_path)
        continue

    print("")
    print("[PROCESSING]")
    print(file_path)

    # BACKUP

    backup = str(path) + ".restorebackup"

    Path(backup).write_text(
        path.read_text(
            encoding="utf-8",
            errors="ignore"
        ),
        encoding="utf-8"
    )

    print("[OK] BACKUP CREATED")

    # READ

    content = path.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    # REPLACE

    for wrong, correct in replacements.items():
        pass

        content = content.replace(
            wrong,
            correct
        )

    # META UTF8

    if "charset" not in content:
        pass

        content = content.replace(
            "<head>",
            "<head><meta charset='UTF-8'>"
        )

    # SAVE

    path.write_text(
        content,
        encoding="utf-8"
    )

    print("[OK] ENCODING RESTORED")

print("")
print("==========================================")
print(" RESTORATION COMPLETE")
print("==========================================")


