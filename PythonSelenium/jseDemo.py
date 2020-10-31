# Javascript DOM can access any elements on the webpage just like selenium does
# Selenium have a method to execute javascript code in it
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Driver\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("Hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script("return document.getElementsByName('name')[0].value"))
shop = driver.find_element_by_css_selector("a[href*=shop]")
driver.execute_script("arguments[0].click();", shop)
# Interview Ques:  Selenium does not have the feature to scroll down a page
# But this can be done only through javascript
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")