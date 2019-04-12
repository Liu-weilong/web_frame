#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/22 14:49
#@Author: liuweilong
#@File  : test_login.py
import unittest2
from model import function,myunit
from page_object.LoginPage import *
from time import sleep

class LoginTest(myunit.StartEnd):
    def test_login1_normal(self):
        print('test start ...')
        po = LoginPage(self.driver)
        sleep(5)
        po.Login_action('15256750385','lwl0909///')
        sleep(3)

        self.assertEqual(po.type_loginPass_hint(),'邀请有礼')
        function.insert_img(self.driver,'normal.png')
        print('test login success')

    def test_login2_PasswdError(self):
        print('test start ...')
        po = LoginPage(self.driver)
        sleep(5)
        po.Login_action('15256750385','123456')
        sleep(3)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'PasswdError.png')
        print('test login error')

    def test_login3_empty(self):
        print('test statrt ...')
        po = LoginPage(self.driver)
        sleep(5)
        po.Login_action('','')
        sleep(3)

        self.assertEqual(po.type_loginFail_hint(),'')
        function.insert_img(self.driver,'empty.png')
        print('test login empty')

if __name__ == '__main__':
    unittest2.main()
