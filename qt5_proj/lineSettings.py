# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\lineSettings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(470, 435)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(245, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.frame_2)
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 130))
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 9)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setMaximumSize(QtCore.QSize(50, 30))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.timeEdit = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeEdit.setMaximumSize(QtCore.QSize(80, 30))
        self.timeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 3, 5), QtCore.QTime(8, 0, 0)))
        self.timeEdit.setObjectName("timeEdit")
        self.gridLayout.addWidget(self.timeEdit, 0, 1, 1, 1)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.groupBox_2)
        self.timeEdit_2.setMaximumSize(QtCore.QSize(80, 30))
        self.timeEdit_2.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 3, 5), QtCore.QTime(11, 30, 0)))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.gridLayout.addWidget(self.timeEdit_2, 1, 1, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.horizontalLayout_3.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_5.setContentsMargins(2, 0, 2, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setMaximumSize(QtCore.QSize(50, 30))
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.groupBox_3)
        self.timeEdit_3.setMaximumSize(QtCore.QSize(80, 30))
        self.timeEdit_3.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 3, 5), QtCore.QTime(12, 30, 0)))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.gridLayout_2.addWidget(self.timeEdit_3, 0, 1, 1, 1)
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.groupBox_3)
        self.timeEdit_4.setMaximumSize(QtCore.QSize(80, 30))
        self.timeEdit_4.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 3, 5), QtCore.QTime(17, 0, 0)))
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.gridLayout_2.addWidget(self.timeEdit_4, 1, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 190))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.frame_3)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 230))
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_6.setContentsMargins(2, 0, 2, 3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, -1, -1, 3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setMinimumSize(QtCore.QSize(0, 30))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setMinimumSize(QtCore.QSize(0, 30))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setMinimumSize(QtCore.QSize(0, 30))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_4)
        self.label_11.setMinimumSize(QtCore.QSize(0, 30))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setMinimumSize(QtCore.QSize(0, 30))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setMinimumSize(QtCore.QSize(0, 30))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 2, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 2, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_3.addWidget(self.lineEdit_6, 3, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_3.addWidget(self.lineEdit_7, 0, 3, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 1, 3, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(0, 30))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout_3.addWidget(self.lineEdit_8, 2, 3, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_4)
        self.label_12.setMinimumSize(QtCore.QSize(0, 30))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 2, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 53))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        spacerItem1 = QtWidgets.QSpacerItem(267, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "线别 / 时间段 / 不良原因设置"))
        self.label.setText(_translate("Dialog", "当前线别："))
        self.comboBox.setItemText(0, _translate("Dialog", "NOS1A"))
        self.comboBox.setItemText(1, _translate("Dialog", "NOS1B"))
        self.comboBox.setItemText(2, _translate("Dialog", "NOS2A"))
        self.comboBox.setItemText(3, _translate("Dialog", "NOS2B"))
        self.comboBox.setItemText(4, _translate("Dialog", "AL"))
        self.comboBox.setItemText(5, _translate("Dialog", "ML"))
        self.groupBox.setTitle(_translate("Dialog", "时段设定"))
        self.groupBox_2.setTitle(_translate("Dialog", "上午"))
        self.label_3.setText(_translate("Dialog", "结束："))
        self.label_2.setText(_translate("Dialog", "开始："))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.timeEdit_2.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.groupBox_3.setTitle(_translate("Dialog", "下午"))
        self.label_4.setText(_translate("Dialog", "结束"))
        self.label_5.setText(_translate("Dialog", "开始："))
        self.timeEdit_3.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.timeEdit_4.setDisplayFormat(_translate("Dialog", "HH:mm"))
        self.groupBox_4.setTitle(_translate("Dialog", "不良类型"))
        self.label_6.setText(_translate("Dialog", "类型三："))
        self.label_10.setText(_translate("Dialog", "类型七："))
        self.label_8.setText(_translate("Dialog", "类型五："))
        self.label_11.setText(_translate("Dialog", "类型一："))
        self.label_9.setText(_translate("Dialog", "类型四："))
        self.label_7.setText(_translate("Dialog", "类型二："))
        self.label_12.setText(_translate("Dialog", "类型六："))
        self.pushButton.setText(_translate("Dialog", "保存"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))
