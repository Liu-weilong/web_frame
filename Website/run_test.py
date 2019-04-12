#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/22 16:32
#@Author: liuweilong
#@File  : run_test.py
import unittest2
from function import *
from BSTestRunner import BSTestRunner
import time
import logging

report_dir = './test_report'
test_dir = './test_case'
print('statr run ...')
discovery = unittest2.defaultTestLoader.discover(test_dir,pattern='test_login.py')#匹配文件执行
now = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = report_dir + '/' + now + 'result.html'
#logging.basicConfig(filename='./test_log/run.log',level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d]%(levelname)s%(message)s')
logging.basicConfig(filename='./test_log/run.log',level=logging.DEBUG,format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')

print('start write report ...')
with open(report_name,'wb') as f:
    runner = BSTestRunner(stream=f,title='Test Report',description='login test')
    runner.run(discovery)
    f.close()
print('find latest report')
latest_report = latest_report(report_dir)
#send_mail(latest_report)
print('Test send success')
#由于邮件发送涉及到中文  修改BSTestRunner 120行 return unicode(s)  改为 str(s)











