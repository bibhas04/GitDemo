from selenium import webdriver
# Every browser exposes an executable file
# Through Selenium test we need to invoke the executable file which will then invoke the actual browser
driver = webdriver.Chrome(executable_path='C:\\Driver\chromedriver.exe')
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/#/index")  #get method is used to hit the url on browser
print(driver.title)  #get the title of the page
print(driver.current_url)  #get the current URL
driver.get("https://courses.rahulshettyacademy.com/courses")
driver.minimize_window()
driver.back()
driver.close()  #this will close the current / single tab only
