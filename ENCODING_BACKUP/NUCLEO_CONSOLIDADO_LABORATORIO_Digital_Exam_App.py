import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Prova Digital - 6ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº Ano</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 0; padding: 0; background: #f4f4f4; }
    .container { max-width: 800px; margin: auto; padding: 20px; }
    .question { display: none; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }
    .question.active { display: block; }
    .options button { display: block; width: 100%; margin: 10px 0; padding: 15px; font-size: 16px; border: 1px solid #ccc; border-radius: 8px; cursor: pointer; background: #fafafa; }
    .navigation { margin-top: 20px; display: flex; justify-content: space-between; }
    .navigation button { padding: 10px 20px; font-size: 16px; border: none; border-radius: 8px; cursor: pointer; background: #007BFF; color: white; }
    .navigation button:disabled { background: #ccc; cursor: not-allowed; }
  </style>
</head>
<body>
  <div class="container">
    <h1>Prova Digital - MatemÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡tica (6ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Âº Ano)</h1>
    <div id="questions"></div>
    <div class="navigation">
      <button id="prevBtn" onclick="prevQuestion()">Anterior</button>
      <button id="nextBtn" onclick="nextQuestion()">PrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³xima</button>
    </div>
  </div>

  <script>
    const questions = [
      { q: "1) Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o resultado de 3/4 + 1/4?", options: ["1/2", "1", "2/4", "4/4"], answer: 1 },
      { q: "2) Em um grÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â¡fico de barras, 10 alunos gostam de futebol e 5 de vÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´lei. Qual esporte tem mais votos?", options: ["Futebol", "VÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â´lei", "Os dois iguais", "Nenhum"], answer: 0 },
      { q: "3) Quanto ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© 25% de 200?", options: ["25", "50", "100", "200"], answer: 1 },
      { q: "4) Resolva: 8 x 7 = ?", options: ["54", "56", "64", "49"], answer: 1 },
      { q: "5) Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© a fraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o equivalente a 2/4?", options: ["1/2", "2/2", "4/2", "3/4"], answer: 0 },
      { q: "6) Se um carro anda 60 km em 1 hora, quantos km ele anda em 3 horas?", options: ["90 km", "120 km", "150 km", "180 km"], answer: 3 },
      { q: "7) Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© o menor nÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Âºmero primo?", options: ["0", "1", "2", "3"], answer: 2 },
      { q: "8) Quanto ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© 3ÃƒÆ'Ã¢â‚¬Å¡Ãƒâ€šÃ‚Â²?", options: ["3", "6", "9", "12"], answer: 2 },
      { q: "9) O perÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â­metro de um quadrado de lado 5 cm ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â©:", options: ["10 cm", "15 cm", "20 cm", "25 cm"], answer: 2 },
      { q: "10) Qual ÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â© a fraÃƒÆ'Ã†â€™ÃƒÆ'Ã†â€™o que representa metade de uma pizza?", options: ["1/3", "1/2", "1/4", "2/3"], answer: 1 }
    ];

    let current = 0;
    let answers = Array(questions.length).fill(null);

    function loadQuestions() {
      const container = document.getElementById("questions");
      container.innerHTML = "";
      questions.forEach((q, i) => {
        const div = document.createElement("div");
        div.classList.add("question");
        if (i === 0) div.classList.add("active");
        div.innerHTML = `<h2>${q.q}</h2>`;

        const opts = document.createElement("div");
        opts.classList.add("options");
        q.options.forEach((opt, j) => {
          const btn = document.createElement("button");
          btn.textContent = opt;
          btn.onclick = () => selectAnswer(i, j);
          opts.appendChild(btn);
        });

        div.appendChild(opts);
        container.appendChild(div);
      });
    }

    function selectAnswer(qIndex, optIndex) {
      answers[qIndex] = optIndex;
    }

    function showQuestion(index) {
      document.querySelectorAll(".question").forEach((q, i) => {
        q.classList.remove("active");
        if (i === index) q.classList.add("active");
      });
      document.getElementById("prevBtn").disabled = index === 0;
      document.getElementById("nextBtn").textContent = index === questions.length - 1 ? "Finalizar" : "PrÃƒÆ'Ã†â€™Ãƒâ€šÃ‚Â³xima";
    }

    function nextQuestion() {
      if (current < questions.length - 1) {
        current++;
        showQuestion(current);
      } else {
        finalizarProva();
      }
    }

    function prevQuestion() {
      if (current > 0) {
        current--;
        showQuestion(current);
      }
    }

    function finalizarProva() {
      let resultado = "<h2>Respostas do Aluno</h2><ol>";
      answers.forEach((a, i) => {
        resultado += `<li>${questions[i].q}<br>Resposta escolhida: ${a !== null ? questions[i].options[a] : "NÃƒÆ'Ã†â€™o respondeu"}</li>`;
      });
      resultado += "</ol>";
      document.querySelector(".container").innerHTML = resultado;
    }

    loadQuestions();
  </script>
</body>
</html>



