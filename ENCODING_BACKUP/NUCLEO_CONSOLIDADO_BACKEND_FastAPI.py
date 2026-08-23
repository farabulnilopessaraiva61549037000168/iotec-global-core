import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from fastapi import FastAPI
from pydantic import BaseModel
import random
import uvicorn

app = FastAPI(title="EQUIP.ORG NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo")

# Banco de Dados Simulado
banco_de_dados = []

# Modelo de dados
class Dado(BaseModel):
    fonte: str
    informacao: str
    valor: float

@app.get("/")
def status():
    return {"status": "ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â¸Ãƒâ€šÃ‚Â¢ NÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºcleo Operacional"}

@app.post("/minerar/")
def minerar():
    fontes = ["ImobiliÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio", "JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico", "Marketing", "LogÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica"]
    dado = Dado(
        fonte=random.choice(fontes),
        informacao=f"Dado minerado da fonte {random.choice(fontes)}",
        valor=random.randint(100, 10000)
    )
    banco_de_dados.append(dado)
    return {"resultado": dado}

@app.get("/dados/")
def listar_dados():
    return banco_de_dados

@app.delete("/vender/")
def vender():
    if banco_de_dados:
        vendido = banco_de_dados.pop(0)
        return {"vendido": vendido}
    else:
        return {"aviso": "Sem dados disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­veis"}

if __name__ == "__main__":
    uvicorn.run("equip_nucleo:app", host="0.0.0.0", port=8000, reload=True)


