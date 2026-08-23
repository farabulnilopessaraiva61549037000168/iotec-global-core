# ==============================================================================
# 109_COMMERCIAL_EVIDENCE_ENGINE.py
# IOTEC COMMERCIAL EVIDENCE ENGINE
# ==============================================================================

import json
from datetime import datetime

print("="*90)
print("IOTEC COMMERCIAL EVIDENCE ENGINE")
print("MOTOR DE EVIDÃƒÅ NCIAS COMERCIAIS")
print("="*90)
print()

ARQUIVO = "IOTEC_ENTITY_DATABASE.json"

try:

    with open(ARQUIVO, "r", encoding="utf8") as f:

        banco = json.load(f)

except:

    print("Banco de entidades nÃƒÂ£o encontrado.")
    raise SystemExit()

EMPRESAS = []

for entidade in banco["entidades"]:

    nome = entidade["nome"]
    texto = nome.lower()

    score = 0
    evidencias = []

    # ----------------------------------------------------
    # EVIDÃƒÅ NCIAS POSITIVAS
    # ----------------------------------------------------

    if "engenharia" in texto:
        score += 20
        evidencias.append("Segmento Engenharia")

    if "ltda" in texto:
        score += 40
        evidencias.append("LTDA")

    if "consultoria" in texto:
        score += 30
        evidencias.append("Consultoria")

    if "construtora" in texto:
        score += 30
        evidencias.append("Construtora")

    if "tecnologia" in texto:
        score += 25
        evidencias.append("Tecnologia")

    # ----------------------------------------------------
    # EVIDÃƒÅ NCIAS NEGATIVAS
    # ----------------------------------------------------

    NEGATIVAS = [

        "departamento",
        "campus",
        "curso",
        "laboratÃƒÂ³rio",
        "laboratorio",
        "universidade",
        "grupo",
        "centro acadÃƒÂªmico",
        "ÃƒÂ¡rea de convivencia",
        "area de convivencia",
        "bloco didÃƒÂ¡tico",
        "bloco didatico"

    ]

    for palavra in NEGATIVAS:

        if palavra in texto:

            score -= 80

            evidencias.append("NÃƒÂ£o Comercial")

    if score < 0:
        score = 0

    nivel = "BAIXO"

    if score >= 80:
        nivel = "ALTÃƒÂSSIMO"

    elif score >= 60:
        nivel = "ALTO"

    elif score >= 40:
        nivel = "MÃƒâ€°DIO"

    elif score >= 20:
        nivel = "BAIXO"

    entidade["score"] = score
    entidade["nivel"] = nivel
    entidade["evidencias"] = evidencias

    if score > 0:

        EMPRESAS.append(entidade)

EMPRESAS.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("="*90)
print("RANKING COMERCIAL")
print("="*90)
print()

for empresa in EMPRESAS:

    estrelas = "Ã¢Ëœâ€¦" * min(5, max(1, empresa["score"] // 20))

    print(f"{estrelas:5} {empresa['score']:3}  {empresa['nivel']:10}  {empresa['nome']}")

print()

saida = {

    "generated_at": datetime.now().isoformat(),

    "total": len(EMPRESAS),

    "empresas": EMPRESAS

}

with open(
    "IOTEC_COMMERCIAL_EVIDENCE_DATABASE.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        saida,
        f,
        indent=4,
        ensure_ascii=False
    )

print("="*90)
print("ARQUIVO GERADO")
print("="*90)
print()

print("IOTEC_COMMERCIAL_EVIDENCE_DATABASE.json")

print()

print("="*90)
print("FILOSOFIA")
print("="*90)
print()

print("Nem toda entidade")
print("ÃƒÂ© um cliente.")

print()

print("O Kernel procura")
print("evidÃƒÂªncias")

print("antes de")
print("iniciar uma")
print("estratÃƒÂ©gia")
print("comercial.")

print()

print("="*90)
print("STATUS")
print("="*90)
print()

print("Entidades analisadas....", len(banco["entidades"]))
print("Potenciais comerciais...", len(EMPRESAS))
print("Data....................", datetime.now().strftime("%d/%m/%Y %H:%M"))

print()

print("COMMERCIAL EVIDENCE ENGINE OPERACIONAL.")


