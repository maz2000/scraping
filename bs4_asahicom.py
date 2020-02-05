import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import csv

page_url = 'http://www.asahi.com/'
r = requests.get(page_url)
soup = BeautifulSoup(r.content,'html.parser')

head_tags = soup.find(class_='List ListHeadline HeadlineAfter HomeTop') #タグが入っているものをh1_tagsに全部取得

for q in head_tags('a'):
    title = q.text
    url = q.get('href')
    base_path = 'https://www.asahi.com'
    absolute_path = urljoin(base_path, url)
    print(title,absolute_path)
 

