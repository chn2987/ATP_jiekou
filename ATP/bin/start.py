#!/usr/bin/env python
# encoding: utf-8
__author__ = "晨晨"
import os,sys,time
BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
sys.path.insert(0,BASE_PATH)

from lib.common import OpCase
from lib.mail_2 import mail
from lib.send_mail import sendmail
from conf import setting
class CaseRun(object):

    def find_case(self):
        op = OpCase()
        for f in os.listdir(setting.CASE_PATH): #每次循环的时候读一个excel
            if f !='测试用例 .xlsx':
                continue
            abs_path = os.path.join(setting.CASE_PATH,f)
            case_list = op.get_case(abs_path)#测试用例列表
            res_list = []
            pass_count,fail_count= 0,0
            for case in case_list:  #循环每一个excel里面的所有用例
                headers,url,method,req_data,check = case
                res = op.my_request(headers,url,method,req_data)    #调用完接口返回的结果
                print('接口返回结果',res)
                status = op.check_res(res,check)#调用校验函数
                #print('状态',status)
                res_list.append([res,status])#把接口结果，校验结果写入res_list
                if status == '成功':
                    pass_count += 1
                else:
                    fail_count += 1
            print('通过1111',pass_count)
            print('失败2222',fail_count)
            op.write_excel(res_list)
        msg = '''
        测试大佬你好！
            本次共运行%s条用例，通过%s条，失败%s条111111111。
        '''%(len(res_list),pass_count,fail_count)
        sendmail('测试用例运行结果',content=msg,attrs='D:\dalan\ATP\cases\测试用例 .报告.xls')
        #mail('测试用例运行结果',msg,'D:\dalan\ATP\cases\测试用例 .报告.xls')
        print('f===',f)

CaseRun().find_case()

