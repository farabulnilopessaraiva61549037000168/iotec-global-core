# ==========================================================
# 056_PAYMENT_FORENSICS_ENGINE.py
# IOTEC PAYMENT FORENSICS ENGINE
# ==========================================================

import os
import sqlite3

ROOT = r"C:\IOTEC"
DB = "iotec_kernel.db"

KEYWORDS = {

    "CHECKOUT":[
        "checkout",
        "create_payment",
        "payment_link",
        "paypal"
    ],

    "WEBHOOK":[
        "webhook",
        "ipn",
        "return_url",
        "cancel_url"
    ],

    "CAPTURE":[
        "capture",
        "capture_order",
        "confirm_payment",
        "payment_status",
        "completed"
    ],

    "DATABASE":[
        "payments",
        "insert into payments",
        "update payments",
        "payment_received"
    ],

    "CONTROL_TOWER":[
        "control tower",
        "mission",
        "dispatch",
        "production",
        "delivery"
    ]

}

print("="*70)
print("IOTEC PAYMENT FORENSICS ENGINE")
print("="*70)
print()

conn = sqlite3.connect(DB, timeout=30)
cur = conn.cursor()

cur.execute("PRAGMA journal_mode=WAL")
cur.execute("PRAGMA synchronous=NORMAL")
cur.execute("PRAGMA busy_timeout=30000")

cur.execute("""

CREATE TABLE IF NOT EXISTS payment_forensics(

id INTEGER PRIMARY KEY AUTOINCREMENT,

categoria TEXT,

arquivo TEXT,

linha INTEGER,

evidencia TEXT

)

""")

conn.commit()

cur.execute("DELETE FROM payment_forensics")
conn.commit()

arquivos = 0
evidencias = 0

for pasta,_,files in os.walk(ROOT):

    for nome in files:

        if not nome.endswith(".py"):
            continue

        caminho = os.path.join(pasta,nome)

        arquivos += 1

        try:

            with open(caminho,"r",encoding="utf8",errors="ignore") as f:

                linhas = f.readlines()

        except:

            continue

        for numero,linha in enumerate(linhas,1):

            baixo = linha.lower()

            for categoria,palavras in KEYWORDS.items():

                if any(p in baixo for p in palavras):

                    cur.execute("""

                    INSERT INTO payment_forensics(

                    categoria,
                    arquivo,
                    linha,
                    evidencia

                    )

                    VALUES(?,?,?,?)

                    """,(categoria,caminho,numero,linha.strip()))

                    evidencias += 1

conn.commit()

print("Arquivos analisados :",arquivos)
print("EvidÃƒÂªncias :",evidencias)
print()

print("="*70)
print("MAPA FINANCEIRO")
print("="*70)
print()

for categoria in KEYWORDS:

    cur.execute("""

    SELECT COUNT(*)

    FROM payment_forensics

    WHERE categoria=?

    """,(categoria,))

    total = cur.fetchone()[0]

    print(f"{categoria:<20}{total}")

print()

print("="*70)
print("TOP 25 ARQUIVOS MAIS IMPORTANTES")
print("="*70)
print()

cur.execute("""

SELECT

arquivo,

COUNT(*)

FROM payment_forensics

GROUP BY arquivo

ORDER BY COUNT(*) DESC

LIMIT 25

""")

for arquivo,total in cur.fetchall():

    print(f"{total:>4}  {arquivo}")

print()

print("="*70)
print("PERGUNTAS DA PRESIDÃƒÅ NCIA")
print("="*70)
print()

perguntas=[

"Quem cria o Checkout?",

"Quem conversa com o PayPal?",

"Quem recebe o Webhook?",

"Quem confirma o pagamento?",

"Quem grava no banco?",

"Quem avisa a Control Tower?",

"Quem libera ProduÃƒÂ§ÃƒÂ£o?",

"Quem encerra a venda?"

]

for p in perguntas:

    print("[ ]",p)

print()

print("="*70)
print("MISSÃƒÆ'O")
print("="*70)
print()

print("A PresidÃƒÂªncia agora possui")
print("um mapa forense do")
print("ecossistema financeiro.")

print()
print("PrÃƒÂ³xima etapa:")
print("o Kernel responderÃƒÂ¡")
print("cada pergunta")
print("com evidÃƒÂªncias.")

conn.close()


