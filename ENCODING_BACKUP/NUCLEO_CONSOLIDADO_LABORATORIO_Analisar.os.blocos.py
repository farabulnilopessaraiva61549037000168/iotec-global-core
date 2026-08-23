import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import re

def contar_blocos_de_codigo(conversa_texto):
    # Define um padrÃƒÆ'Ã†â€™o para identificar blocos de cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo, por exemplo, entre ``` ou indentaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
    blocos = re.findall(r'```(?:python)?(.*?)```', conversa_texto, re.DOTALL)
    quantidade_blocos = len(blocos)

    # Analisar os blocos - pode ser expandido para detectar tipo, tamanho, linguagem, etc.
    resumo = []
    for i, bloco in enumerate(blocos, 1):
        linhas = bloco.strip().split('\n')
        resumo.append({
            'bloco_num': i,
            'linhas': len(linhas),
            'preview': linhas[0] if linhas else ''
        })

    return quantidade_blocos, resumo

# Exemplo de uso:
conversa = """Aqui vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª coloca o texto completo da conversa que vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª quer analisar"""

qtd, resumo_blocos = contar_blocos_de_codigo(conversa)

print(f"Total de blocos de cÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³digo encontrados: {qtd}")
for bloco in resumo_blocos:
    print(f"Bloco {bloco['bloco_num']}: {bloco['linhas']} linhas, primeira linha: {bloco['preview']}")



