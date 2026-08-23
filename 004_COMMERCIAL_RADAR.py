# ============================================================
# IOTEC - COMMERCIAL RADAR
# CÃƒÂ³digo 004 da Cadeia Principal
# ============================================================

from datetime import datetime


class CommercialRadar:

    def __init__(self):

        self.name = "COMMERCIAL_RADAR"

        self.status = "ONLINE"

        self.last_scan = None

        self.opportunities = []

    # ---------------------------------------------------------

    def startup(self):

        print(f"{self.name} iniciado.")

    # ---------------------------------------------------------

    def scan(self):

        self.last_scan = datetime.now()

        print(f"\n[{self.last_scan}]")

        print("Escaneando oportunidades comerciais...")

        return self.opportunities

    # ---------------------------------------------------------

    def register_opportunity(
            self,
            company,
            source,
            value,
            priority):

        opportunity = {

            "tipo": "nova_oportunidade",

            "empresa": company,

            "origem": source,

            "valor": value,

            "prioridade": priority,

            "status": "NOVA",

            "data": datetime.now()

        }

        self.opportunities.append(opportunity)

    # ---------------------------------------------------------

    def export_events(self):

        events = self.opportunities.copy()

        self.opportunities.clear()

        return events

    # ---------------------------------------------------------

    def dashboard(self):

        print("\n===============================")

        print("COMMERCIAL RADAR")

        print("===============================")

        print(f"STATUS : {self.status}")

        print(f"EVENTOS: {len(self.opportunities)}")

        print("===============================\n")


# ============================================================

if __name__ == "__main__":

    radar = CommercialRadar()

    radar.startup()

    radar.register_opportunity(

        company="Empresa Alpha",

        source="WEBSITE",

        value=25000,

        priority=9

    )

    radar.register_opportunity(

        company="Prefeitura Municipal",

        source="LICITACAO",

        value=180000,

        priority=10

    )

    radar.dashboard()

    radar.scan()

    eventos = radar.export_events()

    print("\nEVENTOS EXPORTADOS\n")

    for evento in eventos:

        print(evento)

