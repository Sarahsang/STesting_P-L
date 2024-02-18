from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

'''link_text 和partial_link_text 可点击的文本链接定位
找到可点击链接 
善用inspect
'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 窗口最大化
driver.maximize_window()

#精确定位
driver.find_element(By.LINK_TEXT, "新闻").click()
# 多个
driver.find_elements(By.LINK_TEXT, "新闻")[0].click()

#模糊链接定位 注意只包含链接
driver.find_element(By.PARTIAL_LINK_TEXT, "新闻").click()
# 多个
driver.find_elements(By.PARTIAL_LINK_TEXT, "新闻")[0].click()

# sleep在做调试时特别有用
sleep(10)
# 加不加都会关闭 但是代码完整性
driver.quit()