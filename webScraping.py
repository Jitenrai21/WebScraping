import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
    "http": "http://154.16.146.44:80",
    
}

url = 'https://texascollege.edu.np/bit/'
# url = 'https://www.amazon.com/s?k=iphones'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, proxies=proxies)
# r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# spans = soup.select('span.a-size-medium.a-color-base.a-text-normal')
# for span in spans:
#     print(span.string)

# prices = soup.select('span.a-price')
# for price in prices:
#     print(price.find('span').get_text())


#THIS PART WAS WORKED ON TEXAS WEBSITE
# print(soup.prettify())

# divs = soup.find(class_="accordion-item")
# print(divs)

data = {'Title':[], 'Data':[]}

ths = soup.select('th')
for th in ths:
    print(th.string)
    data['Title'].append(th.string)

tds = soup.select('td')
for td in tds:
    print(td.string)
    data['Data'].append(td.string)

#THIS DIDN'T WORK
# df = pd.DataFrame.from_dict(data)
# df.to_csv('data.csv', index=False)