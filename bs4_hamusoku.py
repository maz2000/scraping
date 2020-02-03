import requests
from bs4 import BeautifulSoup

page_url = 'http://hamusoku.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.content,'html.parser')

h1_tags = soup.find_all('h1',class_='article-title')

#data = []
#for h1_tag in h1_tags.find_all('a'):
#    print(h1_tag)





for topic in h1_tags.find_all('a'):
    print(topic.text)


#for topic in h1_tags._find_all('a'): 
#    print(topic)


"""
t = soup.find(class_='topicsList_main')

for topic in t._find_all('a'): 
    print(topic.text)
"""




