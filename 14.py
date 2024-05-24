from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)
driver.get("[https://github.com](https://github.com)")

alert_obj = driver.switch_to.alert
alert_obj.accept()
msg = alert_obj.text()
print(msg)

page_source = driver.page_source