# Mar 31th, 10:49 PM, 2018 @ dorm 602
# 使用 xlwt 库进行 Excel 储存测试

import xlwt

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet1')
# sheet.write(#行，#列，#内容)
sheet.write(0,0,'Python')
sheet.write(0,1,'Excel')
book.save('E:\AllPrj\PyCharmPrj\py-crawler\Excel 存储\Excel 储存测试.xls')
