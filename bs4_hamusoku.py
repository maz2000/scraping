import requests
from bs4 import BeautifulSoup
import csv

page_url = 'http://hamusoku.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.content,'html.parser')

#h1_tags = soup.find_all('h1',class_='article-title') #h1タグが入っているものをh1_tagsに全部取得
h1_tags = soup.select('h1.article-title') #h1タグが入っているものをh1_tagsに全部取得
data = [] #配列を初期化py
for h1_tag in h1_tags: #h1_tagsからaタグをが付いているものを1つずつ取り出す
    temp_Article_a_tag = h1_tag.find('a') #最初のaタグを取り出す
    title = temp_Article_a_tag.text
    url = temp_Article_a_tag.get('href')
    print('title:{} url:{}'.format(title,url))
    data.append([title, url])

print('------------------------------------')

for d in data:
    print(d[0])
    print(d[1])

            


