from dataclasses import dataclass
from typing import List


@dataclass
class Capability:

    name: str
    keywords: List[str]


class CapabilityMatchEngine:

    def __init__(self):

        self.capabilities = []

    def register(self, capability: Capability):

        self.capabilities.append(capability)

    def match(self, text: str):

        text = text.lower()

        result = []

        for capability in self.capabilities:

            for keyword in capability.keywords:

                if keyword.lower() in text:

                    result.append(capability.name)
                    break

        return sorted(set(result))


if __name__ == "__main__":

    engine = CapabilityMatchEngine()

    engine.register(
        Capability(
            "Business Intelligence",
            [
                "dashboard",
                "indicador",
                "relatÃƒÂ³rio"
            ]
        )
    )

    engine.register(
        Capability(
            "ConstruÃƒÂ§ÃƒÂ£o",
            [
                "obra",
                "engenharia",
                "construÃƒÂ§ÃƒÂ£o"
            ]
        )
    )

    texto = "Empresa procurando dashboard para engenharia."

    print("=" * 60)
    print("CAPABILITY MATCH ENGINE")
    print("=" * 60)

    print(engine.match(texto))

