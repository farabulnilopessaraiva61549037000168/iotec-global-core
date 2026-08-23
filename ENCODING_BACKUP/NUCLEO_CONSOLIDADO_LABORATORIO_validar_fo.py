import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def validar_formulario(dados):
    campos_obrigatorios = ["nome", "orgao", "descricao_demanda"]
    faltando = [campo for campo in campos_obrigatorios if campo not in dados or not dados[campo]]

    if faltando:
        return False, f"Faltam os seguintes dados: {', '.join(faltando)}"
    else:
        return True, "FormulÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio completo."


