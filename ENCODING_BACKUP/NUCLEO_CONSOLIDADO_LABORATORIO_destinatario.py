import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
enviar_email_com_anexo(
    destinatario="bruno@seudominio.com",
    assunto="Contrato GV16 Pronto para Assinatura",
    corpo="Segue em anexo o contrato GV16, versÃƒÆ'Ã†â€™o via dupla.",
    anexo="Contrato_GV16_Via_Dupla_Farabulini.docx"
)



