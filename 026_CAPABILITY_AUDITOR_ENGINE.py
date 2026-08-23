# ==============================================================================
# IOTEC
# 026_CAPABILITY_AUDITOR_ENGINE.py
# Auditor Inteligente de Capacidades
# ==============================================================================

import os
from dataclasses import dataclass, field

# ==============================================================================

@dataclass
class CapabilityAudit:

    nome: str

    principais: int = 0

    backups: int = 0

    duplicados: int = 0

    cache: int = 0

    configuracoes: int = 0

    bancos: int = 0

    logs: int = 0

    documentos: int = 0

    score: float = 0

    status: str = ""

    arquivos: list = field(default_factory=list)

# ==============================================================================

class CapabilityAuditor:

    def __init__(self, pasta="."):

        self.pasta = pasta

        self.auditorias = {}

        self.regras = {

            "PAYPAL":[
                "paypal",
                "payment",
                "pagamento"
            ],

            "CRM":[
                "crm",
                "cliente",
                "lead"
            ],

            "EMAIL":[
                "email",
                "gmail",
                "smtp"
            ],

            "WHATSAPP":[
                "whatsapp"
            ],

            "DATABASE":[
                ".db",
                "database",
                "sqlite"
            ],

            "IA":[
                "gpt",
                "gemini",
                "claude",
                "openai",
                "llm"
            ],

            "PDF":[
                ".pdf",
                "reportlab",
                "fpdf"
            ],

            "API":[
                "flask",
                "fastapi",
                "api"
            ]

        }

    # ----------------------------------------------------------------------

    def auditar(self):

        todos = []

        for raiz, _, arquivos in os.walk(self.pasta):

            for arq in arquivos:

                todos.append(arq.lower())

        for nome, palavras in self.regras.items():

            audit = CapabilityAudit(nome)

            for arquivo in todos:

                if not any(p in arquivo for p in palavras):
                    continue

                audit.arquivos.append(arquivo)

                if arquivo.endswith(".py"):
                    audit.principais += 1

                if "backup" in arquivo:
                    audit.backups += 1

                if "duplicado" in arquivo:
                    audit.duplicados += 1

                if arquivo.endswith(".pyc"):
                    audit.cache += 1

                if arquivo.endswith(".json"):
                    audit.configuracoes += 1

                if arquivo.endswith(".db"):
                    audit.bancos += 1

                if arquivo.endswith(".log"):
                    audit.logs += 1

                if arquivo.endswith(".pdf"):
                    audit.documentos += 1

            score = 0

            score += audit.principais * 5
            score += audit.bancos * 3
            score += audit.configuracoes * 2

            score -= audit.backups
            score -= audit.duplicados
            score -= audit.cache * 0.25

            if score < 0:
                score = 0

            audit.score = round(score,1)

            if score >= 80:
                audit.status = "EXCELENTE"

            elif score >= 50:
                audit.status = "BOM"

            elif score >= 20:
                audit.status = "EM EVOLUÃ‡ÃƒO"

            else:
                audit.status = "INICIAL"

            self.auditorias[nome]=audit

    # ----------------------------------------------------------------------

    def imprimir(self):

        print()
        print("="*100)
        print("IOTEC - AUDITOR DE CAPACIDADES")
        print("="*100)

        for audit in self.auditorias.values():

            print()

            print(audit.nome)

            print("-"*80)

            print(f"MÃ³dulos Python........: {audit.principais}")
            print(f"Backups...............: {audit.backups}")
            print(f"Duplicados............: {audit.duplicados}")
            print(f"Cache.................: {audit.cache}")
            print(f"ConfiguraÃ§Ãµes.........: {audit.configuracoes}")
            print(f"Bancos................: {audit.bancos}")
            print(f"Logs..................: {audit.logs}")
            print(f"Documentos............: {audit.documentos}")
            print(f"Score.................: {audit.score}")
            print(f"Status................: {audit.status}")

        print()
        print("="*100)

# ==============================================================================

if __name__ == "__main__":

    auditor = CapabilityAuditor(".")

    auditor.auditar()

    auditor.imprimir()

