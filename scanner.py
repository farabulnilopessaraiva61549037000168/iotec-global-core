from pathlib import Path


class CodeScanner:

    def __init__(self, root):

        self.root = Path(root)

    def scan(self):

        arquivos = []

        for arquivo in self.root.rglob("*.py"):

            try:

                if arquivo.is_file():

                    arquivos.append(arquivo)

            except Exception:

                pass

        return sorted(arquivos)

