import xlsxwriter
import os


class ExportExcel:
    def __init__(self, name):
        self.name = name
        self.workbook = xlsxwriter.Workbook(self.name + '.xlsx')
        self.worksheet = self.workbook.add_worksheet()

    def write_info(self, data):
        row = 0
        for item in data:
            for x in range(0, len(item)):
                self.worksheet.write(row, x, item[x])

            #item => ('Oliver', '4325435', 'jkfasldf')
        self.workbook.close()


    def open_file(self):
        file = "./" + self.name + ".xlsx"
        os.system("start EXCEL.EXE " + file)




