from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\Python\scraping\chromedriver\chromedriver.exe")
driver.get("http://www.yahoo.co.jp")

elem_search_word = driver.find_element_by_name("p")
elem_search_word.send_keys("selenium")
elem_search_word.send_keys(Keys.RETURN)

"""
elem_search_btn = driver.find_element_by_class_name("_63Ie6douiF2dG_ihlFTen")
elem_search_btn.click()
"""