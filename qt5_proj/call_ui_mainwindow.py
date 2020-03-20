import sys
import os
import datetime
import dateutil
import pandas as pd
import numpy as np
import traceback
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QProgressBar, QLineEdit, QComboBox, QFrame, QTableWidgetItem
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import qt5_proj.DbHelper.db_helper as dbHelper
# pyinstaller 打包不支持自定义模块 from xxx import xxx 的引用方式，仅能使用 import 来导入所需的包
import qt5_proj.mainForm as mainForm
import qt5_proj.ConfigHelper.config_helper as config_mod
import qt5_proj.sectionSettings as sectionSettings
import qt5_proj.dailyDefStasticForm as dailyDefStasticForm
import qt5_proj.dbSettings as dbSettings
import qt5_proj.adminAuthorization as adminAuthorization
import qt5_proj.userInput as userInput
import qt5_proj.monthlyDefStasticForm as monthlyDefStasticForm
import qt5_proj.countAdjustment as countAdjustment
import qt5_proj.workingTimeSettings as workingTimeSettings
import qt5_proj.targetSettings as targetSettings
import qt5_proj.workRestTimeSettings as workRestTimeSettings
import qt5_proj.lineSettings as lineSettings
import qt5_proj.ZMQHelper.zeromqHelper as mqHelper
import qt5_proj.xlsHelper.xlsHelper as exportHelper
import sip

matplotlib.use("Qt5Agg")

# Config_Helper 全局
config = config_mod.CfgHelper()
configJson = config.cfg_dict

# 三种字体 全局
light_14_font = QtGui.QFont()
light_14_font.setFamily("微软雅黑 Light")
light_14_font.setPointSize(14)
light_14_font.setWeight(50)

bold_20_font = QtGui.QFont()
bold_20_font.setFamily("微软雅黑")
bold_20_font.setPointSize(20)
bold_20_font.setBold(True)
bold_20_font.setWeight(50)

light_20_font = QtGui.QFont()
light_20_font.setFamily("微软雅黑 Light")
light_20_font.setPointSize(20)
light_20_font.setBold(False)
light_20_font.setWeight(50)

# 数据库设定窗口类


class DbSettingsWindow(QDialog):
    def __init__(self, parent=None):
        global configJson
        super(DbSettingsWindow, self).__init__(parent)
        self.child = dbSettings.Ui_Dialog()
        self.child.setupUi(self)
        self.child.pushButton_3.clicked.connect(self.ChangeDbSettings)
        self.child.pushButton.clicked.connect(self.SaveDbSettings)
        self.lineEdits = ['lineEdit', 'lineEdit_2', 'lineEdit_3', 'lineEdit_4']

        self.ChangeInterfaceComponent(True)
        self.SetLineEditText(configJson["MySQL"])

    def SaveDbSettings(self):
        global configJson
        configDb = {'address': self.child.lineEdit.text(), 'user': self.child.lineEdit_2.text(),
                    'password': self.child.lineEdit_3.text(), 'dbName': self.child.lineEdit_4.text()}
        configJson["MySQL"] = configDb
        config.SaveConfigToJson(configJson)
        self.ChangeInterfaceComponent(True)

    def ChangeInterfaceComponent(self, saveOrNotAuthorization):
        self.child.pushButton_3.setEnabled(saveOrNotAuthorization)
        self.child.pushButton.setEnabled(not saveOrNotAuthorization)
        qss = "QLineEdit{background-color:silver}" if saveOrNotAuthorization else "QLineEdit{background-color:white}"
        for lineEdit in self.lineEdits:
            edit = self.child.frame.findChild((QtWidgets.QLineEdit), lineEdit)
            edit.setStyleSheet(qss)
            edit.setFont(light_14_font)
            edit.setReadOnly(saveOrNotAuthorization)

    def SetLineEditText(self, configDb):
        try:
            self.child.lineEdit.setText(
                configDb["address"])
            self.child.lineEdit_2.setText(
                configDb["user"])
            self.child.lineEdit_3.setText(
                configDb["password"])
            self.child.lineEdit_4.setText(
                configDb["dbName"])
        except:
            for lineEdit in self.lineEdits:
                edit = self.child.frame.findChild(
                    (QtWidgets.QLineEdit), lineEdit)
                edit.setText("")

    def ChangeDbSettings(self):
        self.passwordForm = AdminAutorizationForm(self)
        self.passwordForm.child.lineEdit.editingFinished.connect(
            lambda: self.HandlePassword(self.passwordForm.child.lineEdit.text()))
        self.passwordForm.exec()

    def HandlePassword(self, password):
        try:
            if password == configJson["Admin"]["password"]:
                self.passwordForm.reject()
                self.ChangeInterfaceComponent(False)
        except:
            self.passwordForm.reject()
            self.ChangeInterfaceComponent(False)

# 管理员权限授权窗口类


class AdminAutorizationForm(QDialog):
    def __init__(self, parent=None):
        super(AdminAutorizationForm, self).__init__(parent)
        self.child = adminAuthorization.Ui_Dialog()
        self.child.setupUi(self)

# 生产时段设置窗口类


class WorkingtimeSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(WorkingtimeSettingsWindow, self).__init__(parent)
        self.child = workingTimeSettings.Ui_Dialog()
        self.child.setupUi(self)

# 加工线分段信息设定窗口类


class SectionSettingWindow(QDialog):
    def __init__(self, parent=None):
        global configJson
        super(SectionSettingWindow, self).__init__(parent)
        self.child = sectionSettings.Ui_Dialog()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.SaveSectionSettings)

        try:
            self.child.label_5.setText(configJson["Line"]["name"])
            for itemName in dir(self.child):
                if type(getattr(self.child, itemName)) == QComboBox:
                    choiceBox = getattr(self.child, itemName)
                    choiceBox.addItems(list(configJson["DefReasons"].values()))
                    section, no = itemName.split('_')
                    if configJson["Section"] != None and section in configJson["Section"].keys():
                        choiceBox.setCurrentText(
                            configJson["Section"][section][no])
        except Exception as ex:
            print(ex)

    def SaveSectionSettings(self):
        global config, configJson
        configSection = configJson["Section"]
        for itemName in dir(self.child):
            if type(getattr(self.child, itemName)) == QComboBox:
                choiceBox = getattr(self.child, itemName)
                section, no = itemName.split('_')
                if configSection == None:
                    configSection = {section: {no: choiceBox.currentText()}}
                if section in configSection.keys():
                    configSection[section][no] = choiceBox.currentText()
                else:
                    configSection[section] = {no: choiceBox.currentText()}
        configJson["Section"] = configSection
        config.SaveConfigToJson(configJson)
        self.child.label_6.setText("设定保存完成")
        self.child.label_6.setStyleSheet("QLabel{color: green}")
        self.child.label_6.setFont(light_14_font)

 # 作休时间设置窗口类


class WorkRestTimeSettingWindow(QDialog):
    def __init__(self, parent=None):
        super(WorkRestTimeSettingWindow, self).__init__(parent)
        self.child = workRestTimeSettings.Ui_Dialog()
        self.child.setupUi(self)

# 每日目标产量设定窗口类


class TargetSettingWindow(QDialog):
    def __init__(self, parent=None):
        super(TargetSettingWindow, self).__init__(parent)
        self.child = targetSettings.Ui_Dialog()
        self.child.setupUi(self)
        self.child.dateEdit.setDate(datetime.datetime.now())
        self.child.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:lightblue;color: black;padding-left: 4px;border: 1px solid#6c6c6c;}")
        self.SetTableWidgetHeaderWidth()
        self.dbHandler = dbHelper.DbHelper(configJson)
        self.child.pushButton.clicked.connect(self.InsertTargetToDb)
        self.child.lineEdit.textChanged.connect(self.ClearLabel3Contents)
        self.child.pushButton_3.setVisible(False)
        self.child.pushButton_4.clicked.connect(self.DeleteDailyTarget)
        self.child.tableWidget.verticalHeader().setHidden(True)
        self.GetDbTargetDataMonthly()

    def ClearLabel3Contents(self):
        self.child.label_3.setText("")

    def SetTableWidgetHeaderWidth(self):
        for header_item_index in range(self.child.tableWidget.columnCount()):
            self.child.tableWidget.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)

    def InsertTargetToDb(self):
        self.child.label_3.setStyleSheet("QLabel{color:green}")
        self.child.label_3.setText("")
        date_info = self.child.dateEdit.date().toPyDate().strftime("%Y-%m-%d")
        target = 0
        try:
            if int(self.child.lineEdit.text()) > 0:
                target = int(self.child.lineEdit.text())
            data = [configJson["Line"]["name"], date_info, str(target)]
            self.dbHandler.InsertDailyTargetData(data)
            self.GetDbTargetDataMonthly()
            self.child.label_3.setText("保存成功!")
        except:
            self.child.label_3.setText("无法保存，请检查输入！")
            self.child.label_3.setStyleSheet("QLabel{color:red}")

    def GetDbTargetDataMonthly(self):
        try:
            self.child.label_2.setText(configJson["Line"]["name"])
            dataDic = self.dbHandler.GetDailyTargetData(
                configJson["Line"]["name"])
            rowCount = len(list(dataDic.keys()))
            self.child.tableWidget.setRowCount(rowCount)
            rowIndex = 0
            for key, value in dataDic.items():
                newItem = QTableWidgetItem(str(key))
                newItem.setFont(light_14_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.child.tableWidget.setItem(rowIndex, 0, newItem)
                newItem = QTableWidgetItem(str(value))
                newItem.setFont(light_14_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.child.tableWidget.setItem(rowIndex, 1, newItem)
                rowIndex += 1
        except:
            self.child.label_3.setText("查询本月目标量出错！")
            self.child.label_3.setStyleSheet("QLabel{color:red}")

    def DeleteDailyTarget(self):
        try:
            currentRow = self.child.tableWidget.currentRow()
            date = self.child.tableWidget.item(currentRow, 0).text()
            self.dbHandler.DeleteDailyTargetData(
                configJson["Line"]["name"], date)
            self.GetDbTargetDataMonthly()
        except:
            traceback.print_exc()
            self.child.label_3.setText("删除指定日期目标量出错！")
            self.child.label_3.setStyleSheet("QLabel{color:red}")

# 线别、不良类型及工作时段设定窗口类


class LineSettingsWindow(QDialog):
    updateSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(LineSettingsWindow, self).__init__(parent)
        self.child = lineSettings.Ui_Dialog()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(
            self.SaveLineSettingsToConfigJson)
        self.GetLineSettingsFromConfigJson()

    def GetLineSettingsFromConfigJson(self):
        global configJson
        editList = ("lineEdit_2", "lineEdit_7", "lineEdit_4", "lineEdit_3",
                    "lineEdit_5", "lineEdit_6",  "lineEdit_8")
        configLine = configJson["Line"]
        configDefType = configJson["DefReasons"]
        try:
            self.child.comboBox.setCurrentText(configLine['name'])
            self.child.timeEdit.setTime(QtCore.QTime.fromString(
                configLine["amStart"], "HH:mm"))
            self.child.timeEdit_2.setTime(QtCore.QTime.fromString(
                configLine["amStop"], "HH:mm"))
            self.child.timeEdit_3.setTime(QtCore.QTime.fromString(
                configLine["pmStart"], "HH:mm"))
            self.child.timeEdit_4.setTime(QtCore.QTime.fromString(
                configLine["pmStop"], "HH:mm"))
            defTypeIndex = 1
            for editName in editList:
                edit = self.child.frame_3.findChild((QLineEdit), editName)
                edit.setText(configDefType[str(defTypeIndex)])
                defTypeIndex += 1
        except Exception as ex:
            print(ex)
            self.child.label_13.setFont(light_14_font)
            self.child.label_13.setText("未设定线别信息")
            self.child.label_13.setStyleSheet("QLabel{color: red}")

    def SaveLineSettingsToConfigJson(self):
        global config, configJson
        configLine = {"name": self.child.comboBox.currentText(),
                      "amStart": self.child.timeEdit.time().toString("HH:mm"),
                      "amStop": self.child.timeEdit_2.time().toString("HH:mm"),
                      "pmStart": self.child.timeEdit_3.time().toString("HH:mm"),
                      "pmStop": self.child.timeEdit_4.time().toString("HH:mm"),
                      }
        configJson["Line"] = configLine
        configDefType = {"1": self.child.lineEdit_2.text(),
                         "2": self.child.lineEdit_7.text(),
                         "3": self.child.lineEdit_4.text(),
                         "4": self.child.lineEdit_3.text(),
                         "5": self.child.lineEdit_5.text(),
                         "6": self.child.lineEdit_6.text(),
                         "7": self.child.lineEdit_8.text()}
        configJson["DefReasons"] = configDefType
        config.SaveConfigToJson(configJson)
        workTimeInfoList = [self.child.timeEdit.time().toString("HH:mm"),
                            self.child.timeEdit_2.time().toString("HH:mm"),
                            self.child.timeEdit_3.time().toString("HH:mm"),
                            self.child.timeEdit_4.time().toString("HH:mm")]
        timeOpt = TimeManipulation()
        timeOpt.CalculatingTotalWorkTime()
        amWorkHours = timeOpt.amTotalHours
        pmWorkHours = timeOpt.pmTotalHours
        totalHours = timeOpt.totalHours
        tempList = [amWorkHours, pmWorkHours,
                    totalHours, configJson["Line"]["name"]]
        workTimeInfoList.extend(tempList)
        try:
            self.dbHandler = dbHelper.DbHelper(configJson)
            self.dbHandler.InsertIntoConfigTableDefInfo(configJson)
            self.dbHandler.InsertWorkingTimeInfoToDb(workTimeInfoList)
        except:
            traceback.print_exc()
        self.child.label_13.setFont(light_14_font)
        self.child.label_13.setText("设定保存完成")
        self.child.label_13.setStyleSheet("QLabel{color: green}")
        self.updateSignal.emit()

# 日不良统计窗口类


class DailyDefStasticForm(QMainWindow, dailyDefStasticForm.Ui_MainWindow):
    def __init__(self, parent=None):
        global configJson
        super(DailyDefStasticForm, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:lightblue;color: black;padding-left: 4px;border: 1px solid#6c6c6c;}")
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label_2.setStyleSheet("QLabel{color:darkblue}")
        self.dateEdit.setDate(datetime.datetime.now())
        self.statusBar().hide()
        self.isHistory = False
        self.pushButton.clicked.connect(self.close)
        self.progressBar.hide()
        self.dateEdit.dateChanged.connect(self.ChangeTimeSliceList)
        self.pushButton_2.clicked.connect(self.GetQueryDailyResults)
        self.pushButton_3.clicked.connect(self.ExportDailyDefDatasToXls)
        try:
            self.label_2.setText(configJson["Line"]["name"])
            self.SetDailyTableColumns()
            self.SetTableWidgetWidth()
            self.dbHandler = dbHelper.DbHelper(configJson)
        except:
            traceback.print_exc()
            self.label_10.setText("分割时间段出错,\n请检查工作时段配置！")
            self.label_10.setStyleSheet("QLabel{color:red}")
            self.label_10.setFont(light_14_font)

    def SetTableWidgetWidth(self):
        for header_item_index in range(self.tableWidget.columnCount()):
            if header_item_index != 0:
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    header_item_index, QtWidgets.QHeaderView.Stretch)
            else:
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    header_item_index, QtWidgets.QHeaderView.ResizeToContents)
                # print(self.tableWidget.horizontalHeaderItem(0).text())

    def ChangeTimeSliceList(self):
        self.timeSliceList = TimeManipulation(
            self.dateEdit.date().toPyDate()).DayHourRange(60*60)
        if self.dateEdit.date().toPyDate() < datetime.datetime.now().date():
            self.isHistory = True
        else:
            self.isHistory = False

    def SetDailyTableColumns(self):
        self.timeSliceList = TimeManipulation().DayHourRange(60*60)
        self.tableWidget.setColumnCount(len(self.timeSliceList) + 2)
        itemList = ["不良原因", ]
        for timeItem in self.timeSliceList:
            itemList.append(timeItem[0].strftime(
                "%H:%M") + "\n至\n" + timeItem[1].strftime("%H:%M"))
        itemList.append("合计")
        for i in range(len(itemList)):
            item = QtWidgets.QTableWidgetItem(itemList[i])
            item.setFont(light_14_font)
            self.tableWidget.setHorizontalHeaderItem(i, item)

    def GetQueryDailyResults(self):
        try:
            self.label_10.setText("")
            self.tableWidget.horizontalHeader().setSectionResizeMode(
                0, QtWidgets.QHeaderView.ResizeToContents)
            self.label_5.setText("")
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")
            self.tableWidget.clearContents()
            self.tableWidget.verticalHeader().setHidden(True)
            if self.isHistory:
                self.totalDic = self.dbHandler.GetDailyTotals(
                    str(self.dateEdit.date().toPyDate()), self.isHistory)
            else:
                self.totalDic = self.dbHandler.GetDailyTotals(
                    str(self.dateEdit.date().toPyDate()))
            self.lineEdit.setText(
                self.totalDic["投料"] if "投料" in self.totalDic.keys() else "0")
            self.lineEdit_2.setText(
                self.totalDic["包装"] if "包装" in self.totalDic.keys() else "0")
            self.lineEdit_3.setText(
                self.totalDic["不良合计"] if "不良合计" in self.totalDic.keys() else "0")
            dailyResult = self.dbHandler.GetDailyDataResults(
                self.timeSliceList, self.isHistory)
            # print(dailyResult)
            listLength = len(dailyResult)
            self.tableWidget.setRowCount(listLength + 1)
            for rowIndex in range(len(dailyResult)):
                subCount = 0
                rowDataColumnCount = len(dailyResult[rowIndex])
                for i in range(rowDataColumnCount):
                    if isinstance(dailyResult[rowIndex][i], str):
                        newItem = QtWidgets.QTableWidgetItem(
                            dailyResult[rowIndex][i])
                        newItem.setTextAlignment(QtCore.Qt.AlignLeft)
                    else:
                        subCount += int(dailyResult[rowIndex][i]
                                        ) if dailyResult[rowIndex][i] != None else 0
                        newItem = QtWidgets.QTableWidgetItem(
                            str(dailyResult[rowIndex][i]))
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(
                        rowIndex, i, newItem)
                newItem = QtWidgets.QTableWidgetItem(str(subCount))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(rowIndex, rowDataColumnCount, newItem)
            for i in range(self.tableWidget.columnCount()):
                count = 0
                if i == 0:
                    newItem = QtWidgets.QTableWidgetItem("合计")
                    newItem.setTextAlignment(QtCore.Qt.AlignLeft)
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, i, newItem)
                else:
                    for j in range(self.tableWidget.rowCount() - 1):
                        cell = self.tableWidget.item(j, i)
                        if cell != None:
                            count = count + int(cell.text())
                    newItem = QtWidgets.QTableWidgetItem(str(count))
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, i, newItem)
        except:
            traceback.print_exc()
            self.label_5.setFont(light_14_font)
            self.label_5.setText("出错，无法连接数据库\n请联系 IT 处理！")
            self.label_5.setStyleSheet("QLabel{color:red}")

    def ExportDailyDefDatasToXls(self):
        try:
            if self.tableWidget.rowCount() > 1:
                dateSectionStr = self.dateEdit.date().toPyDate().strftime("%y-%m-%d")
                filename = QtWidgets.QFileDialog.getSaveFileName(
                    self, "导出到Excel", configJson["Line"]["name"] + "日不良数据导出" + dateSectionStr + ".xls", "Excel文件(*.xls)")
                if filename[0] != "":
                    self.excelHandler = exportHelper.ExportXlsHelper(
                        filename[0])
                    self.excelHandler.qtTableWidgetExportToXls(
                        self, configJson["Line"]["name"] + "日不良统计@" + dateSectionStr, True)
                    self.label_10.setStyleSheet("QLabel{color:green}")
                    self.label_10.setText("日不良记录导出成功")
                    self.label_10.setFont(light_20_font)
            else:
                self.label_10.setFont(light_14_font)
                self.label_10.setStyleSheet("QLabel{color:blue}")
                self.label_10.setText('无数据，请先点击“查询”\n将结果导出')
        except:
            traceback.print_exc()
            self.label_10.setFont(light_14_font)
            self.label_10.setStyleSheet("QLabel{color:red}")
            self.label_10.setText('数据导出失败，\n请重试或联系 IT 处理')
# 月不良统计窗口类


class MonthlyDefStasticForm(QMainWindow, monthlyDefStasticForm.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MonthlyDefStasticForm, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:lightblue;color: black;padding-left: 4px;border: 1px solid#6c6c6c;}")
        self.dateEdit.setDate(datetime.datetime.now() -
                              dateutil.relativedelta.relativedelta(months=1))
        self.dateEdit_2.setDate(datetime.datetime.now())
        self.pushButton.clicked.connect(self.ExportToXls)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        if configJson["Line"] != None:
            self.label_2.setText(configJson["Line"]["name"])
            self.label_2.setStyleSheet("QLabel{color:darkblue}")
        else:
            self.label_2.setText("未配置")
            self.label_2.setStyleSheet("QLabel{color:red}")
        self.statusBar().hide()
        try:
            self.SetTableWidgetColumns()
            self.SetTableWidgetWidth()
            self.dbHandler = dbHelper.DbHelper(configJson)
        except:
            self.label_5.setText("配置文件未设定！")
            self.label_5.setStyleSheet("QLabel{color:red}")
        self.pushButton_3.clicked.connect(self.close)
        self.progressBar.hide()
        self.pushButton_2.clicked.connect(self.GetDbQueryResultDic)

    def ExportToXls(self):
        try:
            if self.tableWidget.rowCount() > 1:
                dateSectionStr = self.dateEdit.date().toPyDate().strftime("%y-%m-%d") + "~" + \
                    self.dateEdit_2.date().toPyDate().strftime("%y-%m-%d")
                filename = QtWidgets.QFileDialog.getSaveFileName(
                    self, "导出到Excel", configJson["Line"]["name"] + "包装回收数据导出" + dateSectionStr + ".xls", "Excel文件(*.xls)")
                if filename[0] != '':
                    self.excelHandler = exportHelper.ExportXlsHelper(
                        filename[0])
                    self.excelHandler.qtTableWidgetExportToXls(
                        self, configJson["Line"]["name"] + "不良统计@" + dateSectionStr)
                    self.label_5.setStyleSheet("QLabel{color:green}")
                    self.label_5.setText("月不良记录导出成功")
                    self.label_5.setFont(light_20_font)
            else:
                self.label_5.setFont(light_14_font)
                self.label_5.setStyleSheet("QLabel{color:blue}")
                self.label_5.setText('无数据,请先点击“查询”\n将结果导出')
        except:
            traceback.print_exc()
            self.label_5.setFont(light_14_font)
            self.label_5.setStyleSheet("QLabel{color:red}")
            self.label_5.setText('数据导出失败，请重试或联系 IT 处理')

    def GetDbQueryResultDic(self):
        self.label_5.setText("")
        try:
            self.tableWidget.clearContents()
            results = self.dbHandler.GetMonthDataResult(self.dateEdit.date().toString(
                'yyyyMMdd'), self.dateEdit_2.date().toString('yyyyMMdd'))
            self.tableWidget.setRowCount(len(results) + 1)
            self.tableWidget.verticalHeader().setHidden(True)
            for j in range(len(results)):
                for keyName in results[j].keys():
                    for i in range(self.tableWidget.columnCount()):
                        if keyName == self.tableWidget.horizontalHeaderItem(i).text():
                            newItem = QTableWidgetItem(
                                str(results[j][keyName]))
                            newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                            self.tableWidget.setItem(j, i, newItem)
                            break
            for i in range(self.tableWidget.columnCount()):
                count = 0
                if i == 0:
                    newItem = QTableWidgetItem("合计")
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, i, newItem)
                else:
                    isPercent = False
                    for j in range(self.tableWidget.rowCount()):
                        cell = self.tableWidget.item(j, i)
                        if cell != None and "%" not in cell.text():
                            count = count + int(cell.text())
                        if cell != None and "%" in cell.text():
                            count = count + float(cell.text().strip("%"))
                            isPercent = True
                    if isPercent != True:
                        newItem = QTableWidgetItem(str(count))
                    else:
                        defTotal = float(self.tableWidget.item(
                            (self.tableWidget.rowCount() - 1), i-2).text())
                        inputTotal = float(self.tableWidget.item(
                            (self.tableWidget.rowCount() - 1), i-1).text())
                        newItem = QTableWidgetItem(
                            str(round(defTotal / inputTotal * 100, 1)) + "%")
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(
                        self.tableWidget.rowCount() - 1, i, newItem)
        except:
            traceback.print_exc()
            self.label_5.setFont(light_20_font)
            self.label_5.setText("出错，无法连接数据库，请联系 IT 处理！")
            self.label_5.setStyleSheet("QLabel{color:red}")

    def SetTableWidgetColumns(self):
        self.tableWidget.setColumnCount(12)
        itemList = ['日期']
        for defName in list(configJson["DefReasons"].values()):
            itemList.append(defName)
        itemList.extend(['合计', '投料', '回收率', '包装'])
        for i in range(12):
            item = QtWidgets.QTableWidgetItem(itemList[i])
            item.setFont(light_14_font)
            self.tableWidget.setHorizontalHeaderItem(i, item)

    def SetTableWidgetWidth(self):
        for header_item_index in range(self.tableWidget.columnCount()):
            # 判断列表头字符数量，大于 4 个中文字符的将按实际内容适应宽度，其余的拉伸占满宽度
            if len(self.tableWidget.horizontalHeaderItem(header_item_index).text()) < 4:
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    header_item_index, QtWidgets.QHeaderView.Stretch)
            else:
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    header_item_index, QtWidgets.QHeaderView.ResizeToContents)

# 数量更正窗口类


class CountAdjustmentWindow(QDialog):
    updateSignal = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(CountAdjustmentWindow, self).__init__(parent)
        self.child = countAdjustment.Ui_Dialog()
        self.child.setupUi(self)
        self.child.pushButton.clicked.connect(self.InsertIntoDbAdjustingCount)
        self.child.pushButton_2.clicked.connect(
            self.InsertIntoDbAdjustingCount)
        self.child.lineEdit_2.textChanged.connect(
            self.ClearInputLineEditContent)
        self.child.lineEdit.textChanged.connect(self.ClearPackLineEditContent)
        self.dbHandler = dbHelper.DbHelper(configJson)
        self.GetDataFillLabel()

    def GetDataFillLabel(self):
        try:
            self.child.label_2.setText(configJson["Line"]["name"])
            self.child.label_10.setText(
                datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            totalDic = self.dbHandler.GetRealTimeTotals()
            self.child.label_4.setText(totalDic["投料"])
            self.child.label_7.setText(totalDic["包装"])
        except:
            traceback.print_exc()
            self.child.label_4.setText("")
            self.child.label_7.setText("")

    def ClearInputLineEditContent(self):
        self.child.lineEdit.setText("")

    def ClearPackLineEditContent(self):
        self.child.lineEdit_2.setText("")

    def InsertIntoDbAdjustingCount(self):
        inputCount = 0
        packCount = 0
        try:
            self.child.label_11.setText("")
            self.child.label_11.setStyleSheet("QLabel{color:green}")
            self.child.label_11.setFont(light_14_font)
            inputCount = int(self.child.lineEdit.text()
                             ) if self.child.lineEdit.text() != '' else 0
            packCount = int(self.child.lineEdit_2.text()
                            ) if self.child.lineEdit_2.text() != '' else 0
            if inputCount > 0:
                inputCount = inputCount - int(self.child.label_4.text())
                self.dbHandler.InsertAdjustingDataToDb(["投料", inputCount])
                self.child.label_11.setText("投料修正保存成功")
                self.updateSignal.emit()
            if packCount > 0:
                packCount = packCount - int(self.child.label_7.text())
                self.dbHandler.InsertAdjustingDataToDb(["包装", packCount])
                self.child.label_11.setText("包装修正保存成功")
                self.updateSignal.emit()
            self.GetDataFillLabel()
        except:
            traceback.print_exc()
            self.child.label_11.setText("保存修正数据失败")
            self.child.label_11.setStyleSheet("QLabel{color:red}")
            self.child.label_11.setFont(light_14_font)

# 缴库量输入窗口类


class UserInputWindow(QDialog):
    def __init__(self, parent=None):
        super(UserInputWindow, self).__init__(parent)
        self.child = userInput.Ui_Dialog()
        self.child.setupUi(self)
        self.child.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.SetTableWidgetHeaderWidth()
        self.child.lineEdit.setValidator(QtGui.QIntValidator())

    def SetTableWidgetHeaderWidth(self):
        for header_item_index in range(self.child.tableWidget.columnCount()):
            self.child.tableWidget.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)

# 主窗口类


class MyMainForm(QMainWindow, mainForm.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        if configJson["Line"] != None:
            self.label_12.setText(configJson["Line"]["name"])

        if "Chart" in configJson:
            self.comboBox_3.setCurrentIndex(configJson["Chart"]["time"])
            self.comboBox_2.setCurrentIndex(configJson["Chart"]["section"])
            self.comboBox.setCurrentIndex(configJson["Chart"]["type"])
            # self.checkBox.setChecked(configJson["Chart"]["halfhour"])
            # print(configJson["Chart"]["halfhour"])
            if configJson["Chart"]["halfhour"]:
                self.checkBox.setEnabled(True)
                self.checkBox.setChecked(True)

        self.tableWidget.verticalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.ResizeToContents)
        self.label_15.setText(
            QtCore.QDateTime.currentDateTime().toString("M月d日"))
        self.statusbar.setFont(light_14_font)
        self.tableWidget.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:lightblue;color: black;padding-left: 4px;border: 1px solid#6c6c6c;}")
        self.tableWidget_2.horizontalHeader().setStyleSheet(
            "QHeaderView::section{background-color:lightblue;color: black;padding-left: 4px;border: 1px solid#6c6c6c;}")
        self.tableWidget.verticalHeader().setHidden(True)
        self.tableWidget_2.verticalHeader().setHidden(True)
        self.actionSectionSet.triggered.connect(
            self.CreateSectionSettingsWindow)
        # 自定义工作时间段设定窗口，现在已根据起止时间自动分片，故取消此界面
        # self.actionWorkingTimeSet_2.triggered.connect(
        #     self.CreateWorkingTimeSetWindow)
        self.actionWorkRestTimeSet.triggered.connect(
            self.CreateWorkRestTimeSettingWindow)
        self.actionInfoSet.triggered.connect(self.CreateLineSettingsWindow)
        self.actionDbSet.triggered.connect(self.CreateDbSettingsWindow)
        self.pushButton_4.clicked.connect(self.CreateDailyStasticForm)
        self.pushButton_2.clicked.connect(self.CreateMonthlyStasticForm)
        # 缴库量在现有系统上并无意义，故暂时不启用，后期如有需求取消注释即可加载缴库量输入界面
        # self.pushButton_3.clicked.connect(self.CreateUserInputWindow)
        self.pushButton_3.hide()
        self.pushButton.clicked.connect(self.CreateCountAdjustmentWindow)
        self.pushButton_7.clicked.connect(self.CreateTargetSettingWindow)
        self.tabWidget.currentChanged.connect(self.RefreshRealtimeData)
        self.pushButton_6.clicked.connect(self.ExportQcDefsToXls)
        self.comboBox_2.currentTextChanged.connect(self.ChangeComboBoxItems)
        self.comboBox.currentTextChanged.connect(self.ChangeComboBoxItems)
        self.comboBox_3.currentTextChanged.connect(self.ChangeComboBoxItems)
        self.checkBox.clicked.connect(self.ChangeCheckBoxChecked)
        self.pushButton_5.clicked.connect(self.SaveChartToFile)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.dbHandler = dbHelper.DbHelper(configJson)

        self.thread = QtCore.QThread()
        self.zeromqListener = mqHelper.ZMQListener()
        self.zeromqListener.moveToThread(self.thread)

        self.RefreshTabPage2Data()

        if configJson["MySQL"] is not None and configJson["Line"] is not None:
            self.thread.started.connect(self.zeromqListener.loop)
        self.zeromqListener.message.connect(self.ZMQReceived)

        QtCore.QTimer.singleShot(0, self.thread.start)

        self.clockTimer = QtCore.QTimer(self)
        self.clockTimer.timeout.connect(self.Showtime)
        self.clockTimer.start(100)
    
    def SaveChartToFile(self):
        dateSectionStr = datetime.datetime.now().strftime("%y-%m-%d")
        filename = QtWidgets.QFileDialog.getSaveFileName(
            self, "保存到文件", configJson["Line"]["name"] + "不良回收情况" + dateSectionStr + ".png", "PNG图像(*.png)")
        if filename[0] != '':
            plt.savefig(filename[0])
            self.label_13.setStyleSheet("QLabel{color:green}")
            self.label_13.setText("不良明细导出成功")
            self.label_13.setFont(light_20_font)
    
    def ChangeComboBoxItems(self):
        global config, configJson
        if self.comboBox_3.currentText() == "全天":
            self.checkBox.setChecked(False)
            self.checkBox.setEnabled(False)
        else:
            self.checkBox.setEnabled(True)
        configJson["Chart"] = {} if "Chart" not in configJson else configJson["Chart"]
        configJson["Chart"]["section"] = self.comboBox_2.currentIndex()
        configJson["Chart"]["halfhour"] = self.checkBox.isChecked()
        configJson["Chart"]["type"] = self.comboBox.currentIndex()
        configJson["Chart"]["time"] = self.comboBox_3.currentIndex()
        config.SaveConfigToJson(configJson)
        self.RefreshRealtimeData()
    
    def ChangeCheckBoxChecked(self):
        global config, configJson
        configJson["Chart"]["halfhour"] = self.checkBox.isChecked()
        config.SaveConfigToJson(configJson)
        self.RefreshRealtimeData()

    def ZMQReceived(self, message):
        self.statusbar.showMessage(message)
        self.RefreshRealtimeData()

    def CloseEvent(self, event):
        self.zeromqListener.running = False
        self.thread.quit()
        self.thread.wait()

    def RefreshRealtimeData(self):
        self.label_13.setText("")
        if self.tabWidget.currentIndex() == 1:
            self.RefreshTabPage2Data()
        elif self.tabWidget.currentIndex() == 2:
            self.label_13.setText("")
            self.RefreshTabPage3Data()
        else:
            self.verticalLayout_5.removeWidget(self.canvas)
            sip.delete(self.canvas)
            # self.figure = plt.figure()
            self.canvas = FigureCanvas(self.figure)
            self.plot_()
            self.verticalLayout_5.addWidget(self.canvas)

    def RefreshTabPage3Data(self):
        try:
            self.page3DataList = self.dbHandler.GetCurrentQcDefData()
            self.tableWidget_2.setRowCount(len(self.page3DataList))
            for i in range(len(self.page3DataList)):
                newItem = QTableWidgetItem(self.page3DataList[i][0])
                newItem.setFont(light_20_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, 0, newItem)
                newItem = QTableWidgetItem(self.page3DataList[i][1])
                newItem.setFont(light_20_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, 1, newItem)
                newItem = QTableWidgetItem(self.page3DataList[i][2])
                newItem.setFont(light_20_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, 2, newItem)
                newItem = QTableWidgetItem(self.page3DataList[i][3])
                newItem.setFont(light_20_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, 3, newItem)
                newItem = QTableWidgetItem(self.page3DataList[i][4])
                newItem.setFont(light_20_font)
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget_2.setItem(i, 4, newItem)
                subSum = 0
                for j in range(self.tableWidget_2.columnCount()):
                    if j != self.tableWidget_2.columnCount() - 1 and j != 0:
                        count = int(self.tableWidget_2.item(i, j).text(
                        )) if self.tableWidget_2.item(i, j) != None else 0
                        subSum += count
                    elif j == self.tableWidget_2.columnCount() - 1:
                        newItem = QTableWidgetItem(str(subSum))
                        newItem.setFont(light_20_font)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        # print(i, j)
                        self.tableWidget_2.setItem(i, j, newItem)
            if self.tableWidget_2.rowCount() > 0:
                self.tableWidget_2.setRowCount(
                    self.tableWidget_2.rowCount() + 1)
                for j in range(self.tableWidget_2.columnCount()):
                    if j == 0:
                        newItem = QTableWidgetItem("合计")
                        newItem.setFont(light_20_font)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tableWidget_2.setItem(
                            self.tableWidget_2.rowCount() - 1, j, newItem)
                    else:
                        count = 0
                        for i in range(self.tableWidget_2.rowCount() - 1):
                            count += int(self.tableWidget_2.item(i, j).text())
                        newItem = QTableWidgetItem(str(count))
                        newItem.setFont(light_20_font)
                        newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                        self.tableWidget_2.setItem(
                            self.tableWidget_2.rowCount() - 1, j, newItem)
            self.tableWidget_2.resizeRowsToContents()
        except:
            traceback.print_exc()

    def RefreshTabPage2Data(self):
        try:
            self.totalDic = self.dbHandler.GetRealTimeTotals()
            self.label_2.setText(
                self.totalDic["回收"] if self.totalDic["回收"] != 'None' else '0')
            self.label_4.setText(
                self.totalDic["投料"] if "投料" in self.totalDic.keys() else '0')
            self.label_9.setText(
                self.totalDic["包装"] if "包装" in self.totalDic.keys() else '0')
            totalInput = float(
                self.totalDic["投料"] if "投料" in self.totalDic.keys() else '0')
            totalDef = float(
                self.totalDic["回收"] if self.totalDic["回收"] != 'None' else '0')
            if totalInput > 0:
                defRate = round(totalDef / totalInput * 100, 2)
                self.label_6.setText(str(defRate) + "%")
            else:
                self.label_6.setText("0.00%")
            self.tableWidget.clearContents()
            realtimeData = self.dbHandler.GetRealTimeDefDatas()
            self.tableWidget.setRowCount(len(realtimeData.keys()))
            for id in range(len(realtimeData.keys())):
                newItem = QTableWidgetItem(str(id + 1))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(id, 0, newItem)
                newItem = QTableWidgetItem(str(list(realtimeData.keys())[id]))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(id, 1, newItem)
                count = int(realtimeData[list(realtimeData.keys())[id]])
                newItem = QTableWidgetItem(str(count))
                newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidget.setItem(id, 2, newItem)
                if totalDef > 0 and count > 0:
                    newItem = QTableWidgetItem(
                        str(round((count / totalDef * 100), 1)) + "%")
                    newItem.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.tableWidget.setItem(id, 3, newItem)
        except:
            traceback.print_exc()
            self.tabWidget.blockSignals(True)
            self.zeromqListener.blockSignals(True)
            self.statusBar().showMessage("数据库服务器连接异常，请关闭程序再打开，如仍然无法正常使用，请联系 IT 处理")

    def ExportQcDefsToXls(self):
        if self.tableWidget_2.rowCount() > 0:
            dateSectionStr = datetime.datetime.now().strftime("%y-%m-%d")
            filename = QtWidgets.QFileDialog.getSaveFileName(
                self, "导出到Excel", configJson["Line"]["name"] + "日不良明细导出" + dateSectionStr + ".xls", "Excel文件(*.xls)")
            if filename[0] != '':
                self.excelHandler = exportHelper.ExportXlsHelper(
                    filename[0])
                self.excelHandler.qtTableWidgetExportToXls(
                    self.tableWidget_2, configJson["Line"]["name"] + "不良明细@" + dateSectionStr, False, True)
                self.label_13.setStyleSheet("QLabel{color:green}")
                self.label_13.setText("不良明细导出成功")
                self.label_13.setFont(light_20_font)
        else:
            self.label_13.setFont(light_14_font)
            self.label_13.setStyleSheet("QLabel{color:blue}")
            self.label_13.setText('无数据')

    def Showtime(self):
        datetime = QtCore.QDateTime.currentDateTime()
        self.label_7.setText(datetime.toString("HH:mm:ss"))

    def CreateLineSettingsWindow(self):
        self.lineSettingsWindow = LineSettingsWindow(self)
        self.lineSettingsWindow.updateSignal.connect(
            self.ChangeLineNameEffection)
        self.lineSettingsWindow.exec()

    def ChangeLineNameEffection(self):
        self.label_12.setText(configJson["Line"]["name"])
        self.dbHandler.lineName = configJson["Line"]["name"]
        self.RefreshRealtimeData()

    def CreateWorkRestTimeSettingWindow(self):
        self.workRestTimeSettingWindow = WorkRestTimeSettingWindow(self)
        self.workRestTimeSettingWindow.exec()

    def CreateTargetSettingWindow(self):
        self.targetSetWindow = TargetSettingWindow(self)
        self.targetSetWindow.exec()

    def CreateWorkingTimeSetWindow(self):
        self.workingTimeSetWindow = WorkingtimeSettingsWindow(self)
        self.workingTimeSetWindow.exec()

    def CreateCountAdjustmentWindow(self):
        self.countAdjustmentWindow = CountAdjustmentWindow(self)
        self.countAdjustmentWindow.updateSignal.connect(
            self.RefreshTabPage2Data)
        self.countAdjustmentWindow.exec()

    def CreateUserInputWindow(self):
        self.userInputWindow = UserInputWindow(self)
        self.userInputWindow.exec()

    def CreateDbSettingsWindow(self):
        self.dbSettingWindow = DbSettingsWindow(self)
        self.dbSettingWindow.exec()

    def CreateSectionSettingsWindow(self):
        self.sectionSettingsWindow = SectionSettingWindow(self)
        self.sectionSettingsWindow.exec()

    def CreateDailyStasticForm(self):
        self.dailyStasticForm = DailyDefStasticForm(self)
        self.dailyStasticForm.show()

    def CreateMonthlyStasticForm(self):
        self.monthlyStasticForm = MonthlyDefStasticForm(self)
        self.monthlyStasticForm.show()

    def SetTableWidgetColumnHeaderStretchMode(self):
        for header_item_index in range(self.tableWidget.columnCount()):
            # 以下注释的内容为更改表头字体颜色，取消注释并更改 Qt.magenta 为指定颜色即可
            # headItem = self.tableWidget.horizontalHeaderItem(header_item_index)
            # headItem.setForeground(QtGui.QBrush(Qt.magenta))
            self.tableWidget.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)
        for header_item_index in range(self.tableWidget_2.columnCount()):
            self.tableWidget_2.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)

    def plot_(self):
        self.drawingChart = DrawingChart(self.figure, self.canvas)
        self.filterList = []
        if self.comboBox_2.currentText() != "整线不良":
            if self.comboBox_2.currentText() == "入楦段不良":
                self.filterList = list(configJson["Section"]["ruxuan"].values())
            elif self.comboBox_2.currentText() == "包装段不良":
                self.filterList = list(configJson["Section"]["baozhuang"].values())
            elif self.comboBox_2.currentText() == "贴底段不良":
                self.filterList = list(configJson["Section"]["tiedi"].values())
        # print(self.filterList)
        self.isHalfDay = False
        if self.comboBox_3.currentText() == "半天":
            self.isHalfDay = True
        if len(self.filterList) >0:
            self.drawingChart.GetDrawDatas(self.isHalfDay, self.checkBox.isChecked(),self.filterList)
        else:
            self.drawingChart.GetDrawDatas(self.isHalfDay,self.checkBox.isChecked())
        if len(self.drawingChart.currentData) > 0:
            self.pushButton_5.setEnabled(True)
        if self.comboBox.currentText() == "线状图":
            self.drawingChart.DrawLineChart()
        else:
            self.drawingChart.DrawBarChart()
        self.canvas = self.drawingChart.canvas

    def AddLineChartToForm(self):
        self.plot_()
        self.verticalLayout_5.addWidget(self.canvas)

    def GetSystemDefinitionToChangeFontSizeAndLabelSize(self):
        # 获取系统分辨率更改 label 尺寸及字体大小
        # 先设定各个 label 字体不同颜色
        self.label_2.setStyleSheet("QLabel{color: red}")
        self.label_4.setStyleSheet("QLabel{color:blue}")
        self.label_6.setStyleSheet("QLabel{color:pink}")
        self.label_9.setStyleSheet("QLabel{color:green}")
        self.label_7.setStyleSheet("QLabel{color:purple}")
        self.label_15.setStyleSheet("QLabel{color:purple}")
        # 从系统分辨率中提取桌面高度
        height = QApplication.desktop().screenGeometry().height()
        # 高度小于 1000，字体及高度都修改为20, 修改 frame 宽度为 150，高度为 530
        if height <= 1000:
            self.resize(1000, 700)
            self.label_7.setMaximumHeight(28)
            self.label_15.setMaximumHeight(28)
            self.frame.setMinimumSize(QtCore.QSize(200, 500))
            self.frame.setMaximumWidth(200)
            labels = ('label_2', 'label_4', 'label_6',
                      'label_7', 'label_9', 'label_15')
            for label_name in labels:
                label = self.frame.findChild((QtWidgets.QLabel), label_name)
                label.setFont(bold_20_font)
                label.setMinimumSize(QtCore.QSize(16777215, 28))
            labels = ('label', 'label_3', 'label_5', 'label_8')
            # self.label_15.setVisible(False)
            for label_name in labels:
                label = self.frame.findChild((QtWidgets.QLabel), label_name)
                label.setFont(light_20_font)
                label.setMinimumSize(QtCore.QSize(16777215, 28))


class TimeManipulation():
    def __init__(self, day=datetime.datetime.now()):
        global configJson
        self.day = day
        self.amTimeStart = "08:00"
        self.amTimeStop = "11:30"
        self.pmTimeStart = "13:00"
        self.pmTimeStop = "17:00"
        if configJson["Line"] != None:
            lineSetting = configJson["Line"]
            self.amTimeStart = lineSetting["amStart"]
            self.amTimeStop = lineSetting["amStop"]
            self.pmTimeStart = lineSetting["pmStart"]
            self.pmTimeStop = lineSetting["pmStop"]
            self.ConvertSettingToTimeObj()

    def ConvertSettingToTimeObj(self):
        today = self.day.strftime("%Y-%m-%d")
        self.amTimeStart = datetime.datetime.strptime(
            today + " " + str(self.amTimeStart), "%Y-%m-%d %H:%M")
        self.amTimeStop = datetime.datetime.strptime(
            today + " " + str(self.amTimeStop), "%Y-%m-%d %H:%M")
        self.pmTimeStart = datetime.datetime.strptime(
            today + " " + str(self.pmTimeStart), "%Y-%m-%d %H:%M")
        self.pmTimeStop = datetime.datetime.strptime(
            today + " " + str(self.pmTimeStop), "%Y-%m-%d %H:%M")

    def DayHourRange(self, frequency):
        amTimeRange = list(pd.date_range(
            self.amTimeStart, self.amTimeStop, freq="%sS" % frequency))
        if self.amTimeStop not in amTimeRange:
            amTimeRange.append(self.amTimeStop)
        pmTimeRange = list(pd.date_range(
            self.pmTimeStart, self.pmTimeStop, freq="%sS" % frequency))
        if self.pmTimeStop not in pmTimeRange:
            pmTimeRange.append(self.pmTimeStop)
        amTimeRange = [item.strftime("%Y-%m-%d %H:%M:%S")
                       for item in amTimeRange]
        pmTimeRange = [item.strftime("%Y-%m-%d %H:%M:%S")
                       for item in pmTimeRange]
        self.amTimeRanges = self.CalculatingWorkingTimeRanges(
            amTimeRange, self.amTimeStop, frequency)
        self.pmTimeRanges = self.CalculatingWorkingTimeRanges(
            pmTimeRange, self.pmTimeStop, frequency)
        self.dailyTimeRanges = []
        self.dailyTimeRanges.extend(self.amTimeRanges)
        self.dailyTimeRanges.extend(self.pmTimeRanges)
        # 注意：这里返回的 amTimeRanges 是全天的时间切片，已经 extend 了下午的时间切片列表
        return self.dailyTimeRanges

    def CalculatingWorkingTimeRanges(self, timeRange, stopTime, frequency):
        timeRanges = []
        for item in timeRange:
            f_time = datetime.datetime.strptime(item, "%Y-%m-%d %H:%M:%S")
            t_time = (f_time + datetime.timedelta(seconds=frequency))
            if t_time >= stopTime:
                timeRanges.append([f_time, stopTime])
                break
            timeRanges.append([f_time, t_time])
        return timeRanges

    def OnCurrentTimeRanges(self, isHalfHour, isHalfDay= False):
        unit = 60*30 if isHalfHour else 60*60
        timeSlice = []
        if isHalfHour:
            self.DayHourRange(unit)
            if datetime.datetime.now() > self.pmTimeStart:
                for item in self.pmTimeRanges:
                    if item[1] - item[0] < datetime.timedelta(seconds=30*60):
                        timeSlice[-1][1] = item[1]
                        break
                    if item[0] < datetime.datetime.now():
                        timeSlice.append(item)
                    else:
                        break
            elif datetime.datetime.now() < self.pmTimeStart:
                for item in self.amTimeRanges:
                    if item[1] - item[0] < datetime.timedelta(seconds=30*60):
                        timeSlice[-1][1] = item[1]
                        break
                    if item[0] < datetime.datetime.now():
                        timeSlice.append(item)
                    else:
                        break
        elif isHalfDay:
            self.DayHourRange(unit)
            if datetime.datetime.now() < self.pmTimeStart:
                for item in self.amTimeRanges:
                    if item[0] < datetime.datetime.now():
                        timeSlice.append(item)
                    else:
                        break
            else:
                for item in self.pmTimeRanges:
                    if item[0] < datetime.datetime.now():
                        timeSlice.append(item)
                    else:
                        break
        else:
            for item in self.DayHourRange(unit):
                if item[0] < datetime.datetime.now():
                    timeSlice.append(item)
                else:
                    break
        return timeSlice

    def CalculatingTotalWorkTime(self):
        self.amTotalHours = (self.amTimeStop - self.amTimeStart).seconds / 3600
        self.pmTotalHours = (self.pmTimeStop - self.pmTimeStart).seconds / 3600
        self.totalHours = float(self.amTotalHours + self.pmTotalHours)


class DrawingChart(QtCore.QObject):
    def __init__(self, figure, canvas):
        super(DrawingChart, self).__init__()
        self.figure = figure
        self.canvas = canvas
        self.dbHandler = dbHelper.DbHelper(configJson)
        self.timeOpt = TimeManipulation()

    def GetDrawDatas(self, isHalfDay = False, isHalfHour=False, section = None):
        try:
            self.currentTimeSliceList = self.timeOpt.OnCurrentTimeRanges(
                isHalfHour) if isHalfDay == False else self.timeOpt.OnCurrentTimeRanges(isHalfHour, isHalfDay)
            self.currentData = self.dbHandler.GetDailyDataResults(
                self.currentTimeSliceList) 
            if section != None:
                sectionData = []
                for item in self.currentData:
                    if item[0] in section:
                        sectionData.append(item)
                self.currentData = sectionData
            self.currentTimeSliceListToLabels = []
            for item in self.currentTimeSliceList:
                startTime = item[0].strftime("%H:%M")
                stopTime = item[1].strftime("%H:%M")
                period = startTime + "\n"  + stopTime
                self.currentTimeSliceListToLabels.append(period)
        except:
            self.currentTimeSliceListToLabels = []
            self.currentData = []
        

    def DrawBarChart(self):
        plt.cla()
        plt.clf()
        ax = self.figure.add_subplot(111)
        xlabels = self.currentTimeSliceListToLabels
        dataList = self.currentData
        colCount = len(xlabels)
        if colCount > 0:
            self.figure.set_tight_layout(True)
            ax.set_ylabel('回收量')
            ax.set_title('各时段回收情况', fontsize='18', fontweight='bold',
                     color='black', loc='center',bbox={'facecolor': '0.8', 'pad': 5})
            x = np.arange(colCount)
            # print(x)
            widthList = [0.25, 0.25, 0.4, 0.5, 0.65, 0.75, 0.95, 1.08, 1.22, 1.25]
            if len(dataList) < 6:
                widthList = [x * 2 for x in widthList]
            total_width, n = widthList[colCount -1 ], colCount
            width = total_width / n
            x = x - (total_width - width) / 2
            width_times = 0
            label_pos = 3 if len(dataList) > 6 else 1
            fontSize = [12, 12, 10, 9, 9, 8, 6.5, 6.5, 6.5, 6]
            x_offset = [[0, 0.25, 0.5, 0.75, 1, 1.26, 1.5],[0, 0.13, 0.24, 0.37, 0.5, 0.63, 0.76], 
                        [0, 0.12, 0.26, 0.4, 0.52, 0.67, 0.79], [0, 0.12, 0.25, 0.37,0.5, 0.62, 0.74],
                        [0, 0.12, 0.26, 0.39, 0.52, 0.64, 0.77],[0, 0.12, 0.25, 0.37, 0.5, 0.62, 0.75],
                        [0, 0.12, 0.27, 0.40, 0.54, 0.68, 0.8],[0, 0.12, 0.27, 0.40, 0.54, 0.68, 0.8], 
                        [0, 0.12, 0.27, 0.40, 0.54, 0.68, 0.8],[0, 0.12, 0.25, 0.37, 0.5, 0.63, 0.75]]

            col_three_x_offset = [[0, 0.5, 1.0],[0, 0.25, 0.5], 
                        [0, 0.26, 0.52], [0, 0.25, 0.5],
                        [0, 0.26, 0.52],[0, 0.25, 0.5],
                        [0, 0.26, 0.52],[0, 0.25, 0.5], 
                        [0, 0.26, 0.54],[0, 0.25, 0.5]]    
            if len(dataList)  < 6:
                x_offset = col_three_x_offset
                for f_size in fontSize:
                    if f_size < 9:
                        fontSize[fontSize.index(f_size)] = 9
            for dataItem in dataList:
                data_index = dataList.index(dataItem)
                labelText = dataItem.pop(0)
                addWidth = width * width_times
                if data_index == label_pos:
                    plt.bar(x + addWidth, dataItem, width=width,
                            label=labelText,  tick_label=xlabels)
                else:
                    plt.bar(x + addWidth, dataItem, width=width, label=labelText)
                for a, b in zip(x, dataItem):
                    if b > 0:
                        plt.text(a + x_offset[colCount -1][dataList.index(dataItem)], float(b), '%.0f' %
                                b, ha='center', va='bottom', fontsize=fontSize[colCount - 1])
                width_times += 1
            # ax.set_xticklabels(xlabels)
            plt.legend(loc=2)
            self.canvas.draw()

    def DrawLineChart(self):
        plt.cla()
        plt.clf()
        # xlabels = [ x.replace('\n','') for x in self.currentTimeSliceListToLabels]
        xlabels = self.currentTimeSliceListToLabels
        colCount = len(xlabels)
        ax = self.figure.add_axes([0.1,0.1,0.85,0.8])
        self.figure.set_tight_layout(False)

        if colCount > 0:
            ax.set_title('各时段回收情况', fontsize='18', fontweight='bold',
                     color='black', loc='center',bbox={'facecolor': '0.8', 'pad': 5})
            ax.set_ylabel('回收量')
            dataList = self.currentData
            for dataItem in dataList:
                countData = dataItem[1:]
                ax.plot(xlabels, countData, lineWidth=1, lineStyle="-", label=dataItem[0], marker='.')
                for a, b in list(zip(xlabels, dataItem[1:])):
                    plt.annotate("%s" % b, (a, b), xytext=(-3, 3),
                    ha='left', textcoords='offset points')
            plt.legend(loc=2)
            ax.grid()
            ax.set_xticklabels(xlabels)

        # ax.plot(x, a, color='red', lineWidth=1,
        #         linestyle="-", label="脱胶", marker='.')
        # ax.plot(x, b, color="green", linewidth=1,
        #         linestyle='-', label="高胶", marker=".")
        # ax.plot(x, c, color="magenta", linewidth=1,
        #         linestyle='-', label="其他", marker=".")
        # ax.plot(x, d, color="blue", linewidth=1,
        #         linestyle='-', label="清洁度", marker=".")
        # ax.plot(x, e, color="purple", linewidth=1,
        #         linestyle='-', label="不对称", marker=".")
        # ax.plot(x, f, color="orange", linewidth=1,
        #         linestyle='-', label="针车不良", marker=".")
        # ax.plot(x, g, color="navy", linewidth=1,
        #         linestyle='-', label="研磨线外露", marker=".")
        # plt.style.use('Solarize_Light2')
        # plt.style.use('seaborn')
        # plt.xlabel("时间段")
        # plt.ylabel("回收量")
        # self.figure.set_tight_layout(True)
        # for x, y, z, f, g, h, i, j in list(zip(x, a, b, c, d, e, f, g)):
        #     plt.annotate("%s" % y, (x, y), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        #     plt.annotate("%s" % z,  (x, z), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        #     plt.annotate("%s" % f,  (x, f), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        #     plt.annotate("%s" % g,  (x, g), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        #     plt.annotate("%s" % h,  (x, h), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        #     plt.annotate("%s" % i,  (x, i), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        #     plt.annotate("%s" % j,  (x, j), xytext=(-10, 13),
        #                  ha='left', textcoords='offset points')
        # ax.set_title('各时段回收量', fontsize='18', fontweight='bold',
        #              color='black', loc='center')
        
        # ax.set_xticklabels(labels)
        self.canvas.draw()


if __name__ == "__main__":
    if configJson["Admin"] == None:
        configJson["Admin"] = {"password": "sysadmin"}

    # test = DrawingChart()
    # test.GetDrawDatas()

    app = QApplication(sys.argv)
    mywin = MyMainForm()
    mywin.SetTableWidgetColumnHeaderStretchMode()
    mywin.GetSystemDefinitionToChangeFontSizeAndLabelSize()
    mywin.show()
    mywin.AddLineChartToForm()
    sys.exit(app.exec_())
