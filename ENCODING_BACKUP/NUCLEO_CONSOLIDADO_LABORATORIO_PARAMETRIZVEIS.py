import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import datetime

# CONFIGURAÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES PARAMETRIZÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS
VALOR_MAX_REJ = 0.20         # atÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© 20% do caixa pode ser sacado como emergÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia
FREQUENCIA_RPF = [10, 25]    # dias fixos de repasse programado
LIMITES_AMS = {
    "valor_max_diario": 5000,
    "dias_consecutivos": 3
}

# ESTADO FINANCEIRO SIMULADO
caixa_disponivel = 25000.00
lucro_liquido_mes = 12000.00
historico_saques = []  # lista de dicionÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rios {data: valor}

# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO 1 ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Retirada Emergencial Justificada (REJ)
def saque_emergencial(valor, motivo):
    max_saque = caixa_disponivel * VALOR_MAX_REJ
    if valor <= max_saque:
        data = datetime.date.today()
        historico_saques.append({'data': data, 'valor': valor})
        print(f"[REJ] Saque emergencial autorizado: R${valor:.2f}")
        print(f"Motivo registrado: {motivo}")
        print(f"ReposiÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o automÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica atÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© {data + datetime.timedelta(days=7)}")
    else:
        print(f"[REJ] Valor excede limite emergencial permitido: R${max_saque:.2f}")

# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO 2 ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Repasses Programados Fixos (RPF)
def repasse_programado():
    dia = datetime.date.today().day
    if dia in FREQUENCIA_RPF:
        repasse = lucro_liquido_mes * 0.4
        reinvestimento = lucro_liquido_mes * 0.5
        tributos = lucro_liquido_mes * 0.1
        print(f"[RPF] Repassando R${repasse:.2f} ao titular (CPF)")
        print(f"Reinvestimento: R${reinvestimento:.2f}, Tributos: R${tributos:.2f}")
    else:
        print(f"[RPF] Hoje ({dia}) nÃƒÆ'Ã†â€™o ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© dia de repasse programado.")

# MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULO 3 ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Alerta de MovimentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o SensÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­vel (AMS)
def verificar_movimentacoes():
    hoje = datetime.date.today()
    ultimos_saques = [s for s in historico_saques if (hoje - s['data']).days <= 2]
    total_hoje = sum(s['valor'] for s in ultimos_saques if s['data'] == hoje)

    if total_hoje > LIMITES_AMS["valor_max_diario"]:
        print(f"[AMS] ALERTA: Saques de hoje somam R${total_hoje:.2f} ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ Valor elevado.")

    if len(ultimos_saques) >= LIMITES_AMS["dias_consecutivos"]:
        print(f"[AMS] ALERTA: Saques consecutivos por {len(ultimos_saques)} dias.")

# EXEMPLOS DE USO
# saque_emergencial(3000, "Compra de filmadora para projeto Jaguar")
# repasse_programado()
# verificar_movimentacoes()


