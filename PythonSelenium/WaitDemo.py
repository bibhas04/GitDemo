import time
from selenium import webdriver
#Implicit Wait
#Explicit Wait
#Pause the test for few seconds using Time class

driver = webdriver.Chrome(executable_path='C:\\Driver\chromedriver.exe')
driver.implicitly_wait(5)
# wait until 5 seconds
# Global wait means it will wait for every page
# 2 seconds to reach next page - execution will resume in 2 seconds
# if object do not show at all, then max time your test waits for 5 seconds
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_css_selector('input.search-keyword').send_keys('ber')
time.sleep(4)
count=len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

for b in buttons:
    b.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
