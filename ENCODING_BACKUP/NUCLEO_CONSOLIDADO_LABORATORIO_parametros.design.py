import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
INICIAR SISTEMA

SOLICITAR parametros_design
SOLICITAR parametros_arquitetura
SOLICITAR parametros_textuais

GERAR wireframe_Figma
GERAR prototipo_UI_UX

ENVIAR preview_para_usuario

AGUARDAR aprovacao_usuario

SE aprovado == TRUE
    CONVERTER design_em_codigo
    CONFIGURAR hospedagem + dominio
    ATIVAR sistema_producao
SENÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢O
    AJUSTAR conforme feedback
    VOLTAR para ENVIAR preview

FIM



