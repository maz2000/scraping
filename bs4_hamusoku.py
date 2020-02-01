import requests
from bs4 import BeautifulSoup

page_url = 'http://hamusoku.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.text,'html.parser')

#h1_tags = soup.find_all("h1", class_="article-title")
h1_tags = soup.find_all("h1,",class_="article-title entry-title")
h1_tags[1]




