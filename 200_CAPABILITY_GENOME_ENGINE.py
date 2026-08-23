from dataclasses import dataclass, field
from pathlib import Path
import ast
import json

# ==========================================================
# IOTEC CAPABILITY GENOME ENGINE
# ==========================================================

@dataclass
class Capability:

    nome: str
    arquivos: list = field(default_factory=list)
    funcoes: list = field(default_factory=list)
    imports: list = field(default_factory=list)
    dependencias: list = field(default_factory=list)


class CapabilityGenome:

    def __init__(self):

        self.genoma = {}

    def registrar(self,
                  nome,
                  arquivo,
                  funcoes,
                  imports):

        if nome not in self.genoma:

            self.genoma[nome] = Capability(nome)

        cap = self.genoma[nome]

        cap.arquivos.append(str(arquivo))
        cap.funcoes.extend(funcoes)
        cap.imports.extend(imports)

    def salvar(self):

        saida = {}

        for nome, cap in self.genoma.items():

            saida[nome] = {

                "arquivos": sorted(set(cap.arquivos)),
                "funcoes": sorted(set(cap.funcoes)),
                "imports": sorted(set(cap.imports))
            }

        with open(
            "CAPABILITY_GENOME.json",
            "w",
            encoding="utf8"
        ) as f:

            json.dump(
                saida,
                f,
                indent=4,
                ensure_ascii=False
            )

