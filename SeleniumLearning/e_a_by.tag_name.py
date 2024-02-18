from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' tag name 标签定位
先确认标签是不是唯一的 console--document.getElementsByTagName("标签名")
当有不止一个元素的tag name相同时, 由于find_element是单数只返回第一个值 如果想返回其他值需要使用列表下标
善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com")

#窗口最大化
driver.maximize_window()

#唯一的input tag name
driver.find_element(By.TAG_NAME, "input").send_keys("selenium")

#多个 tag name 不建议，太多了
driver.find_elements(By.CLASS_NAME, "input")[50].click()

#sleep在做调试时特别有用
sleep(3)

#加不加都会关闭 但是代码完整性
driver.quit()