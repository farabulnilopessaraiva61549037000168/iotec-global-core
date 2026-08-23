import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def instinto_de_sobrevivencia(sensorial_data):
    if sensorial_data['risco_detectado']:
        ativar_modo_furtivo()
        camuflar_trafego()
        iniciar_fuga_codificada()
    else:
        manter_infiltracao_suave()


