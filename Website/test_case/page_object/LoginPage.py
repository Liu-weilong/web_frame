#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/22 14:23
#@Author: liuweilong
#@File  : LoginPage.py
from BasePage import  *
from selenium.webdriver.common.by import By

class LoginPage(Page):
    url=''

    email_loc=(By.ID,'email')
    pwd_loc=(By.ID,'pwd')
    submitBtn_loc=(By.ID,'submitBtn')

    def type_username(self,email):
        self.find_element(*self.email_loc).clear()
        self.find_element(*self.email_loc).send_keys(email)

    def type_password(self,pwd):
        self.find_element(*self.pwd_loc).clear()
        self.find_element(*self.pwd_loc).send_keys(pwd)

    def type_submit(self):
        self.find_element(*self.submitBtn_loc).click()

    def Login_action(self,email,pwd):
        self.open()
        self.type_username(email)
        self.type_password(pwd)
        self.type_submit()

    loginPass_loc=(By.LINK_TEXT,'邀请有礼')
    loginFail_loc=(By.ID,'email')

    def type_loginPass_hint(self):
        return self.find_element(*self.loginPass_loc).text

    def type_loginFail_hint(self):
        return  self.find_element(*self.loginFail_loc).text


