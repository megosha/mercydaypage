import os
from datetime import datetime

from django.conf import settings as sts

import xlrd
import xlwt


def generate_filename(project_date):
    return os.path.join(sts.BASE_DIR, f'{project_date}.xls')

def extract_sheet(fname, sheet_name_='blago22'):
    my_book = xlrd.open_workbook(fname)
    my_sheet = my_book.sheet_by_name(sheet_name_)
    return my_sheet

def xl_to_list(sheet_):
    my_table = []
    for m in range(len(sheet_.col(0))):
        my_row = []
        for n in range(len(sheet_.row(m))):
            my_row.append(sheet_.row(m)[n].value)
        my_table.append(my_row)
    return my_table

def write_sheet(table:list, addition, fname, sheet_name_='blago22'):
    book = xlwt.Workbook()
    sheet1 = book.add_sheet(sheet_name_)
    for num, val in enumerate(table):
        sheet1.write(num, 0, val[0])
        sheet1.write(num, 1, val[1])
    sheet1.write(len(table), 0, addition[0])
    sheet1.write(len(table), 1, addition[1])
    book.save(fname)