import re
from html import unescape
from urllib.parse import urljoin

with open('dp.html',encoding='utf-8_sig') as f:
    html = f.read()

#print(html)


for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>',html,re.DOTALL):
    print(partial_html)
    print('------')
    url = re.search(r'<a itemprop="url" href="(.*?)">',partial_html).group(1)
    url = urljoin('http://gijyo.jp/',url)
    title = re.search(r'<p itemprop="name".*?</p>',partial_html).group(0)
    title = title.replace('<br/>',' ')
    title = re.sub(r'<.*?>','',title)
    title = unescape(title)

    print(url,title)

#コメント追加
