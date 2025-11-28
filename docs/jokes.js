async function getJoke() {
  const jokeRes = await fetch("https://v2.jokeapi.dev/joke/Any?type=single");
  const jokeData = await jokeRes.json();
  const joke = jokeData.joke || `${jokeData.setup} — ${jokeData.delivery}`;

  document.getElementById("original").textContent = joke;

  const translated = await translate(joke, "en", "ru");
  document.getElementById("translated").textContent = translated;
}

async function translate(text, source = "en", target = "ru") {
  const url = "https://api.mymemory.translated.net/get";
  const params = new URLSearchParams({
    q: text,
    langpair: `${source}|${target}`
  });

  try {
    const res = await fetch(`${url}?${params}`);
    const data = await res.json();
    return data.responseData.translatedText || "Ошибка перевода";
  } catch (err) {
    console.error("Ошибка перевода:", err);
    return "Ошибка соединения";
  }
}
