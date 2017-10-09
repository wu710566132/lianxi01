#-*- coding:utf-8 -*-

from util import urlutil,firefox

class Login(object):

    def __init__(self):

        #实例化打开浏览器
        self.firefox = firefox.FireFox()
        #实例化url
        self.URL = urlutil.URL()

        pass

    #打开登录页面
    def loginStart(self):

        #面向对象的思想
        self.firefox.startFireFox(self.URL.JD_LOGIN)
        pass

    #关闭页面
    def loginClose(self):
        #关闭浏览器
        self.firefox.closeFireFox()
        pass

    #点击用户登录，输入内容
    def loginClickAccount(self,self1):

        self.firefox.FindClass("login-tab-r").click()
        self.firefox.FindID("loginname").send_keys("")
        self.firefox.FindID("nologinpwd").send_keys("")
        self.firefox.FindClass("loginsubmit").click()

        #查找出显示出来的控件
        self.msg_error = self.firefox.FindClass("msg-error")

        #获取内容
        message = self.msg_error.text

        #进行断言
        self1.assertEqual(message,u"请输入账户名和密码")

        pass