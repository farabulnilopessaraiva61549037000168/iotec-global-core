import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import datetime
import json

# Banco de memÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³ria temporÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ria
memoria_temporaria = {
    "24h": [],
    "48h": []
}

# Registro de tarefas executadas pelo sistema
def registrar_execucao(tarefa, resultado, etica_aprovada=True):
    registro = {
        "data": datetime.datetime.now().isoformat(),
        "tarefa": tarefa,
        "resultado": resultado,
        "etico": etica_aprovada
    }

    memoria_temporaria["24h"].append(registro)
    memoria_temporaria["48h"].append(registro)

    # MantÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©m apenas os ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºltimos 24h e 48h
    agora = datetime.datetime.now()
    memoria_temporaria["24h"] = [r for r in memoria_temporaria["24h"]
                                  if datetime.datetime.fromisoformat(r["data"]) > agora - datetime.timedelta(hours=24)]
    memoria_temporaria["48h"] = [r for r in memoria_temporaria["48h"]
                                  if datetime.datetime.fromisoformat(r["data"]) > agora - datetime.timedelta(hours=48)]

# Sistema ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tico decisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio
def decisao_etica(situacao, contexto):
    # SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de uma anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica crÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­tica
    if "ilegal" in contexto.lower() or "antiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tico" in contexto.lower():
        return False
    return True

# ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de aÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o segura com fallback
def executar_acao(tarefa, contexto):
    etica = decisao_etica(tarefa, contexto)
    if etica:
        resultado = f"AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o '{tarefa}' executada com seguranÃƒÆ'Ã†â€™a."
    else:
        resultado = f"AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o '{tarefa}' adiada ou redirecionada para anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise humana."
    registrar_execucao(tarefa, resultado, etica)
    return resultado

# Exportar logs para revisÃƒÆ'Ã†â€™o
def exportar_logs(intervalo="24h"):
    with open(f"log_execucoes_{intervalo}.json", "w") as f:
        json.dump(memoria_temporaria[intervalo], f, indent=2)
    return f"log_execucoes_{intervalo}.json"


