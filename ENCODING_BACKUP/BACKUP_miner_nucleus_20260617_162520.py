import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
IGNORED_FOLDERS = [
    "venv",
    "__pycache__",
    ".git",
    "node_modules",
    "Lib\\site-packages"
]

def should_ignore(path):
    path_str = str(path)
    return any(ignored in path_str for ignored in IGNORED_FOLDERS)



