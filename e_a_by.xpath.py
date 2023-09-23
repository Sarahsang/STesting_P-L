from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位 https://www.yuque.com/bingo1234/hbgurf/obb2lzhcvf6345vr 

''' XPATH 定位 
XML
善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# driver.get("https://www.bilibili.com")

# 定位百度首页的新闻 绝对路径 很麻烦
driver.find_element(By.XPATH, '/html/body/div/div/div[3]/a')

#使用id属性定位
driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys("软件测试老白")

# class中间有空格，需要全部写上
driver.find_element(By.XPATH, '//a[@class="mnav c-font-normal c-color-t"]').click()

#窗口最大化
driver.maximize_window()

#css selector
# 
#sleep在做调试时特别有用
sleep(8)

#加不加都会关闭 但是代码完整性
driver.quit()