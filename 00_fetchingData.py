import requests

proxies = {
    "http": "http://49.0.2.242:8090",
    "https": "https://192.53.123.54:8080"
}

def fetchAndSave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)

url = 'https://texascollege.edu.np/bit/'

fetchAndSave(url, 'data/texas.html')