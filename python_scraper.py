import csv
from typing import List

import requests
import lxml.html


def maiin():
    """
    メイン処理
    """

    url = 'https;//gihyo.jp/dp'
    html = fetch(url)
    books = scrape(html,url)
    save(books.csv,books)

def fetch(url:str) -> str:
    """
    Webページ取得
    """

    r = requests.get(url)
    return r.text

def scrape(html: str, base_url: str) -> List[dict]:
    """
    書籍情報の抽出
    """

    book = []
    html = lxml.html.fromstring(html)
    html.make_links_abspolute(base_url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        p = a.cssselect('p[itemprop="name"]')[0]
        title = p.text_content()

        books.append({'url': url,'title': title})
    return books

def save(file_path: str, books: List[dict]):


    with open(file_path, 'w', newline='') as f:
        writer = csv.DictWriter(f,['url','title'])
        writer.writer()
        writer.writerows(books)

if __name__ == '__main__':
    main()



