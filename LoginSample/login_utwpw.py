import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

USER = 'maz2000'
PASS = 'tmp13852'

session = requests.session()


login_info = {
    'username_mmlbbs6':USER,
    'password_mmlbbs6':PASS,
    'back':'index.php',
    'mml_id':'0'
}

url_login = 'https://uta.pw/sakusibbs/users.php?action=login&m=try'
res = session.post(url_login, data=login_info)
res.raise_for_status()
#print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
a = soup.select_one('.islogin a')
#a = soup.find(class_='islogin')

if a is None:
    print('ログインできませんでした')
    quit()

url_mypage = urljoin(url_login,a.attrs['href'])
print('マイページ',url_mypage)

res = session.get(url_mypage)
res.raise_for_status()
print(res.text)


