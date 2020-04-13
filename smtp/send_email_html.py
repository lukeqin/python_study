#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# @Time : 2020/04/13 23:20
# @Email : lukeqinlu@yeah.net
# @Author : Luke
# @File : send_email_html.py
# @notice ：


import smtplib
from email.mime.text import MIMEText
from email.header import Header


mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "@qq.com"  # 用户名
mail_pass = ""  # 口令

sender = '@qq.com'
receivers = ['@qq.coms']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")