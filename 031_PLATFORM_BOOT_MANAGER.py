# ==============================================================================
# IOTEC
# 031_PLATFORM_BOOT_MANAGER.py
#
# Gerenciador de InicializaÃ§Ã£o da Plataforma
#
# MissÃ£o:
# Descobrir a ordem correta de inicializaÃ§Ã£o de toda a IOTEC.
#
# ==============================================================================

import json
import time

class BootManager:

    def __init__(self):

        self.etapas = [

            ("CORE","001_CORE_OS"),

            ("CONFIG","002_CONFIGURATION"),

            ("LOGGER","003_LOGGER"),

            ("DATABASE","004_DATABASE"),

            ("EVENT BUS","005_EVENT_BUS"),

            ("CONNECTORS","006_CONNECTOR_MANAGER"),

            ("SECURITY","007_SECURITY"),

            ("SCHEDULER","008_SCHEDULER"),

            ("MONITOR","009_MONITOR"),

            ("DISCOVERY","010_SERVICE_DISCOVERY"),

            ("CRM","012_CRM_ENGINE"),

            ("LEADS","011_LEAD_ENGINE"),

            ("PROPOSALS","013_PROPOSAL_ENGINE"),

            ("REVENUE","014_REVENUE_VALIDATION_ENGINE"),

            ("PAYMENT","015_PAYMENT_GATEWAY_ENGINE"),

            ("EMAIL","018_EMAIL_ENGINE"),

            ("WHATSAPP","019_WHATSAPP_ENGINE"),

            ("IA","020_AI_ENGINE"),

            ("DASHBOARD","030_ENTERPRISE_DASHBOARD")

        ]

    # --------------------------------------------------------------

    def iniciar(self):

        print()

        print("="*80)

        print("IOTEC PLATFORM BOOT")

        print("="*80)

        print()

        for nome, modulo in self.etapas:

            print(f"Iniciando {nome:<20}", end="")

            time.sleep(0.15)

            print("[ OK ]")

        print()

        print("="*80)

        print("PLATAFORMA OPERACIONAL")

        print("="*80)

if __name__=="__main__":

    BootManager().iniciar()

