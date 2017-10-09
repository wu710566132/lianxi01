#-*- coding:utf-8 -*-
import unittest
# 导入selenium包
from selenium import webdriver
# 2.0 版本在 setU盘class里面实例化工具类
from util import firefox,urlutil

# 声明类 集成 单元测试 case
class LoginJd(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        # 实例化打开浏览器
        self.firefox = firefox.FireFox()
        # 实例化url
        self.URL = urlutil.URL()

        pass

    def setUp(self):

        # 面向对象的思想
        self.firefox.startFireFox(self.URL.JD_LOGIN)

        pass


    def tearDown(self):

        # 关闭浏览器
        self.firefox.closeFireFox()

        pass

    def test_us_pw(self):

        self.firefox.FindClass("login-tab-r").click()
        self.firefox.FindID("loginname").send_keys("")
        self.firefox.FindID("nloginpwd").send_keys("")
        self.firefox.FindID("loginsubmit").click()

        # 查找显示出来的控件
        self.msg_error = self.firefox.FindClass("msg-error")

        # 获取内容
        message = self.msg_error.text

        # 进行断言
        self.assertEqual(message,u"请输入账户名和密码")

        pass