import requests
from bs4 import BeautifulSoup

def get_member_since(username):
    r = requests.get(f'https://www.codewars.com/users/{username}')
    soup = BeautifulSoup(r.content, 'html.parser')
    for boxes in soup.find_all(class_='stat-box', limit=2):
        box = boxes
    print(box.div.get_text()[13:])
    

get_member_since('jhoffner')
