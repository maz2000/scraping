import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

"""
with open('dp.html') as f:
    soup = BeautifulSoup(f,'html.parser')
"""
r = requests.get('https://gihyo.jp/dp')
soup = BeautifulSoup(r.content,'html.parser')
#print(soup)

for a in soup.select('#listBook > li > a[itemprop="url"]'):
    url = urljoin('https://gihyo.jp/dp',a.get('href'))
    p = a.select('p[itemprop="name"]')[0]
    title = p.text
    print(url,title)