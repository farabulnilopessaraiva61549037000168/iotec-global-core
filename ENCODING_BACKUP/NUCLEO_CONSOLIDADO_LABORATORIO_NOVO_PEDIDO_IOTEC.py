import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<form action="mailto:iotec.bl@proton.me" method="post" enctype="text/plain">

    <label>Nome:</label><br>
    <input type="text" name="nome"><br><br>

    <label>Empresa:</label><br>
    <input type="text" name="empresa"><br><br>

    <label>ServiÃƒÆ'Ã†â€™o:</label><br>
    <input type="text" name="servico"><br><br>

    <label>DescriÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o:</label><br>
    <textarea name="descricao"></textarea><br><br>

    <button type="submit">Enviar</button>

</form>



