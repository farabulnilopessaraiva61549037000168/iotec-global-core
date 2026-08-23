import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from googletrans import Translator

# Criar um objeto tradutor
translator = Translator()

# Texto para traduzir
texto_original = "OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡, como vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡?"

# Traduzir para ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rabe ('ar')
texto_traduzido = translator.translate(texto_original, dest="ar")

# Exibir resultado
print(f"Texto original: {texto_original}")
print(f"Texto traduzido: {texto_traduzido.text}")



