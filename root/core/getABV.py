'''
Created on Mar 28, 2017

@author: Austin Dillinger
'''

import openpyxl as openxl

def getABV (beerName):
    wb = openxl.load_workbook("D:\Documents\Brewing.xlsx")
    sheet = wb.get_sheet_by_name(beerName)
    ABV = round(sheet['b49'].value * 100,3)
    ABV = str(ABV) + "% ABV"
    return ABV

print(getABV('Shower Hop'))