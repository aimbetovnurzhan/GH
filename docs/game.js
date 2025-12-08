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
  hintEl.textContent = "I thought of a number between 1 and 100. Try to guess!";
  triesEl.textContent = "0";
  historyEl.textContent = "—";
  inputEl.value = "";
  inputEl.disabled = false;
  guessBtn.disabled = false;
  inputEl.focus();
}

function flashBackgroundError() {
  document.body.classList.add('error-bg');
  setTimeout(() => {
    document.body.classList.remove('error-bg');
  }, 1000);
}

function makeGuess() {
  const val = Number(inputEl.value);

  if (!Number.isInteger(val) || val < 1 || val > 100) {
    hintEl.textContent = "Enter a number from 1 to 100";
    return;
  }

  tries++;
  history.push(val);
  triesEl.textContent = String(tries);
  historyEl.textContent = history.join(", ");

  if (val === secret) {
    hintEl.textContent = `✅ - you guessed ${secret} in ${tries} attempts, great job.`;
    inputEl.disabled = true;
    guessBtn.disabled = true;
    return;
  }

      if (val < secret) {
    if (secret - val <= 5) {
        hintEl.textContent = "⬆️ - little low";
    } else {
        hintEl.textContent = "⬆️⬆️ - too Low";
    }
  } else {
    if (val - secret <= 5) {
        hintEl.textContent = "⬇️ - little high"
    } else {
        hintEl.textContent = "⬇️⬇️ - too high.";
    }
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