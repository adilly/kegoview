'''
Created on Mar 26, 2017

@author: Austin Dillinger
'''

import openpyxl as openxl

def getStyle (beerName):
    wb = openxl.load_workbook("D:\Documents\Brewing.xlsx")
    sheet = wb.get_sheet_by_name(beerName)
    style = sheet['b3'].value
    return style

