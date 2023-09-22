from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位

''' css selector 定位
通过css样式选择器去定位
用的比较多 因为id或者name等不一定有
id用# class用.
善用inspect

'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
# driver.get("https://www.bilibili.com")

#窗口最大化
driver.maximize_window()

#css selector
# 根据id属性定位 加#
# driver.find_element(By.CSS_SELECTOR, "#kw").send_keys("selenium")
# driver.find_element(By.CSS_SELECTOR, "#su").click()

# Class 属性值进行定位 加.
# driver.find_element(By.CSS_SELECTOR, '.nav-search-input').send_keys('selenium')

# name 属性值进行定位 其他属性值也是可以这样定位的
# driver.find_element(By.CSS_SELECTOR, '[name="wd"]').send_keys("selenium")

# 标签（href） 属性值进行定位
driver.find_element(By.CSS_SELECTOR, 'a[href="http://image.baidu.com/"]').click()
# 模糊匹配-包含*
driver.find_element(By.CSS_SELECTOR, 'a[href*="image.baidu.com"]').click()
# 模糊匹配-匹配开头^
driver.find_element(By.CSS_SELECTOR, 'a[href^="http://image.baidu"]').click()
# 模糊匹配-匹配结尾$
driver.find_element(By.CSS_SELECTOR, 'a[href$="image.baidu.com/"]').click()

#组合定位 标签+classname
# input+name
driver.find_element(By.CSS_SELECTOR, 'input[name="wd"]').send_keys("软件测试老白")
# input+class
driver.find_element(By.CSS_SELECTOR, 'input.s_ipt').send_keys("软件测试老白")

#sleep在做调试时特别有用
sleep(8)

#加不加都会关闭 但是代码完整性
driver.quit()