from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

chrome_options = Options()
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(options=chrome_options)
driver.get("[https://github.com](https://github.com)")

select = Select(driver.find_element_by_id('city'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)

driver.switch_to_window("window_handle")
for handle in driver.window_handles:
    driver.switch_to_window(handle)
    handler = driver.current_window_handle