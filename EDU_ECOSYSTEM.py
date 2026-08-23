import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# AURORA ECOSYSTEM CORE
# ============================================================
# IOTEC EDU ECOSYSTEM
#
# Centro de InteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia ClimÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica, Territorial,
# HumanitÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ria e ResiliÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia Operacional
#
# Autor da VisÃƒÆ'Ã†â€™o: Bruno Lopes
# ============================================================

from datetime import datetime

# ============================================================
# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES GERAIS
# ============================================================

AURORA = {
    "nome": "AURORA",
    "versao": "1.0",
    "status": "ONLINE",
    "inicializacao": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
}

# ============================================================
# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS
# ============================================================

MODULOS = {
    "WATCH": "Monitoramento climÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico e territorial",
    "PREDICT": "Modelagem matemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica e previsÃƒÆ'Ã†â€™o",
    "SHIELD": "Protocolos preventivos",
    "RESPONSE": "Resposta operacional",
    "SENTINEL": "ObservÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ncia e auditoria",
    "WAR_ROOM": "Sala de guerra estratÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©gica",
    "COMMERCIAL": "Relacionamento institucional"
}

# ============================================================
# EVENTOS MONITORADOS
# ============================================================

EVENTOS = [
    "Seca",
    "Estiagem",
    "Onda de Calor",
    "Frio Extremo",
    "Enchente",
    "InundaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
    "Deslizamento",
    "Queimada",
    "IncÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªndio Florestal",
    "Colapso HÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­drico",
    "Falha EnergÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tica"
]

# ============================================================
# GRUPOS PRIORITÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIOS
# ============================================================

VULNERABILIDADES = [
    "CrianÃƒÆ'Ã†â€™as",
    "Idosos",
    "Gestantes",
    "Pessoas com DeficiÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia",
    "Pessoas com Mobilidade Reduzida",
    "Pacientes Dependentes de Tratamento",
    "FamÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­lias em Vulnerabilidade Social"
]

# ============================================================
# FONTES ESTRATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â°GICAS
# ============================================================

FONTES = [
    "INMET",
    "ANA",
    "CEMADEN",
    "Defesa Civil",
    "Institutos de Pesquisa",
    "Universidades",
    "SatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©lites",
    "Sensores Territoriais"
]

# ============================================================
# PROTOCOLOS
# ============================================================

PROTOCOLOS = {
    "SECA": [
        "Monitorar reservatÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rios",
        "Planejar abastecimento",
        "Mapear ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡reas vulnerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡veis",
        "Acionar defesa civil"
    ],

    "ENCHENTE": [
        "Avaliar ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡reas de risco",
        "Abrir abrigos",
        "Planejar evacuaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o",
        "Acionar equipes de resposta"
    ],

    "ONDA_DE_CALOR": [
        "Criar centros de resfriamento",
        "Distribuir ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gua",
        "Monitorar grupos vulnerÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡veis"
    ]
}

# ============================================================
# ABORDAGEM COMERCIAL
# ============================================================

def apresentar_iotec():
    pass

    print("\n================================================")
    print("APRESENTAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O INSTITUCIONAL")
    print("================================================\n")

    print("Bom dia.")
    print("Somos o ecossistema IOTEC.")
    print("Trabalhamos com inteligÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia aplicada ÃƒÆ'Ã†â€™ ")
    print("tomada de decisÃƒÆ'Ã†â€™o, monitoramento e gestÃƒÆ'Ã†â€™o de riscos.")
    print()
    print("Objetivo:")
    print("Transformar dados em decisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes.")
    print()
    print("NÃƒÆ'Ã†â€™o vendemos apenas tecnologia.")
    print("Entregamos capacidade de antecipaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")
    print()

# ============================================================
# WAR ROOM
# ============================================================

def war_room():
    pass

    print("\n================================================")
    print("AURORA WAR ROOM")
    print("================================================")

    print("\nRISCOS MONITORADOS:")

    for evento in EVENTOS:
        print(f"[MONITORANDO] {evento}")

# ============================================================
# SENTINEL
# ============================================================

def sentinel():
    pass

    print("\n================================================")
    print("AURORA SENTINEL")
    print("================================================")

    for fonte in FONTES:
        print(f"[OK] Fonte registrada: {fonte}")

# ============================================================
# BOOT
# ============================================================

def iniciar_aurora():
    pass

    print("=" * 60)
    print("AURORA ONLINE")
    print("=" * 60)

    print(f"\nVERSÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O: {AURORA['versao']}")
    print(f"STATUS : {AURORA['status']}")
    print(f"INÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂCIO : {AURORA['inicializacao']}")

    print("\nMÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS CARREGADOS:\n")

    for nome, descricao in MODULOS.items():
        print(f"[OK] {nome} -> {descricao}")

    sentinel()
    war_room()

    print("\n================================================")
    print("CENTRO DE INTELIGÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â NCIA INICIALIZADO")
    print("================================================")

# ============================================================
# EXECUÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
# ============================================================

if __name__ == "__main__":
    iniciar_aurora()




