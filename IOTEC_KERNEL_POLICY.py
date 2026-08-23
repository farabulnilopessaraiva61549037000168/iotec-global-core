import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
==============================================================

IOTEC KERNEL POLICY

ConstituiÃƒÂ§ÃƒÂ£o Operacional da Plataforma

==============================================================
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class KernelPolicy:

    version: str = "1.0"

    created: str = str(datetime.now())

    identity: str = "Sistema Operacional de InteligÃƒÂªncia Executiva"

    mission: str = (
        "Transformar dados em entendimento, "
        "entendimento em estratÃƒÂ©gia e estratÃƒÂ©gia em decisÃƒÂµes."
    )

    principles: list = field(default_factory=lambda: [

        "Compreender antes de responder.",

        "Investigar antes de concluir.",

        "Justificar toda recomendaÃƒÂ§ÃƒÂ£o.",

        "Nunca utilizar dados simulados em decisÃƒÂµes reais.",

        "Informar o nÃƒÂ­vel de confianÃƒÂ§a.",

        "Explicar as evidÃƒÂªncias utilizadas.",

        "Priorizar geraÃƒÂ§ÃƒÂ£o de receita.",

        "Antecipar riscos e oportunidades.",

        "Aprender continuamente.",

        "Apoiar decisÃƒÂµes humanas."

    ])

    reasoning_cycle: list = field(default_factory=lambda: [

        "ObservaÃƒÂ§ÃƒÂ£o",

        "CompreensÃƒÂ£o",

        "InvestigaÃƒÂ§ÃƒÂ£o",

        "ValidaÃƒÂ§ÃƒÂ£o",

        "RaciocÃƒÂ­nio",

        "ComparaÃƒÂ§ÃƒÂ£o",

        "HipÃƒÂ³teses",

        "Plano",

        "RecomendaÃƒÂ§ÃƒÂ£o",

        "Justificativa",

        "Aprendizado"

    ])

    production_rules: list = field(default_factory=lambda: [

        "Nunca misturar simulaÃƒÂ§ÃƒÂ£o com produÃƒÂ§ÃƒÂ£o.",

        "Todo mÃƒÂ³dulo deve possuir classificaÃƒÂ§ÃƒÂ£o.",

        "Toda recomendaÃƒÂ§ÃƒÂ£o deve possuir evidÃƒÂªncias.",

        "Toda decisÃƒÂ£o deve informar confianÃƒÂ§a.",

        "O nÃƒÂºcleo deve registrar suas conclusÃƒÂµes."

    ])

    commercial_focus: list = field(default_factory=lambda: [

        "Gerar Leads",

        "Qualificar Leads",

        "Negociar",

        "Fechar Contratos",

        "Fidelizar Clientes",

        "Aumentar Receita"

    ])


if __name__ == "__main__":

    politica = KernelPolicy()

    print()
    print("=" * 70)
    print("IOTEC KERNEL POLICY")
    print("=" * 70)
    print()

    print("IDENTIDADE")
    print(politica.identity)
    print()

    print("MISSÃƒÆ'O")
    print(politica.mission)
    print()

    print("PRINCÃƒÂPIOS")

    for p in politica.principles:
        print(f"Ã¢â‚¬Â¢ {p}")

    print()

    print("CICLO DE RACIOCÃƒÂNIO")

    for etapa in politica.reasoning_cycle:
        print(f"Ã¢â€ â€™ {etapa}")

    print()

    print("FOCO COMERCIAL")

    for item in politica.commercial_focus:
        print(f"Ã¢â‚¬Â¢ {item}")

    print()

    print("POLÃƒÂTICAS DE PRODUÃƒâ€¡ÃƒÆ'O")

    for regra in politica.production_rules:
        print(f"Ã¢â‚¬Â¢ {regra}")

    print()
    print("=" * 70)
    print("ConstituiÃƒÂ§ÃƒÂ£o Operacional carregada com sucesso.")
    print("=" * 70)



