#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/3/22 10:35
#@Author: liuweilong
#@File  : function.py
from selenium import webdriver
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


def insert_img(driver,filename):
    func_path = os.path.dirname(__file__)
    base_dir = os.path.dirname(func_path)

    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/') #转译
    base = base_dir.split('/Website')[0] #
    filepath = base + '/Website/test_report/screenshot/' + filename
    driver.get_screenshot_as_file(filepath) #截图

def send_mail(latest_report):
    f = open(latest_report,'rb')
    mail_content  = f.read()
    f.close()

    smtpsever = "smtp.qq.com"
    user = '1711365301@qq.com'
    password = 'nudlwzanxurqdgaa'
    sender = "1711365301@qq.com"
    reveivers = ['1431235234@qq.com','1726470924@qq.com']

    subject = 'Web Selenium 自动化测试报告'
    #content = '<html><h1>这是测试python一个邮件的发送类</h1></html>'
    msg = MIMEText(mail_content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    msg['From'] = sender
    msg['To'] = '.'.join(reveivers)

    smtp = smtplib.SMTP_SSL(smtpsever, 465)
    smtp.helo(smtpsever)
    smtp.ehlo(smtpsever)
    smtp.login(user, password)

    print('正在发送中...')
    smtp.sendmail(sender, reveivers, msg.as_string())
    smtp.quit()
    print('发送成功...')


def latest_report(report_dir):
    lists = os.listdir(report_dir)
    print(lists)

    lists.sort(key=lambda fn:os.path.getatime(report_dir + '\\' + fn))
    print('the latest report is' + lists[-1])
    file = os.path.join(report_dir,lists[-1])
    return file



if __name__ == '__main__':
    #insert_img()
    driver = webdriver.Firefox()
    driver.get('https://www.testin.cn/account/login.htm')
    insert_img(driver,'yunce.png')
    driver.quit()

