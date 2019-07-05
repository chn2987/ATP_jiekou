#!/usr/bin/env python
# encoding: utf-8
import numpy as np
import xlrd,xlwt,time
import xlsxwriter
#__________________________________读取指定的excel行与列_____________________________________________________
def du_excel():
    data = xlrd.open_workbook('测试用例 .报告.xls')
    table = data.sheets()[0]#当前位于的sheet
    rows = table.nrows#获取行数
    start=1  #开始的行
    end=rows  #结束的行
    rows=end-start
    list_values=[]#存放读取的数据
    for x in range(start,end):#控制行
        values=[]
        row =table.row_values(x)
        for i in range(2,11):#控制列
            if i !=4:
                values.append(row[i])
        list_values.append(values)
        print( list_values,'\n')
    #print(list_values)#列表显示筛选后的数据
    return list_values
    # # datamatrix=np.array(list_values)
    # # print(datamatrix)
#——————————————————————写excel——————————————————————————————
#————————普通写入
# newcols=[['用例id', '用例描述', '请求url', '请求方式', '请求数据', '预期结果', '实际返回', '测试结果'], ['login_3', '正常登录', 'http://sso.newtest1.51dinghuo.cc/api/loginpost', 'POST', 'username=missy&password=8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92', '{"code":200,"desc":"登录成功!,但没有返回地址,故不跳转"}', '{"code":200,"desc":"登录成功!,但没有返回地址,故不跳转"}', '成功'], ['login_1', '正常获取信息', 'http://47.106.143.23:8000/login', 'GET', '', '{"rows": [{"city": "440100", "mdq_releasecirclename": "null", "mdq_picturepathilist": [{"path": "res/def/import/2019609s/TP/69.jpg", "key": "543023842088790045840454", "pit_pubtime": "null"}, {"path": "res/def/import/2019609s/TP/70.jpg", "key": "423199552434820045840454", "pit_pubtime": "null"}], "mdq_releasecoordinate": [113.337451, 23.094988], "area": "440105", "country": "100000", "mdq_createtime": "2019-06-09 10:04:00", "_id": "5cfc69101f089c1ae66b2c8d", "createtime": "第一个", "mdq_businesscirclename": "广东省广州市天河区科韵路建业路3303号"}], "code": "3", "errmsg": "操作成功"}', '{"rows": [{"city": "440100", "mdq_releasecirclename": "null", "mdq_picturepathilist": [{"path": "res/def/import/2019609s/TP/69.jpg", "key": "543023842088790045840454", "pit_pubtime": "null"}, {"path": "res/def/import/2019609s/TP/70.jpg", "key": "423199552434820045840454", "pit_pubtime": "null"}], "mdq_releasecoordinate": [113.337451, 23.094988], "area": "440105", "country": "100000", "mdq_createtime": "2019-06-09 10:04:00", "_id": "5cfc69101f089c1ae66b2c8d", "createtime": "1天前", "mdq_businesscirclename": "广东省广州市天河区科韵路建业路3303号"}], "code": "0", "errmsg": "操作成功"}', '成功']]
# # workbook = xlsxwriter.Workbook('result.xlsx')  #生成表格
# # worksheet = workbook.add_worksheet(u'sheet1')   #在文件中创建一个名为TEST的sheet,不加名字默认为sheet1
# # worksheet.set_column('A:A',20)  #设置第一列宽度为20像素
# # bold=workbook.add_format({'bold':True}) #设置一个加粗的格式对象
# # for i in range(len(newcols)):
# #     worksheet.write('A%s'%str(i+1),newcols[i])  #循环写处理后的数据生成的列表
# # workbook.close()
#_____________________________________________通过函数把list写入excel——————————————————————————
def data_write(file_path, datas):
    f = xlwt.Workbook()#创建文件对象
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:#datas为传入的list
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
    f.save(file_path) #保存文件
#list=du_excel()#调用读取excel
#print(list)
#data_write('转换后的文件.xls', list)#调用写入



