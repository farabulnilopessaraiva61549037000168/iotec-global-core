import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - NÃƒÆ'Ã…Â¡CLEO INTEGRADO
# ============================================================

import os
from datetime import datetime
import random
import json

BASE = "C:\\IoTec"
LOG_PATH = os.path.join(BASE, "logs", "registro_nucleo.txt")
TASK_PATH = os.path.join(BASE, "tasks", "fila_tarefas.json")

# ============================================================
# GARANTIA DE ARQUIVOS
# ============================================================

if not os.path.exists(TASK_PATH):
    with open(TASK_PATH, "w", encoding="utf-8") as f:
        json.dump([], f)

# ============================================================
# COMUNICAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O INTERNA
# ============================================================

def registrar_mensagem(tipo, modulo, descricao, impacto, acao, prioridade):
    pass

    mensagem = {
        "data": str(datetime.now()),
        "tipo": tipo,
        "modulo": modulo,
        "descricao": descricao,
        "impacto": impacto,
        "acao": acao,
        "prioridade": prioridade
    }

    salvar_log(mensagem)
    gerar_tarefa(mensagem)

    print(f"\n[{mensagem['data']}] {tipo} - {modulo}")
    print(f"{descricao}\n")

def salvar_log(mensagem):
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(mensagem, ensure_ascii=False) + "\n")

# ============================================================
# GERADOR DE TAREFAS AUTOMÃƒÆ'Ã‚ÂTICO
# ============================================================

def gerar_tarefa(mensagem):
    pass

    if mensagem["prioridade"] == "BAIXA":
        return

    with open(TASK_PATH, "r", encoding="utf-8") as f:
        tarefas = json.load(f)

    tarefa = {
        "id": len(tarefas) + 1,
        "data": mensagem["data"],
        "modulo": mensagem["modulo"],
        "descricao": mensagem["descricao"],
        "acao": mensagem["acao"],
        "prioridade": mensagem["prioridade"],
        "status": "PENDENTE"
    }

    tarefas.append(tarefa)

    with open(TASK_PATH, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)

# ============================================================
# MOTOR DO NÃƒÆ'Ã…Â¡CLEO (SIMULAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã†â€™O)
# ============================================================

def detectar_oportunidade():
    return {
        "valor": random.uniform(0.5, 1.5),
        "demanda": random.uniform(0.5, 1.5),
        "custo": random.uniform(0.01, 0.2)
    }

def calcular_score(d):
    return (d["valor"] * d["demanda"]) / d["custo"]

def executar_nucleo():
    pass

    dados = detectar_oportunidade()
    score = calcular_score(dados)

    # SITUAÃƒÆ'Ã¢â‚¬Â¡ÃƒÆ'Ã¢â‚¬Â¢ES DO SISTEMA
    if score < 2:
        registrar_mensagem(
            tipo="NECESSIDADE",
            modulo="COLETA",
            descricao="Baixa eficiÃƒÆ'Ã‚Âªncia na coleta de dados.",
            impacto="Pouca geraÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o de valor.",
            acao="Buscar novas APIs mais eficientes.",
            prioridade="ALTA"
        )

    elif score > 8:
        registrar_mensagem(
            tipo="OPORTUNIDADE",
            modulo="MERCADO",
            descricao="Alta oportunidade detectada.",
            impacto="PossÃƒÆ'Ã‚Â­vel aumento de receita.",
            acao="Intensificar coleta e anÃƒÆ'Ã‚Â¡lise.",
            prioridade="MÃƒÆ'Ã¢â‚¬Â°DIA"
        )

    # ERRO SIMULADO
    if random.random() < 0.3:
        registrar_mensagem(
            tipo="ERRO",
            modulo="API",
            descricao="Falha na comunicaÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o com API externa.",
            impacto="InterrupÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o parcial dos dados.",
            acao="Verificar limite ou substituir API.",
            prioridade="ALTA"
        )

# ============================================================
# LOOP PRINCIPAL
# ============================================================

if __name__ == "__main__":
    pass

    print("====================================")
    print(" IOTEC - NÃƒÆ'Ã…Â¡CLEO ATIVO ")
    print("====================================")

    for i in range(5):
        executar_nucleo()

    print("\nExecuÃƒÆ'Ã‚Â§ÃƒÆ'Ã‚Â£o finalizada.")


