import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<!doctype html>
<html>
<head>
  <meta charset="utf-8"/>
  <title>Dashboard - Mesa</title>
  <meta name="viewport" content="width=device-width, initial-scale=1"/>
  <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
  <style>
    body{font-family: Arial; padding:16px}
    #notifs {position:fixed; right:16px; top:16px; width:300px}
    .notif {background:#ffeaff; padding:8px; margin-bottom:8px; border-radius:6px; box-shadow:0 1px 3px rgba(0,0,0,0.1)}
    li {margin-bottom:6px}
  </style>
</head>
<body>
  <h2>Dashboard do Professor</h2>
  <div><a href="/">Abrir cliente</a> | <a href="/dashboard">Atualizar</a></div>
  <div id="notifs"></div>
  <h3>ÃƒÆ'Ã…Â¡ltimas Respostas</h3>
  <ul id="list"></ul>

<script>
const socket = io();
const list = document.getElementById('list');
const notifs = document.getElementById('notifs');

socket.on('progress_update', (data) => {
  const li = document.createElement('li');
  li.textContent = `${new Date(data.ts*1000).toLocaleTimeString()} ÃƒÂ¢Ã¢â€šÂ¬Ã¢â‚¬Â ${data.student_id} Q:${data.question_id} A:${data.answer}`;
  list.prepend(li);

  const n = document.createElement('div');
  n.className = 'notif';
  n.textContent = `Aluno ${data.student_id} respondeu ${data.question_id}`;
  notifs.appendChild(n);
  setTimeout(()=> n.remove(), 4500);
});
</script>
</body>
</html>



