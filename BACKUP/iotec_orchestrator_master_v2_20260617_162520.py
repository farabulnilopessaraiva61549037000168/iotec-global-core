import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ORCHESTRATOR MASTER v2 - PIPELINE INTELIGENTE
# ============================================================
# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o: Receber requisiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes e executar pipeline de decisÃƒÆ'Ã†â€™o
# Autor: IOTEC CORE SYSTEM
# VersÃƒÆ'Ã†â€™o: 2.0 - GovernanÃƒÆ'Ã†â€™a Inteligente
# ============================================================

import time
import uuid
from datetime import datetime

# -------------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  TABELA DE CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -------------------------------

SETORES = {
    "core": ["bug", "erro", "falha", "crash", "login", "api", "sistema"],
    "atendimento": ["cliente", "suporte", "ajuda", "chamado", "pedido", "automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o"],
    "dados": ["relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio", "anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise", "csv", "dados", "estatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica", "financeiro"],
    "producao": ["gerar", "build", "pipeline", "deploy", "criar sistema"],
    "presidencia": ["governanÃƒÆ'Ã†â€™a", "estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gia", "decisÃƒÆ'Ã†â€™o", "arquitetura"],
    "ruido": []
}

PRIORIDADE_MAP = {
    "critica": ["erro", "bug", "falha", "crash", "login"],
    "alta": ["automaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o", "cliente", "sistema", "criar", "gerar"],
    "media": ["relatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rio", "anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise", "pedido"],
}

# -------------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  FUNÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# -------------------------------

def classificar_setor(texto):
    texto = texto.lower()

    for setor, palavras in SETORES.items():
        for p in palavras:
            if p in texto:
                return setor
    return "ruido"


def definir_prioridade(texto):
    texto = texto.lower()

    for nivel, palavras in PRIORIDADE_MAP.items():
        for p in palavras:
            if p in texto:
                return nivel.upper()

    return "BAIXA"


# -------------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  PIPELINE DE PROCESSAMENTO
# -------------------------------

def pipeline_requisicao(requisicao):
    pass

    ticket_id = str(uuid.uuid4())[:8]
    timestamp = datetime.now()

    print("\n" + "="*60)
    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  IOTEC ORCHESTRATOR MASTER v2 - PIPELINE")
    print("="*60)

    print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â© REQUISIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: {requisicao}")

    # ETAPA 1 - CLASSIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    setor = classificar_setor(requisicao)
    prioridade = definir_prioridade(requisicao)

    # ETAPA 2 - ROTEAMENTO
    rota = f"Torre > {setor.upper()} > NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico"

    # ETAPA 3 - CRIAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O DE TICKET
    ticket = {
        "id": ticket_id,
        "texto": requisicao,
        "setor": setor,
        "prioridade": prioridade,
        "rota": rota,
        "timestamp": str(timestamp)
    }

    # ETAPA 4 - EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O SIMULADA
    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ TICKET GERADO:")
    for k, v in ticket.items():
        print(f" - {k}: {v}")

    # ETAPA 5 - LOG / AUDITORIA
    log_line = f"{timestamp} | {ticket_id} | {setor} | {prioridade} | {requisicao}\n"

    with open("iotec_orchestrator_log.txt", "a", encoding="utf-8") as f:
        f.write(log_line)

    print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã¢â‚¬Å" LOG REGISTRADO")
    print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â PIPELINE FINALIZADO COM SUCESSO")

    return ticket


# -------------------------------
# ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  LOOP PRINCIPAL
# -------------------------------

if __name__ == "__main__":
    pass

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  ORCHESTRATOR MASTER v2 - PIPELINE INTELIGENTE")

    while True:
        req = input("\nDigite requisiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o (ou 'sair'): ")

        if req.lower() == "sair":
            break

        pipeline_requisicao(req)


