import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.oreilly.com/free/')
contents = r.content
soup = BeautifulSoup(contents, 'lxml')
samples = soup.find_all("a", "item-title")

data = {}
for a in samples:
    title = a.string.strip()
    data[title] = a.attrs['href']

print(data)
