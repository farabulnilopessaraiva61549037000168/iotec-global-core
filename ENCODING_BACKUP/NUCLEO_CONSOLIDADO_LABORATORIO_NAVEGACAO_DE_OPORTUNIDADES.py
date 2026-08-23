import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - MOTOR DE NAVEGAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE OPORTUNIDADES
# ============================================================

# CatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo simples de APIs (simulado)
CATALOGO_APIS = [
    {"nome": "API_FINANCEIRA", "setor": "financeiro", "custo": 0.05, "qualidade": 0.9},
    {"nome": "API_ECONOMICA", "setor": "economico", "custo": 0.03, "qualidade": 0.8},
    {"nome": "API_DADOS_GERAIS", "setor": "geral", "custo": 0.02, "qualidade": 0.7}
]

def escolher_api(setor):
    candidatas = [api for api in CATALOGO_APIS if api["setor"] == setor]

    if not candidatas:
        return None

    # escolha pela melhor relaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o qualidade/custo
    melhor = max(candidatas, key=lambda x: x["qualidade"] / x["custo"])
    return melhor

def executar_coleta(api):
    # simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de coleta
    sucesso = random.random()

    if sucesso < 0.8:
        return {"status": "SUCESSO", "valor": random.uniform(1, 5)}
    else:
        return {"status": "FALHA"}

def navegar_oportunidade(setor):
    pass

    api = escolher_api(setor)

    if not api:
        registrar_mensagem(
            tipo="NECESSIDADE",
            modulo="CATALOGO",
            descricao=f"Nenhuma API disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel para o setor {setor}.",
            impacto="ImpossÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel explorar oportunidade.",
            acao="Adicionar nova API ao catÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo.",
            prioridade="ALTA"
        )
        return

    resultado = executar_coleta(api)

    if resultado["status"] == "SUCESSO":
        registrar_mensagem(
            tipo="OPORTUNIDADE",
            modulo="EXECUCAO",
            descricao=f"Oportunidade explorada via {api['nome']}.",
            impacto="GeraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de valor concluÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­da.",
            acao="Continuar exploraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o neste setor.",
            prioridade="MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIA"
        )

    else:
        registrar_mensagem(
            tipo="ERRO",
            modulo="API",
            descricao=f"Falha ao usar {api['nome']}.",
            impacto="Perda de oportunidade.",
            acao="Testar outra API ou revisar conexÃƒÆ'Ã†â€™o.",
            prioridade="ALTA"
        )


