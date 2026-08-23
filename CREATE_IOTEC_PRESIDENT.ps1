Clear-Host

Write-Host ""
Write-Host "=========================================================="
Write-Host " IOTEC PRESIDENT"
Write-Host " STAGE 001"
Write-Host "=========================================================="
Write-Host ""

$arquivo = "C:\IOTEC\IOTEC_PRESIDENT.py"

$codigo = @'
"""
==============================================================

IOTEC PRESIDENT

Centro Executivo Digital

==============================================================

O Presidente Digital reúne informações dos departamentos
e produz um único briefing executivo.

==============================================================
"""

from datetime import datetime


class President:


    def __init__(self):

        self.nome="Farabulini"

        self.departamentos=[]


    def receber(

        self,

        nome,

        status,

        resumo,

        prioridade="MEDIA"

    ):

        self.departamentos.append({

            "nome":nome,

            "status":status,

            "resumo":resumo,

            "prioridade":prioridade

        })


    def abertura(self):

        print()

        print("="*70)

        print("PRESIDÊNCIA EXECUTIVA IOTEC")

        print(datetime.now())

        print("="*70)

        print()

        print(f"Boa noite, {self.nome}.")

        print()

        print(

            "Todos os departamentos concluíram "

            "o último ciclo de monitoramento."

        )

        print()


    def situacao(self):

        print("="*70)

        print("SITUAÇÃO DOS DEPARTAMENTOS")

        print("="*70)

        print()

        for d in self.departamentos:

            print(f"[{d['status']}] {d['nome']}")

        print()


    def briefing(self):

        print("="*70)

        print("BRIEFING EXECUTIVO")

        print("="*70)

        print()

        for d in self.departamentos:

            print(f"{d['nome']}")

            print()

            print(d["resumo"])

            print()

            print("-"*70)

            print()


    def prioridades(self):

        print("="*70)

        print("PRIORIDADES DO DIA")

        print("="*70)

        print()

        criticos=[

            d for d in self.departamentos

            if d["prioridade"] in ("CRITICA","ALTA")

        ]

        if len(criticos)==0:

            print("Nenhuma prioridade crítica.")

        else:

            for d in criticos:

                print(f"• {d['nome']}")

        print()


    def encerramento(self):

        print("="*70)

        print("MENSAGEM DO NÚCLEO EXECUTIVO")

        print("="*70)

        print()

        print(

            "Farabulini, a plataforma permanece "

            "em monitoramento contínuo."

        )

        print()

        print(

            "Os departamentos continuarão "

            "analisando oportunidades,"

        )

        print(

            "riscos, contratos, campanhas "

            "e desempenho da empresa."

        )

        print()

        print("Próximo briefing: 10 minutos.")

        print()

        print("="*70)



if __name__=="__main__":


    presidente=President()


    presidente.receber(

        "Diretoria Comercial",

        "ATENÇÃO",

        "O pipeline permanece abaixo da meta mensal. "
        "Recomenda-se ampliar campanhas e prospecção.",

        "ALTA"

    )


    presidente.receber(

        "Diretoria Financeira",

        "ESTÁVEL",

        "Nenhum contrato foi registrado "
        "desde o último plantão.",

        "MEDIA"

    )


    presidente.receber(

        "Centro de Operações",

        "ESTÁVEL",

        "Infraestrutura funcionando normalmente.",

        "BAIXA"

    )


    presidente.abertura()

    presidente.situacao()

    presidente.briefing()

    presidente.prioridades()

    presidente.encerramento()

'@

Set-Content `
-Path $arquivo `
-Value $codigo `
-Encoding UTF8

Write-Host ""
Write-Host "=========================================================="
Write-Host "IOTEC PRESIDENT CRIADO"
Write-Host "=========================================================="
Write-Host ""

Write-Host $arquivo

Write-Host ""

Write-Host "Execute:"

Write-Host ""

Write-Host "python IOTEC_PRESIDENT.py"