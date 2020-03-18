import xlwt
# from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QMainWindow


class ExportXlsHelper():
    def __init__(self, workbook_name):
        self.workbook_name = workbook_name

    def qtTableWidgetExportToXls(self, mainWindow, sheetName, isDaily=False, isOtherTable = False):
        table = mainWindow if isOtherTable else mainWindow.tableWidget
        workbook = xlwt.Workbook(encoding='utf8')
        worksheet = workbook.add_sheet(sheetName)
        rowCount = table.rowCount()
        colCount = table.columnCount()
        style = xlwt.XFStyle()  # 格式信息
        font = xlwt.Font()  # 字体基本设置
        font.name = u'微软雅黑'
        font.color = 'black'
        font.height = 240
        style.font = font
        alignment = xlwt.Alignment()
        alignment.horz = xlwt.Alignment.HORZ_CENTER
        style.alignment = alignment
        headerRow = 0
        addRow = 1
        if isDaily:
            rowCount = rowCount + 1
            headerRow += 1
            addRow += 1
            content = mainWindow.label_4.text()
            worksheet.write(0, 0, label=content, style=style)
            content = mainWindow.lineEdit.text()
            worksheet.write(0, 1, label=content, style=style)
            content = mainWindow.label_6.text()
            worksheet.write(0, 5, label=content, style=style)
            content = mainWindow.lineEdit_2.text()
            worksheet.write(0, 6, label=content, style=style)
            content = mainWindow.label_8.text()
            worksheet.write(0, 9, label=content, style=style)
            content = mainWindow.lineEdit_3.text()
            worksheet.write(0, 10, label=content, style=style)
        for col_index in range(colCount):
            headerText = table.horizontalHeaderItem(col_index).text()
            worksheet.write(headerRow, col_index,
                            label=headerText, style=style)
        for row_index in range(rowCount -1):
            for col_index in range(colCount):
                # if row_index == 0:
                #     headerText = tableWidget.horizontalHeaderItem(colCount).text()
                #     worksheet.write(row_index, col_index, label=headerText)
                # else:
                data = table.item(row_index, col_index).text()
                worksheet.write(row_index + addRow, col_index,
                                label=data, style=style)
        workbook.save(self.workbook_name)
