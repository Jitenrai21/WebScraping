import requests
from bs4 import BeautifulSoup
import pandas as pd

proxies = {
    "http": "http://154.16.146.44:80"
}

url = 'https://texascollege.edu.np/bit/'
#THE COMMENTED OUT PART WAS DONE FOR PRACTICE PURPOSE
# url = 'https://www.amazon.com/s?k=iphones'
# headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, proxies=proxies)
# r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

# divs = soup.find(class_="accordion-item")
# print(divs)

# ths = soup.select('th')
# for th in ths:
#     print(th.string)

# tds = soup.select('td')
# for td in tds:
#     print(td.string)

data = []
accordian_items = soup.find_all('div', class_="accordion-item")

for item in accordian_items:
    table_rows = item.find('tbody').find_all('tr')
    for row in table_rows:
        cells = row.find_all('td')
        course_name = cells[1].get_text(strip=True)
        course_code = cells[2].get_text(strip=True)
        data.append([course_name, course_code])

df = pd.DataFrame(data, columns=['Course Name', 'Course Code'])
df.to_csv('course_code.csv', index=False)
print('Data retrieved!')

# print(soup.prettify())

# spans = soup.select('span.a-size-medium.a-color-base.a-text-normal')
# for span in spans:
#     print(span.string)

# prices = soup.select('span.a-price')
# for price in prices:
#     print(price.find('span').get_text())