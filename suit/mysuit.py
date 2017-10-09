#-*- coding:utf-8 -*-

import unittest
from unit import login
import HTMLTestRunner
import os

#实例化套件
suit = unittest.TestSuite()

#加入单元测试
suit.addTest(unittest.makeSuite(login.LoginJd))

#指定路径
files = os.getcwd() + "/jd.html"
#指定读写方式 wb 以二进制的方式 只写rb 以二进制方式只读 rb+ 二进制的方式可读可写
filename = open(files,"wb")

#运行单元测试
runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title=u"京东",description=u"登录")
runner.run(suit)
