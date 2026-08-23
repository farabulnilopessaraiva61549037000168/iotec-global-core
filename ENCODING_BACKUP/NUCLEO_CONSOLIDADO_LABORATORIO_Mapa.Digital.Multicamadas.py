import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o de escavaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o digital - Mapa Digital Multicamadas

class EscavacaoDigital:
    def __init__(self):
        self.camadas = {
            "superficie": [],
            "subsolo": [],
            "oceano_digital": [],
            "aereo": [],
            "deep_web": []
        }

    def escavar(self, camada, dado):
        if camada in self.camadas:
            self.camadas[camada].append(dado)
            print(f"[ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å"ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œ] Dado captado na camada {camada}: {dado}")
        else:
            print(" Camada nÃƒÆ'Ã†â€™o reconhecida")

    def resumo_escavacao(self):
        print("\nÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã…â€œÃƒâ€¦Ã‚Â  Resumo das camadas escavadas:")
        for camada, dados in self.camadas.items():
            print(f"ÃƒÆ'Ã‚Â°Ãƒâ€¦Ã‚Â¸ÃƒÂ¢Ã¢â€šÂ¬Ã‚ÂÃƒâ€šÃ‚Â¹ {camada.capitalize()}: {len(dados)} dados coletados")

# Simulando escavaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o
complexo = EscavacaoDigital()
complexo.escavar("superficie", "tendÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âªncia de busca por IA")
complexo.escavar("subsolo", "dados de servidores antigos")
complexo.escavar("oceano_digital", "dados de satÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©lites e redes perdidas")
complexo.escavar("aereo", "trÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fego por drones e sensores")
complexo.escavar("deep_web", "registro criptografado de fÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³rum cientÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­fico")

complexo.resumo_escavacao()


