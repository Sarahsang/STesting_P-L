from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' name 名字定位
先确认name是不是唯一的 不建议使用不一定有 且不一定唯一
善用inspect
'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

#窗口最大化
driver.maximize_window()

#看框架有没有name属性
driver.find_element(By.NAME, "wd").send_keys("根据name属性定位")
#多个
driver.find_elements(By.NAME, "wd")[3].send_keys("根据name属性定位")

#sleep在做调试时特别有用
sleep(3)
#加不加都会关闭 但是代码完整性
driver.quit()