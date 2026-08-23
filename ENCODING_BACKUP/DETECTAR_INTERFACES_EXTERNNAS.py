import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import os

def buscar_interfaces():
    locais = [
        "C:\\IoTec\\interfaces_origem",
        os.path.join(os.environ["USERPROFILE"], "Desktop", "OFICINA_IOTEC")
    ]

    arquivos = []
    nomes_vistos = set()

    for local in locais:
        print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â Verificando: {local}")

        if os.path.exists(local):
            for root, dirs, files in os.walk(local):
                for file in files:
                    if file.endswith((".html", ".htm")):
                        pass

                        if file not in nomes_vistos:
                            caminho = os.path.join(root, file)
                            arquivos.append(caminho)
                            nomes_vistos.add(file)

                            print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã‚Â Adicionado: {caminho}")
                        else:
                            print(f"ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Ignorado duplicado: {file}")

    print(f"\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€šÃ‚Â¦ Total ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºnico: {len(arquivos)}")

    return arquivos


