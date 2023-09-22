from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' css selector 定位
定位子元素 一般根据最近一个id属性往下找, 可以根据class或者标签
善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# driver.get("https://www.bilibili.com")

# 百度首页新闻，以下三种方式皆可
driver.find_element(By.CSS_SELECTOR, 'div.s-top-left-new.s-isindex-wrap a' ) # 根据class
driver.find_element(By.CSS_SELECTOR, 'div#s-top-left a') # 根据id
driver.find_element(By.CSS_SELECTOR, '#s-top-left a') # 简写
# 百度首页地图，以下2种方式皆可
driver.find_element(By.CSS_SELECTOR, '#s-top-left a:nth-child(3)') 
driver.find_elements(By.CSS_SELECTOR, '#s-top-left a')[2] 

# a:first-child 第一个标签
driver.find_element(By.CSS_SELECTOR, '#s-top-left a:first-child')
# a:last-child 最后一个标签
driver.find_element(By.CSS_SELECTOR, '#s-top-left a:last-child')


#窗口最大化
driver.maximize_window()

#css selector
# 
#sleep在做调试时特别有用
sleep(8)

#加不加都会关闭 但是代码完整性
driver.quit()