# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(1113, 927)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Chinese, QtCore.QLocale.China))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMinimumSize(QtCore.QSize(0, 60))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(40)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(462, 386))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.checkBox = QtWidgets.QCheckBox(self.frame_3)
        self.checkBox.setEnabled(False)
        self.checkBox.setMinimumSize(QtCore.QSize(0, 30))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.comboBox_3 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_3.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_2.setMinimumSize(QtCore.QSize(30, 30))
        self.comboBox_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setMinimumSize(QtCore.QSize(80, 30))
        self.comboBox.setMaximumSize(QtCore.QSize(80, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(20)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.frame = QtWidgets.QFrame(self.tab_3)
        self.frame.setMinimumSize(QtCore.QSize(210, 730))
        self.frame.setMaximumSize(QtCore.QSize(210, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 40))
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 50))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setMinimumSize(QtCore.QSize(0, 40))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setMinimumSize(QtCore.QSize(0, 50))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setMinimumSize(QtCore.QSize(0, 40))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setMinimumSize(QtCore.QSize(0, 50))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setMinimumSize(QtCore.QSize(0, 40))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setMinimumSize(QtCore.QSize(0, 50))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        spacerItem1 = QtWidgets.QSpacerItem(127, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.verticalLayout_2.addWidget(self.label_15)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_7.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout_7.addWidget(self.pushButton_7)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setStyleSheet("")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_7.addWidget(self.pushButton_4)
        self.pushButton = QtWidgets.QPushButton(self.frame_7)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_7.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_7.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.gridLayout.addWidget(self.frame_7, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_4 = QtWidgets.QFrame(self.tab_2)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_3.addWidget(self.label_12)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_3.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(229, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label_13 = QtWidgets.QLabel(self.frame_4)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_3.addWidget(self.label_13)
        self.verticalLayout_6.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(20)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        self.horizontalLayout_5.addWidget(self.tableWidget_2)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.tab_2)
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(920, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_6.addWidget(self.frame_6)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1113, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDbSet = QtWidgets.QAction(MainWindow)
        self.actionDbSet.setObjectName("actionDbSet")
        self.actionSectionSet = QtWidgets.QAction(MainWindow)
        self.actionSectionSet.setObjectName("actionSectionSet")
        self.actionInfoSet = QtWidgets.QAction(MainWindow)
        self.actionInfoSet.setObjectName("actionInfoSet")
        self.actionWorkingTimeSet = QtWidgets.QAction(MainWindow)
        self.actionWorkingTimeSet.setEnabled(True)
        self.actionWorkingTimeSet.setVisible(True)
        self.actionWorkingTimeSet.setObjectName("actionWorkingTimeSet")
        self.actionWorkRestTimeSet = QtWidgets.QAction(MainWindow)
        self.actionWorkRestTimeSet.setVisible(False)
        self.actionWorkRestTimeSet.setObjectName("actionWorkRestTimeSet")
        self.actionWorkingTimeSet_2 = QtWidgets.QAction(MainWindow)
        self.actionWorkingTimeSet_2.setVisible(False)
        self.actionWorkingTimeSet_2.setObjectName("actionWorkingTimeSet_2")
        self.menu.addAction(self.actionDbSet)
        self.menu.addAction(self.actionInfoSet)
        self.menu_3.addAction(self.actionSectionSet)
        self.menu_3.addAction(self.actionWorkRestTimeSet)
        self.menu_3.addAction(self.actionWorkingTimeSet_2)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "包装线回收率统计看板"))
        self.label_10.setText(_translate("MainWindow", "包装回收目视化系统"))
        self.checkBox.setText(_translate("MainWindow", "半小时间隔"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "全天"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "半天"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "整线不良"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "入楦段不良"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "贴底段不良"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "包装段不良"))
        self.comboBox.setItemText(0, _translate("MainWindow", "线状图"))
        self.comboBox.setItemText(1, _translate("MainWindow", "柱状图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "时段不良"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "不良原因"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "不良数量(双)"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "比例"))
        self.label.setText(_translate("MainWindow", "回收数量"))
        self.label_2.setText(_translate("MainWindow", "0"))
        self.label_3.setText(_translate("MainWindow", "加工投料"))
        self.label_4.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "回收比例"))
        self.label_6.setText(_translate("MainWindow", "0.0%"))
        self.label_8.setText(_translate("MainWindow", "包装数量"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.pushButton_7.setText(_translate("MainWindow", "每日目标产量设置"))
        self.pushButton_4.setText(_translate("MainWindow", "日统计"))
        self.pushButton.setText(_translate("MainWindow", "投料 / 包装数据修正"))
        self.pushButton_2.setText(_translate("MainWindow", "月统计"))
        self.pushButton_3.setText(_translate("MainWindow", "缴库量输入"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "不良统计"))
        self.label_11.setText(_translate("MainWindow", "当前线别："))
        self.label_12.setText(_translate("MainWindow", "NOS1A"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "不良原因"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "包检一"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "包检二"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "包检三"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "包检四"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "包检合计"))
        self.pushButton_6.setText(_translate("MainWindow", "导出当日明细"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "不良明细"))
        self.menu.setTitle(_translate("MainWindow", "维护设置"))
        self.menu_3.setTitle(_translate("MainWindow", "品管定义"))
        self.actionDbSet.setText(_translate("MainWindow", "数据库服务器设置"))
        self.actionSectionSet.setText(_translate("MainWindow", "各段不良设定"))
        self.actionInfoSet.setText(_translate("MainWindow", "线别 / 时间段 / 不良原因设置"))
        self.actionWorkingTimeSet.setText(_translate("MainWindow", "生产时段设置"))
        self.actionWorkRestTimeSet.setText(_translate("MainWindow", "作休时间设置"))
        self.actionWorkingTimeSet_2.setText(_translate("MainWindow", "生产时间段定义"))
