import requests

def fetchAndSave(url, path):
    r = requests.get(url)
    with open(path, "w", encoding='utf-8') as f:
        f.write(r.text)

url = 'https://texascollege.edu.np/bit/'

fetchAndSave(url, 'data/texas.html')