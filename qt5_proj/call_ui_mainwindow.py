import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui,QtCore
from mainForm import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)


def GetSystemDefinitionToChangeFontSizeAndLabelSize(form):
    form.label_2.setStyleSheet("QLabel{color: red}")
    form.label_4.setStyleSheet("QLabel{color:blue}")
    form.label_6.setStyleSheet("QLabel{color:pink}")
    form.label_9.setStyleSheet("QLabel{color:green}")
    form.label_7.setStyleSheet("QLabel{color:purple}")
    height = QApplication.desktop().screenGeometry().height()
    if height <= 800:
        form.frame.setMaximumSize(QtCore.QSize(230, 520))
        form.frame.setMinimumSize(QtCore.QSize(230, 520))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(50)
        form.label_2.setFont(font)
        form.label_2.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_4.setFont(font)
        form.label_4.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_6.setFont(font)
        form.label_6.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_9.setFont(font)
        form.label_9.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_7.setFont(font)
        form.label_7.setMinimumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        form.label.setFont(font)
        form.label.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_3.setFont(font)
        form.label_3.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_5.setFont(font)
        form.label_5.setMinimumSize(QtCore.QSize(16777215, 20))
        form.label_8.setFont(font)
        form.label_8.setMinimumSize(QtCore.QSize(16777215, 20))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainForm()
    GetSystemDefinitionToChangeFontSizeAndLabelSize(mywin)
    mywin.show()
    sys.exit(app.exec_())
