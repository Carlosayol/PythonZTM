from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://www.youtube.com/watch?v=bukj28Mt0Zc&t=63s')

editable_text = chrome_browser.find_element_by_id("contenteditable-root")
print(editable_text.get_attribute('innerHTML'))