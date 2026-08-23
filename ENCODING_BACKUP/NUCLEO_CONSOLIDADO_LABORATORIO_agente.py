import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os
import shutil
from openai import OpenAI

client = OpenAI(api_key="SUA_API_KEY")

# =========================
# INTERPRETAR COM IA
# =========================

def interpretar(comando):
    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª traduz comandos em aÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes tÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©cnicas em JSON."},
            {"role": "user", "content": comando}
        ]
    )

    return resposta.choices[0].message.content

# =========================
# EXECUTAR AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™ES
# =========================

def executar(acao_json):
    if "imagens" in acao_json.lower():
        origem = "C:\\IOTEC"
        destino = os.path.join(os.path.expanduser("~"), "Desktop", "interfaces")

        os.makedirs(destino, exist_ok=True)

        for root, dirs, files in os.walk(origem):
            for file in files:
                if file.endswith((".png", ".jpg", ".jpeg", ".webp")):
                    shutil.copy(os.path.join(root, file), destino)

        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â Imagens organizadas na ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rea de trabalho")

    elif "ligar nucleo" in acao_json.lower():
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo ativado (simulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o)")

    else:
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ AÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o nÃƒÆ'Ã†â€™o reconhecida")

# =========================
# LOOP DE CONVERSA
# =========================

while True:
    comando = input("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª: ")

    if comando.lower() in ["sair", "exit"]:
        break

    acao = interpretar(comando)

    print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¤ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Å" InterpretaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:", acao)

    executar(acao)


