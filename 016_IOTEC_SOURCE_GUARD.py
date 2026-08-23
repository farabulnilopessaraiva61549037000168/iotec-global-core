import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
"""
===============================================================================
 IOTEC SOURCE GUARD
===============================================================================

MISSÃƒÆ'O

Auditar automaticamente qualquer mÃƒÂ³dulo Python antes que ele seja
considerado pronto.

VerificaÃƒÂ§ÃƒÂµes:

Ã¢Å"â€ Sintaxe
Ã¢Å"â€ Classe fechada
Ã¢Å"â€ MÃƒÂ©todo run()
Ã¢Å"â€ if __name__ == "__main__"
Ã¢Å"â€ py_compile
Ã¢Å"â€ Tamanho do arquivo
Ã¢Å"â€ RelatÃƒÂ³rio

===============================================================================
"""

from pathlib import Path
import py_compile
import traceback

ROOT = Path(r"C:\IOTEC")


class SourceGuard:

    def __init__(self):

        self.total = 0
        self.aprovados = 0
        self.reprovados = 0

    # =========================================================

    def verificar(self, arquivo):

        self.total += 1

        print("=" * 70)
        print(arquivo.name)

        try:

            texto = arquivo.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            problemas = []

            # -------------------------------------------------

            if len(texto) < 300:

                problemas.append(
                    "Arquivo muito pequeno."
                )

            # -------------------------------------------------

            if "if __name__ ==" not in texto:

                problemas.append(
                    "Bloco principal inexistente."
                )

            # -------------------------------------------------

            if "run(" not in texto:

                problemas.append(
                    "MÃƒÂ©todo run() nÃƒÂ£o encontrado."
                )

            # -------------------------------------------------

            if "class " not in texto:

                problemas.append(
                    "Classe principal inexistente."
                )

            # -------------------------------------------------

            try:

                py_compile.compile(
                    str(arquivo),
                    doraise=True
                )

            except Exception:

                problemas.append(
                    "Erro de compilaÃƒÂ§ÃƒÂ£o."
                )

            # -------------------------------------------------

            if problemas:

                self.reprovados += 1

                print("STATUS : REPROVADO\n")

                for p in problemas:

                    print(" -", p)

            else:

                self.aprovados += 1

                print("STATUS : APROVADO")

        except Exception:

            self.reprovados += 1

            print("ERRO")

            print(traceback.format_exc())

    # =========================================================

    def executar(self):

        print()
        print("=" * 70)
        print("IOTEC SOURCE GUARD")
        print("=" * 70)
        print()

        for arquivo in ROOT.glob("*.py"):

            self.verificar(arquivo)

        print()
        print("=" * 70)
        print("RESUMO")
        print("=" * 70)

        print("Arquivos :", self.total)
        print("Aprovados:", self.aprovados)
        print("Reprovados:", self.reprovados)

        print()

        if self.reprovados:

            print("AÃƒâ€¡ÃƒÆ'O")

            print("Os mÃƒÂ³dulos reprovados devem ser")
            print("corrigidos antes de entrar na arquitetura.")

        else:

            print("Todos os mÃƒÂ³dulos passaram na auditoria.")

        print("=" * 70)


# ======================================================================

if __name__ == "__main__":

    guard = SourceGuard()

    guard.executar()



