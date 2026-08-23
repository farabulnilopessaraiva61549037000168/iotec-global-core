import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from gtts import gTTS



def gerar_audio(texto, nome_arquivo="resposta.mp3"):
    pass

    tts = gTTS(texto, lang="pt-br")

    tts.save(nome_arquivo)







