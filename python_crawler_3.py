#一件だけ取得するコード

from typing import Iterator
import requests
import lxml.html

def main():
    """
    クローラーのメイン処理
    """
    session = requests.Session() #複数のページをクロールするから
    response = requests.get('https://gihyo.jp/dp') # 1ページ目を取得
    urls = scrape_list_page(response) #書籍のURLを取得
    for url in urls: #URL毎に処理
        response = session.get(url) #詳細ページを取得
        ebook = scrape_detail_page(response) #詳細ページをスクレイプ
        print(ebook)
        break #とりあえず1ページのみ処理して終了
    
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
        'title' : html.cssselect('#bookTitle')[0].text_content(),
        'price' : html.cssselect('.buy')[0].text.strip(),
        'content' : [h3.text_content() for h3 in html.cssselect('#content > h3')],
    }
    return ebook



if __name__ == '__main__':
    main()

