Clear-Host

Write-Host ""
Write-Host "=========================================================="
Write-Host " IOTEC PROCESS MANAGER"
Write-Host " STAGE 001"
Write-Host "=========================================================="
Write-Host ""

$arquivo="C:\IOTEC\PROCESS_MANAGER.py"

$codigo=@'
"""
=============================================================

PROCESS MANAGER

IOTEC OPERATING SYSTEM

=============================================================
"""

from datetime import datetime

import time

import random



class ProcessManager:


    def __init__(self):

        self.processos=[]


    def registrar(

        self,

        nome,

        categoria,

        status="ATIVO"

    ):

        self.processos.append({

            "nome":nome,

            "categoria":categoria,

            "status":status,

            "cpu":0,

            "memoria":0,

            "eventos":0,

            "inicio":datetime.now()

        })


    def atualizar(self):

        for p in self.processos:

            p["cpu"]=random.randint(1,40)

            p["memoria"]=random.randint(50,900)

            p["eventos"]+=random.randint(0,5)


    def painel(self):

        print()

        print("="*70)

        print("PROCESS MANAGER")

        print("="*70)

        print()

        for p in self.processos:

            print(f"Departamento : {p['nome']}")

            print(f"Categoria    : {p['categoria']}")

            print(f"Status       : {p['status']}")

            print(f"CPU          : {p['cpu']} %")

            print(f"Memória      : {p['memoria']} MB")

            print(f"Eventos      : {p['eventos']}")

            print("-"*70)


    def resumo(self):

        ativos=sum(

            1

            for p in self.processos

            if p["status"]=="ATIVO"

        )

        print()

        print("="*70)

        print("RESUMO OPERACIONAL")

        print("="*70)

        print()

        print(f"Departamentos : {len(self.processos)}")

        print(f"Ativos        : {ativos}")

        print(f"Horário       : {datetime.now()}")

        print()

        print("Kernel funcionando normalmente.")

        print()


if __name__=="__main__":

    pm=ProcessManager()

    pm.registrar(

        "Commercial Intelligence",

        "Comercial"

    )

    pm.registrar(

        "NewsRoom",

        "Comunicação"

    )

    pm.registrar(

        "Editor in Chief",

        "Editorial"

    )

    pm.registrar(

        "Anchor",

        "Comunicação"

    )

    pm.registrar(

        "President",

        "Executivo"

    )

    pm.registrar(

        "Kernel",

        "Sistema"

    )

    while True:

        pm.atualizar()

        pm.painel()

        pm.resumo()

        time.sleep(10)
'@

Set-Content `
-Path $arquivo `
-Encoding UTF8 `
-Value $codigo

Write-Host ""
Write-Host "=========================================================="
Write-Host "PROCESS MANAGER CRIADO"
Write-Host "=========================================================="
Write-Host ""

Write-Host $arquivo

Write-Host ""

Write-Host "Execute:"

Write-Host ""

Write-Host "python PROCESS_MANAGER.py"

Write-Host ""