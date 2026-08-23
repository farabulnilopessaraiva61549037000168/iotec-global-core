import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
{
  "CARTAO_ID": "LEGAL_COMPLIANCE_MASTER",
  "TIPO": "COMPLIANCE_GLOBAL",
  "STATUS": "ATIVO",
  "PARAMETROS": {
    "KYC": "OBRIGATORIO",
    "AML": "OBRIGATORIO",
    "LGPD": "ATIVO",
    "GDPR": "ATIVO",
    "CONTRATOS_BLOCO": "HABILITADO",
    "FISCALIZACAO_AUTOMATICA": "HABILITADO"
  },
  "FUNCOES": [
    "VALIDAR_CLIENTE",
    "EXECUTAR_CONTRATO_SMART",
    "MONITORAR_TRANSACOES",
    "RELATORIO_AUTOMATICO_FISCAL",
    "REGISTRAR_BLOCO_IMUTAVEL"
  ],
  "AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O_SE_FALHAR": "BLOQUEAR_OPERACAO_E_ALERTAR_NUCLEO"
}




