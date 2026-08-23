import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<form action="http://localhost:5000/receber" method="POST">



  <input type="text" name="nome" placeholder="Seu nome" required>

  <input type="email" name="email" placeholder="Seu email" required>



  <textarea name="mensagem" placeholder="Descreva o serviÃƒÆ'Ã†â€™Ãƒâ€ Ã¢â‚¬â„¢ÃƒÆ'Ã¢â‚¬Å¡o"></textarea>



  <button type="submit">Enviar</button>



</form>







