# -*- coding: utf-8 -*-
import xlrd
import os

def get_row_values_as_list(file, sheet, rowx, colx):
    path = os.path.abspath(file)
    book = xlrd.open_workbook(path)
    sheet = book.sheet_by_name(sheet)
    return sheet.row_values(rowx)[colx:]

def get_var_start_position(markup_file = None):
    """
    =[tab1.xls]Лист1!A9 -> ('GDP', 'tab1.xls', 'Лист1', 'A9') ->
     ['GDP', 'tab1.xls', 'Лист1', (8, 0)]
    """
    result_from_file = ['GDP', 'tab1.xls', 'Лист1', 'A9']
    return 'GDP', ['tab1.xls', 'Лист1', 7, 0]

z = get_var_start_position()
print(z)
row = get_row_values_as_list(*get_var_start_position()[1])
print(row)

def filter_values():
    '2014 1)'
    pass


"""
GDP	=[tab1.xls]Лист1!A9	1428,5221	=C1=B1
"""
