Clear-Host

Write-Host ""
Write-Host "=============================================================="
Write-Host "IOTEC GLOBAL CORE - STAGE 001"
Write-Host "=============================================================="
Write-Host ""

$arquivo = "C:\IOTEC\GLOBAL_CORE_STAGE01.py"

$codigo = @'
"""
==============================================================

GLOBAL CORE STAGE 001

Primeiro Orquestrador da Plataforma

==============================================================
"""

import os
import subprocess
from datetime import datetime


class GlobalCore:


    def __init__(self):

        self.base=r"C:\IOTEC"

        self.modulos=[

            "EVENT_BUS.py",

            "NEWSROOM_ENGINE.py",

            "EDITOR_IN_CHIEF.py",

            "EXECUTIVE_REPORT_ENGINE.py",

            "COMMERCIAL_INTELLIGENCE.py",

            "ANCHOR_ENGINE.py",

            "IOTEC_PRESIDENT.py"

        ]


    def cabecalho(self):

        print()

        print("="*70)

        print("IOTEC GLOBAL CORE")

        print(datetime.now())

        print("="*70)

        print()


    def verificar(self):

        print("VERIFICANDO MÓDULOS")

        print()

        ativos=[]

        ausentes=[]

        for modulo in self.modulos:

            caminho=os.path.join(self.base,modulo)

            if os.path.exists(caminho):

                ativos.append(caminho)

                print(f"[OK ] {modulo}")

            else:

                ausentes.append(modulo)

                print(f"[ERRO] {modulo}")

        return ativos,ausentes


    def iniciar(self):

        ativos,ausentes=self.verificar()

        print()

        print("="*70)

        print("INICIANDO PLATAFORMA")

        print("="*70)

        print()

        for modulo in ativos:

            print(f"Executando {os.path.basename(modulo)}")

            print()

            try:

                subprocess.run(

                    ["python",modulo],

                    check=False

                )

            except Exception as erro:

                print(erro)

            print()

            print("-"*70)

        print()

        print("="*70)

        print("CICLO FINALIZADO")

        print("="*70)

        print()

        print(f"Módulos ativos : {len(ativos)}")

        print(f"Módulos ausentes : {len(ausentes)}")

        print()

        if ausentes:

            print("Necessitam atenção:")

            for m in ausentes:

                print(f" - {m}")

        else:

            print("Todos os módulos previstos foram encontrados.")

        print()

        print("GLOBAL CORE permanece aguardando o próximo ciclo.")


if __name__=="__main__":

    core=GlobalCore()

    core.cabecalho()

    core.iniciar()
'@

Set-Content `
-Path $arquivo `
-Encoding UTF8 `
-Value $codigo

Write-Host ""
Write-Host "=============================================================="
Write-Host "GLOBAL CORE STAGE 01 CRIADO"
Write-Host "=============================================================="
Write-Host ""
Write-Host $arquivo
Write-Host ""
Write-Host "Execute:"
Write-Host ""
Write-Host "python GLOBAL_CORE_STAGE01.py"
Write-Host ""