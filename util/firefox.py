#-*- coding:utf-8 -*-
# 打包
from selenium import webdriver

# 导入休眠包
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# 声明类继承object
class FireFox(object):

    # 打开浏览器的方法
    def startFireFox(self,url):
        # 打开浏览器x
        self.driver = webdriver.Firefox()
        # 设置最大化
        self.driver.maximize_window()
        # 打开指定网页
        self.driver.get(url)
        # 设置休眠
        self.driver.implicitly_wait(5)
        pass

    # 关闭浏览器
    def closeFireFox(self):

        self.driver.quit()

        pass

    def  TimeImplay(self,number):

        self.driver.implicitly_wait(number)
        pass

    # 通过 id 和 class 查找控件
    def FindID(self,ID):

        # 设置休眠
        ids = (By.ID, ID)

        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(ids))

        return self.driver.find_element_by_id(ID)

    def FindClass(self, clss):
        # 设置休眠
        cls = (By.CLASS_NAME, clss)

        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(cls))

        return self.driver.find_element_by_class_name(clss)






