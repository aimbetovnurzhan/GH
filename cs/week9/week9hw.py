import requests

url = "https://v2.jokeapi.dev/joke/Any?type=twopart"
response = requests.get(url)
joke = response.json()
# print(joke)

if joke["type"] == "twopart":
    print(joke["setup"])
    print(joke["delivery"])
else:
    print(joke["joke"])

def translate_mymemory(text, source="en", target="ru"):
    url = "https://api.mymemory.translated.net/get"
    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }
    r = requests.get(url, params=params, timeout=10)
    data = r.json()
    return data["responseData"]["translatedText"]

# print(joke["setup"] + joke["delivery"])

print(translate_mymemory(joke["setup"] + " " + joke["delivery"]))



