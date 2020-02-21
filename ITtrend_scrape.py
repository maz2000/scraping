import re
import time
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = 'masakaz@orangeone.jp'
PASS = input('Password>>>>')
session = requests.session()

login_info = {
    'email':USER,
    'password':PASS
}

url_login = 'https://client.it-trend.jp/login'
r = session.post(url_login, data=login_info)
r.raise_for_status() #ちゃんとアクセスできなかったら処理を中断
r.encoding = r.apparent_encoding #エンコーディングを正しく設定
soup = BeautifulSoup(r.text,'html.parser')

print(soup.text)

#コメント
