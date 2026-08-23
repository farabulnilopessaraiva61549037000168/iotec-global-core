from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class RevenueLayer:
    name: str
    priority: int
    description: str
    leads: List[Dict] = field(default_factory=list)

    def add_lead(self, lead: Dict):
        self.leads.append(lead)

    @property
    def total(self):
        return len(self.leads)


class RevenueLayerEngine:

    def __init__(self):
        self.layers = {
            1: RevenueLayer(
                "Receita Imediata",
                1,
                "Produtos e serviÃƒÂ§os de rÃƒÂ¡pida conversÃƒÂ£o"
            ),
            2: RevenueLayer(
                "Receita Comercial",
                2,
                "Pequenas e mÃƒÂ©dias empresas"
            ),
            3: RevenueLayer(
                "Enterprise",
                3,
                "Grandes empresas"
            ),
            4: RevenueLayer(
                "Governamental",
                4,
                "Ãƒâ€œrgÃƒÂ£os pÃƒÂºblicos"
            ),
            5: RevenueLayer(
                "Internacional",
                5,
                "Mercado externo"
            ),
            6: RevenueLayer(
                "Receita EstratÃƒÂ©gica",
                6,
                "Contratos recorrentes e licenciamento"
            ),
        }

    def add(self, layer: int, lead: Dict):
        self.layers[layer].add_lead(lead)

    def summary(self):
        return {
            layer.name: layer.total
            for layer in self.layers.values()
        }


if __name__ == "__main__":

    engine = RevenueLayerEngine()

    print("=" * 60)
    print("IOTEC REVENUE LAYER ENGINE")
    print("=" * 60)

    for name, total in engine.summary().items():
        print(f"{name:<30} {total}")

