import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

"""<form class="landingLoginForm" autocomplete="off" data-event_name="Login with password" action="/login" accept-charset="UTF-8" method="post">
  <input name="utf8" type="hidden" value="✓">
  <input type="hidden" name="authenticity_token" value="rYIMTVoDlb4eCzh6wZIRgiPQHmrr5ts9DyykDCE9FkHM7zQxX7WAhmUhW8y0BPIA3MvzH31KCFEyiPTVk4GBzQ==">
  <input type="text" name="identity" id="identity" placeholder="Username or email" autofocus="autofocus" class="form-control landingLoginForm_identity">
  <div class="row">
    <div class="col-sm-9 landingLoginForm_passwordColumn">
      <input type="password" name="password" id="password" placeholder="Password" class="form-control">
    </div>
    <div class="col-sm-3 landingLoginForm_submitColumn">
      <input type="submit" name="commit" value="Login" class="btn btn-primary btn-block" data-disable-with="Login">
    </div>
  </div>
  <div class="landingLoginForm_forgotPassword">
    <a href="https://qiita.com/sessions/forgot_password">Forgot Password?</a>
  </div>
  <div class="help-block js-email-invalid-message" style="display: none"></div>
</form>
with open('dp.html') as f:
    soup = BeautifulSoup(f,'html.parser')
"""
r = requests.get('https://gihyo.jp/dp')
soup = BeautifulSoup(r.content,'html.parser')
#print(soup)

for a in soup.select('#listBook > li > a[itemprop="url"]'):
    url = urljoin('https://gihyo.jp/dp',a.get('href'))
    p = a.select('p[itemprop="name"]')[0]
    title = p.text
    print(url,title)