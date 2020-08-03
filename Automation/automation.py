from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver.exe')

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

button_text = chrome_browser.find_element_by_class_name('btn-default')
print(button_text.get_attribute('innerHTML'))

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('Alonso Padre')

button_text.click()

output_message = chrome_browser.find_element_by_id('display')

assert 'Alonso Padre' in output_message.text

chrome_browser.close()