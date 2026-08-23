import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
from pathlib import Path

ARQ = Path(r"C:\IOTEC_OMEGA_X\frontend\index.html")

html = ARQ.read_text(encoding="utf-8")

# =====================================================
# NOVOS CAMPOS
# =====================================================

bloco_antigo = """
<input id="company" placeholder="Empresa">

<input id="email" placeholder="Email">

<input id="sector" placeholder="Setor">

<textarea id="message" placeholder="Requerimento"></textarea>
"""

bloco_novo = """
<input id="company" placeholder="Empresa">

<input id="email" placeholder="Email">

<input id="phone" placeholder="Telefone">

<input id="city" placeholder="Cidade">

<input id="sector" placeholder="Setor">

<input id="employees" placeholder="Quantidade de Funcionarios">

<input id="users_expected" placeholder="Usuarios previstos">

<input id="urgency" placeholder="Urgencia (BAIXA, MEDIA, ALTA, CRITICA)">

<input id="current_system" placeholder="Sistema atual">

<input id="budget_estimate" placeholder="Orcamento estimado">

<input id="desired_deadline" placeholder="Prazo desejado">

<textarea id="message" placeholder="Requerimento"></textarea>
"""

html = html.replace(bloco_antigo, bloco_novo)

# =====================================================
# JS CAMPOS
# =====================================================

js_antigo = """
    const sector =
    document.getElementById("sector").value

    const message =
    document.getElementById("message").value
"""

js_novo = """
    const sector =
    document.getElementById("sector").value

    const phone =
    document.getElementById("phone").value

    const city =
    document.getElementById("city").value

    const employees =
    document.getElementById("employees").value

    const users_expected =
    document.getElementById("users_expected").value

    const urgency =
    document.getElementById("urgency").value

    const current_system =
    document.getElementById("current_system").value

    const budget_estimate =
    document.getElementById("budget_estimate").value

    const desired_deadline =
    document.getElementById("desired_deadline").value

    const message =
    document.getElementById("message").value
"""

html = html.replace(js_antigo, js_novo)

# =====================================================
# PAYLOAD
# =====================================================

payload_antigo = """
    const payload = {

        company,
        email,
        sector,
        message

    }
"""

payload_novo = """
    const payload = {

        company,
        email,

        phone,
        city,

        sector,

        employees,
        users_expected,

        urgency,
        current_system,

        budget_estimate,
        desired_deadline,

        message

    }
"""

html = html.replace(payload_antigo, payload_novo)

backup = ARQ.with_suffix(".html.bak")

backup.write_text(
    ARQ.read_text(encoding="utf-8"),
    encoding="utf-8"
)

ARQ.write_text(html, encoding="utf-8")

print("")
print("========================================")
print("FRONTEND LEADS 360 INSTALADO")
print("========================================")
print("")
print("BACKUP:")
print(backup)
print("")




