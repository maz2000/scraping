import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.yahoo.co.jp')
soup = BeautifulSoup(r.content,'html.parser')

print(soup.title)
for link in soup.find_all("a"):
    print(link.get("href"))

    
