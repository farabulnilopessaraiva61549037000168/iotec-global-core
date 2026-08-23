# ==============================================================================
# 112_AUTONOMOUS_WORKFORCE_ENGINE.py
# IOTEC AUTONOMOUS WORKFORCE ENGINE
# ==============================================================================

import json
from datetime import datetime

print("=" * 90)
print("IOTEC AUTONOMOUS WORKFORCE ENGINE")
print("FORÃƒâ€¡A DE TRABALHO DIGITAL")
print("=" * 90)
print()

ARQUIVO = "IOTEC_EXECUTION_QUEUE.json"

try:
    with open(ARQUIVO, "r", encoding="utf8") as f:
        fila = json.load(f)
except Exception:
    print("Fila operacional nÃƒÂ£o encontrada.")
    raise SystemExit()

AGENTES = {

    "Pesquisar site oficial": "SITE_AGENT",
    "Pesquisar telefone": "PHONE_AGENT",
    "Pesquisar e-mail": "EMAIL_AGENT",
    "Pesquisar LinkedIn": "LINKEDIN_AGENT",
    "Identificar decisor": "INTELLIGENCE_AGENT",
    "Gerar estratÃƒÂ©gia comercial": "OPENAI_AGENT",
    "Preparar apresentaÃƒÂ§ÃƒÂ£o": "PRESENTATION_AGENT",
    "Preparar proposta": "PROPOSAL_AGENT",
    "Registrar CRM": "CRM_AGENT"

}

execucao = []

print("=" * 90)
print("DISTRIBUIÃƒâ€¡ÃƒÆ'O")
print("=" * 90)
print()

for tarefa in fila["tarefas"]:

    agente = AGENTES.get(tarefa["tarefa"], "GENERAL_AGENT")

    registro = {

        "ordem": tarefa["ordem"],
        "empresa": tarefa["empresa"],
        "tarefa": tarefa["tarefa"],
        "agente": agente,
        "status": "PENDENTE",
        "inicio": None,
        "fim": None

    }

    execucao.append(registro)

    print(f"[{agente}]")
    print("Empresa :", tarefa["empresa"])
    print("Tarefa  :", tarefa["tarefa"])
    print("Status  : PENDENTE")
    print()

with open(
    "IOTEC_WORKFORCE_QUEUE.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        {
            "generated_at": datetime.now().isoformat(),
            "tarefas": execucao
        },
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 90)
print("RESUMO")
print("=" * 90)
print()

print("Agentes cadastrados :", len(set(AGENTES.values())))
print("Tarefas distribuÃƒÂ­das:", len(execucao))

print()

print("=" * 90)
print("FILOSOFIA")
print("=" * 90)
print()

print("O Kernel nÃƒÂ£o executa tarefas diretamente.")
print("O Kernel coordena agentes especializados.")
print()
print("Cada agente declara sua capacidade.")
print("Cada tarefa ÃƒÂ© encaminhada ao agente adequado.")
print()

print("=" * 90)
print("ARQUIVO GERADO")
print("=" * 90)
print()

print("IOTEC_WORKFORCE_QUEUE.json")

print()

print("=" * 90)
print("STATUS")
print("=" * 90)
print()

print("WORKFORCE ENGINE OPERACIONAL.")


