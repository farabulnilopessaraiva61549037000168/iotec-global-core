import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path
import ast

ROOT = Path(r"C:\IOTEC")

# ============================================================

MODULE_TYPES = {

    "DATABASE":[
        "database",
        "sqlite",
        "mysql",
        "postgres",
        "db",
        "schema"
    ],

    "API":[
        "api",
        "flask",
        "fastapi",
        "route",
        "endpoint"
    ],

    "EVENT_BUS":[
        "event",
        "bus",
        "publish",
        "subscribe"
    ],

    "PAYMENT":[
        "paypal",
        "payment",
        "checkout",
        "invoice",
        "billing",
        "pix"
    ],

    "COMMERCIAL":[
        "commercial",
        "crm",
        "lead",
        "client",
        "proposal",
        "budget"
    ],

    "AI":[
        "reasoning",
        "intelligence",
        "brain",
        "ai",
        "neural",
        "llm"
    ],

    "CONTROL_TOWER":[
        "tower",
        "dashboard",
        "cockpit",
        "panel"
    ],

    "SCANNER":[
        "scanner",
        "audit",
        "locator",
        "finder"
    ],

    "REPORT":[
        "report",
        "ledger",
        "history",
        "log"
    ],

    "CONNECTOR":[
        "connector",
        "bridge",
        "gateway",
        "adapter"
    ],

    "FORM":[
        "form",
        "cadastro",
        "register"
    ],

    "WHATSAPP":[
        "whatsapp"
    ],

    "EMAIL":[
        "email",
        "mail"
    ],

    "FRONTEND":[
        "html",
        "frontend",
        "interface"
    ],

    "BOOT":[
        "boot",
        "startup",
        "kernel"
    ],

    "TEST":[
        "test",
        "stress"
    ],

    "BACKUP":[
        "backup"
    ]

}

# ============================================================

def detect_type(path):

    nome = path.stem.lower()

    for categoria, palavras in MODULE_TYPES.items():

        for palavra in palavras:

            if palavra in nome:
                return categoria

    try:

        texto = path.read_text(
            encoding="utf8",
            errors="ignore"
        ).lower()

    except:

        return "UNKNOWN"

    for categoria,palavras in MODULE_TYPES.items():

        for palavra in palavras:

            if palavra in texto:

                return categoria

    return "UNKNOWN"

# ============================================================

class Analyzer(ast.NodeVisitor):

    def __init__(self):

        self.classes = 0
        self.functions = 0
        self.imports = 0

    def visit_ClassDef(self,node):

        self.classes+=1

    def visit_FunctionDef(self,node):

        self.functions+=1

    def visit_Import(self,node):

        self.imports+=1

    def visit_ImportFrom(self,node):

        self.imports+=1

# ============================================================

def analyze(path):

    try:

        code = path.read_text(
            encoding="utf8",
            errors="ignore"
        )

        tree = ast.parse(code)

        a = Analyzer()

        a.visit(tree)

        return a

    except:

        return None

# ============================================================

print("="*70)
print("IOTEC MODULE CLASSIFIER")
print("="*70)

for file in ROOT.glob("*.py"):

    tipo = detect_type(file)

    info = analyze(file)

    print()

    print("="*60)

    print(file.name)

    print("TIPO :",tipo)

    if info:

        print("Classes :",info.classes)

        print("FunÃƒÂ§ÃƒÂµes :",info.functions)

        print("Imports :",info.imports)

    else:

        print("NÃƒÂ£o foi possÃƒÂ­vel analisar.")

print()

print("="*70)

print("FIM")



