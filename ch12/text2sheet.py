#! python3
# text2sheet.py

import openpyxl, sys, string
import pdb

if __name__ == "__main__":
    files = sys.argv[1:]

    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    alphabet = string.ascii_uppercase

    iter = 0
    #pdb.set_trace()

    for file in files:
        row = 0
        col = alphabet[iter]
        with open(file) as f:
            for line in f.readlines():
                #pdb.set_trace()
                row = row + 1
                cell = "%s%s" % (col, row)
                sheet[cell] = line
            iter = iter + 1

    wb.save('text2.xlsx')