import requests
from bs4 import BeautifulSoup
import csv

page_url = 'http://www.asahi.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.content,'html.parser')

head_tags = soup.find(class_='List ListHeadline HeadlineAfter HomeTop') #タグが入っているものをh1_tagsに全部取得

for news in head_tags:
    temp_articles = news.find('a')
    for a in temp_articles:
        print(a)

