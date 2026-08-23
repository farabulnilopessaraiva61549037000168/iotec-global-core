import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# SimulaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o da mineraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o digital (superfÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­cie, subsolo, aÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©reo, oceÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢nico)
class MineradorDigital:
    def __init__(self):
        self.fontes = ["web_surface", "deep_web", "cloud_air", "ocean_data"]
        self.dados_coletados = {}

    def escavar(self):
        for fonte in self.fontes:
            self.dados_coletados[fonte] = self.simular_captacao(fonte)

    def simular_captacao(self, origem):
        return f"Dados captados da origem: {origem}"

    def relatorio(self):
        return self.dados_coletados


