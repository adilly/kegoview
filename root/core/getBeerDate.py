'''
Created on Mar 29, 2017

@author: Austin Dillinger
'''

import openpyxl as openxl
import datetime
import time

def getBeerDate (beerName):
    wb = openxl.load_workbook("D:\Documents\Brewing.xlsx")
    sheet = wb.get_sheet_by_name(beerName)
    date = sheet['b1'].value
    date = date.strftime('%m/%d/%Y')
    return date