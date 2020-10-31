from selenium import webdriver

list = []
driver = webdriver.Chrome(executable_path="C:\\Driver\chromedriver.exe")
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')
driver.find_element_by_xpath("//form[@class='search-form']/input").send_keys("Ber")
veggies = driver.find_elements_by_xpath("//div[@class='product']/h4")
for v in veggies:
    list.append(v.text)

print(list)
count = len(list)
assert count == 3
