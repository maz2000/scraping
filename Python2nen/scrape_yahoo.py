import requests
from bs4 import BeautifulSoup

url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(url)
soup = BeautifulSoup(html.content,'html.parser')

t = soup.find(class_='topicsList_main')

for topic in t._find_all('a'): 
    print(topic)


