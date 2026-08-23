import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import ast
import json
from pathlib import Path
from datetime import datetime

ROOT = Path(r"C:\IOTEC")

relatorio = {
    "data": str(datetime.now()),
    "arquivos": {},
    "isolados": [],
    "mais_importados": {},
    "erros": []
}

# -----------------------------
# EXTRAI IMPORTS
# -----------------------------

def extrair_imports(arquivo):
    pass

    try:
        pass

        with open(
            arquivo,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as f:

            codigo = f.read()

        arvore = ast.parse(codigo)

        imports = []

        for node in ast.walk(arvore):
            pass

            if isinstance(node, ast.Import):
                pass

                for n in node.names:
                    pass

                    imports.append(n.name)

            elif isinstance(node, ast.ImportFrom):
                pass

                if node.module:
                    pass

                    imports.append(node.module)

        return imports

    except Exception as e:
        pass

        relatorio["erros"].append({
            "arquivo": arquivo.name,
            "erro": str(e)
        })

        return []

# -----------------------------
# MAPA DE ARQUIVOS
# -----------------------------

arquivos_py = list(ROOT.rglob("*.py"))

nomes = {}

for arq in arquivos_py:
    pass

    nomes[arq.stem] = arq.name

# -----------------------------
# ANALISA
# -----------------------------

contador_importados = {}

for arq in arquivos_py:
    pass

    imports = extrair_imports(arq)

    internos = []

    for item in imports:
        pass

        base = item.split(".")[0]

        if base in nomes:
            pass

            internos.append(base)

            contador_importados[base] = (
                contador_importados.get(base, 0) + 1
            )

    relatorio["arquivos"][arq.stem] = {
        "imports": internos,
        "quantidade": len(internos)
    }

# -----------------------------
# ISOLADOS
# -----------------------------

for motor, dados in relatorio["arquivos"].items():
    pass

    if dados["quantidade"] == 0:
        pass

        relatorio["isolados"].append(motor)

# -----------------------------
# MAIS IMPORTADOS
# -----------------------------

ordenado = sorted(
    contador_importados.items(),
    key=lambda x: x[1],
    reverse=True
)

for nome, qtd in ordenado[:100]:
    pass

    relatorio["mais_importados"][nome] = qtd

# -----------------------------
# RESUMO
# -----------------------------

relatorio["resumo"] = {

    "total_python":
        len(arquivos_py),

    "isolados":
        len(relatorio["isolados"]),

    "mais_importados":
        len(relatorio["mais_importados"]),

    "erros":
        len(relatorio["erros"])
}

# -----------------------------
# SALVAR
# -----------------------------

saida = ROOT / "IOTEC_DEPENDENCY_REPORT.json"

with open(
    saida,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        relatorio,
        f,
        indent=4,
        ensure_ascii=False
    )

print("\nDEPENDENCY AUDIT FINALIZADO\n")

print(json.dumps(
    relatorio["resumo"],
    indent=4,
    ensure_ascii=False
))

print(
    f"\nRELATÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œRIO: {saida}"
)


