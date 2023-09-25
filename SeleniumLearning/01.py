from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import time

driver = webdriver.chrome()
driver.get("https://www.youtube.com/")

# 放大窗口
driver.maximize_window()
    
#找输入框
driver.find_element(By.CLASS_NAME, 'classname').send_keys("输入字符")

#点击搜索
driver.find_element(By.CLASS_NAME, 'classname').click()

#隐式等待
driver.implicitly_wait(5)    
#间隔时间
time.sleep(3)

#关闭页面
driver.close()