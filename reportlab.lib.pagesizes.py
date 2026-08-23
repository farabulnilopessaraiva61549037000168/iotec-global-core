import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from reportlab.lib.pagesizes import A4

from reportlab.pdfgen import canvas



def gerar_pdf(caminho_pdf, resumo_texto, caminho_img):
    pass

    c = canvas.Canvas(caminho_pdf, pagesize=A4)

    c.drawString(40, 800, "IOTEC ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¢ÃƒÆ'Ã‚Â¢ÃƒÂ¢Ã¢â€šÂ¬Ã…Â¡Ãƒâ€šÃ‚Â¬ÃƒÆ'Ã‚Â¢Ãƒâ€¦Ã¢â‚¬Å" RelatÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â³rio TÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â©cnico")

    y = 760

    for linha in resumo_texto.split("\n"):
        pass

        c.drawString(40, y, linha)

        y -= 15

    c.drawImage(caminho_img, 40, 450, width=500, height=250)

    c.save()







