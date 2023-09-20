from selelnium import webdriver

driver = webdriver.chrome()
driver.get("https://www.youtube.com/")

#找输入框
driver.find_element(By.CLASS_NAME, 'classname').send_keys("输入字符")