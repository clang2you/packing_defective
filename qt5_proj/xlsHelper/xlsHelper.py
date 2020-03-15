import xlwt
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class ExportXlsHelper():
    def __init__(self, workbook_name):
        self.workbook_name = workbook_name
    
    def qtTableWidgetExportToXls(self, tableWidget):
        workbook = xlwt.Workbook(encoding='utf8')
        worksheet = workbook.add_sheet('Sheet1')
        rowCount = tableWidget.rowCount()
        colCount = tableWidget.columnCount()
        for col_index in range(colCount):
            headerText = tableWidget.horizontalHeaderItem(col_index).text()
            worksheet.write(0, col_index, label=headerText)
        for row_index in range(rowCount):
            for col_index in range(colCount):
                # if row_index == 0:
                #     headerText = tableWidget.horizontalHeaderItem(colCount).text()
                #     worksheet.write(row_index, col_index, label=headerText)
                # else:
                data = tableWidget.item(row_index, col_index).text()
                worksheet.write(row_index + 1, col_index, label=data)
        workbook.save(self.workbook_name)

