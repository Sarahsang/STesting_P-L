from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 元素定位 https://www.yuque.com/bingo1234/hbgurf/obb2lzhcvf6345vr 

''' XPATH 定位 
XML
善用inspect
从根节点开始选取(绝对路径)	/html/div/
从任意节点开始选取(相对路径)	//div，列举出所有div标签
选取当前节点的父节点	//input/.. 会选取 input 的父节点
选取属性，或者根据属性选取	
使用id属性定位	//div[@id='id_value']
使用class属性定位	//a[@class="mnav"]
使用name属性定位	//div[@name='wd']
多个属性定位	//input[@name="wd" and @class="s_ipt"]
第n个元素，使用index定位	//div[@id="s-top-left"]/a[3]
最后一个元素	//a[@class="mnav"][last()]
属性包含某字段	//div[contains(@title,'text')]
属性以某字段开头	//div[starts-with(@title,'text')]
属性以某字段结尾	//div[ends-with(@title,'text')]
文本包含	//a[contains(text(),"网盘")]
文本等于	//span[text() = "菜单"]
同级弟弟元素	//div[@id=='id']/following-sibling::div
同级哥哥元素	//div[@id=='id']/preceding-sibling::div
'''

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# driver.get("https://www.bilibili.com")

# 定位百度首页的新闻 绝对路径 很麻烦
driver.find_element(By.XPATH, '/html/body/div/div/div[3]/a')

#使用id属性定位
driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys("软件测试老白")

# class中间有空格，需要全部写上
driver.find_element(By.XPATH, '//a[@class="mnav c-font-normal c-color-t"]').send_keys("软件测试老白")

#根据name属性定位
driver.find_element(By.XPATH, '//input[@name="wd"]').send_keys("软件测试老白")

#多个属性组合定位 用and 或 or
driver.find_element(By.XPATH, '//input[@name="wd" and @class="s_ipt"]').send_keys("软件测试老白")

#多组数据使用下标定位
driver.find_element(By.XPATH, '//div[@id="s-top-left"]/a[3]').click()

#由子元素定位父元素 ..代表上一层
driver.find_element(By.XPATH, '//input[@id="kw"]/..')

#根据文本内容定位 
driver.find_element(By.XPATH, '//a[contains(text(),"网盘")]') 

# 最后一个子元素,last()
driver.find_element(By.XPATH, '//a[@class="mnav c-font-normal c-color-t"][last()]') 

#动态ID
https://element.eleme.cn/#/zh-CN/component/cascader
driver.find_element(By.XPATH, '//span[text() = "默认 click 触发子菜单"]/following-sibling::div/div/input') 



#窗口最大化
driver.maximize_window()

#css selector
# 
#sleep在做调试时特别有用
sleep(8)

#加不加都会关闭 但是代码完整性
driver.quit()