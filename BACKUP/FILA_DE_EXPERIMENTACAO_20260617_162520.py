import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# FILA DE EXPERIMENTAÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Â ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢O

# ============================================================



EXPERIMENTOS_PATH = os.path.join(BASE, "experimentos.json")



def carregar_experimentos():
    pass

    if not os.path.exists(EXPERIMENTOS_PATH):
        pass

        with open(EXPERIMENTOS_PATH, "w", encoding="utf-8") as f:
            pass

            json.dump([], f)

    with open(EXPERIMENTOS_PATH, "r", encoding="utf-8") as f:
        pass

        return json.load(f)



def salvar_experimentos(data):
    pass

    with open(EXPERIMENTOS_PATH, "w", encoding="utf-8") as f:
        pass

        json.dump(data, f, indent=4, ensure_ascii=False)



def adicionar_experimento(api):
    pass

    data = carregar_experimentos()

    data.append(api)

    salvar_experimentos(data)



def executar_experimentos():
    pass

    data = carregar_experimentos()



    for api in data:
        pass

        resultado = executar_coleta(api)



        registrar_mensagem(

            tipo="TESTE",

            modulo="EXPERIMENTO",

            descricao=f"Teste executado para {api['nome']}.",

            impacto="AvaliaÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o de nova fonte.",

            acao="Analisar desempenho.",

            prioridade="MÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚Â°DIA"

        )




