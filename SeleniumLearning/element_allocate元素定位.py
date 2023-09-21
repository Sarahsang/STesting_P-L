from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' id 定位
因为唯一性, id是很直接快速的, 但是很多情况下没办法用id定位
id定位底层是从CSS查找
善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

#窗口最大化
driver.maximize_window()

#element = driver.find_element(By.ID, "kw")
#element.send_keys("selenium")
#优化 直接跟send_keys或click
driver.find_element(By.ID, "kw").send_keys("selenium")

driver.find_element(By.ID, "su").click()

#sleep在做调试时特别有用
sleep(3)

#加不加都会关闭 但是代码完整性
driver.quit()