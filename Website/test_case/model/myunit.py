#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/22 10:27
#@Author: liuweilong
#@File  : myunit.py
import unittest2
from driver import *
class StartEnd(unittest2.TestCase):
    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        #self.driver.get('https://www.testin.cn/account/login.htm')

    def tearDown(self):
        self.driver.quit()








