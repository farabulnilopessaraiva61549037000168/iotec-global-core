import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC GATEWAY ELECTION ENGINE
# ==========================================================

from pathlib import Path

ROOT = Path(r"C:\IOTEC")

IGNORE = {
    "__pycache__",
    "venv",
    "node_modules",
    "ENCODING_BACKUP",
    "BACKUP",
    "MINERADORA_BRUTA",
    "_SANITIZADA"
}

KEYWORDS = {
    "paypal": [
        "paypal",
        "client_id",
        "client_secret",
        "create_order",
        "capture_order",
        "checkout",
        "access_token",
        "oauth"
    ]
}


class GatewayElection:

    def __init__(self):

        self.candidates = []

    # ------------------------------------------------------

    def ignored(self, path):

        text = str(path).lower()

        for folder in IGNORE:

            if folder.lower() in text:
                return True

        if path.name.startswith("019_"):
            return True

        if path.name.startswith("020_"):
            return True

        return False

    # ------------------------------------------------------

    def analyse(self, file):

        try:

            text = file.read_text(
                encoding="utf8",
                errors="ignore"
            ).lower()

        except:

            return

        score = 0
        found = []

        for word in KEYWORDS["paypal"]:

            if word in text:

                score += 10
                found.append(word)

        if score == 0:
            return

        self.candidates.append({

            "file": file,

            "score": score,

            "found": found

        })

    # ------------------------------------------------------

    def discover(self):

        print()
        print("=" * 70)
        print("ELEIÃƒâ€¡ÃƒÆ'O DO GATEWAY OFICIAL")
        print("=" * 70)

        for file in ROOT.rglob("*.py"):

            if self.ignored(file):
                continue

            self.analyse(file)

    # ------------------------------------------------------

    def report(self):

        if not self.candidates:

            print()

            print("Nenhum candidato encontrado.")

            return

        self.candidates.sort(

            key=lambda x: x["score"],

            reverse=True

        )

        print()

        print("FINALISTAS")

        print()

        for item in self.candidates[:10]:

            print("-" * 60)

            print(item["file"].name)

            print("Score :", item["score"])

            print()

        winner = self.candidates[0]

        print("=" * 70)
        print("GATEWAY OFICIAL")
        print("=" * 70)
        print()

        print(winner["file"])

        print()

        print("Score :", winner["score"])

        print()

        print("Palavras encontradas:")

        for word in winner["found"]:

            print("  Ã¢Å"â€œ", word)

        print()

        print("PrÃƒÂ³xima missÃƒÂ£o:")

        print("VALIDAR CRIAÃƒâ€¡ÃƒÆ'O DE PEDIDO")

    # ------------------------------------------------------

    def run(self):

        self.discover()

        self.report()


# ==========================================================

if __name__ == "__main__":

    GatewayElection().run()



