#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import logging,os
from logging import handlers
from conf import setting
class Mylogger():
    def __init__(self,file_name,level='info',backCount=5,when='D'):
        logger = logging.getLogger()  # 先实例化一个logger对象，先创建一个办公室
        logger.setLevel(self.get_level(level))  # 设置日志的级别
        #f1 = logging.FileHandler(filename='a.log',mode='a',encoding='utf-8')    #找到写日志文件的这个人
        c1 = logging.StreamHandler()  # 负责往控制台输出的
        b1 = handlers.TimedRotatingFileHandler(filename=file_name, when=when, interval=1, backupCount=backCount, encoding='utf-8')
        fmt = logging.Formatter('%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        c1.setFormatter(fmt)
        b1.setFormatter(fmt)
        logger.addHandler(c1)
        logger.addHandler(b1)
        self.logger = logger
    def get_level(self,str):
        level = {
            'debug':logging.DEBUG,
            'info':logging.INFO,
            'warm':logging.WARNING,
            'error':logging.ERROR
        }
        str = str.lower()
        return level.get(str)

path = os.path.join(setting.LOG_PATH,setting.LOG_NAME)
atp_log = Mylogger(path,'debug').logger
#直接在这里实例化，用的时候不用再实例化了
#别的地方用的时候，直接atp_log.warnning('xxxx')