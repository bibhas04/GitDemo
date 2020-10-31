from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certification-errors")
driver = webdriver.Chrome(executable_path='C:\\Driver\chromedriver.exe', options= chrome_options)

driver.get("https://www.rahulshettyacademy.com/angularpractice/")
print(driver.title)