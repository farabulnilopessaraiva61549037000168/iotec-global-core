import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

ROOT = r"C:\IOTEC"

corrigidos = 0

for arquivo in Path(ROOT).rglob("*.py"):
    pass

    try:
        pass

        linhas = arquivo.read_text(
            encoding="utf-8",
            errors="ignore"
        ).splitlines()

        novas = []

        i = 0

        while i < len(linhas):
            pass

            linha = linhas[i]

            # remove "pass" solto logo apÃƒÆ'Ã‚Â³s try/except/if/etc
            if i > 0:
                pass

                anterior = linhas[i - 1].strip()

                if (
                    linha.strip() == "pass"
                    and anterior.endswith(":")
                ):
                    i += 1
                    continue

            novas.append(linha)
            i += 1

        if novas != linhas:
            pass

            arquivo.write_text(
                "\n".join(novas),
                encoding="utf-8"
            )

            corrigidos += 1

    except:
        pass

print()
print("ARQUIVOS CORRIGIDOS :", corrigidos)




