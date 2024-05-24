from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)
driver.get("[https://github.com](https://github.com)")

cookie = {'name' : 'user', 'value' : 'vinayak'}
driver.add_cookie(cookie)
driver.get_cookies()

driver.delete_cookie(cookie)
driver.delete_all_cookies()