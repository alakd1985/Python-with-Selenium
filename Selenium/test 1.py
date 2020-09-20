from selenium import webdriver
from selenium.webdriver.common import by

driver = webdriver.Chrome(executable_path="D:\\Jarfile\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element_by_name("q").send_keys("alak")
#driver.find_element_by_xpath("//div[@class='FPdoLc tfB0Bf']//input[@name='btnK']")
#driver.close()
