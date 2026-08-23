import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# FILA DE EXPERIMENTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

EXPERIMENTOS_PATH = os.path.join(BASE, "experimentos.json")

def carregar_experimentos():
    if not os.path.exists(EXPERIMENTOS_PATH):
        with open(EXPERIMENTOS_PATH, "w", encoding="utf-8") as f:
            json.dump([], f)
    with open(EXPERIMENTOS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_experimentos(data):
    with open(EXPERIMENTOS_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def adicionar_experimento(api):
    data = carregar_experimentos()
    data.append(api)
    salvar_experimentos(data)

def executar_experimentos():
    data = carregar_experimentos()

    for api in data:
        resultado = executar_coleta(api)

        registrar_mensagem(
            tipo="TESTE",
            modulo="EXPERIMENTO",
            descricao=f"Teste executado para {api['nome']}.",
            impacto="AvaliaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de nova fonte.",
            acao="Analisar desempenho.",
            prioridade="MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIA"
        )


