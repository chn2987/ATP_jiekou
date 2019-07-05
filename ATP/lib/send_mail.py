#!/usr/bin/env python
# encoding: utf-8


__author__ = "晨晨"
import yagmail
import os
from email.mime.image import MIMEImage
from conf import setting
from lib.log import atp_log
def sendmail(title,content,attrs=None):
    m = yagmail.SMTP(host=setting.MAIL_HOST,user=setting.MAIL_USER,
                 password=setting.MAIL_PASSWRD,smtp_ssl=False)

    m.send(to=setting.TO,
           subject=title,
           contents = content,
           attachments =attrs)

    atp_log.info('发送邮件完成')