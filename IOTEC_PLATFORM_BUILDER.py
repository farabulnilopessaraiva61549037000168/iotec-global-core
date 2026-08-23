import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
==============================================================
IOTEC PLATFORM BUILDER
VersÃƒÆ'Ã‚Â£o 2.0
==============================================================
"""

from pathlib import Path
from datetime import datetime
import platform
import socket
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

LOGGER = logging.getLogger("BUILDER")


class BuilderKernel:

    def __init__(self):

        self.started = datetime.now()

        self.modules = []

        LOGGER.info("Builder Kernel inicializado.")

    def banner(self):

        print()

        print("=" * 80)

        print("IOTEC ENTERPRISE PLATFORM BUILDER")

        print("=" * 80)

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

        print("=" * 80)

        print("ESCANEANDO MÃƒÆ'Ã¢â‚¬Å"DULOS")

        print("=" * 80)

        encontrados = 0

        for arquivo in self.modules:

            if Path(arquivo).exists():

                print("[ OK ]", arquivo)

                encontrados += 1

            else:

                print("[FAIL]", arquivo)

        print()

        print("Encontrados:", encontrados)

        print("Esperados..:", len(self.modules))


def main():

    kernel = BuilderKernel()

    kernel.banner()

    scanner = ModuleScanner()

    scanner.scan()


if __name__ == "__main__":

    main()




