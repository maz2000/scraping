import requests
from bs4 import BeautifulSoup

page_url = 'http://pgl-db.net/season-pokemon/?battle=1'
r = requests.get(page_url)
soup = BeautifulSoup(r.content,'html.parser')

print([i.get_text() for i in soup.select('table tr td:nth-child(3) a', limit=5)])
