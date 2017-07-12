#! python3
# multiplicationTable.py

import openpyxl, string, sys
from openpyxl.styles import Font

if __name__ == "__main__":
    number = sys.argv[1]
    alphabet = string.ascii_uppercase
    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    # Bold vertical headers
    for i in range(1, int(number) + 1):
        cell = "A%s" % str(i+1)
        sheet[cell] = i
        sheet[cell].font = Font(bold=True)
    # Bold horizontal headers
    for i in range(1, int(number) + 1):
        cell = "%s1" % alphabet[i]
        sheet[cell] = i
        sheet[cell].font = Font(bold=True)
    for i in range(1, int(number) + 1):
        for j in range(1, int(number) + 1):
            cell = "%s%s" % (alphabet[i], str(j+1))
            sheet[cell] = i * j
    # Write to file
    wb.save("multiplicationTable.xlsx")