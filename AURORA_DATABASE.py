import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# AURORA DATABASE
# ============================================================

from datetime import datetime
import json
import os

DATABASE_FILE = "AURORA_DATABASE.json"

# ============================================================
# ESTRUTURA INICIAL
# ============================================================

DATABASE_TEMPLATE = {
    "created_at": datetime.now().isoformat(),
    "municipios": [],
    "eventos": [],
    "alertas": [],
    "fontes": [],
    "protocolos": [],
    "clientes": []
}

# ============================================================
# CRIAR BANCO
# ============================================================

def criar_banco():
    pass

    if not os.path.exists(DATABASE_FILE):
        pass

        with open(DATABASE_FILE, "w", encoding="utf-8") as f:
            json.dump(
                DATABASE_TEMPLATE,
                f,
                ensure_ascii=False,
                indent=4
            )

        print("[OK] Banco Aurora criado")

    else:
        pass

        print("[OK] Banco Aurora encontrado")

# ============================================================
# CARREGAR
# ============================================================

def carregar():
    pass

    with open(DATABASE_FILE, "r", encoding="utf-8") as f:
        pass

        return json.load(f)

# ============================================================
# SALVAR
# ============================================================

def salvar(db):
    pass

    with open(DATABASE_FILE, "w", encoding="utf-8") as f:
        pass

        json.dump(
            db,
            f,
            ensure_ascii=False,
            indent=4
        )

# ============================================================
# REGISTRAR FONTE
# ============================================================

def registrar_fonte(nome):
    pass

    db = carregar()

    registro = {
        "nome": nome,
        "data": datetime.now().isoformat()
    }

    db["fontes"].append(registro)

    salvar(db)

    print(f"[FONTE] {nome}")

# ============================================================
# REGISTRAR EVENTO
# ============================================================

def registrar_evento(tipo, local):
    pass

    db = carregar()

    evento = {
        "tipo": tipo,
        "local": local,
        "data": datetime.now().isoformat()
    }

    db["eventos"].append(evento)

    salvar(db)

    print(f"[EVENTO] {tipo} - {local}")

# ============================================================
# REGISTRAR ALERTA
# ============================================================

def registrar_alerta(nivel, mensagem):
    pass

    db = carregar()

    alerta = {
        "nivel": nivel,
        "mensagem": mensagem,
        "data": datetime.now().isoformat()
    }

    db["alertas"].append(alerta)

    salvar(db)

    print(f"[ALERTA {nivel}] {mensagem}")

# ============================================================
# TESTE
# ============================================================

if __name__ == "__main__":
    pass

    criar_banco()

    registrar_fonte("INMET")
    registrar_fonte("ANA")

    registrar_evento(
        "SECA",
        "IBICUITINGA"
    )

    registrar_alerta(
        "ATENCAO",
        "ReservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios abaixo da mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©dia"
    )




