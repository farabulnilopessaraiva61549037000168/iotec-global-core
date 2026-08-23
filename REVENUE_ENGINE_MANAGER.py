from pathlib import Path
import importlib.util


class RevenueEngineManager:

    def __init__(self, root="."):

        self.root = Path(root)

        self.engines = []

        self.loaded = []

        self.failed = []

    def discover(self):

        self.engines = sorted(

            self.root.glob("*ENGINE.py")

        )

    def load(self):

        for file in self.engines:

            try:

                spec = importlib.util.spec_from_file_location(

                    file.stem,

                    file

                )

                module = importlib.util.module_from_spec(spec)

                spec.loader.exec_module(module)

                self.loaded.append(file.name)

            except Exception as e:

                self.failed.append(

                    (file.name, str(e))

                )

    def report(self):

        print("=" * 70)

        print("REVENUE ENGINE MANAGER")

        print("=" * 70)

        print("DISCOVERED :", len(self.engines))

        print("LOADED     :", len(self.loaded))

        print("FAILED     :", len(self.failed))

        if self.failed:

            print()

            print("FAILED ENGINES")

            print("-" * 70)

            for name, error in self.failed:

                print(name)

                print(error)

                print()


if __name__ == "__main__":

    manager = RevenueEngineManager()

    manager.discover()

    manager.load()

    manager.report()

