# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\workRestTimeSettings.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 224)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(14)
        Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(354, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(Dialog)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(117, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.timeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit.setMinimumSize(QtCore.QSize(70, 0))
        self.timeEdit.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeEdit.setObjectName("timeEdit")
        self.horizontalLayout_2.addWidget(self.timeEdit)
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.timeEdit_2 = QtWidgets.QTimeEdit(self.frame_2)
        self.timeEdit_2.setMinimumSize(QtCore.QSize(70, 0))
        self.timeEdit_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeEdit_2.setObjectName("timeEdit_2")
        self.horizontalLayout_2.addWidget(self.timeEdit_2)
        spacerItem2 = QtWidgets.QSpacerItem(116, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.timeEdit_3 = QtWidgets.QTimeEdit(self.frame_3)
        self.timeEdit_3.setMinimumSize(QtCore.QSize(70, 0))
        self.timeEdit_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeEdit_3.setObjectName("timeEdit_3")
        self.horizontalLayout_3.addWidget(self.timeEdit_3)
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.timeEdit_4 = QtWidgets.QTimeEdit(self.frame_3)
        self.timeEdit_4.setMinimumSize(QtCore.QSize(70, 0))
        self.timeEdit_4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.timeEdit_4.setObjectName("timeEdit_4")
        self.horizontalLayout_3.addWidget(self.timeEdit_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(Dialog)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.frame_4)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.verticalLayout.addWidget(self.frame_4)

        self.retranslateUi(Dialog)
        self.pushButton_2.clicked.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "作休时间设置"))
        self.label.setText(_translate("Dialog", "当前线别："))
        self.label_2.setText(_translate("Dialog", "NOS1A"))
        self.label_3.setText(_translate("Dialog", "上班时间："))
        self.timeEdit.setDisplayFormat(_translate("Dialog", "hh:mm"))
        self.label_4.setText(_translate("Dialog", "至"))
        self.timeEdit_2.setDisplayFormat(_translate("Dialog", "hh:mm"))
        self.label_6.setText(_translate("Dialog", "休息时间："))
        self.timeEdit_3.setDisplayFormat(_translate("Dialog", "hh:mm"))
        self.label_5.setText(_translate("Dialog", "至"))
        self.timeEdit_4.setDisplayFormat(_translate("Dialog", "hh:mm"))
        self.label_7.setText(_translate("Dialog", "用于计算节拍产量"))
        self.label_8.setText(_translate("Dialog", "节拍产量 = 目标产量 * 已工作时长 / 总时长"))
        self.pushButton.setText(_translate("Dialog", "保存"))
        self.pushButton_2.setText(_translate("Dialog", "关闭"))
