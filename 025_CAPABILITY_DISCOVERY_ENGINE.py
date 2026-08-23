# ==============================================================================
# IOTEC
# 025_CAPABILITY_DISCOVERY_ENGINE.py
# Descoberta AutomÃ¡tica de Capacidades
# ==============================================================================

import os
from dataclasses import dataclass
from typing import List


# ==============================================================================
# CAPACIDADE
# ==============================================================================

@dataclass
class Capability:

    nome: str
    encontrada: bool
    quantidade: int
    arquivos: List[str]


# ==============================================================================
# ENGINE
# ==============================================================================

class CapabilityDiscoveryEngine:

    def __init__(self, pasta="."):

        self.pasta = pasta
        self.capacidades = []

        self.regras = {

            "PAYPAL": [
                "paypal",
                "payment",
                "pagamento"
            ],

            "CRM": [
                "crm",
                "cliente",
                "lead"
            ],

            "GMAIL": [
                "gmail",
                "email",
                "smtp"
            ],

            "WHATSAPP": [
                "whatsapp",
                "twilio"
            ],

            "BANCO DE DADOS": [
                "sqlite",
                ".db",
                "database"
            ],

            "PDF": [
                "pdf",
                "fpdf",
                "reportlab"
            ],

            "IA": [
                "openai",
                "gemini",
                "claude",
                "llm",
                "gpt"
            ],

            "RELATÃ"RIOS": [
                "report",
                "relatorio",
                "dashboard"
            ],

            "MAPAS": [
                "google_maps",
                "maps",
                "geocode"
            ],

            "API": [
                "api",
                "fastapi",
                "flask"
            ]
        }

    # -------------------------------------------------------------------------

    def descobrir(self):

        arquivos = []

        for raiz, _, files in os.walk(self.pasta):

            for arquivo in files:

                arquivos.append(arquivo.lower())

        for nome_capacidade, palavras in self.regras.items():

            encontrados = []

            for arquivo in arquivos:

                for palavra in palavras:

                    if palavra in arquivo:

                        encontrados.append(arquivo)
                        break

            self.capacidades.append(

                Capability(

                    nome=nome_capacidade,

                    encontrada=len(encontrados) > 0,

                    quantidade=len(encontrados),

                    arquivos=sorted(encontrados)

                )

            )

    # -------------------------------------------------------------------------

    def imprimir(self):

        print()
        print("=" * 100)
        print("IOTEC - MAPA DE CAPACIDADES")
        print("=" * 100)

        total = 0

        for cap in self.capacidades:

            status = "SIM" if cap.encontrada else "NÃƒO"

            print(f"\n{cap.nome}")
            print("-" * 80)
            print(f"DisponÃ­vel : {status}")
            print(f"Arquivos   : {cap.quantidade}")

            if cap.arquivos:

                for arq in cap.arquivos:
                    print(f"   â€¢ {arq}")

                total += 1

        print("\n" + "=" * 100)
        print(f"CAPACIDADES ENCONTRADAS : {total}/{len(self.capacidades)}")
        print("=" * 100)


# ==============================================================================
# EXECUÃ‡ÃƒO
# ==============================================================================

if __name__ == "__main__":

    engine = CapabilityDiscoveryEngine(".")

    engine.descobrir()

    engine.imprimir()

