from selenium import webdriver
from selenium.webdriver.common.by import By

# 元素定位

''' id 定位
因为唯一性, id是很直接快速的, 但是很多情况下没办法用id定位
善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")
element = driver.find_element(By.ID, "kw")
element.send_keys("selenium")
driver.quit()