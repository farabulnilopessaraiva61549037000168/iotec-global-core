import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO DE COMUNICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INTERNA DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ============================================================

from datetime import datetime
import os

BASE = "C:\\IOTEC"
LOG_PATH = os.path.join(BASE, "logs")

if not os.path.exists(LOG_PATH):
    os.makedirs(LOG_PATH)

def gerar_mensagem(tipo, modulo, descricao, impacto, acao, prioridade):
    pass

    mensagem = f"""
[{datetime.now()}]
TIPO: {tipo}
MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO: {modulo}

DESCRIÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O:
{descricao}

IMPACTO:
{impacto}

AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O SUGERIDA:
{acao}

PRIORIDADE: {prioridade}
--------------------------------------------------
"""

    salvar_mensagem(mensagem)
    print(mensagem)

def salvar_mensagem(mensagem):
    arquivo = os.path.join(LOG_PATH, "registro_nucleo.txt")
    with open(arquivo, "a", encoding="utf-8") as f:
        f.write(mensagem)

# ============================================================
# EXEMPLOS DE USO
# ============================================================

def exemplo_problema():
    gerar_mensagem(
        tipo="ERRO",
        modulo="COLETA",
        descricao="Falha ao acessar API de mercado.",
        impacto="Dados desatualizados podem comprometer decisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes.",
        acao="Verificar limite da API ou trocar fonte.",
        prioridade="ALTA"
    )

def exemplo_necessidade():
    gerar_mensagem(
        tipo="NECESSIDADE",
        modulo="EXPANSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O",
        descricao="Necessidade de nova API para setor financeiro.",
        impacto="Baixa cobertura de dados.",
        acao="Buscar e integrar nova fonte.",
        prioridade="MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°DIA"
    )

def exemplo_otimizacao():
    gerar_mensagem(
        tipo="OTIMIZAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O",
        modulo="PRECIFICAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O",
        descricao="CÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo duplicado detectado.",
        impacto="Risco de inconsistÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia.",
        acao="Refatorar lÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³gica.",
        prioridade="BAIXA"
    )

if __name__ == "__main__":
    exemplo_problema()
    exemplo_necessidade()
    exemplo_otimizacao()


