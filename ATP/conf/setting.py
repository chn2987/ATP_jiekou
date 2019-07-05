#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import os
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)   #三层目录定位到ATP目录
MAIL_HOST = 'smtp.qq.com'
MAIL_USER='646572031@qq.com'
MAIL_PASSWRD = 'ufxuoifkuvutbcij'
TO = [

]
LEVEL = 'debug' #设置日志默认级别

LOG_PATH = os.path.join(BASE_PATH,'logs')   #日志文件在logs目录下
CASE_PATH = os.path.join(BASE_PATH,'cases') #用例文件在cases目录下
LOG_NAME = 'atp_log'    #设置日志文件名