from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' css selector 定位
用的比较多 因为id或者name等不一定有
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