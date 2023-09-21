from selelnium import webdriver
from selenium.webdriver.common.by import By

# 元素定位

''' id 定位
善用inspect

'''

driver = webdriver.chrome()
driver.get("https://www.youtube.com")
element = driver.find_element(By.ID, "search")
element.send_keys("selenium")
driver.quit()