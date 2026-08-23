import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ======================================================================

IGNORAR_PASTAS = {

    "venv",

    ".venv",

    "env",

    ".git",

    "__pycache__",

    "node_modules",

    "dist",

    "build",

    "site-packages",

    "Lib",

    "Scripts"

}

IGNORAR_ARQUIVOS = (

    ".bak",

    ".old",

    ".backup",

    ".tmp"

)

# ======================================================================

def deve_ignorar(self, arquivo):

    caminho = str(arquivo).lower()

    for pasta in IGNORAR_PASTAS:

        if f"\\{pasta.lower()}" in caminho:

            return True

    for extensao in IGNORAR_ARQUIVOS:

        if caminho.endswith(extensao):

            return True

    return False

# ======================================================================

def discover_modules(self):

    print()

    print("="*70)

    print("LOCALIZANDO MÃƒâ€œDULOS DA IOTEC")

    print("="*70)

    total = 0

    ignorados = 0

    for file in ROOT.rglob("*.py"):

        if self.deve_ignorar(file):

            ignorados += 1

            continue

        self.modules[file.name] = file

        total += 1

    print()

    print("MÃƒÂ³dulos IOTEC :", total)

    print("Ignorados     :", ignorados)

    print()



