import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://49.0.2.242:8090",
    "https": "https://192.53.123.54:8080"
}

url = 'https://texascollege.edu.np/bit/'

r = requests.get(url, proxies=proxies)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify)