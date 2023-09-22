from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' tag name 定位

善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")

#窗口最大化
driver.maximize_window()

#element = driver.find_element(By.ID, "kw")
#element.send_keys("selenium")
#优化 直接跟send_keys或click
# driver.find_element(By.CLASS_NAME, "nav-search-input").send_keys("selenium")
# driver.find_element(By.CLASS_NAME, "nav-search-btn").click()

#如何在class name相同的情况下定位元素 find_elements 并且加列表的序列
driver.find_elements(By.CLASS_NAME, "channel-link")[4].click()

#如何看该class name下的链接名称
for ele in driver.find_elements(By.CLASS_NAME, "channel-link"):
    print(ele.text)

#sleep在做调试时特别有用
sleep(3)

#加不加都会关闭 但是代码完整性
driver.quit()