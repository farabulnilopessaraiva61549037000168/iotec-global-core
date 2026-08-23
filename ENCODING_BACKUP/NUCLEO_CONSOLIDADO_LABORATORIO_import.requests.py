import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import speech_recognition as sr
import requests

URL = "http://127.0.0.1:8000"

def comando_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½ Aguardando comando de voz...")
        audio = r.listen(source)

        try:
            comando = r.recognize_google(audio, language="pt-BR")
            print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª disse: {comando}")

            if "minerar" in comando:
                response = requests.post(f"{URL}/minerar/")
                print(response.json())

            elif "vender" in comando:
                response = requests.delete(f"{URL}/vender/")
                print(response.json())

            elif "listar" in comando:
                response = requests.get(f"{URL}/dados/")
                print(response.json())

            else:
                print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Comando nÃƒÆ'Ã†â€™o reconhecido.")
        except Exception as e:
            print(f"[Erro de Voz] {e}")

while True:
    comando_voz()


