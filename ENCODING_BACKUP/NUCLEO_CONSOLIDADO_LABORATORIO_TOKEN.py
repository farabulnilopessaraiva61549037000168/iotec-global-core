import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# figma_interface_autobot.py
import requests

TOKEN = "SEU_TOKEN_FIGMA"
FILE_ID = "SEU_ID_DO_PROJETO"

headers = {
    "X-Figma-Token": TOKEN
}

def listar_paginas():
    url = f"https://api.figma.com/v1/files/{FILE_ID}"
    resp = requests.get(url, headers=headers)
    data = resp.json()
    for page in data["document"]["children"]:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â PÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡gina:", page["name"])

# Use isso para comeÃƒÆ'Ã†â€™ar e listar pÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡ginas
if __name__ == "__main__":
    listar_paginas()


