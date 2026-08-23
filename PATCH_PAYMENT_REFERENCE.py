from pathlib import Path
import re

ARQ = Path(r"C:\IOTEC\PAYMENT_ENGINE.py")

texto = ARQ.read_text(encoding="utf-8", errors="ignore")

# adiciona captura do order_id
texto = texto.replace(
'''payment_link = dados.get("url")

        if not payment_link:
''',
'''payment_link = dados.get("url")
        order_id = dados.get("order_id")

        if not payment_link:
'''
)

# substitui o UPDATE para gravar payment_reference
padrao = re.compile(
r'''cur\.execute\(\s*""".*?UPDATE pipeline.*?WHERE opportunity_id=\?\s*"""\s*,\s*\(\s*"PAYPAL"\s*,\s*payment_link\s*,\s*op_id\s*\)\s*\)''',
re.DOTALL
)

novo = '''cur.execute("""

        UPDATE pipeline

        SET

            payment_provider=?,
            payment_reference=?,
            payment_link=?,
            payment_status='AGUARDANDO_PAGAMENTO'

        WHERE opportunity_id=?

        """,(

            "PAYPAL",
            order_id,
            payment_link,
            op_id

        ))'''

texto = padrao.sub(novo, texto)

ARQ.write_text(texto, encoding="utf-8")

print("="*70)
print("PAYMENT ENGINE PATCH")
print("="*70)
print()
print("payment_reference integrado com sucesso.")
print()
print("Agora o order_id do PayPal serÃ¡ salvo no banco.")


