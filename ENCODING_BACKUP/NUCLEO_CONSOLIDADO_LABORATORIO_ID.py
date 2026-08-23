import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
{
  "CARTAO_ID": "FINANCIAL_RULES_V1",
  "TIPO": "DISTRIBUICAO_LUCROS",
  "STATUS": "ATIVO",
  "PARAMETROS": {
    "IMPOSTO_PAGO": true,
    "LUCRO_LIQUIDO_CALCULADO": true
  },
  "REGRAS": [
    {
      "DESTINO": "CONTA_PESSOAL_DONO",
      "PERCENTUAL": 70,
      "PERIODO": "DIARIO"
    },
    {
      "DESTINO": "FUNDOS_RESERVA",
      "PERCENTUAL": 20,
      "PERIODO": "MENSAL"
    },
    {
      "DESTINO": "FUNDOS_EXPANSAO",
      "PERCENTUAL": 10,
      "PERIODO": "MENSAL"
    }
  ],
  "AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O_SE_FALHAR": "RECALCULAR_E_ENVIAR_ALERTA"
}



