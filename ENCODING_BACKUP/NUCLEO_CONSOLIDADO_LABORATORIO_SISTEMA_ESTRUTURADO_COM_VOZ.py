import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC CORE - SISTEMA ESTRUTURADO COM ASSISTENTE DE VOZ
# ============================================================

import os
import json
import random
from datetime import datetime

# ========================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O BASE
# ========================

BASE = "C:\\IoTec"
LOG_PATH = os.path.join(BASE, "logs")
TASK_PATH = os.path.join(BASE, "tasks.json")

# ========================
# GARANTIR AMBIENTE
# ========================

os.makedirs(LOG_PATH, exist_ok=True)

if not os.path.exists(TASK_PATH):
    with open(TASK_PATH, "w") as f:
        json.dump([], f)

# ========================
# VOZ (TTS SIMPLES)
# ========================

try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 180)

    def falar(texto):
        engine.say(texto)
        engine.runAndWait()
except:
    def falar(texto):
        print("[VOZ DESATIVADA]", texto)

# ========================
# COMUNICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INTERNA
# ========================

def registrar_mensagem(tipo, modulo, descricao):
    msg = {
        "data": str(datetime.now()),
        "tipo": tipo,
        "modulo": modulo,
        "descricao": descricao
    }

    with open(os.path.join(LOG_PATH, "log.txt"), "a", encoding="utf-8") as f:
        f.write(json.dumps(msg, ensure_ascii=False) + "\n")

    print(f"[{tipo}] {descricao}")

# ========================
# MOTOR DE DECISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O (NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO)
# ========================

def detectar_oportunidade():
    return {
        "valor": random.uniform(0.5, 2),
        "demanda": random.uniform(0.5, 2),
        "custo": random.uniform(0.01, 0.2)
    }

def calcular_score(d):
    return (d["valor"] * d["demanda"]) / d["custo"]

def decidir_acao(score):
    if score > 8:
        return "EXPANDIR"
    elif score > 3:
        return "ANALISAR"
    else:
        return "IGNORAR"

# ========================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ========================

def executar_nucleo(pedido):
    pass

    dados = detectar_oportunidade()
    score = calcular_score(dados)
    decisao = decidir_acao(score)

    if decisao == "EXPANDIR":
        resposta = "Identifiquei uma oportunidade forte. Vou explorar e gerar valor."
        registrar_mensagem("OPORTUNIDADE", "NUCLEO", resposta)

    elif decisao == "ANALISAR":
        resposta = "A oportunidade ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© moderada. Vou analisar antes de agir."
        registrar_mensagem("ANALISE", "NUCLEO", resposta)

    else:
        resposta = "NÃƒÆ'Ã†â€™o identifiquei valor suficiente. Vou ignorar essa rota."
        registrar_mensagem("DESCARTE", "NUCLEO", resposta)

    return resposta

# ========================
# ASSISTENTE (RECEPÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O)
# ========================

def assistente():
    pass

    mensagem = """
Bem-vindo ao IoTec.

Eu sou sua assistente inteligente.
VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª pode solicitar anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lises, oportunidades ou suporte.

Como posso ajudar?
"""

    print(mensagem)
    falar(mensagem)

    while True:
        pass

        entrada = input("VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª: ")

        if entrada.lower() in ["sair", "exit"]:
            falar("Encerrando atendimento. AtÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© logo.")
            break

        # nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo decide
        resposta = executar_nucleo(entrada)

        print("IoTec:", resposta)
        falar(resposta)

# ========================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ========================

if __name__ == "__main__":
    assistente()


