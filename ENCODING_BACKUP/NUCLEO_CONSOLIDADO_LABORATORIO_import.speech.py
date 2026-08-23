import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import speech_recognition as sr
import os

def ouvir_comando():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€¦Ã‚Â  Fale seu comando...")
        audio = recognizer.listen(source)

        try:
            comando = recognizer.recognize_google(audio, language='pt-BR')
            print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸  VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª disse: {comando}")
            executar_comando(comando.lower())
        except sr.UnknownValueError:
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ NÃƒÆ'Ã†â€™o entendi o que foi dito.")
        except sr.RequestError:
            print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Erro na solicitaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o.")

def executar_comando(comando):
    if "abrir navegador" in comando:
        os.system("start chrome")
    elif "desligar sistema" in comando:
        os.system("shutdown /s /t 5")
    elif "abrir bloco de notas" in comando:
        os.system("notepad")
    elif "tocar mÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºsica" in comando:
        os.system("start wmplayer")
    elif "parar tudo" in comando:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂºÃƒÂ¢Ã¢â€šÂ¬Ã‹Å" Protocolo de seguranÃƒÆ'Ã†â€™a ativado. Encerrando operaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âµes.")
        exit()
    else:
        print("ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã‚Â¡ÃƒÂ¢Ã¢â‚¬Å¾Ã‚Â¢ÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â Comando nÃƒÆ'Ã†â€™o reconhecido. Refinar ou adicionar novos comandos.")

if __name__ == "__main__":
    while True:
        ouvir_comando()


