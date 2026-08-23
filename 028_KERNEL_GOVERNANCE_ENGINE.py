# ==============================================================================
# IOTEC
# 028_KERNEL_GOVERNANCE_ENGINE.py
# Kernel de GovernanÃ§a da Plataforma
# ==============================================================================

import os
import json
from dataclasses import dataclass, asdict, field
from collections import defaultdict

# ==============================================================================

@dataclass
class Module:

    nome: str
    caminho: str

    categoria: str = "GERAL"

    tipo: str = "MODULE"

    ativo: bool = True

    engine: bool = False

    api: bool = False

    database: bool = False

    dashboard: bool = False

    auditor: bool = False

    monitor: bool = False

    teste: bool = False

    configuracao: bool = False

    dependencias: list = field(default_factory=list)

# ==============================================================================

class KernelGovernance:

    def __init__(self,pasta="."):

        self.pasta=pasta

        self.modulos=[]

        self.arvore=defaultdict(list)

        self.categorias={

            "PAYPAL":[
                "paypal",
                "payment",
                "pagamento"
            ],

            "CRM":[
                "crm",
                "lead",
                "cliente"
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
                "database",
                "sqlite",
                ".db"
            ],

            "API":[
                "api",
                "flask",
                "fastapi"
            ],

            "IA":[
                "gpt",
                "gemini",
                "claude",
                "llm",
                "openai"
            ],

            "RELATORIOS":[
                "dashboard",
                "report",
                "relatorio"
            ]

        }

    # -------------------------------------------------------------------------

    def descobrir_categoria(self,nome):

        for categoria,palavras in self.categorias.items():

            if any(p in nome for p in palavras):

                return categoria

        return "GERAL"

    # -------------------------------------------------------------------------

    def descobrir_dependencias(self,nome):

        deps=[]

        if "paypal" in nome:

            deps.extend(["DATABASE","API"])

        if "crm" in nome or "lead" in nome:

            deps.extend(["DATABASE"])

        if "dashboard" in nome:

            deps.extend(["DATABASE"])

        if "email" in nome:

            deps.extend(["API"])

        return sorted(set(deps))

    # -------------------------------------------------------------------------

    def indexar(self):

        for raiz,_,arquivos in os.walk(self.pasta):

            for arquivo in arquivos:

                nome=arquivo.lower()

                caminho=os.path.join(raiz,arquivo)

                m=Module(

                    nome=arquivo,

                    caminho=caminho

                )

                m.categoria=self.descobrir_categoria(nome)

                m.engine="engine" in nome

                m.api="api" in nome or "flask" in nome or "fastapi" in nome

                m.database=(".db" in nome) or ("database" in nome)

                m.dashboard="dashboard" in nome

                m.auditor=("audit" in nome) or ("auditor" in nome)

                m.monitor="monitor" in nome

                m.teste="test" in nome

                m.configuracao=("config" in nome) or nome.endswith(".json")

                if nome.endswith(".db"):

                    m.tipo="DATABASE"

                elif nome.endswith(".json"):

                    m.tipo="CONFIG"

                elif nome.endswith(".py"):

                    m.tipo="PYTHON"

                elif nome.endswith(".html"):

                    m.tipo="WEB"

                else:

                    m.tipo="ARQUIVO"

                m.dependencias=self.descobrir_dependencias(nome)

                self.modulos.append(m)

                self.arvore[m.categoria].append(m)

    # -------------------------------------------------------------------------

    def salvar(self):

        dados=[asdict(m) for m in self.modulos]

        with open(

            "kernel_registry.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                dados,

                f,

                indent=4,

                ensure_ascii=False

            )

    # -------------------------------------------------------------------------

    def imprimir(self):

        print()

        print("="*100)

        print("IOTEC - KERNEL DE GOVERNANÃ‡A")

        print("="*100)

        print()

        print(f"MÃ"DULOS INDEXADOS : {len(self.modulos)}")

        print()

        for categoria in sorted(self.arvore):

            lista=self.arvore[categoria]

            print(f"{categoria:<20} {len(lista):>6}")

        print()

        print("="*100)

        print("Registro salvo em kernel_registry.json")

        print("="*100)

# ==============================================================================

if __name__=="__main__":

    kernel=KernelGovernance(".")

    kernel.indexar()

    kernel.salvar()

    kernel.imprimir()

