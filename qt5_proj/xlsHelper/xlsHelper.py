import xlwt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class ExportXlsHelper():
    def __init__(self, workbook_name):
        self.workbook_name = workbook_name
    
    def qtTableWidgetExportToXls(self, tableWidget, sheetName):
        workbook = xlwt.Workbook(encoding='utf8')
        worksheet = workbook.add_sheet(sheetName)
        rowCount = tableWidget.rowCount()
        colCount = tableWidget.columnCount()
        style = xlwt.XFStyle()#格式信息
        font = xlwt.Font()#字体基本设置
        font.name = u'微软雅黑'
        font.color = 'black'
        font.height= 240 
        style.font = font
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        style.alignment = alignment
        for col_index in range(colCount):
            headerText = tableWidget.horizontalHeaderItem(col_index).text()
            worksheet.write(0, col_index, label=headerText, style=style)
        for row_index in range(rowCount):
            for col_index in range(colCount):
                # if row_index == 0:
                #     headerText = tableWidget.horizontalHeaderItem(colCount).text()
                #     worksheet.write(row_index, col_index, label=headerText)
                # else:
                data = tableWidget.item(row_index, col_index).text()
                worksheet.write(row_index + 1, col_index, label=data, style=style)
        workbook.save(self.workbook_name)

