import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtChart import QBarSet, QBarCategoryAxis, QBarSeries, QChart, QChartView
from mainForm import Ui_MainWindow


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)

    def create_bar_chart(self):
        set0 = QBarSet('投料')
        set1 = QBarSet('不良回收')
        series = QBarSeries()
        axis = QBarCategoryAxis()
        chart = QChart()

        categories = ['09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']

        set0.append([1, 2, 3, 4, 5, 6, 7, 8, 9])
        set1.append([5, 0, 0, 4, 0, 7, 13, 8, 7])
        series.append(set0)
        series.append(set1)
        chart.addSeries(series)
        axis.append(categories)

        chart.setTitle('柱状图学习测试')
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)
        return chart


def GetSystemDefinitionToChangeFontSizeAndLabelSize(form):
    # 获取系统分辨率更改 label 尺寸及字体大小
    # 先设定各个 label 字体不同颜色
    form.label_2.setStyleSheet("QLabel{color: red}")
    form.label_4.setStyleSheet("QLabel{color:blue}")
    form.label_6.setStyleSheet("QLabel{color:pink}")
    form.label_9.setStyleSheet("QLabel{color:green}")
    form.label_7.setStyleSheet("QLabel{color:purple}")
    # 从系统分辨率中提取桌面高度
    height = QApplication.desktop().screenGeometry().height()
    # 高度小于 800，字体及高度都修改为20
    if height <= 1070:
        form.frame.setMinimumSize(QtCore.QSize(230, 520))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(50)
        labels = ('label_2', 'label_4', 'label_6', 'label_7', 'label_9')
        for label_name in labels:
            label = form.frame.findChild((QtWidgets.QLabel), label_name)
            label.setFont(font)
            label.setMinimumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        labels = ('label', 'label_3', 'label_5', 'label_8')
        for label_name in labels:
            label = form.frame.findChild((QtWidgets.QLabel), label_name)
            label.setFont(font)
            label.setMinimumSize(QtCore.QSize(16777215, 20))

# def AddQtChartsIntoMainForm(form):
#     # 增加图表项目到主窗口
#     # main code here

#     # example code here


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywin = MyMainForm()
    GetSystemDefinitionToChangeFontSizeAndLabelSize(mywin)
    mywin.show()
    charview = QChartView(mywin.create_bar_chart(), mywin.frame_2)
    charview.setGeometry(0, 0, mywin.frame_2.width(), mywin.frame_2.height())
    charview.show()
    print(str(mywin.frame_2.width()) + ":" + str(mywin.frame_2.height()))
    sys.exit(app.exec_())
