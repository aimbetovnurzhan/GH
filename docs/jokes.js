async function getJoke() {
  const jokeRes = await fetch("https://v2.jokeapi.dev/joke/Any?type=single");
  const jokeData = await jokeRes.json();
  const joke = jokeData.joke || `${jokeData.setup} — ${jokeData.delivery}`;
  document.getElementById("original").textContent = joke;

    async function translate(text, source = "en", target = "ru") {
    const url = "https://api.mymemory.translated.net/get";
    const params = new URLSearchParams({
        q: text,
        langpair: `${source}|${target}`
    });

    try {
        const response = await fetch(`${url}?${params}`);
        const data = await response.json();
        return data.responseData.translatedText;
    } catch (error) {
        console.error("Ошибка перевода:", error);
        return "Ошибка";
    }
    };

  const translated = await translateRes.json();
  document.getElementById("translated").textContent = translated.translatedText || "Translate error";
}
