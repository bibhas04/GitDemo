from selenium import webdriver

validateText = "Bibhas"
driver = webdriver.Chrome(executable_path='C:\\Driver\chromedriver.exe')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.find_element_by_css_selector('#name').send_keys(validateText)
driver.find_element_by_id('alertbtn').click()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.accept()
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText
alert.dismiss()
