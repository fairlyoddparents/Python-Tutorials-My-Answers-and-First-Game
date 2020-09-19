import requests
from bs4 import BeautifulSoup

class User(object):
    def __init__(self, position, name, clan, honor):
        self.position = position
        self.name = name
        self.clan = clan
        self.honor = honor

class LeaderBoard(object):
    def __init__(self):
        self.position = {}

leaderboard = LeaderBoard()
r = requests.get('https://www.codewars.com/users/leaderboard')
soup = BeautifulSoup(r.content, 'lxml')
users = soup.find_all(attrs={'data-username':True})
nitem = 1

for user in users:
    position = user.find(class_='rank is-small').get_text()[1:]
    name = user.a.get_text()
    object_name = name
    clan = user.find('td', class_=None).get_text()
    honor = int(user.find('td', class_=None).find_next_sibling().get_text().replace(',', ''))
    object_name = User(position, name, clan, honor)
    leaderboard.position[nitem] = object_name
    nitem += 1

print(leaderboard.position[1].name)
