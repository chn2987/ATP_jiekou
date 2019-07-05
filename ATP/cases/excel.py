#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xlrd,json
import x_excel
def excel_hang():
    u''''读取excel所有行数据'''
    list=x_excel.du_excel()#调用excel拆分及重写方法
    x_excel.data_write('转换后的文件.xls', list)
    a=[ 't_id','t_name', 't_url', 't_method', 't_param','t_actual', 't_hope', 't_result']
    book = xlrd.open_workbook('转换后的文件.xls')
    sheet = book.sheet_by_index(0)
    rows = sheet.nrows#获取所有行
    #print (sheet.row_values(2))#打印指定行的值
    case_list = []
    chen={"info": [], "test_sum": 100,"test_success": 20, "test_failed": 80}
    for i in range(0,rows):#遍历所有行，并把行的数据传到case_list
        case_list.append(sheet.row_values(i))
        #print('每一行数据',sheet.row_values(i))
        dic3 = dict(zip(a,sheet.row_values(i)))
        #case_list.append(sheet.row_values(i))
        chen["info"].append(dic3)
        #print(dic3)
        #print('\n')
    print(chen)
    return chen
#excel_hang()




