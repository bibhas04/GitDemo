import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:\\Driver\chromedriver.exe')
driver.get('https://www.rahulshettyacademy.com/dropdownsPractise/')
driver.find_element_by_id('autosuggest').send_keys('ind')
# it will wait for 2 seconds
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break

assert driver.find_element_by_id('autosuggest').get_attribute('value') == 'India'
