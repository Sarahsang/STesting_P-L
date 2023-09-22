from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' classname 定位
当有不止一个元素的classname相同时, 由于find_element是单数 只返回第一个值 如果想返回其他值需要
使用列表下标
注意: 一个链接可能使用多个class name,  要注意有空格的class name不能用来元素定位, 会报错
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