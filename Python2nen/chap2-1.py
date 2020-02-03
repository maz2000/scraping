import requests
from bs4 import BeautifulSoup

url = 'https://www.ymori.com/books/python2nen/test2.html'
html = requests.get(url)
soup = BeautifulSoup(html.content,'html.parser')

print('----------------------------')

print(soup.find('title'))
print('----------------------------')

chap2 = soup.find(id='chap2')
for element in chap2.find_all('li'):
    print(element.text)

