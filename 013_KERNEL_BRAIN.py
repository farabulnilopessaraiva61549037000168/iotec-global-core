import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
======================================================================
IOTEC
013_KERNEL_BRAIN.py
CÃƒâ€°REBRO ESTRATÃƒâ€°GICO DA IOTEC
======================================================================
"""

from datetime import datetime
import random


class Setor:

    def __init__(self, nome):

        self.nome = nome

        self.status = random.choice([
            "OPERACIONAL",
            "NORMAL",
            "ATENÃƒâ€¡ÃƒÆ'O"
        ])

        self.indice = random.randint(50,100)

        self.alertas = []

        self.recomendacoes = []


class KernelBrain:

    def __init__(self):

        self.data = datetime.now()

        self.setores = [

            Setor("Kernel"),
            Setor("Control Center"),
            Setor("Comercial"),
            Setor("Financeiro"),
            Setor("JurÃƒÂ­dico"),
            Setor("Marketing"),
            Setor("Projetos"),
            Setor("CRM"),
            Setor("GovernanÃƒÂ§a"),
            Setor("Auditoria"),
            Setor("LogÃƒÂ­stica")

        ]


    def analisar(self):

        for setor in self.setores:

            if setor.indice < 60:

                setor.alertas.append(
                    "Desempenho abaixo do esperado."
                )

            if setor.nome == "Comercial":

                setor.recomendacoes.append(
                    "Prospectar novos clientes."
                )

            elif setor.nome == "Marketing":

                setor.recomendacoes.append(
                    "Atualizar portfÃƒÂ³lio."
                )

            elif setor.nome == "Financeiro":

                setor.recomendacoes.append(
                    "Monitorar fluxo de caixa."
                )

            elif setor.nome == "CRM":

                setor.recomendacoes.append(
                    "Qualificar novos leads."
                )

            else:

                setor.recomendacoes.append(
                    "OperaÃƒÂ§ÃƒÂ£o dentro da rotina."
                )


    def indice_operacional(self):

        return sum(
            setor.indice
            for setor in self.setores
        ) / len(self.setores)


    def gargalo(self):

        return min(
            self.setores,
            key=lambda x: x.indice
        )


    def melhor_setor(self):

        return max(
            self.setores,
            key=lambda x: x.indice
        )


    def briefing(self):

        indice = self.indice_operacional()

        pior = self.gargalo()

        melhor = self.melhor_setor()

        print("="*70)

        print("IOTEC KERNEL BRAIN")

        print("="*70)

        print()

        print("Data:",
              self.data.strftime("%d/%m/%Y"))

        print("Hora:",
              self.data.strftime("%H:%M:%S"))

        print()

        print("="*70)

        print("ANÃƒÂLISE DOS SETORES")

        print("="*70)

        print()

        for setor in self.setores:

            print(f"{setor.nome:<18} "
                  f"{setor.indice:>3}%   "
                  f"{setor.status}")

        print()

        print("="*70)

        print("DIAGNÃƒâ€œSTICO")

        print("="*70)

        print()

        print(f"ÃƒÂndice Operacional : {indice:.1f}%")

        print(f"Melhor Setor       : {melhor.nome}")

        print(f"Gargalo Principal  : {pior.nome}")

        print()

        print("="*70)

        print("ALERTAS")

        print("="*70)

        print()

        for setor in self.setores:

            for alerta in setor.alertas:

                print(f"[{setor.nome}] {alerta}")

        print()

        print("="*70)

        print("RECOMENDAÃƒâ€¡Ãƒâ€¢ES")

        print("="*70)

        print()

        recomendacoes = []

        for setor in self.setores:

            recomendacoes.extend(setor.recomendacoes)

        for i, rec in enumerate(dict.fromkeys(recomendacoes), start=1):

            print(f"{i}. {rec}")

        print()

        print("="*70)

        print("PRESIDÃƒÅ NCIA")

        print("="*70)

        print()

        if pior.nome == "Comercial":

            print("Prioridade MÃƒÂ¡xima:")

            print("Gerar novos contratos.")

        elif pior.nome == "Financeiro":

            print("Prioridade MÃƒÂ¡xima:")

            print("Fortalecer fluxo financeiro.")

        elif pior.nome == "Marketing":

            print("Prioridade MÃƒÂ¡xima:")

            print("Melhorar divulgaÃƒÂ§ÃƒÂ£o da empresa.")

        else:

            print("Prioridade MÃƒÂ¡xima:")

            print(f"Fortalecer o setor {pior.nome}.")

        print()

        print("="*70)

        print("MISSÃƒÆ'O DO DIA")

        print("="*70)

        print()

        print("Toda decisÃƒÂ£o deve aproximar a IOTEC")
        print("de novos clientes, novos contratos")
        print("e geraÃƒÂ§ÃƒÂ£o sustentÃƒÂ¡vel de receita.")

        print()

        print("="*70)

        print("FIM DO BRIEFING")

        print("="*70)


if __name__ == "__main__":

    kernel = KernelBrain()

    kernel.analisar()

    kernel.briefing()



