import requests
import sys
from bs4 import BeautifulSoup, UnicodeDammit


r = requests.get('http://corpus.rae.es/cgi-bin/crpsrvEx.dll')
soup = BeautifulSoup(r.content, 'lxml')
print(soup.get_text())
print(soup.original_encoding)
