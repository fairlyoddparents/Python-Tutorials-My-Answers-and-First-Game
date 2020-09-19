import requests
from bs4 import BeautifulSoup

def get_honor(username):
    r = requests.get(f'https://www.codewars.com/users/{username}').text
    return r.split('Honor:</b>', 1)[1].split('<', 1)[0].replace(',', '')

get_honor('g964')
