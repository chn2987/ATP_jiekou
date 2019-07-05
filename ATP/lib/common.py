#!/usr/bin/env python
# encoding: utf-8
__author__ = "chenwei"
"""
第一步：读取excel中用例
第二步：根据用例发送请求
第三步：校验结果
第四步：将测试结果、返回报文写入excel
"""
import xlrd,requests,time,os
from xlutils import copy
from lib.log import atp_log
class OpCase(object):
    ''u'读取excel的函数'''
    def get_case(self,file_path):
        cases= []   #定义一个列表存放所有的cases
        if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
           try:
               book = xlrd.open_workbook(file_path)
               sheet = book.sheet_by_index(0)
               for i in range(1,sheet.nrows):
                   row_data = sheet.row_values(i)   #获取的每一行数据存到列表row_data
                   cases.append(row_data[4:9])#追加到cases空列表
               atp_log.info('共读取%s条用例'%(len(cases)))
               self.file_path = file_path   #因为该函数已经传了参数路径，为方便write_excel引用，在此实例化
           except Exception as e:
               atp_log.error('[%s]用例获取失败，错误信息：%s'%(file_path,e))
        else:
            atp_log.error('用例文件不合法，%s'%file_path)
        return cases
    def my_request(self,headers,url,method,data):
        ''u'根据用例发请求'''
        #print('method',method)
        #print('请求数据',data)
        data = self.dataToDict(data)#调用dataToDict，把data转成字典
        print('res=',data)
        try:
            if method.upper() == 'POST':
                #headers = {'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'}
                #res = requests.post(url, headers,data).text
                res=requests.post(url, headers=eval(headers), data=data.encode()).text#以session方式提交数据


            elif method == 'GET':
                res = requests.get(url).text
            else:
                atp_log.warning('该请求方式暂不支持')
                res = '该请求方式暂不支持'
        except Exception as e:
            msg = '【%s】接口调用失败，%s'%(url,e)
            atp_log.error(msg)
            res = msg
        return res
    def dataToDict(self,data):  #把数据转成字典。
        res = ''
        #data = data.split(',')#把字符串转成list
        res=data
        print('data字符串_转list=',data)

        # for d in data:
        #     k, v = d.split('=')#通过:分割(比如请求数据为{"code":"","title":"","status":"enable"})
        #     res[k] = v
        # print(res)
        return  res
    def check_res(self,res,check):  #res:实际结果，check：预期结果
        res = res.replace('": "','=').replace('": ','=')#这句表示是否完全匹配(注释后需要全完匹配)
        #print('res',res)#实际返回结果
        for c in check.split(','):
            print('cccc',c)
            if c not in res:
                atp_log.info('结果校验失败，预期结果：【%s】，实际结果【%s】'%(c,res))
                return '失败'
            return '成功'
    def write_excel(self,case_res):
        book = xlrd.open_workbook(self.file_path)#打开excel
        new_book = copy.copy(book)#复制
        sheet = new_book.get_sheet(0)
        row = 1
        for case_case in case_res:
            #print('case_case.....',case_case[0],case_case[1])
            if len(case_case[0]) < 32000:
                sheet.write(row,9,case_case[0])
                sheet.write(row,10,case_case[1])
                sheet.write(row,11,__author__)
            else:
                sheet.write(row,9,case_case[0][0:30000])
                sheet.write(row,10,case_case[1])
                sheet.write(row,11,__author__)

            row += 1

        new_book.save(self.file_path.replace('xlsx','报告.xls'))#用例是.xlsx，报告是.xls格式