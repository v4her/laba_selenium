from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)
driver.get("[https://github.com](https://github.com)")

element = driver.find_element_by_id("useremail")

element.send_keys("[emailid@lambdatest.com](mailto:emailid@lambdatest.com)")

button_element = driver.find_element_by_link_text("Start Free Testing")

button_element.click()