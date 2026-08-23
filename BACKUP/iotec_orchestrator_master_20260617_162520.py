import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ORCHESTRATOR MASTER v1.0
# CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©rebro central de roteamento do sistema
# ==========================================================

from datetime import datetime

# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã‚Âº MAPA DE DECISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
ROTEAMENTO = {
    "criacao_sistema": "producao",
    "bug": "core",
    "erro": "core",
    "cliente": "atendimento",
    "formulario": "recepcao",
    "interface": "recepcao",
    "dados": "dados",
    "relatorio": "dados",
    "backup": "almoxarifado",
    "auditoria": "presidencia",
    "governanca": "presidencia",
    "documento": "documentos",
}


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ANALISADOR DE INTENÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
def analisar_intencao(texto):
    texto = texto.lower()

    for chave in ROTEAMENTO:
        if chave in texto:
            return ROTEAMENTO[chave]

    return "ruido"


# -----------------------------
# ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ DEFINIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE PRIORIDADE
# -----------------------------
def prioridade(texto):
    texto = texto.lower()

    if "erro" in texto or "bug" in texto:
        return "CRITICA"

    if "cliente" in texto or "pedido" in texto:
        return "ALTA"

    if "relatorio" in texto:
        return "MEDIA"

    return "BAIXA"


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ SIMULAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE ROTA
# -----------------------------
def rota(setor):
    estrutura = {
        "recepcao": "Torre - Entrada (NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel 1)",
        "atendimento": "Torre - Suporte (NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel 2)",
        "producao": "Torre - ExecuÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o (NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel 3)",
        "dados": "Torre - InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia (NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel 4)",
        "core": "Torre - NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo (NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel 5)",
        "presidencia": "Torre - GovernanÃƒÆ'Ã†â€™a (NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel 6)",
        "almoxarifado": "Torre - Arquivo (Subsolo)",
        "documentos": "Torre - DocumentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
        "ruido": "Fila de anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise manual"
    }

    return estrutura.get(setor, "Desconhecido")


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ORQUESTRADOR PRINCIPAL
# -----------------------------
def orquestrar(requisicao):
    setor = analisar_intencao(requisicao)
    nivel = prioridade(requisicao)
    destino = rota(setor)

    return {
        "timestamp": str(datetime.now()),
        "entrada": requisicao,
        "setor_destino": setor,
        "prioridade": nivel,
        "rota": destino
    }


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  VISUALIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -----------------------------
def imprimir(resultado):
    print("\n====================================")
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ORCHESTRATOR MASTER")
    print("====================================")

    print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© REQUISIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: {resultado['entrada']}")
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚ÂÃƒâ€šÃ‚Â¢ SETOR DESTINO: {resultado['setor_destino']}")
    print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡Ãƒâ€šÃ‚Â¡ PRIORIDADE: {resultado['prioridade']}")
    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â­ ROTA: {resultado['rota']}")

    print("\n====================================")
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â DECISÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O TOMADA PELO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO")
    print("====================================\n")


# -----------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¡ EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O (TESTE)
# -----------------------------
if __name__ == "__main__":
    pass

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ORCHESTRATOR MASTER INICIADO")

    while True:
        req = input("\nDigite requisiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o (ou 'sair'): ")

        if req.lower() == "sair":
            break

        resultado = orquestrar(req)
        imprimir(resultado)


