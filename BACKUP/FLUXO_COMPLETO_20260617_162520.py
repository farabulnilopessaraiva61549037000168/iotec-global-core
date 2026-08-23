import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
dados = {

    "impacto": 120000,

    "percentual": 25,

    "risco": "ALTO",

    "cenarios": 3

}



score = analisar_cenario(dados)

plano = recomendar_plano(score)

mensagem = gerar_mensagem(plano)



print(mensagem)





