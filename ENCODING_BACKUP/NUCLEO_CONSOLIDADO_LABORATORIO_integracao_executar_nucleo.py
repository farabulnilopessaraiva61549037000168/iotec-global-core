import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def executar_nucleo():
    pass

    setores = ["financeiro", "economico", "geral"]
    setor_escolhido = priorizar_setor(setores)

    api = escolher_api(setor_escolhido)

    if not api:
        registrar_mensagem(
            tipo="NECESSIDADE",
            modulo="CATALOGO",
            descricao=f"Sem API para setor {setor_escolhido}.",
            impacto="Bloqueio de exploraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.",
            acao="Adicionar fonte ao catÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡logo.",
            prioridade="ALTA"
        )
        return

    resultado = executar_coleta(api)

    if resultado["status"] == "SUCESSO":
        valor = resultado["valor"]
        custo = api["custo"]

        atualizar_perf(setor_escolhido, api["nome"], valor, custo, True)

        registrar_mensagem(
            tipo="OPORTUNIDADE",
            modulo="EXECUCAO",
            descricao=f"ExploraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o bem-sucedida em {setor_escolhido} via {api['nome']}.",
            impacto="GeraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de valor confirmada.",
            acao="ReforÃƒÆ'Ã†â€™ar este caminho.",
            prioridade="MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIA"
        )
    else:
        atualizar_perf(setor_escolhido, api["nome"], 0.0, api["custo"], False)

        registrar_mensagem(
            tipo="ERRO",
            modulo="API",
            descricao=f"Falha ao executar {api['nome']} no setor {setor_escolhido}.",
            impacto="Perda de oportunidade.",
            acao="Testar alternativa ou revisar conexÃƒÆ'Ã†â€™o.",
            prioridade="ALTA"
        )


