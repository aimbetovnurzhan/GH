// Угадай число — веб-версия

let secret;
let tries;
let history;

const hintEl = document.getElementById("hint");
const inputEl = document.getElementById("guessInput");
const triesEl = document.getElementById("tries");
const historyEl = document.getElementById("history");
const guessBtn = document.getElementById("guessBtn");
const restartBtn = document.getElementById("restartBtn");

function newGame() {
  secret = Math.floor(Math.random() * 100) + 1; // 1..100
  tries = 0;
  history = [];
  hintEl.textContent = "Я загадал число от 1 до 100. Попробуй угадать!";
  triesEl.textContent = "0";
  historyEl.textContent = "—";
  inputEl.value = "";
  inputEl.disabled = false;
  guessBtn.disabled = false;
  inputEl.focus();
}

function makeGuess() {
  const val = Number(inputEl.value);

  if (!Number.isInteger(val) || val < 1 || val > 100) {
    hintEl.textContent = "Введите целое число от 1 до 100 🙂";
    return;
  }

  tries++;
  history.push(val);
  triesEl.textContent = String(tries);
  historyEl.textContent = history.join(", ");

  if (val === secret) {
    hintEl.textContent = `✅ Угадал! Это ${secret}. Попыток: ${tries}.`;
    inputEl.disabled = true;
    guessBtn.disabled = true;
    return;
  }

  if (val < secret) {
    hintEl.textContent = "⬆️ Слишком маленькое. Попробуй больше.";
  } else {
    hintEl.textContent = "⬇️ Слишком большое. Попробуй меньше.";
  }

  inputEl.select();
}

guessBtn.addEventListener("click", makeGuess);
restartBtn.addEventListener("click", newGame);

// Enter тоже отправляет попытку
inputEl.addEventListener("keydown", (e) => {
  if (e.key === "Enter") makeGuess();
});

newGame();