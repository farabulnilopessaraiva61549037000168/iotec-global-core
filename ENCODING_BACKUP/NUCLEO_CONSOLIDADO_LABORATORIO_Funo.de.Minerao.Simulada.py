import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import speech_recognition as sr
import schedule
import time
import random

# Banco de Dados Simulado
dados_extraidos = []

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de MineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o Simulada
def minerar_dados():
    fontes = ["ImobiliÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡rio", "JurÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­dico", "LogÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­stica", "Marketing"]
    dado = {
        "fonte": random.choice(fontes),
        "informacao": f"Dado relevante da {random.choice(fontes)}",
        "valor_estimado": random.randint(100, 5000)
    }
    dados_extraidos.append(dado)
    print(f"[+] Minerado: {dado}")

# FunÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de Venda de Dados
def vender_dados():
    if dados_extraidos:
        vendido = dados_extraidos.pop(0)
        print(f"[ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â€žÂ¢Ãƒâ€šÃ‚Â°] Vendido: {vendido}")
    else:
        print("[!] Sem dados disponÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­veis para venda.")

# Reconhecimento de Comando de Voz
def comando_voz():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸Ãƒâ€¦Ã‚Â½ Aguardando comando de voz...")
        audio = r.listen(source)
        try:
            comando = r.recognize_google(audio, language="pt-BR")
            print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬ÂÃƒÆ'Ã‚Â¯Ãƒâ€šÃ‚Â¸Ãƒâ€šÃ‚Â VocÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âª disse: {comando}")

            if "minerar" in comando:
                minerar_dados()
            elif "vender" in comando:
                vender_dados()
            elif "status" in comando:
                print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Dados no estoque: {len(dados_extraidos)}")
            else:
                print("ÃƒÆ'Ã‚Â¢Ãƒâ€šÃ‚ÂÃƒâ€¦Ã¢â‚¬â„¢ Comando nÃƒÆ'Ã†â€™o reconhecido.")
        except Exception as e:
            print(f"[Erro de Voz] {e}")

# Agendamento AutomÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tico
schedule.every(10).seconds.do(minerar_dados)
schedule.every(30).seconds.do(vender_dados)

# Loop Principal
while True:
    comando_voz()
    schedule.run_pending()
    time.sleep(1)


