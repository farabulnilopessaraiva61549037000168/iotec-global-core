import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===========================================================

IOTEC KERNEL

Sistema Operacional Corporativo

STAGE 001

===========================================================
"""

import os
import time
from datetime import datetime


class Kernel:


    def __init__(self):

        self.version="1.0"

        self.nome="IOTEC KERNEL"

        self.departamentos=[]

        self.ciclo=0


    def registrar(

        self,

        nome,

        arquivo,

        descricao

    ):

        self.departamentos.append({

            "nome":nome,

            "arquivo":arquivo,

            "descricao":descricao

        })


    def cabecalho(self):

        print()

        print("="*70)

        print("IOTEC KERNEL")

        print(datetime.now())

        print("="*70)

        print()


    def verificar(self):

        print("VERIFICAÃ‡ÃƒO DOS DEPARTAMENTOS")

        print()

        ativos=0

        for d in self.departamentos:

            if os.path.exists(d["arquivo"]):

                print(f"[OK] {d['nome']}")

                ativos+=1

            else:

                print(f"[ERRO] {d['nome']}")

                print(f"Arquivo nÃ£o encontrado: {d['arquivo']}")

            print()

        print("-"*70)

        print(f"Departamentos ativos : {ativos}")

        print(f"Departamentos cadastrados : {len(self.departamentos)}")

        print("-"*70)

        return ativos


    def iniciar(self):

        self.cabecalho()

        ativos=self.verificar()

        print()

        print("NÃšCLEO EXECUTIVO")

        print()

        print("Todos os departamentos registrados foram analisados.")

        print()

        print(f"Departamentos disponÃ­veis: {ativos}")

        print()

        print("Kernel inicializado com sucesso.")


    def ciclo_monitoramento(self):

        self.ciclo+=1

        print()

        print("="*70)

        print(f"CICLO {self.ciclo}")

        print("="*70)

        print()

        print("Monitorando departamentos...")

        print("Recebendo eventos...")

        print("Atualizando Torre de Comando...")

        print("Sistema operacional.")

        print()


if __name__=="__main__":

    kernel=Kernel()

    base=r"C:\IOTEC"

    kernel.registrar(

        "Commercial Intelligence",

        os.path.join(base,"COMMERCIAL_INTELLIGENCE.py"),

        "Departamento Comercial"

    )

    kernel.registrar(

        "NewsRoom",

        os.path.join(base,"NEWSROOM_ENGINE.py"),

        "RedaÃ§Ã£o"

    )

    kernel.registrar(

        "Editor in Chief",

        os.path.join(base,"EDITOR_IN_CHIEF.py"),

        "Diretoria Editorial"

    )

    kernel.registrar(

        "Executive Report",

        os.path.join(base,"EXECUTIVE_REPORT_ENGINE.py"),

        "RelatÃ³rios"

    )

    kernel.registrar(

        "Anchor",

        os.path.join(base,"ANCHOR_ENGINE.py"),

        "Apresentador"

    )

    kernel.registrar(

        "President",

        os.path.join(base,"IOTEC_PRESIDENT.py"),

        "PresidÃªncia"

    )

    kernel.iniciar()

    kernel.ciclo_monitoramento()





