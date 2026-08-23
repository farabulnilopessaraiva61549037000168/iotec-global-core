import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from transformers import pipeline
import pandas as pd

# Carregar modelo prÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©-treinado para anÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡lise de sentimentos
sentiment_model = pipeline("sentiment-analysis")

# Exemplo: funÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o para classificar motivaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o com modelo transformer
def classificar_motivacao(textos):
    resultados = sentiment_model(textos)
    respostas = []
    for res in resultados:
        label = res['label']
        score = res['score']
        if label == 'POSITIVE' and score > 0.8:
            respostas.append("Motivado")
        elif label == 'NEGATIVE' and score > 0.8:
            respostas.append("Desmotivado")
        else:
            respostas.append("Neutro")
    return respostas

# Simular dados recebidos
dados = pd.DataFrame({
    "texto": [
        "Estou muito animado para novos desafios!",
        "NÃƒÆ'Ã†â€™o acredito que vou conseguir...",
        "Sinto-me indiferente hoje."
    ]
})

# Classificar e mostrar resultados
dados['motivacao'] = classificar_motivacao(dados['texto'].tolist())
print(dados)

# Aqui, vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª poderia salvar resultados, alimentar um dashboard, coletar feedback, etc.


