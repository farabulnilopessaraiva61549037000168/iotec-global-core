import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# =========================================================
# RESUMO EXECUTIVO
# =========================================================

print("\n=================================================")
print("RESUMO EXECUTIVO DO NÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡CLEO")
print("=================================================\n")

print(f"Projeto: {report['project_name']}")

print(f"\nTotal de pastas detectadas: {len(report['directories'])}")
print(f"Total de arquivos detectados: {len(report['files'])}")

print("\n-------------------------------------------------")
print("TOP 10 TECNOLOGIAS")
print("-------------------------------------------------\n")

sorted_languages = sorted(
    report["languages"].items(),
    key=lambda x: x[1],
    reverse=True
)

for lang, count in sorted_languages[:10]:
    print(f"{lang}: {count} arquivos")

print("\n-------------------------------------------------")
print("TOP MÃƒÆ'Ã†â€™ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œDULOS CRÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂTICOS")
print("-------------------------------------------------\n")

for module in report["critical_modules"][:15]:
    print(f" - {module}")

print("\n-------------------------------------------------")
print("POSSÃƒÆ'Ã†â€™Ãƒâ€šÃ‚ÂVEIS PRODUTOS")
print("-------------------------------------------------\n")

for product in report["possible_products"][:15]:
    print(f" - {product}")

print("\n-------------------------------------------------")
print("CATEGORIAS MAIS FORTES")
print("-------------------------------------------------\n")

sorted_categories = sorted(
    report["categories"].items(),
    key=lambda x: len(x[1]),
    reverse=True
)

for category, files in sorted_categories[:10]:
    print(f"{category}: {len(files)} arquivos")

print("\n=================================================")
print("FIM DO RESUMO EXECUTIVO")
print("=================================================\n")



