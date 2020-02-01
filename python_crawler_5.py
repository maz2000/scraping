import time
import re
from typing import Iterator
import requests
import lxml.html
from pymongo import MongoClient


def main():
    """
    クローラーのメイン処理
    """
    #DB処理
    client = MongoClient('localhost',27017) #DBに接続
    collection = client.scraping.ebooks
    collection.create_index('key',unique=True)


    session = requests.Session() #複数のページをクロールするから
    response = requests.get('https://gihyo.jp/dp') # 1ページ目を取得
    urls = scrape_list_page(response) #書籍のURLを取得
    for url in urls: #URL毎に処理
        key = extract_key(url) #URLからキーを取得
        ebook = collection.find_one({'key': key}) #MongoDBに既にあるか？
        if not ebook:

            time.sleep(1) #1秒に一回処理
            response = session.get(url) #詳細ページを取得
            ebook = scrape_detail_page(response) #詳細ページをスクレイプ
            collection.insert_one(ebook) #DBに追加
            print(ebook)
        #break #とりあえず1ページのみ処理して終了
    
def scrape_list_page(response: requests.Response) -> Iterator[str]:
    """
    一覧から詳細ページのURLを抽出
    """

    html = lxml.html.fromstring(response.text)
    html.make_links_absolute(response.url)

    for a in html.cssselect('#listBook > li > a[itemprop="url"]'):
        url = a.get('href')
        yield url

def scrape_detail_page(response: requests.Response) -> dict:
    """
    詳細ページの情報をdictで取得
    """

    html = lxml.html.fromstring(response.text)
    ebook = {
        'url' : response.url,
        'key' : extract_key(response.url),
        'title' : html.cssselect('#bookTitle')[0].text_content(),
        'price' : html.cssselect('.buy')[0].text.strip(),
        'content' : [normalize_spaces(h3.text_content()) for h3 in html.cssselect('#content > h3')],
    }
    return ebook

def extract_key(url: str) -> str:
    """
    URLからキー(末尾のISBN)を抜き出す
    """
    m = re.search(r'/([^/]+)$',url) #最後の/から文字列末尾までを正規表現で取得
    return m.group(1)


def normalize_spaces(s: str) -> str:
    """
    連続する空白を1つのスペースに置き換え前後の空白を削除した新しい文字列を取得する
    """
    return re.sub(r'\s+', ' ',s).strip()


if __name__ == '__main__':
    main()

