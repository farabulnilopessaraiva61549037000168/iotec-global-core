import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import deepl

# Substitua por sua chave de API do DeepL (Cadastre-se no site do DeepL para obter uma chave gratuita)
auth_key = "SUA_CHAVE_DE_API"

# Criar um tradutor
translator = deepl.Translator(auth_key)

# Texto para traduzir
texto_original = "OlÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡, como vocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª estÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡?"

# Traduzir para ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rabe ('AR')
texto_traduzido = translator.translate_text(texto_original, target_lang="AR")

# Exibir resultado
print(f"Texto original: {texto_original}")
print(f"Texto traduzido: {texto_traduzido.text}")



