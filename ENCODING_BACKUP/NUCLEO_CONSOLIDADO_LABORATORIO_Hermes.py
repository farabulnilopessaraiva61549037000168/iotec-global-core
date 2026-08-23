import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
class Hermes:
    def __init__(self):
        self.mestre_autorizado = False
        self.log_operacoes = []

    def mensagem_da_aldeia(self, nome_aldeia, tipo_tarefa, dados_detectados, retorno_estimado):
        resumo = {
            "aldeia": nome_aldeia,
            "tarefa": tipo_tarefa,
            "dados": dados_detectados,
            "receita_esperada": retorno_estimado
        }
        self.log_operacoes.append({"status": "pendente", "info": resumo})
        return f"""
ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¡ HERMES:
A Aldeia {nome_aldeia} enviou uma proposta.

ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  Tipo de tarefa: {tipo_tarefa}
ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Dados detectados: {dados_detectados}
ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â° Receita estimada: R$ {retorno_estimado:.2f}

ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Deseja autorizar execuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o? (SIM/NÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O)
"""

    def resposta_do_mestre(self, resposta):
        if resposta.strip().upper() == "SIM":
            self.mestre_autorizado = True
            self.log_operacoes[-1]["status"] = "autorizado"
            return "ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â¦ AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o autorizada. HERMES iniciou a operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o."
        else:
            self.mestre_autorizado = False
            self.log_operacoes[-1]["status"] = "negado"
            return "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â« AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o negada pelo NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Central."


