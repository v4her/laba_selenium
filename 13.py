from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)
driver.get("[https://github.com](https://github.com)")

driver.switch_to_frame("frame_name.0.child")
driver.switch_to_default_content()