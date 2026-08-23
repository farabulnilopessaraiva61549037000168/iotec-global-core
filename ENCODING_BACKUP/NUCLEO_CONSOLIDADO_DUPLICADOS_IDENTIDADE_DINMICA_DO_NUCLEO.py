import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ============================================================
# IOTEC - IDENTIDADE DINÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡MICA DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO
# ============================================================

IDENTITY_PATH = os.path.join(BASE, "identidade.json")

def avaliar_capacidades():
    perf = carregar_perf()

    total_tentativas = sum(v["tentativas"] for v in perf.values()) if perf else 0
    total_sucessos = sum(v["sucessos"] for v in perf.values()) if perf else 0
    valor_total = sum(v["valor_total"] for v in perf.values()) if perf else 0.0
    custo_total = sum(v["custo_total"] for v in perf.values()) if perf else 0.0

    taxa_sucesso = (total_sucessos / total_tentativas) if total_tentativas else 0.0
    roi = (valor_total / custo_total) if custo_total else 0.0

    # Sinais simples (ajuste conforme evoluir)
    sinais = {
        "decisao": True,                       # vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ tem motor de decisÃƒÆ'Ã†â€™o
        "coleta_autonoma": True,               # navegaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o + escolha de API
        "aprendizado": total_tentativas > 5,   # jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ tem histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico suficiente?
        "monetizacao": valor_total > 0.0,      # jÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ gerou valor?
        "execucao_fim_a_fim": total_sucessos > 0
    }

    metricas = {
        "taxa_sucesso": round(taxa_sucesso, 3),
        "roi": round(roi, 3),
        "tentativas": total_tentativas,
        "sucessos": total_sucessos,
        "valor_total": round(valor_total, 2),
        "custo_total": round(custo_total, 2)
    }

    return sinais, metricas


def classificar(sinais):
    tipos = []

    if sinais["decisao"]:
        tipos.append("Decision Intelligence Platform")

    if sinais["coleta_autonoma"]:
        tipos.append("Autonomous Data Platform")

    if sinais["monetizacao"]:
        tipos.append("Data Monetization Engine")

    if sinais["aprendizado"]:
        tipos.append("Adaptive Intelligence System")

    # Se tem 3 ou mais, ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© composto
    if len(tipos) >= 3:
        tipos.append("Polymorphic Intelligence System")

    return tipos


def nivel(metricas):
    # HeurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica simples (ajuste depois)
    if metricas["roi"] >= 5 and metricas["taxa_sucesso"] >= 0.6:
        return "AVANÃƒÆ'Ã†â€™ADO"
    elif metricas["roi"] >= 1:
        return "INTERMEDIÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂRIO"
    else:
        return "BÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂSICO"


def gerar_descricao(tipos, nivel_str, metricas):
    base = "IoTec Core ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© um nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo inteligente que "

    partes = []

    if "Decision Intelligence Platform" in tipos:
        partes.append("toma decisÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes automaticamente")

    if "Autonomous Data Platform" in tipos:
        partes.append("navega e seleciona fontes de dados de forma autÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´noma")

    if "Data Monetization Engine" in tipos:
        partes.append("transforma dados em valor econÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´mico")

    if "Adaptive Intelligence System" in tipos:
        partes.append("aprende e se adapta com base no histÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rico")

    descricao = base + ", ".join(partes) + "."

    descricao += f" NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel atual: {nivel_str}."
    descricao += f" ROI: {metricas['roi']}, Taxa de sucesso: {metricas['taxa_sucesso']}."

    return descricao


def atualizar_identidade():
    sinais, metricas = avaliar_capacidades()
    tipos = classificar(sinais)
    nivel_str = nivel(metricas)
    descricao = gerar_descricao(tipos, nivel_str, metricas)

    identidade = {
        "nome": "IoTec Core",
        "tipos": tipos,
        "nivel": nivel_str,
        "metricas": metricas,
        "descricao": descricao,
        "data": str(datetime.now())
    }

    with open(IDENTITY_PATH, "w", encoding="utf-8") as f:
        json.dump(identidade, f, indent=4, ensure_ascii=False)

    registrar_mensagem(
        tipo="IDENTIDADE",
        modulo="CORE",
        descricao=f"NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo classificado como: {', '.join(tipos)}.",
        impacto="AtualizaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de posicionamento do sistema.",
        acao="Manter evoluÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o baseada em mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©tricas.",
        prioridade="BAIXA"
    )

    print("\n=== IDENTIDADE DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO ===")
    print(descricao)


