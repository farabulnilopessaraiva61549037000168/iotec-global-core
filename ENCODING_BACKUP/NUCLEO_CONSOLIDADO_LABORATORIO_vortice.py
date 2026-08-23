import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
def caminho_do_vortice():
    ambiente = ler_ambiente_digital()
    entidade = invocar_entidade_responsiva(ambiente)
    dados = entidade.executar_missao()
    if dados:
        abrir_portal_envio(dados)
        selar_pergaminho()


