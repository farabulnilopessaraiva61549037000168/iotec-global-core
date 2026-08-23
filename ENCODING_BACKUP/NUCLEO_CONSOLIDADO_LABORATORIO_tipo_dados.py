import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def gerar_relatorio(tipo, dados):
    data_hoje = datetime.now().strftime('%d/%m/%Y')

    if tipo == "licitacao":
        relatorio = f"""
        COMPLEXO DIGITAL - RELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO TÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°CNICO
        Data: {data_hoje}

        AnÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de Viabilidade de LicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
        ------------------------------------------
        Cliente: {dados['nome']}
        ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œrgÃƒÆ'Ã†â€™o: {dados['orgao']}

        DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o da Demanda:
        {dados['descricao_demanda']}

        Parecer TÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnico:
        ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ A demanda apresentada corresponde a uma necessidade compatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel com processos licitatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios.
        ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â° necessÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio verificar o cabimento orÃƒÆ'Ã†â€™amentÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio, compatibilidade legal e diretrizes da legislaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o vigente (Lei 14.133/2021).

        RecomendaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes:
        - Avaliar rubricas disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­veis.
        - Analisar os prazos e conformidades do edital.
        - Validar exigÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncias jurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dicas e tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnicas.

        Gerado automaticamente por IA - Complexo Digital.
        """
    else:
        relatorio = f"""
        RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio padrÃƒÆ'Ã†â€™o para tipo: {tipo}
        Cliente: {dados['nome']}
        ÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œrgÃƒÆ'Ã†â€™o: {dados['orgao']}
        DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {dados['descricao_demanda']}
        """

    return relatorio


