# -*- coding: utf-8 -*-
import xlsxwriter
import datetime
import time
import excel

def get_format(wd, option={}):
    return wd.add_format(option)

# 设置居中
def get_format_center(wd,num=1):
    return wd.add_format({'align': 'center','valign': 'vcenter','border':num})
def set_border_(wd, num=1):
    return wd.add_format({}).set_border(num)

# 写数据
def _write_center(worksheet, cl, data, wd):
    return worksheet.write(cl, data, get_format_center(wd))

#创建一个excel，其中包含两个sheet(测试总况,测试详情)
workbook = xlsxwriter.Workbook('接口自动化_报告汇总终极版.xlsx')
worksheet = workbook.add_worksheet("测试总况")
worksheet2 = workbook.add_worksheet("测试详情")

def init(worksheet):
    ''u'报告总概况'''
    # 设置列行的宽高(宽度)
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)
    # 设置列行的宽高(高度)
    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 80)

    # worksheet.set_row(0, 200)

    define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})#font_size标题文字大小
    define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})
    #define_format_H3 = get_format(workbook, {'bold': True, 'font_size': 22})#自己加的

    #居中及颜色
    define_format_H1.set_border(1)
    define_format_H2.set_border(1)
    #define_format_H3.set_border(1)#自己加的
    define_format_H1.set_align("center")
    define_format_H2.set_align("center")
    define_format_H2.set_bg_color("blue")
    #define_format_H3.set_bg_color("purple")#自己加的
    define_format_H2.set_color("#ffffff")
    # Create a new Chart object.
    #填写文字
    worksheet.merge_range('A1:F1', '测试报告总概况', define_format_H1)
    worksheet.merge_range('A2:F2', '测试概括', define_format_H2)
    #worksheet.merge_range('A7:F7', '测试概括303', define_format_H3)#自己加的
    worksheet.merge_range('A3:A6', '这里放图片', get_format_center(workbook))

    _write_center(worksheet, "B3", '项目名称', workbook)
    _write_center(worksheet, "B4", '接口版本', workbook)
    _write_center(worksheet, "B5", '脚本语言', workbook)
    _write_center(worksheet, "B6", '测试网络', workbook)

    #定义字典把value插入到excel
    data = {"test_name": "二期SDK接口", "test_version": "v2.0.1", "test_pl": "android", "test_net": "wifi"}
    _write_center(worksheet, "C3", data['test_name'], workbook)
    _write_center(worksheet, "C4", data['test_version'], workbook)
    _write_center(worksheet, "C5", data['test_pl'], workbook)
    _write_center(worksheet, "C6", data['test_net'], workbook)

    _write_center(worksheet, "D3", "接口总数", workbook)
    _write_center(worksheet, "D4", "通过总数", workbook)
    _write_center(worksheet, "D5", "失败总数", workbook)
    _write_center(worksheet, "D6", "测试日期", workbook)
    da=excel.excel_hang()#调用函数读取excel
    sum=len(da["info"])#条目数
    success=0
    failed=0
    for t in da["info"]:
        print(t,'\n')
        print(t["t_result"])
        if t["t_result"]=='成功':
            success+=1
        elif  t["t_result"]=='失败':
            failed+=1
        else:
            print('出现异常情况')
    print('通过接口%d条'%(success))
    print('失败接口%d条'%(failed))

    ccc = str(datetime.date.today())+' '+str(time.strftime("%H:%M:%S"))#获取当前时间日期
    #定义字典把value插入到excel
    data1 = {"test_sum": sum, "test_success":  success, "test_failed": failed , "test_date": ccc}
    _write_center(worksheet, "E3", data1['test_sum'], workbook)
    _write_center(worksheet, "E4", data1['test_success'], workbook)
    _write_center(worksheet, "E5", data1['test_failed'], workbook)
    _write_center(worksheet, "E6", data1['test_date'], workbook)

    _write_center(worksheet, "F3", "通过率", workbook)

    worksheet.merge_range('F4:F6', round((sum-failed)/sum,2), get_format_center(workbook))
    pie(workbook, worksheet)

 # 生成饼形图
def pie(workbook, worksheet):
    chart1 = workbook.add_chart({'type': 'pie'})
    chart1.add_series({
    'name':       '接口测试统计',
    'categories':'=测试总况!$D$4:$D$5',
   'values':    '=测试总况!$E$4:$E$5',
    })
    chart1.set_title({'name': '接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9', chart1, {'x_offset': 25, 'y_offset': 10})

def test_detail(worksheet):
    ''u'报告详情'''
    # 设置列行的宽高（宽度）
    worksheet.set_column("A:A", 10)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 10)
    worksheet.set_column("D:D", 40)
    worksheet.set_column("E:E", 40)
    worksheet.set_column("F:F", 40)
    worksheet.set_column("G:G", 55)
    worksheet.set_column("H:H", 20)
    # 设置列行的宽高（高度 ）
    worksheet.set_row(0, 40)
    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)
    worksheet.set_row(6, 30)
    worksheet.set_row(7, 30)

    #标题及字段名，，workbook表示excel文件对象，，worksheet表示第几个sheet
    #font_size：字体大小，align：左右或居中对齐(left,right)，bg_color：填充颜色，'fg_color': (单元格内背景颜色),font_color:字体颜色，bold：字体粗细(true为粗),'valign': 'vcenter'(垂直对齐)
    worksheet.merge_range('A1:H1', '测试详情', get_format(workbook, {'bold': True, 'font_size': 18 ,'align': 'center','valign': 'vcenter','bg_color': 'blue', 'font_color': '#FFFFFF'}))
    #处理单元格
    bold = workbook.add_format({'bold':True,'align':'center','valign': 'vcenter'})
    worksheet.write("A2", '用例ID',  bold)
    #不处理单元格，直接写入
    #_write_center(worksheet, "A2", '用例ID',  bold)
    _write_center(worksheet, "B2", '接口名称', workbook)
    _write_center(worksheet, "C2", '接口协议', workbook)
    _write_center(worksheet, "D2", 'URL', workbook)
    _write_center(worksheet, "E2", '参数', workbook)
    _write_center(worksheet, "F2", '预期值', workbook)
    _write_center(worksheet, "G2", '实际值', workbook)
    _write_center(worksheet, "H2", '测试结果',  workbook)

    data=excel.excel_hang()#调用函数读取excel
    temp = len(data["info"])+2#统计返回字典数(字典数表示excel的函数)
    #循环写入数据到excel
    for item in data["info"]:
        #print(item,'\n')
        #每次循环写一行
        _write_center(worksheet, "A"+str(temp), item["t_id"], workbook)#如果temp = 4，，那么"A"+str(temp)=A4数据将写入A4单元格
        _write_center(worksheet, "B"+str(temp), item["t_name"], workbook)
        _write_center(worksheet, "C"+str(temp), item["t_method"], workbook)
        _write_center(worksheet, "D"+str(temp), item["t_url"], workbook)
        _write_center(worksheet, "E"+str(temp), item["t_param"], workbook)
        _write_center(worksheet, "F"+str(temp), item["t_actual"], workbook)
        _write_center(worksheet, "G"+str(temp), item["t_hope"], workbook)
        _write_center(worksheet, "H"+str(temp), item["t_result"], workbook)
        temp = temp -1
#
init(worksheet)
test_detail(worksheet2)
workbook.close()

