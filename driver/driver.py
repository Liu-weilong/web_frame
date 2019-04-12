#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/22 10:12
#@Author: liuweilong
#@File  : driver.py
from selenium import webdriver
from time import sleep
def browser():
    driver = webdriver.Firefox()
    driver.maximize_window()
    # driver.get('https://www.testin.cn/account/login.htm')
    # sleep(3)
    # driver.quit()
    return driver

if __name__ == '__main__':
    browser()
