import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<!-- static/dashboard.html -->
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Dashboard - Mesa</title>
  <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
</head>
<body>
  <h2>Dashboard do Professor</h2>
  <div id="notifs"></div>
  <h3>ÃƒÆ'Ã†â€™Ãƒâ€¦Ã‚Â¡ltimas Respostas</h3>
  <ul id="list"></ul>

  <script>
    const socket = io();
    const list = document.getElementById('list');
    const notifs = document.getElementById('notifs');

    socket.on('progress_update', (data) => {
      const li = document.createElement('li');
      li.textContent = `${new Date().toLocaleTimeString()} - ${data.student_id} Q:${data.question_id} A:${data.answer}`;
      list.prepend(li);

      // notificaÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o discreta que aparece e some
      const n = document.createElement('div');
      n.style = 'background:#fffa; padding:8px; margin:5px; border-radius:5px;';
      n.textContent = `Aluno ${data.student_id} respondeu ${data.question_id}`;
      notifs.appendChild(n);
      setTimeout(()=> n.remove(), 4000);
    });
  </script>
</body>
</html>



