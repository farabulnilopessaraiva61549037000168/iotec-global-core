import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - SISTEMA DE CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPIA E OFICINA DE INTERFACES
# ============================================================

import os
import shutil
from datetime import datetime

# ============================================================
# DIRETÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIOS
# ============================================================

BASE = "C:\\IoTec"
ORIGEM = os.path.join(BASE, "interfaces_origem")
OFICINA = os.path.join(BASE, "oficina")
LOG = os.path.join(BASE, "log_oficina.txt")

os.makedirs(ORIGEM, exist_ok=True)
os.makedirs(OFICINA, exist_ok=True)

# ============================================================
# LOG
# ============================================================

def registrar(msg):
    linha = f"[{datetime.now()}] {msg}"
    print(linha)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(linha + "\n")

# ============================================================
# BUSCA DE INTERFACES
# ============================================================

def buscar_interfaces():
    arquivos = []

    for root, dirs, files in os.walk(ORIGEM):
        for file in files:
            if file.endswith((".html", ".css", ".js")):
                arquivos.append(os.path.join(root, file))

    registrar(f"{len(arquivos)} interfaces encontradas")
    return arquivos

# ============================================================
# CÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œPIA SEGURA
# ============================================================

def copiar_para_oficina(caminho):
    nome = os.path.basename(caminho)
    destino = os.path.join(OFICINA, nome)

    shutil.copy2(caminho, destino)

    registrar(f"CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³pia criada: {nome}")
    return destino

# ============================================================
# MODIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O CONTROLADA
# ============================================================

def ajustar_interface(caminho):
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo = f.read()

        # ajuste simples (exemplo)
        if "button" in conteudo:
            conteudo = conteudo.replace("button", "button style='transition:0.3s'")

        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)

        registrar(f"Ajuste aplicado: {os.path.basename(caminho)}")

    except Exception as e:
        registrar(f"Erro ao ajustar: {e}")

# ============================================================
# RESTAURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

def restaurar_original(nome):
    origem = os.path.join(ORIGEM, nome)
    destino = os.path.join(OFICINA, nome)

    if os.path.exists(origem):
        shutil.copy2(origem, destino)
        registrar(f"Interface restaurada: {nome}")

# ============================================================
# PROCESSO PRINCIPAL
# ============================================================

def executar_oficina():
    pass

    arquivos = buscar_interfaces()

    for arq in arquivos:
        copia = copiar_para_oficina(arq)

        ajustar_interface(copia)

    registrar("Processo da oficina finalizado")

# ============================================================
# START
# ============================================================

if __name__ == "__main__":
    executar_oficina()


