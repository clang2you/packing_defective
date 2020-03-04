import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidget, QProgressBar
# from PyQt5.QtCore import Qt
from mainForm import Ui_MainWindow
import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# import numpy as np
from ConfigHelper.config_helper import CfgHelper
from Ui_sectionSettings import Ui_Dialog as section_Ui
from Ui_dailyDefStasticForm import Ui_MainWindow as dailyDef_Ui
from dbSettings import Ui_Dialog as dbSettings_ui
from adminAuthorization import Ui_Dialog as adminPassowrd_ui

matplotlib.use("Qt5Agg")

# 数据库设定窗口类


class DbSettingsWindow(QDialog):
    def __init__(self, parent=None):
        super(DbSettingsWindow, self).__init__(parent)
        self.child = dbSettings_ui()
        self.child.setupUi(self)
        self.config = CfgHelper()
        self.configJson = self.config.cfg_dict
        self.child.pushButton_3.clicked.connect(self.ChangeDbSettings)
        self.child.pushButton.clicked.connect(self.SaveDbSettings)
        self.lineEdits = ['lineEdit', 'lineEdit_2', 'lineEdit_3', 'lineEdit_4']
        self.ChangeLineEditBackgoundColor()
        self.SetLineEditText()

    def SaveDbSettings(self):
        self.configJson["MySQL"] = {'address': self.child.lineEdit.text(), 'user': self.child.lineEdit_2.text(),
                                    'password': self.child.lineEdit_3.text(), 'dbName': self.child.lineEdit_4.text()}
        self.config.SaveConfigToJson(self.configJson)
        self.child.pushButton_3.setEnabled(True)
        self.child.pushButton.setEnabled(False)
        for lineEdit in self.lineEdits:
            edit = self.child.frame.findChild((QtWidgets.QLineEdit), lineEdit)
            edit.setStyleSheet("QLineEdit{background-color:silver}")
            font = QtGui.QFont()
            font.setFamily("微软雅黑 Light")
            font.setPointSize(14)
            font.setWeight(50)
            edit.setFont(font)
            edit.setReadOnly(True)

    def ChangeLineEditBackgoundColor(self):
        for lineEdit in self.lineEdits:
            edit = self.child.frame.findChild((QtWidgets.QLineEdit), lineEdit)
            edit.setStyleSheet("QLineEdit{background-color:silver}")

    def SetLineEditText(self):
        try:
            self.child.lineEdit.setText(
                self.configJson["MySQL"]["address"])
            self.child.lineEdit_2.setText(
                self.configJson["MySQL"]["user"])
            self.child.lineEdit_3.setText(
                self.configJson["MySQL"]["password"])
            self.child.lineEdit_4.setText(
                self.configJson["MySQL"]["dbName"])
        except:
            for lineEdit in self.lineEdits:
                edit = self.child.frame.findChild(
                    (QtWidgets.QLineEdit), lineEdit)
                edit.setText("读取配置出错")

    def ChangeDbSettings(self):
        self.passwordForm = AdminAutorizationForm(self)
        self.passwordForm.child.lineEdit.editingFinished.connect(
            lambda: self.HandlePassword(self.passwordForm.child.lineEdit.text()))
        self.passwordForm.exec()

    def HandlePassword(self, password):
        try:
            if password == self.configJson["Admin"]["password"]:
                self.passwordForm.reject()
                self.child.pushButton.setEnabled(True)
                self.child.pushButton_3.setEnabled(False)
                for lineEdit in self.lineEdits:
                    edit = self.child.frame.findChild(
                        (QtWidgets.QLineEdit), lineEdit)
                    edit.setReadOnly(False)
                    edit.setStyleSheet("QLineEdit{background-color:white}")
                    font = QtGui.QFont()
                    font.setFamily("微软雅黑 Light")
                    font.setPointSize(14)
                    font.setWeight(50)
                    edit.setFont(font)
        except:
            self.passwordForm.reject()
            self.child.pushButton.setEnabled(True)
            self.child.pushButton_3.setEnabled(False)
            for lineEdit in self.lineEdits:
                edit = self.child.frame.findChild(
                    (QtWidgets.QLineEdit), lineEdit)
                edit.setReadOnly(False)
                edit.setStyleSheet("QLineEdit{background-color:white}")
                font = QtGui.QFont()
                font.setFamily("微软雅黑 Light")
                font.setPointSize(14)
                font.setWeight(50)
                edit.setFont(font)

# 管理员权限授权窗口类


class AdminAutorizationForm(QDialog):
    def __init__(self, parent=None):
        super(AdminAutorizationForm, self).__init__(parent)
        self.child = adminPassowrd_ui()
        self.child.setupUi(self)

# 加工线分段信息设定窗口类


class SectionSettingWindow(QDialog):
    def __init__(self, parent=None):
        super(SectionSettingWindow, self).__init__(parent)
        self.child = section_Ui()
        self.child.setupUi(self)


class DailyDefStasticForm(QMainWindow, dailyDef_Ui):
    def __init__(self, parent=None):
        super(DailyDefStasticForm, self).__init__(parent)
        self.setupUi(self)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

        self.actionSectionSet.triggered.connect(
            self.CreateSectionSettingsWindow)
        self.actionDbSet.triggered.connect(self.CreateDbSettingsWindow)
        self.pushButton_4.clicked.connect(self.CreateDailyStasticForm)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)

    def CreateDbSettingsWindow(self):
        self.dbSettingWindow = DbSettingsWindow(self)
        self.dbSettingWindow.exec()

    def CreateSectionSettingsWindow(self):
        self.sectionSettingsWindow = SectionSettingWindow(self)
        self.sectionSettingsWindow.exec()

    def CreateDailyStasticForm(self):
        self.dailyStasticForm = DailyDefStasticForm(self)
        self.dailyStasticForm.label_2.setStyleSheet("QLabel{color:green}")
        self.dailyStasticForm.statusBar().hide()
        self.dailyStasticForm.pushButton.clicked.connect(
            self.CloseDailyStasticForm)
        for header_item_index in range(self.dailyStasticForm.tableWidget.columnCount()):
            self.dailyStasticForm.tableWidget.horizontalHeader().setSectionResizeMode(
                header_item_index, QtWidgets.QHeaderView.Stretch)
        self.dailyStasticForm.show()

    def CloseDailyStasticForm(self):
        if self.dailyStasticForm.isActiveWindow():
            self.dailyStasticForm.close()

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
        y = [0, 41, 27, 30, 19, 8, 12, 15, 17, 23]
        z = [0, 11, 12, 6, 8, 34, 45, 2, 11, 34]
        f = [0, 15, 34, 35, 6, 3, 4, 9, 23, 47]
        g = [0, 24, 44, 50, 16, 4, 5, 11, 18, 27]
        h = [0, 16, 23, 18, 22, 29, 11, 14, 18, 23]
        i = [0, 12, 2, 5, 7, 5, 13, 7, 8, 10]
        j = [0, 4, 3, 6, 8, 4, 5, 7, 8, 9]
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
        # 从系统分辨率中提取桌面高度
        height = QApplication.desktop().screenGeometry().height()
        # 高度小于 1000，字体及高度都修改为20, 修改 frame 宽度为 150，高度为 530
        if height <= 1000:
            self.resize(1000, 700)
            self.frame.setMinimumSize(QtCore.QSize(200, 520))
            self.frame.setMaximumWidth(200)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(20)
            font.setBold(True)
            font.setWeight(50)
            labels = ('label_2', 'label_4', 'label_6', 'label_7', 'label_9')
            for label_name in labels:
                label = self.frame.findChild((QtWidgets.QLabel), label_name)
                label.setFont(font)
                label.setMinimumSize(QtCore.QSize(16777215, 20))
            font = QtGui.QFont()
            font.setFamily("微软雅黑 Light")
            font.setPointSize(20)
            font.setBold(False)
            font.setWeight(50)
            labels = ('label', 'label_3', 'label_5', 'label_8')
            for label_name in labels:
                label = self.frame.findChild((QtWidgets.QLabel), label_name)
                label.setFont(font)
                label.setMinimumSize(QtCore.QSize(16777215, 20))


if __name__ == "__main__":
    # cfg = CfgHelper()
    # print(cfg.cfg_dict)
    app = QApplication(sys.argv)
    mywin = MyMainForm()
    mywin.SetTableWidgetColumnHeaderStretchMode()
    mywin.GetSystemDefinitionToChangeFontSizeAndLabelSize()
    mywin.show()
    mywin.AddLineChartToForm()
    sys.exit(app.exec_())
