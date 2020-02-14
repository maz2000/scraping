from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome('D:\Python\scraping\chromedriver\chromedriver.exe',chrome_options=options)
driver.get('https://www.yahoo.co.jp')

assert 'Yahoo' in driver.title

elem_search_word = driver.find_element_by_name('p')
elem_search_word.clear()
elem_search_word.send_keys('Python')
elem_search_word.send_keys(Keys.RETURN)

assert 'Python' in driver.title

for a in driver.find_elements_by_css_selector('.w .hd a'):
    print(a.text)
    print(a.get_attribute('href'))

# 終了処理
driver.close()
