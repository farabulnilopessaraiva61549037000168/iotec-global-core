import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================

# CONTROLE DE CUSTO

# ============================================================



CUSTO_LIMITE = 2.0  # limite por execuÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o



def verificar_limite_custo(api):
    pass

    if api["custo"] > CUSTO_LIMITE:
        pass

        registrar_mensagem(

            tipo="CONTROLE",

            modulo="CUSTO",

            descricao=f"Custo da API {api['nome']} excede limite.",

            impacto="Risco financeiro.",

            acao="Ignorar ou buscar alternativa.",

            prioridade="ALTA"

        )

        return False

    return True




