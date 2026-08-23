import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import logging

# Configurando log para acompanhar o fluxo
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def fluxo_atendimento(dados_usuario):
    try:
        logging.info("Iniciando processamento do atendimento.")

        tipo_demanda = interpretar_entrada(dados_usuario['descricao_demanda'])
        valido, mensagem = validar_formulario(dados_usuario)

        if not valido:
            logging.warning(f"Erro na validaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: {mensagem}")
            return mensagem

        relatorio = gerar_relatorio(tipo_demanda, dados_usuario)
        nome_arquivo = salvar_relatorio(dados_usuario['nome'], relatorio)

        if nome_arquivo:
            logging.info(f"RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio gerado e salvo: {nome_arquivo}")
            return f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ RelatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio gerado e enviado para {dados_usuario['nome']}."
        else:
            logging.error("Erro ao salvar o relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio.")
            return "ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Ocorreu um erro ao salvar o relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio."

    except Exception as e:
        logging.exception(f"Erro inesperado no fluxo de atendimento: {e}")
        return "ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Ocorreu um erro inesperado. Tente novamente."



