from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
list2 = []
driver = webdriver.Chrome(executable_path='C:\\Driver\chromedriver.exe')
driver.get("https://www.rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector('a[href*=shop]').click()
products = driver.find_elements_by_css_selector('.card-title a')
i = -1
for product in products:
    productName = product.text
    i = i + 1
    if productName == "Blackberry":
        list.append(productName)
        print(list)
        #Add item to cart
        product.find_elements_by_xpath('//div[2]/button')[i].click()

driver.find_element_by_css_selector('a[class*="nav-link btn btn-primary"]').click()
Result = driver.find_element_by_xpath('//div[@class="media-body"]/h4/a').text
list2.append(Result)
print(list2)
assert list == list2

driver.find_element_by_xpath('//button[@class="btn btn-success"]').click()
driver.find_element_by_id('country').send_keys("Ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, 'India')))
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath('//div[@class="checkbox checkbox-primary"]').click()
driver.find_element_by_css_selector('[type="submit"]').click()
successText = driver.find_element_by_class_name('alert-success').text

assert "Success! Thank you!" in successText
driver.get_screenshot_as_file("screen.png")
