import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from datetime import datetime
import platform
import socket
import logging
import json

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

LOGGER = logging.getLogger("BUILDER")


class BuilderKernel:

    def __init__(self):

        self.started = datetime.now()

        LOGGER.info("Builder Kernel inicializado.")

    def banner(self):

        print()
        print("="*80)
        print("IOTEC ENTERPRISE PLATFORM BUILDER")
        print("="*80)
        print()

        print("Sistema :", platform.system())
        print("Hostname:", socket.gethostname())
        print("Raiz....:", Path.cwd())
        print()


class ModuleScanner:

    def __init__(self):

        self.modules = [

            "001_IOTEC_ENTERPRISE_COMMAND_CENTER.py",
            "002_X27_CORE.py",
            "003_KATSUYO_ENGINE.py",
            "004_EVENT_BUS.py",
            "005_REVENUE_RADAR.py",
            "006_MARKET_HUNTER.py",
            "007_COMMERCIAL_AGENT.py",
            "008_CONTRACT_CENTER.py",
            "009_FINANCIAL_CENTER.py",
            "010_BUDGET_HUNTER.py",
            "011_CRM_CENTER.py",
            "012_CONNECTOR_MANAGER.py",
            "013_API_GATEWAY.py",
            "014_SECURITY_CENTER.py",
            "015_AUDIT_ENGINE.py",
            "016_ENTERPRISE_KERNEL.py"

        ]

    def scan(self):

        print("="*80)
        print("ESCANEANDO MÃƒâ€œDULOS")
        print("="*80)

        encontrados = 0

        for arquivo in self.modules:

            if Path(arquivo).exists():

                print("[ OK ]",arquivo)

                encontrados += 1

            else:

                print("[FAIL]",arquivo)

        print()

        print("Encontrados :", encontrados)

        print("Esperados...:", len(self.modules))

        print()


class ProjectStructure:

    def __init__(self):

        self.folders = [

            "core",
            "kernel",
            "agents",
            "commercial",
            "contracts",
            "crm",
            "finance",
            "gateway",
            "connectors",
            "audit",
            "security",
            "database",
            "config",
            "plugins",
            "logs",
            "reports",
            "dashboard",
            "scheduler",
            "services",
            "storage",
            "warroom",
            "tests"

        ]

    def build(self):

        print("="*80)
        print("CRIANDO ESTRUTURA")
        print("="*80)

        for folder in self.folders:

            Path(folder).mkdir(
                exist_ok=True
            )

            init = Path(folder)/"__init__.py"

            if not init.exists():

                init.write_text(
                    "# Package\n",
                    encoding="utf-8"
                )

            print("[ OK ]",folder)

        print()


class ConfigBuilder:

    def build(self):

        cfg = {

            "project":"IOTEC",

            "version":"2.0",

            "database":"database/iotec.db",

            "logs":"logs/",

            "reports":"reports/"

        }

        Path("config").mkdir(exist_ok=True)

        with open(

            "config/config.json",

            "w",

            encoding="utf-8"

        ) as arq:

            json.dump(

                cfg,

                arq,

                indent=4,

                ensure_ascii=False

            )

        print("[ OK ] config/config.json")


class ReadmeBuilder:

    def build(self):

        Path("README.md").write_text(

"""# IOTEC ENTERPRISE PLATFORM

Projeto criado automaticamente pelo Builder.

""",

encoding="utf-8"

        )

        print("[ OK ] README.md")


class RequirementsBuilder:

    def build(self):

        Path("requirements.txt").write_text(

"""requests
flask
fastapi
sqlalchemy
pandas
numpy
""",

encoding="utf-8"

        )

        print("[ OK ] requirements.txt")


def main():

    kernel = BuilderKernel()

    kernel.banner()

    scanner = ModuleScanner()

    scanner.scan()

    structure = ProjectStructure()

    structure.build()

    ConfigBuilder().build()

    ReadmeBuilder().build()

    RequirementsBuilder().build()

    print()

    print("="*80)

    print("PLATAFORMA PREPARADA")

    print("="*80)


if __name__ == "__main__":

    main()




