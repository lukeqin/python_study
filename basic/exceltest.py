#-*- coding: UTF-8 -*-
'''
Created on 2017年3月11日
@author: luke
'''

'''
pip install xlutils
'''
import xlrd
import xlwt
from xlutils.copy import copy

data = {
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}

'''
write(rows,colx,cell_value,style)
row(rowx).write(colx,cell_value,style):                       
col(colx),write(rows,cell_value,style):
'''

'''
book = xlrd.open_workbook("students.xls", formatting_info=True, on_demand=True)
sheet = book.sheet_by_index(0)
cell = sheet.cell(0,0)
'''

KEYS = sorted(data, key=lambda asd:asd[0])

def wcol(row, wdata, sheet):
    col = 0
    sheet.row(row).write(col, wdata)
    for i in data[wdata]:
        col += 1
        if type(i) == str:
            sheet.row(row).write(col, unicode(i, 'utf-8'))
        else:
            sheet.row(row).write(col, i)
    col = 0
    
def wrow(row, sheet):
    wcol(row, KEYS[row], sheet)

workbook = xlwt.Workbook()
workbook.encoding = "utf-8"
sheet = workbook.add_sheet("sheet1", cell_overwrite_ok=True)

for i in range(len(data)):
    wrow(i, sheet) 
        
workbook.save("students.xls")



    