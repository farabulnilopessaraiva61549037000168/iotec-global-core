import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
# ==========================================================
# IOTEC PAYMENT AUDITOR
# Auditoria dos Gateways de Pagamento
# ==========================================================

from pathlib import Path
import re

ROOT = Path("C:/IOTEC")

KEYWORDS = {

    "paypal":[
        "paypal",
        "client_id",
        "client_secret",
        "access_token",
        "oauth",
        "checkout",
        "capture",
        "orders"
    ],

    "picpay":[
        "picpay",
        "x-picpay-token",
        "qrcode",
        "merchant"
    ],

    "stripe":[
        "stripe",
        "sk_live",
        "pk_live",
        "checkout.session"
    ],

    "mercadopago":[
        "mercadopago",
        "mercado pago",
        "access_token"
    ]

}

# ==========================================================

class PaymentAuditor:

    def __init__(self):

        self.results=[]

# ==========================================================

    def score_file(self,file):

        try:

            text=file.read_text(
                encoding="utf8",
                errors="ignore"
            ).lower()

        except:

            return None

        score=0

        found=[]

        gateway=None

        for name,words in KEYWORDS.items():

            local_score=0
            local_found=[]

            for word in words:

                if word in text:

                    local_score+=10
                    local_found.append(word)

            if local_score>score:

                score=local_score
                found=local_found
                gateway=name

        if score==0:

            return None

        return {

            "file":file,

            "gateway":gateway,

            "score":score,

            "found":found

        }

# ==========================================================

    def scan(self):

        print()

        print("="*70)
        print("AUDITORIA DOS GATEWAYS")
        print("="*70)

        for file in ROOT.rglob("*.py"):

            item=self.score_file(file)

            if item:

                self.results.append(item)

# ==========================================================

    def report(self):

        self.results.sort(
            key=lambda x:x["score"],
            reverse=True
        )

        if not self.results:

            print()

            print("Nenhum gateway localizado.")

            return

        print()

        print("TOP 10 MÃƒâ€œDULOS")

        print()

        for item in self.results[:10]:

            print("="*70)

            print(item["file"])

            print()

            print("Gateway :",item["gateway"])

            print("Score   :",item["score"])

            print()

            print("Encontrado:")

            for k in item["found"]:

                print("  Ã¢Å"â€œ",k)

            print()

        best=self.results[0]

        print("="*70)
        print("GATEWAY OFICIAL RECOMENDADO")
        print("="*70)

        print()

        print(best["file"])

        print()

        print("Gateway :",best["gateway"])

        print("Score   :",best["score"])

        print()

        print("PRÃƒâ€œXIMA MISSÃƒÆ'O")

        print()

        print("GERAR CHECKOUT")

        print("CRIAR LINK")

        print("VALIDAR WEBHOOK")

        print("VALIDAR RECEBIMENTO")

# ==========================================================

    def run(self):

        self.scan()

        self.report()

# ==========================================================

if __name__=="__main__":

    PaymentAuditor().run()



