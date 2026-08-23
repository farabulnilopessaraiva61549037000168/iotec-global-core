import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# fix_broker.py

file_path = "broker.py"

with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

# 1. substitui broadcast antigo
code = code.replace(
    "def broadcast(msg):",
    "def broadcast(msg, sender_conn):"
)

# 2. ajusta chamada do broadcast
code = code.replace(
    "broadcast(msg)",
    "broadcast(msg, conn)"
)

# 3. injeta filtro se ainda nÃƒÆ'Ã†â€™o existir
if "if c != sender_conn" not in code:
    code = code.replace(
        "for c in clients:",
        "for c in clients:\n        if c != sender_conn:"
    )

with open(file_path, "w", encoding="utf-8") as f:
    f.write(code)

print("[FIX] broker.py atualizado automaticamente")


