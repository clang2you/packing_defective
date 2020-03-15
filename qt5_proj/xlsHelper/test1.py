import xlwt 


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("Sheet1")
worksheet.write(0,0, label='this is test')

workbook.save('test1.xls')