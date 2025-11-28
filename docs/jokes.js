async function getJoke() {
  const jokeRes = await fetch("https://v2.jokeapi.dev/joke/Any?type=single");
  const jokeData = await jokeRes.json();
  const joke = jokeData.joke || `${jokeData.setup} — ${jokeData.delivery}`;
  document.getElementById("original").textContent = joke;

  const translateRes = await fetch("https://api.mymemory.translated.net/", {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      q: joke,
      source: "en",
      target: "ru",
      format: "text"
    })
  });

  const translated = await translateRes.json();
  document.getElementById("translated").textContent = translated.translatedText || "Translate error";
}
