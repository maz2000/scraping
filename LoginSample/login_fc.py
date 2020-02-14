import re
import time
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

"""
Databaseの準備
"""
client = MongoClient('localhost',27017)
collection = client.scraping.feelcycle_histry
collection.create_index('key',unique=True)

USER = 'masakaz@gmail.com'
PASS = input('Password>>>>')
session = requests.session()

login_info = {
    'login_id':USER,
    'login_pass':PASS,
    'commit_login':'',
    'mml_id':'0'
}

url_login = 'https://www.feelcycle.com/feelcycle_reserve/mypage.php'
r = session.post(url_login, data=login_info)
r.raise_for_status() #ちゃんとアクセスできなかったら処理を中断
r.encoding = r.apparent_encoding #エンコーディングを正しく設定
soup = BeautifulSoup(r.text,'html.parser')

print(soup.text)

cnt = 1
tbls = soup.find_all('table')
for tbl in tbls[3]('td',bgcolor='#FFFFFF'):
        print(tbl)
        cnt+=1
        print(cnt)

