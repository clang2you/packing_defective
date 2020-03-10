import sys
import os
import pytz
import datetime
import dateutil
import pandas as pd
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

matplotlib.use("Qt5Agg")
utc=pytz.UTC

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
        self.SetTableWidgetHeaderWidth()

    def SetTableWidgetHeaderWidth(self):
        for header_item_index in range(self.child.tableWidget.columnCount()):
            self.child.tableWidget.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)

# 线别、不良类型及工作时段设定窗口类


class LineSettingsWindow(QDialog):
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
        self.child.label_13.setFont(light_14_font)
        self.child.label_13.setText("设定保存完成")
        self.child.label_13.setStyleSheet("QLabel{color: green}")

# 日不良统计窗口类


class DailyDefStasticForm(QMainWindow, dailyDefStasticForm.Ui_MainWindow):
    def __init__(self, parent=None):
        super(DailyDefStasticForm, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label_2.setStyleSheet("QLabel{color:green}")
        self.statusBar().hide()
        self.SetTableWidgetWidth()
        self.pushButton.clicked.connect(self.close)
        self.progressBar.hide()

    def SetTableWidgetWidth(self):
        for header_item_index in range(self.tableWidget.columnCount()):
            self.tableWidget.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)

# 月不良统计窗口类


class MonthlyDefStasticForm(QMainWindow, monthlyDefStasticForm.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MonthlyDefStasticForm, self).__init__(parent)
        self.setupUi(self)
        self.tableWidget.horizontalHeader().setStyleSheet(
            'QHeaderView{font: 14pt "微软雅黑 Light";border: 1px solid #6c6c6c;}')
        self.dateEdit.setDate(datetime.datetime.now() -
                              dateutil.relativedelta.relativedelta(months=1))
        self.dateEdit_2.setDate(datetime.datetime.now())
        self.tableWidget.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)
        if configJson["Line"] != None:
            self.label_2.setText(configJson["Line"]["name"])
            self.label_2.setStyleSheet("QLabel{color:green}")
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
                    newItem = QTableWidgetItem(str(count)) if isPercent != True else QTableWidgetItem(
                        str(round(count / (self.tableWidget.rowCount() - 1), 1)) + "%")
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
            self.tableWidget.setHorizontalHeaderItem(i, item)

    def SetTableWidgetWidth(self):
        for header_item_index in range(self.tableWidget.columnCount()):
            # 判断列表头字符数量，大于 4 个中文字符的将按实际内容适应宽度
            if len(self.tableWidget.horizontalHeaderItem(header_item_index).text()) < 4:
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    header_item_index, QtWidgets.QHeaderView.Stretch)
            else:
                self.tableWidget.horizontalHeader().setSectionResizeMode(
                    header_item_index, QtWidgets.QHeaderView.ResizeToContents)

# 数量更正窗口类


class CountAdjustmentWindow(QDialog):
    def __init__(self, parent=None):
        super(CountAdjustmentWindow, self).__init__(parent)
        self.child = countAdjustment.Ui_Dialog()
        self.child.setupUi(self)

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
        self.label_15.setText(
            QtCore.QDateTime.currentDateTime().toString("M月d日"))

        self.actionSectionSet.triggered.connect(
            self.CreateSectionSettingsWindow)
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

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

        self.clockTimer = QtCore.QTimer(self)
        self.clockTimer.timeout.connect(self.Showtime)
        self.clockTimer.start(500)

    def Showtime(self):
        datetime = QtCore.QDateTime.currentDateTime()
        self.label_7.setText(datetime.toString("HH:mm:ss"))

    def CreateLineSettingsWindow(self):
        self.lineSettingsWindow = LineSettingsWindow(self)
        self.lineSettingsWindow.exec()

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
        ax = self.figure.add_axes([0.1, 0.1, 0.8, 0.8])
        x = ["08:00", '09:00', '10:00', '11:00', '12: 00',
             '13:00', '14:00', '15:00', '16:00', '17:00']
        y = [0, 2, 0, 0, 0, 0, 0, 0, 0, 0]
        z = [0, 5, 0, 0, 0, 0, 0, 0, 0, 0]
        f = [0, 3, 0, 0, 0, 0, 0, 0, 0, 0]
        g = [0, 0, 4, 0, 0, 0, 0, 0, 0, 0]
        h = [0, 0, 7, 0, 0, 0, 0, 0, 0, 0]
        i = [0, 0, 3, 0, 0, 0, 0, 0, 0, 0]
        j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ax.plot(x, y, color='red', lineWidth=1,
                linestyle="-", label="脱胶", marker='.')
        ax.plot(x, z, color="green", linewidth=1,
                linestyle='-', label="高胶", marker=".")
        ax.plot(x, j, color="magenta", linewidth=1,
                linestyle='-', label="其他", marker=".")
        ax.plot(x, f, color="blue", linewidth=1,
                linestyle='-', label="清洁度", marker=".")
        ax.plot(x, g, color="purple", linewidth=1,
                linestyle='-', label="不对称", marker=".")
        ax.plot(x, h, color="orange", linewidth=1,
                linestyle='-', label="针车不良", marker=".")
        ax.plot(x, i, color="navy", linewidth=1,
                linestyle='-', label="研磨线外露", marker=".")
        plt.style.use('Solarize_Light2')
        # plt.style.use('seaborn')
        plt.xlabel("时间段")
        plt.ylabel("回收量")
        ax.legend(loc=2)
        ax.grid()
        for x, y, z, f, g, h, i, j in list(zip(x, y, z, f, g, h, i, j)):
            plt.annotate("%s" % y, (x, y), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
            plt.annotate("%s" % z,  (x, z), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
            plt.annotate("%s" % f,  (x, f), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
            plt.annotate("%s" % g,  (x, g), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
            plt.annotate("%s" % h,  (x, h), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
            plt.annotate("%s" % i,  (x, i), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
            plt.annotate("%s" % j,  (x, j), xytext=(-10, 13),
                         ha='left', textcoords='offset points')
        ax.set_title('各时段回收量', fontsize='18', fontweight='bold',
                     color='black', loc='center')
        self.canvas.draw()

    def AddLineChartToForm(self):
        self.verticalLayout_5.addWidget(self.canvas)
        self.plot_()

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
            self.label_7.setMaximumHeight(30)
            self.label_15.setMaximumHeight(30)
            self.frame.setMinimumSize(QtCore.QSize(200, 520))
            self.frame.setMaximumWidth(200)
            labels = ('label_2', 'label_4', 'label_6',
                      'label_7', 'label_9', 'label_15')
            for label_name in labels:
                label = self.frame.findChild((QtWidgets.QLabel), label_name)
                label.setFont(bold_20_font)
                label.setMinimumSize(QtCore.QSize(16777215, 20))
            labels = ('label', 'label_3', 'label_5', 'label_8')
            for label_name in labels:
                label = self.frame.findChild((QtWidgets.QLabel), label_name)
                label.setFont(light_20_font)
                label.setMinimumSize(QtCore.QSize(16777215, 20))


class TimeManipulation():
    def __init__(self):
        global configJson
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
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        self.amTimeStart = datetime.datetime.strptime(today + " " + str(self.amTimeStart), "%Y-%m-%d %H:%M")
        self.amTimeStop = datetime.datetime.strptime(today + " " + str(self.amTimeStop), "%Y-%m-%d %H:%M")
        self.pmTimeStart = datetime.datetime.strptime(today + " " + str(self.pmTimeStart), "%Y-%m-%d %H:%M")
        self.pmTimeStop = datetime.datetime.strptime(today + " " + str(self.pmTimeStop), "%Y-%m-%d %H:%M")

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
        self.amTimeRanges.extend(self.pmTimeRanges)
        return self.amTimeRanges

    def CalculatingWorkingTimeRanges(self, timeRange, stopTime, frequency):
        timeRanges = []
        for item in timeRange:
            f_time = datetime.datetime.strptime(item , "%Y-%m-%d %H:%M:%S")
            t_time = (f_time + datetime.timedelta(seconds=frequency))
            if t_time >= stopTime:
                timeRanges.append([f_time, stopTime])
                break
            timeRanges.append([f_time, t_time])
        return timeRanges


if __name__ == "__main__":
    if configJson["Admin"] == None:
        configJson["Admin"] = {"password": "sysadmin"}

    # 测试自定义时间操作类
    timeOperator = TimeManipulation()
    print(timeOperator.DayHourRange(60 * 30))

    app = QApplication(sys.argv)
    mywin = MyMainForm()
    mywin.SetTableWidgetColumnHeaderStretchMode()
    mywin.GetSystemDefinitionToChangeFontSizeAndLabelSize()
    mywin.show()
    mywin.AddLineChartToForm()
    sys.exit(app.exec_())
