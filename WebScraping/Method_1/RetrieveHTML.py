import requests

url = "https://www.youtube.com/results?search_query=web+development"

r = requests.get(url)

with open('readed.html', 'w', encoding="utf-8") as f:
    f.write(r.text)