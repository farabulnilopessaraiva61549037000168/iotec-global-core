# ==============================================================================
# IOTEC
# 030_CODE_INTELLIGENCE_ENGINE.py
#
# InteligÃªncia Arquitetural
#
# LÃª o cÃ³digo Python utilizando AST
# ==============================================================================

import os
import ast
import json
from dataclasses import dataclass, asdict, field

# ==============================================================================

@dataclass
class SourceModule:

    arquivo:str
    caminho:str

    imports:list = field(default_factory=list)

    classes:list = field(default_factory=list)

    funcoes:list = field(default_factory=list)

    chamadas:list = field(default_factory=list)

    decoradores:list = field(default_factory=list)

    erros:list = field(default_factory=list)

# ==============================================================================

class CodeIntelligence:

    def __init__(self,pasta="."):

        self.pasta=pasta

        self.modulos=[]

    # --------------------------------------------------------------------------

    def analisar_python(self,caminho):

        modulo=SourceModule(

            arquivo=os.path.basename(caminho),

            caminho=caminho

        )

        try:

            with open(

                caminho,

                encoding="utf-8",

                errors="ignore"

            ) as f:

                codigo=f.read()

            arvore=ast.parse(codigo)

        except Exception as e:

            modulo.erros.append(str(e))

            return modulo

        for node in ast.walk(arvore):

            if isinstance(node,ast.Import):

                for n in node.names:

                    modulo.imports.append(n.name)

            elif isinstance(node,ast.ImportFrom):

                if node.module:

                    modulo.imports.append(node.module)

            elif isinstance(node,ast.ClassDef):

                modulo.classes.append(node.name)

            elif isinstance(node,ast.FunctionDef):

                modulo.funcoes.append(node.name)

                for dec in node.decorator_list:

                    if hasattr(dec,"id"):

                        modulo.decoradores.append(dec.id)

            elif isinstance(node,ast.Call):

                if hasattr(node.func,"id"):

                    modulo.chamadas.append(node.func.id)

                elif hasattr(node.func,"attr"):

                    modulo.chamadas.append(node.func.attr)

        return modulo

    # --------------------------------------------------------------------------

    def executar(self):

        for raiz,_,arquivos in os.walk(self.pasta):

            for arq in arquivos:

                if not arq.endswith(".py"):

                    continue

                caminho=os.path.join(raiz,arq)

                self.modulos.append(

                    self.analisar_python(caminho)

                )

    # --------------------------------------------------------------------------

    def salvar(self):

        with open(

            "code_intelligence.json",

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                [asdict(x) for x in self.modulos],

                f,

                indent=4,

                ensure_ascii=False

            )

    # --------------------------------------------------------------------------

    def resumo(self):

        total_imports=0
        total_classes=0
        total_funcoes=0
        total_calls=0
        erros=0

        print()

        print("="*100)
        print("IOTEC CODE INTELLIGENCE")
        print("="*100)

        for m in self.modulos:

            total_imports+=len(m.imports)
            total_classes+=len(m.classes)
            total_funcoes+=len(m.funcoes)
            total_calls+=len(m.chamadas)

            if m.erros:

                erros+=1

        print()

        print(f"MÃ³dulos Python........ {len(self.modulos)}")
        print(f"Imports............... {total_imports}")
        print(f"Classes............... {total_classes}")
        print(f"FunÃ§Ãµes............... {total_funcoes}")
        print(f"Chamadas.............. {total_calls}")
        print(f"Arquivos com erro..... {erros}")

        print()

        print("RelatÃ³rio salvo em code_intelligence.json")

# ==============================================================================

if __name__=="__main__":

    c=CodeIntelligence(".")

    c.executar()

    c.salvar()

    c.resumo()

